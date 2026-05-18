# SQL Interview
*Query plans, locking, and classic interview problems*

> Builds on `02-queries.md` (joins, CTEs, window functions) and `03-indexes-performance.md` (indexes, EXPLAIN basics, isolation table). Only interview-specific gaps live here.

## Reading a Query Plan
*Estimated vs actual, node types*

**Estimated rows** – Planner's guess from table statistics  
**Actual rows** – Real rows returned (only with `ANALYZE`)  
**Big estimate vs actual gap** – Stale stats → run `ANALYZE table`  
**loops** – Times a node ran (inner side of nested loop)

```sql
EXPLAIN ANALYZE
SELECT * FROM orders WHERE user_id = 42;
```

```
Index Scan using idx_orders_user on orders
  (cost=0.42..8.45 rows=3 width=64)
  (actual time=0.018..0.021 rows=3 loops=1)
  Index Cond: (user_id = 42)
Planning Time: 0.10 ms
Execution Time: 0.04 ms
```

- `cost=start..total` – arbitrary units; compare alternatives, not seconds
- `rows=3` (estimate) vs `actual ... rows=3` – close → stats healthy
- **Seq Scan** good only for small tables or low selectivity
- **Index Scan** one row at a time; **Bitmap Heap Scan** many matches
- **Nested Loop** small driver table; **Hash Join** large unsorted; **Merge Join** sorted inputs

---

## Why an Index Is NOT Used
*Sargability killers in WHERE*

**Sargable** – Predicate that can use an index range scan

```sql
-- Function wraps the column → index ignored
WHERE LOWER(email) = 'a@x.com'      -- needs expression index
WHERE created_at::date = '2025-01-01'  -- cast on column

-- Leading wildcard → B-tree useless
WHERE name LIKE '%son'              -- no prefix to seek
WHERE name LIKE 'son%'             -- OK: prefix usable

-- Implicit type cast (column int, literal text)
WHERE user_id = '42'               -- may cast every row

-- Low selectivity → Seq Scan is cheaper
WHERE status = 'active'            -- 90% of rows match

-- OR across different columns → index per branch not combined
WHERE email = 'a@x.com' OR phone = '555'   -- rewrite as UNION
```

**Fixes**: expression index, keep column bare (`created_at >= d AND < d+1`), match literal types, `UNION` instead of `OR`, partial index for skewed values.

---

## N+1 Query Problem
*One query per parent row*

> JOIN fix shown in `03-indexes-performance.md`. Here: ORM cause + alternatives.

```python
# ❌ N+1: lazy relationship hit inside the loop
users = session.query(User).all()        # 1 query
for u in users:
    print(u.orders)                      # +1 query EACH user → N+1

# ✅ Eager load (single round trip, ORM-generated JOIN)
users = session.query(User).options(joinedload(User.orders)).all()

# ✅ Batch with IN (2 queries total, any data layer)
users = session.query(User).all()
ids   = [u.id for u in users]
orders = session.query(Order).filter(Order.user_id.in_(ids)).all()
```

**Detect**: query logger shows repeated identical SQL with different param. **Fix**: eager loading (`joinedload` / `selectinload`), `IN` batching, or JOIN.

---

## Window Function Ranking
*RANK vs DENSE_RANK vs ROW_NUMBER*

> Syntax for ROW_NUMBER, RANK, LAG/LEAD, running total: `02-queries.md`. Here: the tie behaviour difference asked in interviews.

```sql
SELECT name, score,
  ROW_NUMBER() OVER (ORDER BY score DESC) AS rn,   -- 1,2,3,4 (no ties)
  RANK()       OVER (ORDER BY score DESC) AS rnk,  -- 1,2,2,4 (gap)
  DENSE_RANK() OVER (ORDER BY score DESC) AS drnk  -- 1,2,2,3 (no gap)
FROM players;

-- scores 90,80,80,70 →
-- rn: 1 2 3 4 | rnk: 1 2 2 4 | drnk: 1 2 2 3
```

**ROW_NUMBER** unique sequence  •  **RANK** ties share, skips next  •  **DENSE_RANK** ties share, no skip

---

## Recursive CTE
*Walk a hierarchy / org chart*

**Anchor** – Base rows (top of tree)  
**Recursive term** – Joins back to the CTE until no new rows

```sql
WITH RECURSIVE org AS (
    SELECT id, name, manager_id, 1 AS depth      -- anchor: CEO
    FROM employees
    WHERE manager_id IS NULL

    UNION ALL

    SELECT e.id, e.name, e.manager_id, o.depth + 1
    FROM employees e
    JOIN org o ON e.manager_id = o.id            -- recurse on children
)
SELECT repeat('  ', depth - 1) || name AS tree, depth
FROM org
ORDER BY depth;

-- CEO
--   VP Eng
--     Dev A
--   VP Sales
```

**Also for**: bill of materials, category trees, graph paths. Guard infinite loops with a `depth < N` filter.

---

## Isolation Levels & Anomalies
*Which anomaly each level prevents*

> Level/anomaly matrix is in `03-indexes-performance.md`. Here: what each anomaly means.

**Dirty read** – Read another tx's uncommitted change (may roll back)  
**Non-repeatable read** – Same row, different value on re-read (other tx updated + committed)  
**Phantom read** – Same query, new rows appear (other tx inserted matching rows)  
**Lost update** – Two tx read-modify-write; one overwrites the other

```sql
-- READ COMMITTED (PostgreSQL default): no dirty reads
-- REPEATABLE READ: snapshot fixed at tx start; PG also blocks phantoms
-- SERIALIZABLE: behaves as if tx ran one-by-one (may abort with 40001 → retry)
SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;
```

Higher isolation = fewer anomalies, more blocking/aborts. Default `READ COMMITTED` is fine for most apps.

---

## Deadlocks
*Two tx wait on each other's locks*

```
T1: UPDATE accounts WHERE id=1;   -- locks row 1
T2: UPDATE accounts WHERE id=2;   -- locks row 2
T1: UPDATE accounts WHERE id=2;   -- waits for T2
T2: UPDATE accounts WHERE id=1;   -- waits for T1 → DEADLOCK
```

- **Cause** – Circular lock-wait between transactions
- **DB resolution** – Detects cycle, aborts the cheaper victim (`deadlock detected`, SQLSTATE 40P01)
- **Avoid** – Lock rows in a consistent order (e.g. always ascending `id`), keep transactions short, lower isolation, add `NOWAIT` / `SKIP LOCKED` where suitable
- **Handle** – Catch the error and retry the transaction

---

## Pessimistic vs Optimistic Locking
*Lock upfront vs detect conflict at write*

| | Pessimistic | Optimistic |
|---|---|---|
| Mechanism | `SELECT ... FOR UPDATE` row lock | `version` column compared on update |
| Conflict | Blocks other writers | Detected at commit (retry) |
| Best for | High contention, short tx | Low contention, web requests |

```sql
-- Pessimistic: hold the row until COMMIT
BEGIN;
SELECT balance FROM accounts WHERE id = 1 FOR UPDATE;
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
COMMIT;

-- Optimistic: update only if version unchanged
UPDATE accounts
SET balance = 900, version = version + 1
WHERE id = 1 AND version = 7;
-- 0 rows affected → someone else changed it → reload & retry
```

`FOR UPDATE SKIP LOCKED` – queue/worker pattern: grab next free row, skip locked ones.

---

## Classic Interview Queries
*Memorize the canonical solutions*

### Nth Highest Value
*Top-N without LIMIT tricks*

```sql
-- 2nd highest salary (handles ties + NULL when none)
SELECT MAX(salary) AS second_highest
FROM employees
WHERE salary < (SELECT MAX(salary) FROM employees);

-- Nth highest, general (N=3)
SELECT DISTINCT salary
FROM employees
ORDER BY salary DESC
OFFSET 2 LIMIT 1;           -- skip N-1
```

### Find Duplicates
*Group and keep counts > 1*

```sql
SELECT email, COUNT(*) AS cnt
FROM users
GROUP BY email
HAVING COUNT(*) > 1;
```

### Delete Duplicates Keeping One
*Lowest id survives*

```sql
DELETE FROM users a
USING users b
WHERE a.email = b.email
  AND a.id   > b.id;        -- keep min(id) per email

-- Window-function variant
DELETE FROM users WHERE id IN (
  SELECT id FROM (
    SELECT id, ROW_NUMBER() OVER (
      PARTITION BY email ORDER BY id) AS rn
    FROM users
  ) t WHERE rn > 1
);
```

### Second Highest Per Group
*Window + filter on rank*

```sql
SELECT department, name, salary
FROM (
  SELECT department, name, salary,
    DENSE_RANK() OVER (
      PARTITION BY department ORDER BY salary DESC) AS rnk
  FROM employees
) ranked
WHERE rnk = 2;              -- 2nd highest within each department
```

---

## Best Practices

- Always run `EXPLAIN ANALYZE` on slow queries before guessing
- Keep WHERE columns bare (sargable); index expressions when needed
- Default to `READ COMMITTED`; raise isolation only when an anomaly bites
- Lock rows in consistent order to prevent deadlocks; retry on `40001`/`40P01`
- Prefer optimistic locking for web requests, pessimistic for hot rows
- Use `DENSE_RANK` for "Nth per group", correlated `MAX` for global Nth
