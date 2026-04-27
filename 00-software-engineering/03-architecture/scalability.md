# Scalability & Reliability
*Building systems that grow and stay up*

## Scalability
*Handling more load*

**Vertical Scaling (Scale Up)** – Bigger machine (more CPU, RAM)  
**Horizontal Scaling (Scale Out)** – More machines (add instances)

```
Vertical:
  Server: 2 CPU, 4GB RAM  →  8 CPU, 32GB RAM
  Limit: hardware ceiling, single point of failure

Horizontal:
  1 server → 3 servers (behind load balancer)
  Limit: stateless design required
```

---

## Horizontal Scaling Requirements
*What your app needs to scale horizontally*

```
✓ Stateless – no local session/memory between requests
✓ Shared state in external store (Redis, DB)
✓ Load balancer in front
✓ Shared file storage (S3, EFS — not local disk)
✓ Database can handle multiple app connections

❌ Sessions stored in memory (lost on restart)
❌ Files written to local disk
❌ Hardcoded IPs
```

---

## High Availability (HA)
*Minimizing downtime*

**High Availability** – System remains operational despite failures  
**SLA** – Service Level Agreement (uptime commitment)

```
Uptime SLA:
  99%      → 87.6 hours downtime/year
  99.9%    → 8.76 hours downtime/year   (3 nines)
  99.99%   → 52.6 minutes downtime/year (4 nines)
  99.999%  → 5.26 minutes downtime/year (5 nines)
```

### HA Patterns

**Redundancy** – Multiple instances of everything  
**Failover** – Automatic switch to backup on failure  
**Health checks** – Load balancer removes unhealthy instances

```
Multi-AZ deployment (AWS):
  AZ-1: App Instance + DB Primary
  AZ-2: App Instance + DB Replica
         ↑
  Load Balancer routes to healthy instances
  DB fails over automatically to replica
```

---

## Fault Tolerance
*Handling failures gracefully*

**Graceful degradation** – Reduce functionality instead of total failure

```python
def get_product(product_id):
    try:
        # Try cache first
        return cache.get(f"product:{product_id}")
    except CacheError:
        # Cache down → fall back to DB
        return db.get_product(product_id)

def get_recommendations(user_id):
    try:
        return recommendation_service.get(user_id)
    except ServiceUnavailable:
        # Recommendation service down → return popular items
        return get_popular_items()
```

**Timeout** – Don't wait forever for a response

```python
response = requests.get(url, timeout=5)  # fail after 5 seconds
```

**Retry with backoff** – Retry failed requests with increasing delay

```python
for attempt in range(3):
    try:
        return api.call()
    except TemporaryError:
        if attempt == 2:
            raise
        time.sleep(2 ** attempt)  # 1s, 2s, 4s
```

---

## CAP Theorem
*Fundamental trade-off in distributed systems*

**C – Consistency** – All nodes see the same data at the same time  
**A – Availability** – Every request gets a response (not guaranteed to be latest)  
**P – Partition Tolerance** – System works despite network splits

**Rule** – In a distributed system, you can only guarantee 2 of 3

```
CP (Consistency + Partition): PostgreSQL, MongoDB (strong consistency)
  → On network split: refuse requests to maintain consistency

AP (Availability + Partition): DynamoDB, Cassandra (eventual consistency)
  → On network split: serve possibly stale data

CA (Consistency + Availability): only possible without network partitions
  → Not realistic in distributed systems
```

---

## Caching Strategies for Scale

```
CDN          → static assets (images, JS, CSS)        milliseconds
Redis        → DB query results, sessions              <1ms
DB Read Replica → offload read queries from primary
DB Connection Pool → reuse connections, limit spikes
```

---

## Database Scaling

**Read Replica** – Copy of DB for read-only queries (scales reads)

```
Writes → Primary DB
Reads  → Read Replica 1 or 2
```

**Sharding** – Split data across multiple DBs by key

```
user_id 1-1000   → DB Shard 1
user_id 1001-2000 → DB Shard 2
```

**Connection Pooling** – Reuse DB connections

```python
# PgBouncer, SQLAlchemy pool
engine = create_engine(url, pool_size=10, max_overflow=20)
```

---

## Performance Metrics

**Throughput** – Requests per second the system handles  
**Latency** – Time to respond to one request  
**p50 / p95 / p99** – Median, 95th, 99th percentile response times

```
p50 = 50ms   → half of requests faster than 50ms
p95 = 200ms  → 95% of requests faster than 200ms
p99 = 1000ms → 99% of requests faster than 1s
              ↑ watch this — worst-case for most users
```

---

## Best Practices

- Design for failure — assume any component can fail
- Use health checks on every service
- Set timeouts on all external calls
- Monitor p95/p99 latency, not just averages
- Test failure scenarios (chaos engineering)
- Use multiple availability zones for critical systems
- Auto-scaling based on metrics (CPU, request rate)
