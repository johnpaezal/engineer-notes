# Advanced SQL
*Views, stored procedures, triggers, and more*

## Views
*Saved queries as virtual tables*

**View** – A named query stored in the DB, used like a table  
**Materialized View** – View whose results are physically stored (refreshed manually)

```sql
-- Create a view
CREATE VIEW user_order_summary AS
SELECT
    u.id,
    u.name,
    COUNT(o.id)   AS total_orders,
    SUM(o.total)  AS total_spent
FROM users u
LEFT JOIN orders o ON u.id = o.user_id
GROUP BY u.id, u.name;

-- Use the view like a table
SELECT * FROM user_order_summary WHERE total_spent > 100;

-- Update view
CREATE OR REPLACE VIEW user_order_summary AS ...;

-- Drop view
DROP VIEW user_order_summary;
```

### Materialized Views (PostgreSQL)

```sql
-- Create (stores result physically)
CREATE MATERIALIZED VIEW monthly_sales AS
SELECT DATE_TRUNC('month', created_at) AS month, SUM(total) AS revenue
FROM orders
GROUP BY 1;

-- Refresh (update stored data)
REFRESH MATERIALIZED VIEW monthly_sales;

-- Auto-refresh: use a cron job or pg_cron extension
```

**Use when** – Expensive aggregations queried frequently (dashboards, reports)

---

## Stored Procedures & Functions
*Reusable logic stored in the database*

```sql
-- Function (returns a value, PostgreSQL)
CREATE OR REPLACE FUNCTION get_user_total(p_user_id INT)
RETURNS DECIMAL AS $$
BEGIN
    RETURN (
        SELECT COALESCE(SUM(total), 0)
        FROM orders
        WHERE user_id = p_user_id
    );
END;
$$ LANGUAGE plpgsql;

-- Call the function
SELECT get_user_total(1);
SELECT name, get_user_total(id) AS total FROM users;

-- Procedure (no return value, PostgreSQL 11+)
CREATE OR REPLACE PROCEDURE deactivate_user(p_user_id INT)
LANGUAGE plpgsql AS $$
BEGIN
    UPDATE users SET active = false WHERE id = p_user_id;
    INSERT INTO audit_log (action, user_id) VALUES ('deactivated', p_user_id);
    COMMIT;
END;
$$;

-- Call procedure
CALL deactivate_user(5);
```

---

## Triggers
*Automatic actions on table events*

```sql
-- Function to run on trigger
CREATE OR REPLACE FUNCTION update_updated_at()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = NOW();
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Attach trigger to table
CREATE TRIGGER set_updated_at
BEFORE UPDATE ON users
FOR EACH ROW
EXECUTE FUNCTION update_updated_at();

-- Audit log trigger
CREATE OR REPLACE FUNCTION log_user_delete()
RETURNS TRIGGER AS $$
BEGIN
    INSERT INTO audit_log (action, user_id, deleted_at)
    VALUES ('deleted', OLD.id, NOW());
    RETURN OLD;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER on_user_delete
AFTER DELETE ON users
FOR EACH ROW
EXECUTE FUNCTION log_user_delete();
```

---

## Schema Design Patterns

### Soft Delete
*Mark records as deleted instead of removing them*

```sql
ALTER TABLE users ADD COLUMN deleted_at TIMESTAMP;

-- Soft delete
UPDATE users SET deleted_at = NOW() WHERE id = 1;

-- Query only active users
SELECT * FROM users WHERE deleted_at IS NULL;

-- Create view for convenience
CREATE VIEW active_users AS
SELECT * FROM users WHERE deleted_at IS NULL;
```

### Audit Columns
*Track when and who changed records*

```sql
CREATE TABLE products (
    id         SERIAL PRIMARY KEY,
    name       VARCHAR(100),
    price      DECIMAL(10, 2),
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW(),
    created_by INT REFERENCES users(id),
    updated_by INT REFERENCES users(id)
);
```

### UUID Primary Keys
*Use when distributing across multiple DBs or exposing IDs in APIs*

```sql
-- PostgreSQL: enable extension
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

CREATE TABLE users (
    id    UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    email VARCHAR(255) UNIQUE
);

-- PostgreSQL 13+: built-in
CREATE TABLE users (
    id    UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    email VARCHAR(255) UNIQUE
);
```

---

## Normalization
*Organizing data to reduce redundancy*

### 1NF (First Normal Form)
*Each column holds atomic (indivisible) values*

```
❌ Not 1NF:
orders: id | products
        1  | "shirt, pants, shoes"   ← multiple values in one column

✅ 1NF:
order_items: order_id | product_name
             1        | shirt
             1        | pants
```

### 2NF (Second Normal Form)
*1NF + no partial dependency on composite PK*

```
❌ Not 2NF (composite PK: order_id + product_id):
order_items: order_id | product_id | product_name   ← product_name depends only on product_id

✅ 2NF: separate products table
products: id | name
order_items: order_id | product_id | quantity
```

### 3NF (Third Normal Form)
*2NF + no transitive dependency*

```
❌ Not 3NF:
employees: id | department_id | department_name   ← department_name depends on department_id, not id

✅ 3NF: separate departments table
departments: id | name
employees: id | department_id
```

---

## EXPLAIN ANALYZE Output

```sql
EXPLAIN ANALYZE
SELECT u.name, COUNT(o.id) AS orders
FROM users u
LEFT JOIN orders o ON u.id = o.user_id
WHERE u.country = 'US'
GROUP BY u.id, u.name;
```

```
Hash Left Join  (cost=... rows=...)
  Hash Cond: (o.user_id = u.id)
  ->  Seq Scan on orders        ← full scan (add index on user_id?)
  ->  Hash
        ->  Index Scan on users  ← using index on country
              Filter: (country = 'US')
Planning time: 1.5 ms
Execution time: 42.3 ms
```

**What to look for**:
- `Seq Scan` on large tables → missing index
- High `rows` estimates → outdated statistics (`ANALYZE tablename`)
- High `Execution time` → investigate joins and indexes

---

## Useful PostgreSQL Commands

```sql
-- Table info
\d tablename              -- describe table (psql)
\dt                       -- list all tables

-- Running queries
SELECT * FROM pg_stat_activity;   -- active connections

-- Table size
SELECT pg_size_pretty(pg_total_relation_size('users'));

-- Index usage
SELECT * FROM pg_stat_user_indexes WHERE relname = 'users';

-- Update statistics (helps query planner)
ANALYZE users;

-- Vacuum (reclaim dead rows space)
VACUUM ANALYZE users;
```
