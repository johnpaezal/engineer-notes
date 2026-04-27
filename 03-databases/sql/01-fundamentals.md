# SQL Fundamentals
*Core concepts and data types*

## What is a Database
*Organized storage for structured data*

**Database** – Organized collection of structured data  
**RDBMS** – Relational Database Management System (PostgreSQL, MySQL, SQLite, SQL Server)  
**Table** – Collection of rows and columns (like a spreadsheet)  
**Schema** – Blueprint defining tables, columns, and their types

```
Database: ecommerce
├── Table: users       (id, name, email, created_at)
├── Table: products    (id, name, price, stock)
└── Table: orders      (id, user_id, product_id, total)
```

---

## Data Types
*Choosing the right type for each column*

### Numeric
```sql
INT             -- integer: -2,147,483,648 to 2,147,483,647
BIGINT          -- large integer (use for IDs in big tables)
SMALLINT        -- small integer (-32,768 to 32,767)
DECIMAL(p, s)   -- exact decimal: DECIMAL(10, 2) → 99999999.99
FLOAT           -- approximate decimal (avoid for money)
NUMERIC(p, s)   -- same as DECIMAL (PostgreSQL)
```

### Text
```sql
VARCHAR(n)      -- variable-length string, max n chars
CHAR(n)         -- fixed-length string (padded with spaces)
TEXT            -- unlimited text (no length limit)
```

### Date / Time
```sql
DATE            -- 2025-01-15
TIME            -- 14:30:00
TIMESTAMP       -- 2025-01-15 14:30:00
TIMESTAMPTZ     -- timestamp with timezone (PostgreSQL)
INTERVAL        -- duration (PostgreSQL)
```

### Other
```sql
BOOLEAN         -- TRUE / FALSE
UUID            -- universally unique identifier
JSON / JSONB    -- JSON data (JSONB = binary, indexed in PostgreSQL)
SERIAL          -- auto-incrementing integer (PostgreSQL)
AUTO_INCREMENT  -- auto-incrementing integer (MySQL)
```

---

## Keys and Constraints
*Enforcing data integrity*

```sql
CREATE TABLE users (
    id          SERIAL PRIMARY KEY,        -- auto-increment + unique + not null
    email       VARCHAR(255) UNIQUE,       -- must be unique across table
    name        VARCHAR(100) NOT NULL,     -- cannot be null
    age         INT CHECK (age >= 0),      -- must satisfy condition
    role        VARCHAR(20) DEFAULT 'user' -- default value
);

CREATE TABLE orders (
    id          SERIAL PRIMARY KEY,
    user_id     INT NOT NULL,
    total       DECIMAL(10, 2),
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);
```

### Constraint Types
| Constraint | What it does |
|---|---|
| `PRIMARY KEY` | Unique + Not null. One per table. |
| `UNIQUE` | All values in column must differ |
| `NOT NULL` | Column cannot be empty |
| `CHECK` | Value must pass a condition |
| `DEFAULT` | Value if none provided |
| `FOREIGN KEY` | References PK in another table |

### Foreign Key Actions
```sql
ON DELETE CASCADE    -- delete child rows when parent is deleted
ON DELETE SET NULL   -- set foreign key to NULL when parent deleted
ON DELETE RESTRICT   -- prevent deletion if child rows exist (default)
```

---

## DDL – Data Definition Language
*Defining the structure of the database*

```sql
-- Create table
CREATE TABLE products (
    id    SERIAL PRIMARY KEY,
    name  VARCHAR(100) NOT NULL,
    price DECIMAL(10, 2),
    stock INT DEFAULT 0
);

-- Add column
ALTER TABLE products ADD COLUMN category VARCHAR(50);

-- Rename column
ALTER TABLE products RENAME COLUMN category TO type;

-- Change column type
ALTER TABLE products ALTER COLUMN price TYPE NUMERIC(12, 2);

-- Drop column
ALTER TABLE products DROP COLUMN type;

-- Rename table
ALTER TABLE products RENAME TO items;

-- Delete table (irreversible)
DROP TABLE items;

-- Delete table only if it exists
DROP TABLE IF EXISTS items;
```

---

## DML – Data Manipulation Language
*Reading and writing data*

```sql
-- Insert one row
INSERT INTO users (name, email) VALUES ('Alice', 'alice@example.com');

-- Insert multiple rows
INSERT INTO users (name, email) VALUES
    ('Bob', 'bob@example.com'),
    ('Carol', 'carol@example.com');

-- Insert or ignore duplicates (PostgreSQL)
INSERT INTO users (email, name)
VALUES ('alice@example.com', 'Alice')
ON CONFLICT (email) DO NOTHING;

-- Insert or update on conflict
INSERT INTO users (email, name)
VALUES ('alice@example.com', 'Alice Updated')
ON CONFLICT (email) DO UPDATE SET name = EXCLUDED.name;

-- Read all rows
SELECT * FROM users;

-- Read specific columns
SELECT name, email FROM users;

-- Update
UPDATE users SET name = 'Bob Smith' WHERE id = 1;

-- Delete
DELETE FROM users WHERE id = 1;

-- Delete all rows (faster than DELETE with no WHERE)
TRUNCATE TABLE users;
```

---

## Best Practices

- Always use `SERIAL` or `UUID` for primary keys, not business values (email, phone)
- Use `DECIMAL` for money, never `FLOAT`
- Use `TIMESTAMPTZ` in PostgreSQL for timestamps (timezone-aware)
- Prefer `NOT NULL` where possible — nulls add complexity to queries
- Name foreign key columns `<table>_id` (e.g., `user_id`, `order_id`)
