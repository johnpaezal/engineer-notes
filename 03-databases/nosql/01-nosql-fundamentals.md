# NoSQL Fundamentals
*Non-relational databases for specific use cases*

## What is NoSQL
*Databases that don't use the relational model*

**NoSQL** – "Not only SQL" — databases designed for specific data models and scale  
**When to use**: Flexible schema, massive scale, specific access patterns, non-tabular data

### SQL vs NoSQL

| | SQL (Relational) | NoSQL |
|---|---|---|
| Schema | Fixed, predefined | Flexible, dynamic |
| Data model | Tables with rows | Documents, key-value, wide-column, graph |
| Relationships | JOINs | Embedded or references |
| ACID | Full ACID | Varies (eventual consistency common) |
| Scaling | Vertical (mainly) | Horizontal (designed for it) |
| Query language | SQL (standard) | DB-specific API |
| Best for | Complex queries, relations | Scale, simple access patterns |

---

## NoSQL Types

### 1. Document (MongoDB, DynamoDB, Firestore)
*Data stored as documents (JSON/BSON)*

```json
// users collection — MongoDB
{
  "_id": "64abc123",
  "name": "Alice",
  "email": "alice@example.com",
  "address": {
    "city": "New York",
    "country": "US"
  },
  "orders": [
    { "id": 1, "total": 99.99 },
    { "id": 2, "total": 49.99 }
  ]
}
```

**Good for**: Content management, user profiles, catalogs, e-commerce  
**Key feature**: Embed related data in one document (no JOINs needed for common access)

### 2. Key-Value (Redis, DynamoDB, Memcached)
*Simple mapping: key → value*

```
key: "session:user123"
value: {"userId": 123, "role": "admin", "exp": 1700000000}

key: "product:456:price"
value: "29.99"
```

**Good for**: Caching, sessions, feature flags, rate limiting, leaderboards  
**Key feature**: Extremely fast (O(1) reads and writes)

### 3. Wide-Column (Cassandra, HBase, DynamoDB)
*Rows with dynamic columns, optimized for large-scale writes*

```
Table: sensor_readings
Partition key: sensor_id

sensor_id | 2024-01-01 00:00 | 2024-01-01 00:01 | 2024-01-01 00:02
sensor_1  | 22.5°C          | 22.8°C          | 23.1°C
sensor_2  | 18.0°C          | 18.2°C          | 18.5°C
```

**Good for**: Time-series data, IoT, event logs, high-write workloads  
**Key feature**: Scales horizontally across many nodes

### 4. Graph (Neo4j, Amazon Neptune)
*Data as nodes and edges (relationships)*

```
(Alice) -[FOLLOWS]→ (Bob)
(Alice) -[PURCHASED]→ (Product: Laptop)
(Bob)   -[REVIEWED]→ (Product: Laptop)
```

**Good for**: Social networks, recommendation engines, fraud detection, knowledge graphs  
**Key feature**: Traverse relationships efficiently

---

## DynamoDB (AWS)
*Key-value and document DB, fully managed by AWS*

### Core Concepts

**Table** – Collection of items (like a SQL table)  
**Item** – A record (like a row), can have any attributes  
**Attribute** – Key-value pair within an item  
**Primary Key** – Uniquely identifies each item

### Primary Key Types

```
1. Partition Key only (simple PK)
   ├── Table: users
   └── PK: user_id = "u123"

2. Partition Key + Sort Key (composite PK)
   ├── Table: orders
   ├── PK (partition): user_id = "u123"
   └── SK (sort): order_date = "2024-01-15"
   → Can store multiple orders per user
```

### DynamoDB Example (Python Boto3)

```python
import boto3

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('users')

# Put item (create or replace)
table.put_item(Item={
    'user_id': 'u123',
    'name': 'Alice',
    'email': 'alice@example.com',
    'created_at': '2024-01-15T10:00:00Z'
})

# Get item by primary key
response = table.get_item(Key={'user_id': 'u123'})
user = response['Item']

# Update item
table.update_item(
    Key={'user_id': 'u123'},
    UpdateExpression='SET #n = :name',
    ExpressionAttributeNames={'#n': 'name'},
    ExpressionAttributeValues={':name': 'Alice Updated'}
)

# Delete item
table.delete_item(Key={'user_id': 'u123'})

# Query (requires partition key)
response = table.query(
    KeyConditionExpression='user_id = :uid',
    ExpressionAttributeValues={':uid': 'u123'}
)

# Scan (avoid in production — reads entire table)
response = table.scan(
    FilterExpression='country = :c',
    ExpressionAttributeValues={':c': 'US'}
)
```

### DynamoDB Access Patterns

```
Design DynamoDB tables around access patterns, not entities.

Access pattern: "Get all orders for a user, sorted by date"
→ PK: user_id, SK: order_date

Access pattern: "Get user by email"
→ Create a Global Secondary Index (GSI) on email
```

### GSI (Global Secondary Index)

```python
# Define GSI when creating table
table = dynamodb.create_table(
    TableName='users',
    KeySchema=[
        {'AttributeName': 'user_id', 'KeyType': 'HASH'}
    ],
    GlobalSecondaryIndexes=[{
        'IndexName': 'email-index',
        'KeySchema': [{'AttributeName': 'email', 'KeyType': 'HASH'}],
        'Projection': {'ProjectionType': 'ALL'}
    }]
)

# Query by GSI
response = table.query(
    IndexName='email-index',
    KeyConditionExpression='email = :e',
    ExpressionAttributeValues={':e': 'alice@example.com'}
)
```

---

## Redis
*In-memory key-value store — extremely fast*

### Use Cases

```
Caching         → store DB query results
Session store   → user sessions
Rate limiting   → count requests per IP
Pub/Sub         → real-time messaging
Leaderboards    → sorted sets
Distributed locks → prevent race conditions
```

### Data Structures

```bash
# String
SET user:123:name "Alice"
GET user:123:name
SET session:token "eyJ..." EX 3600   # expires in 1 hour

# Hash (object)
HSET user:123 name "Alice" email "alice@example.com"
HGET user:123 name
HGETALL user:123

# List (queue/stack)
RPUSH queue:emails "email1" "email2"   # push to right
LPOP queue:emails                       # pop from left (FIFO queue)

# Set (unique values)
SADD user:123:tags "admin" "premium"
SMEMBERS user:123:tags
SISMEMBER user:123:tags "admin"   # is "admin" in set?

# Sorted Set (leaderboard)
ZADD leaderboard 1500 "alice" 2200 "bob" 800 "carol"
ZREVRANGE leaderboard 0 9 WITHSCORES   # top 10

# Increment (rate limiting)
INCR api:rate:ip:192.168.1.1
EXPIRE api:rate:ip:192.168.1.1 60    # reset after 60 seconds
```

### Caching Pattern (Python)

```python
import redis
import json

r = redis.Redis(host='localhost', port=6379, db=0)

def get_user(user_id):
    cache_key = f"user:{user_id}"
    
    # Check cache first
    cached = r.get(cache_key)
    if cached:
        return json.loads(cached)
    
    # Cache miss → query DB
    user = db.query("SELECT * FROM users WHERE id = %s", user_id)
    
    # Store in cache for 5 minutes
    r.setex(cache_key, 300, json.dumps(user))
    return user
```

---

## Choosing the Right Database

| Scenario | Database |
|---|---|
| Complex queries, reporting, financial data | PostgreSQL / MySQL |
| User profiles, catalogs, flexible schema | MongoDB / DynamoDB |
| Caching, sessions, rate limiting | Redis |
| Massive write throughput, IoT, time-series | Cassandra / DynamoDB |
| Social graphs, recommendations | Neo4j / Neptune |
| Full-text search | Elasticsearch / OpenSearch |
| Simple AWS-native NoSQL | DynamoDB |

---

## Best Practices

- Don't use NoSQL just because it's "modern" — SQL is still the right choice for most apps
- Design DynamoDB around access patterns, not entities
- Always set TTL (expiration) on Redis cache keys
- Use Redis for caching, not as primary storage (unless you accept data loss)
- DynamoDB: avoid Scan operations in production (full table read)
- MongoDB: avoid deeply nested documents (hard to query and index)
- NoSQL consistency: understand eventual vs strong consistency for your use case
