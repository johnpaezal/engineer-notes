# SQL Queries
*Filtering, sorting, aggregating, and joining data*

## SELECT & Filtering

```sql
-- All rows and columns
SELECT * FROM users;

-- Specific columns
SELECT name, email FROM users;

-- With alias
SELECT name AS full_name, email AS contact FROM users;

-- Distinct values
SELECT DISTINCT country FROM users;

-- Filter with WHERE
SELECT * FROM users WHERE age > 18;
SELECT * FROM users WHERE age BETWEEN 18 AND 30;
SELECT * FROM users WHERE country IN ('US', 'UK', 'CA');
SELECT * FROM users WHERE email IS NOT NULL;
SELECT * FROM users WHERE email IS NULL;

-- Pattern matching with LIKE
SELECT * FROM users WHERE name LIKE 'A%';    -- starts with A
SELECT * FROM users WHERE name LIKE '%son';  -- ends with son
SELECT * FROM users WHERE name LIKE '%ali%'; -- contains ali
SELECT * FROM users WHERE name ILIKE '%ali%'; -- case-insensitive (PostgreSQL)

-- Combine conditions
SELECT * FROM users WHERE age > 18 AND country = 'US';
SELECT * FROM users WHERE country = 'US' OR country = 'UK';
SELECT * FROM users WHERE NOT country = 'US';
```

---

## Sorting & Pagination

```sql
-- Sort ascending (default)
SELECT * FROM users ORDER BY name ASC;

-- Sort descending
SELECT * FROM users ORDER BY created_at DESC;

-- Sort by multiple columns
SELECT * FROM orders ORDER BY user_id ASC, created_at DESC;

-- Limit results
SELECT * FROM users LIMIT 10;

-- Pagination: page 3 (30 rows per page)
SELECT * FROM users
ORDER BY id
LIMIT 30 OFFSET 60;   -- skip first 60, return next 30
```

---

## Aggregate Functions

```sql
SELECT COUNT(*)          FROM users;           -- total rows
SELECT COUNT(DISTINCT country) FROM users;     -- distinct values
SELECT SUM(total)        FROM orders;          -- sum
SELECT AVG(total)        FROM orders;          -- average
SELECT MAX(total)        FROM orders;          -- max
SELECT MIN(total)        FROM orders;          -- min
SELECT ROUND(AVG(total), 2) FROM orders;       -- rounded average
```

---

## GROUP BY and HAVING

```sql
-- Count users per country
SELECT country, COUNT(*) AS total
FROM users
GROUP BY country;

-- Average order total per user
SELECT user_id, ROUND(AVG(total), 2) AS avg_total
FROM orders
GROUP BY user_id;

-- HAVING: filter after grouping (like WHERE but for aggregates)
SELECT country, COUNT(*) AS total
FROM users
GROUP BY country
HAVING COUNT(*) > 10;   -- only countries with more than 10 users
```

**Rule**: `WHERE` filters rows before grouping. `HAVING` filters groups after aggregation.

```sql
-- Correct: filter before and after
SELECT country, COUNT(*) AS total
FROM users
WHERE created_at > '2024-01-01'   -- filter rows first
GROUP BY country
HAVING COUNT(*) > 5;              -- then filter groups
```

---

## JOINs
*Combining data from multiple tables*

```
users               orders
id | name           id | user_id | total
1  | Alice          1  | 1       | 99.99
2  | Bob            2  | 1       | 49.99
3  | Carol          3  | 2       | 19.99
                    4  | 99      | 5.00   ← no matching user
```

### INNER JOIN
*Only rows that match in both tables*

```sql
SELECT u.name, o.id AS order_id, o.total
FROM users u
INNER JOIN orders o ON u.id = o.user_id;

-- Result: Alice (x2), Bob (x1) — Carol and order 4 excluded
```

### LEFT JOIN
*All rows from left, matching from right (NULL if no match)*

```sql
SELECT u.name, o.id AS order_id, o.total
FROM users u
LEFT JOIN orders o ON u.id = o.user_id;

-- Result: Alice (x2), Bob (x1), Carol (order_id=NULL, total=NULL)
```

### RIGHT JOIN
*All rows from right, matching from left*

```sql
SELECT u.name, o.id AS order_id, o.total
FROM users u
RIGHT JOIN orders o ON u.id = o.user_id;

-- Result: Alice (x2), Bob (x1), NULL (order 4 — no user)
```

### FULL OUTER JOIN
*All rows from both tables*

```sql
SELECT u.name, o.id AS order_id
FROM users u
FULL OUTER JOIN orders o ON u.id = o.user_id;

-- Result: all users + all orders, NULLs where no match
```

### Self JOIN
*Join a table to itself*

```sql
-- Find employees and their managers (same table)
SELECT e.name AS employee, m.name AS manager
FROM employees e
LEFT JOIN employees m ON e.manager_id = m.id;
```

---

## Subqueries

```sql
-- Subquery in WHERE
SELECT name FROM users
WHERE id IN (SELECT user_id FROM orders WHERE total > 100);

-- Subquery in FROM (derived table)
SELECT country, avg_age FROM (
    SELECT country, AVG(age) AS avg_age
    FROM users
    GROUP BY country
) AS country_stats
WHERE avg_age > 25;

-- Correlated subquery (references outer query)
SELECT name, (
    SELECT COUNT(*) FROM orders WHERE orders.user_id = users.id
) AS order_count
FROM users;

-- EXISTS
SELECT name FROM users u
WHERE EXISTS (
    SELECT 1 FROM orders o WHERE o.user_id = u.id
);
```

---

## Common Table Expressions (CTEs)
*Readable, reusable subqueries*

```sql
-- Simple CTE
WITH recent_orders AS (
    SELECT user_id, SUM(total) AS total_spent
    FROM orders
    WHERE created_at > NOW() - INTERVAL '30 days'
    GROUP BY user_id
)
SELECT u.name, r.total_spent
FROM users u
JOIN recent_orders r ON u.id = r.user_id
ORDER BY r.total_spent DESC;

-- Multiple CTEs
WITH
  active_users AS (
    SELECT id FROM users WHERE last_login > NOW() - INTERVAL '7 days'
  ),
  user_orders AS (
    SELECT user_id, COUNT(*) AS order_count
    FROM orders
    WHERE user_id IN (SELECT id FROM active_users)
    GROUP BY user_id
  )
SELECT u.name, uo.order_count
FROM users u
JOIN user_orders uo ON u.id = uo.user_id;
```

---

## Window Functions
*Calculations across rows without collapsing them*

```sql
-- ROW_NUMBER: rank rows within a partition
SELECT name, country,
    ROW_NUMBER() OVER (PARTITION BY country ORDER BY name) AS row_num
FROM users;

-- RANK: allows ties (gaps in ranking)
SELECT name, total,
    RANK() OVER (ORDER BY total DESC) AS rank
FROM orders;

-- Running total
SELECT id, total,
    SUM(total) OVER (ORDER BY created_at) AS running_total
FROM orders;

-- Moving average (last 3 rows)
SELECT id, total,
    AVG(total) OVER (ORDER BY created_at ROWS BETWEEN 2 PRECEDING AND CURRENT ROW) AS moving_avg
FROM orders;

-- LAG / LEAD: access previous/next row
SELECT id, total,
    LAG(total) OVER (ORDER BY created_at)  AS prev_total,
    LEAD(total) OVER (ORDER BY created_at) AS next_total
FROM orders;
```

---

## String Functions

```sql
UPPER(name)                   -- 'alice' → 'ALICE'
LOWER(email)                  -- 'ALICE@...' → 'alice@...'
LENGTH(name)                  -- number of characters
TRIM(name)                    -- remove leading/trailing spaces
SUBSTRING(name, 1, 3)         -- first 3 chars
CONCAT(first_name, ' ', last_name)
name || ' (' || email || ')'  -- string concatenation (PostgreSQL)
REPLACE(name, 'old', 'new')
SPLIT_PART(email, '@', 2)     -- domain part of email (PostgreSQL)
```

## Date Functions

```sql
NOW()                         -- current timestamp with timezone
CURRENT_DATE                  -- current date
CURRENT_TIME                  -- current time
DATE_TRUNC('month', created_at)  -- truncate to month start
EXTRACT(YEAR FROM created_at)    -- extract part
AGE(created_at)               -- interval since date (PostgreSQL)
created_at + INTERVAL '7 days'   -- add 7 days
```

---

## Best Practices

- Use `JOIN` instead of subqueries where possible (optimizer handles it better)
- Always specify columns in `SELECT` for production code — avoid `SELECT *`
- Use CTEs for readability in complex queries
- Use `EXPLAIN ANALYZE` to understand query execution
- Add `LIMIT` when exploring unknown tables
- `HAVING` = filter on aggregates, `WHERE` = filter on rows
