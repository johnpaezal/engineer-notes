# Indexes & Performance
*Making queries fast at scale*

## How Indexes Work
*Speed up reads by avoiding full table scans*

**Without index** – DB reads every row to find matches (full table scan)  
**With index** – DB uses a B-tree to jump directly to matching rows

```
Table: users (1,000,000 rows)

Without index on email:
  SELECT * FROM users WHERE email = 'alice@example.com'
  → scan all 1,000,000 rows → slow

With index on email:
  → look up in B-tree → find row pointer → read 1 row → fast
```

---

## Creating Indexes

```sql
-- Basic index (B-tree by default)
CREATE INDEX idx_users_email ON users(email);

-- Unique index (also enforces uniqueness)
CREATE UNIQUE INDEX idx_users_email ON users(email);

-- Composite index (multiple columns)
CREATE INDEX idx_orders_user_date ON orders(user_id, created_at);

-- Partial index (only index a subset of rows)
CREATE INDEX idx_active_users ON users(email) WHERE active = true;

-- Index on expression
CREATE INDEX idx_lower_email ON users(LOWER(email));

-- Drop index
DROP INDEX idx_users_email;

-- List indexes (PostgreSQL)
SELECT indexname, indexdef FROM pg_indexes WHERE tablename = 'users';
```

---

## When to Add an Index

```
✓ Columns used in WHERE clauses frequently
✓ Columns used in JOIN ON conditions
✓ Columns used in ORDER BY (can avoid sort step)
✓ Foreign key columns
✓ Columns with high cardinality (many unique values)

✗ Small tables (full scan is faster)
✗ Columns rarely queried
✗ Columns with low cardinality (boolean, status with 2-3 values)
✗ Tables with heavy writes (every write updates all indexes)
```

---

## Composite Index Column Order
*Order matters — leftmost prefix rule*

```sql
CREATE INDEX idx_orders_user_date ON orders(user_id, created_at);

-- Uses index:
WHERE user_id = 1
WHERE user_id = 1 AND created_at > '2024-01-01'

-- Does NOT use index:
WHERE created_at > '2024-01-01'   -- skips first column
```

**Rule** – Put the most selective column first, then filter columns.

---

## EXPLAIN and Query Analysis

```sql
-- Show query execution plan
EXPLAIN SELECT * FROM users WHERE email = 'alice@example.com';

-- Show plan + actual execution stats
EXPLAIN ANALYZE SELECT * FROM users WHERE email = 'alice@example.com';
```

### Reading EXPLAIN output

```
Seq Scan on users  (cost=0.00..18334.00 rows=1 width=...)
  Filter: (email = 'alice@example.com')
```

- **Seq Scan** – Full table scan (bad for large tables, add index)
- **Index Scan** – Uses an index (good)
- **Bitmap Heap Scan** – Multi-row index scan (ok)
- **cost=start..total** – Estimated cost (lower is better)
- **rows** – Estimated rows returned

---

## Transactions
*All-or-nothing operations*

**Transaction** – A group of SQL statements that execute as one unit  
**ACID**:
- **Atomicity** – All or nothing
- **Consistency** – DB stays valid
- **Isolation** – Transactions don't interfere
- **Durability** – Committed data survives crashes

```sql
-- Explicit transaction
BEGIN;
    UPDATE accounts SET balance = balance - 100 WHERE id = 1;
    UPDATE accounts SET balance = balance + 100 WHERE id = 2;
COMMIT;

-- On error, rollback
BEGIN;
    UPDATE accounts SET balance = balance - 100 WHERE id = 1;
    -- something fails
ROLLBACK;   -- undo everything in this transaction
```

### Savepoints

```sql
BEGIN;
    INSERT INTO orders (user_id, total) VALUES (1, 99.99);
    SAVEPOINT after_order;
    
    INSERT INTO order_items (order_id, product_id) VALUES (1, 99);  -- fails
    ROLLBACK TO after_order;   -- undo only to savepoint
    
COMMIT;
```

### Isolation Levels

```sql
-- Set isolation level for a transaction
SET TRANSACTION ISOLATION LEVEL REPEATABLE READ;
BEGIN;
  ...
COMMIT;
```

| Level | Dirty Read | Non-repeatable Read | Phantom Read |
|---|---|---|---|
| `READ UNCOMMITTED` | possible | possible | possible |
| `READ COMMITTED` (default) | no | possible | possible |
| `REPEATABLE READ` | no | no | possible |
| `SERIALIZABLE` | no | no | no |

---

## N+1 Query Problem
*Common ORM performance trap*

```python
# ❌ N+1: 1 query for users + N queries for orders (1 per user)
users = db.query("SELECT * FROM users")
for user in users:
    orders = db.query(f"SELECT * FROM orders WHERE user_id = {user.id}")

# ✅ 1 query with JOIN
results = db.query("""
    SELECT u.name, o.total
    FROM users u
    LEFT JOIN orders o ON u.id = o.user_id
""")
```

---

## Query Optimization Tips

```sql
-- ❌ Avoids index (function on column)
SELECT * FROM users WHERE LOWER(email) = 'alice@example.com';

-- ✅ Use expression index instead
CREATE INDEX idx_lower_email ON users(LOWER(email));
SELECT * FROM users WHERE LOWER(email) = 'alice@example.com'; -- now uses index

-- ❌ SELECT * fetches all columns (wasted IO)
SELECT * FROM users WHERE id = 1;

-- ✅ Select only what you need
SELECT name, email FROM users WHERE id = 1;

-- ❌ OFFSET-based pagination is slow on large tables
SELECT * FROM users ORDER BY id LIMIT 20 OFFSET 100000;

-- ✅ Keyset (cursor) pagination
SELECT * FROM users WHERE id > 100000 ORDER BY id LIMIT 20;
```

---

## Common Performance Issues

| Problem | Symptom | Fix |
|---|---|---|
| Missing index | Seq Scan on large table | Add index on filter column |
| N+1 queries | Many small queries | Use JOIN or eager loading |
| SELECT * | Slow queries, high IO | Select specific columns |
| No connection pool | Connection exhaustion | Use PgBouncer / SQLAlchemy pool |
| Large OFFSET | Pagination slow at end | Switch to keyset pagination |
| Index not used | Seq Scan despite index | Check for function on column, type mismatch |

---

## Connection Pooling

```python
# SQLAlchemy connection pool
from sqlalchemy import create_engine

engine = create_engine(
    "postgresql://user:pass@host/db",
    pool_size=10,        # max persistent connections
    max_overflow=20,     # extra connections allowed temporarily
    pool_timeout=30,     # wait time before giving up
    pool_recycle=1800    # recycle connections after 30 min
)
```

**Tools**: PgBouncer (PostgreSQL proxy pool), HikariCP (Java), SQLAlchemy pool (Python)
