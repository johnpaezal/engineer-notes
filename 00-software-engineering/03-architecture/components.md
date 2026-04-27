# Architecture Components
*Building blocks of software systems*

## API Gateway
*Single entry point for all client requests*

**API Gateway** – Reverse proxy that routes requests to backend services

```
Clients ──► API Gateway ──► User Service
  (web)          │       ──► Order Service
  (mobile)       │       ──► Payment Service
  (3rd party)    │
                 └── handles: auth, rate limiting, SSL, logging
```

**Responsibilities** – Authentication, rate limiting, routing, SSL termination, logging  
**Examples** – AWS API Gateway, Kong, Nginx, Traefik

---

## Load Balancer
*Distributes traffic across multiple instances*

```
                 ┌──► Server 1
Clients ──► LB ──┼──► Server 2
                 └──► Server 3
```

### Load Balancing Algorithms

**Round Robin** – Rotate through servers in order  
**Least Connections** – Send to server with fewest active connections  
**IP Hash** – Same client always goes to same server (sticky sessions)  
**Weighted** – Send more traffic to more powerful servers

### Load Balancer Types

**Layer 4 (Transport)** – Routes by IP + port (fast, no content inspection)  
**Layer 7 (Application)** – Routes by HTTP content (URL, headers, cookies)

```
L7 routing example:
  /api/*      → API servers
  /static/*   → CDN / storage
  /admin/*    → admin servers
```

**AWS** – ALB (Application, L7) and NLB (Network, L4)

---

## Cache
*Store frequently accessed data for fast retrieval*

```
Without cache:          With cache:
Request → DB (50ms)     Request → Cache hit (1ms)
                        Request → Cache miss → DB → Cache → (51ms first, 1ms after)
```

### Cache Strategies

**Cache-aside (Lazy loading)** – App checks cache first, loads from DB on miss

```python
def get_user(user_id):
    user = cache.get(f"user:{user_id}")
    if user is None:
        user = db.get_user(user_id)
        cache.set(f"user:{user_id}", user, ttl=300)
    return user
```

**Write-through** – Write to cache and DB simultaneously  
**Write-behind** – Write to cache, async write to DB later  
**Read-through** – Cache handles DB read automatically

### Cache Invalidation

**TTL (Time To Live)** – Expire after fixed time  
**Event-based** – Invalidate when data changes  
**Manual** – Explicitly delete key on update

```python
def update_user(user_id, data):
    db.update_user(user_id, data)
    cache.delete(f"user:{user_id}")  # invalidate
```

**Tools** – Redis, Memcached, CDN (for static assets)

---

## CDN – Content Delivery Network
*Serve static content from servers close to users*

```
User in Colombia ──► CDN Edge (Bogotá) ──► file served locally
                     (not going to US origin server)
```

**Purpose** – Reduce latency for static assets (images, JS, CSS, videos)  
**Examples** – CloudFront (AWS), Cloudflare, Fastly, Akamai

```
Origin Server (US East) ──► CDN caches globally
                              ├── Edge: São Paulo
                              ├── Edge: Madrid
                              └── Edge: Tokyo
```

---

## Database
*Persistence layer*

### SQL (Relational)

**Use when** – Structured data, relationships, ACID transactions needed

```
PostgreSQL, MySQL, SQLite
Tables, schemas, foreign keys, joins
```

### NoSQL

**Document** – JSON-like documents (MongoDB, DynamoDB)
```json
{"user_id": 1, "name": "Alice", "orders": [101, 102]}
```

**Key-Value** – Simple lookups (Redis, DynamoDB)
```
key: "session:abc123" → value: {"user_id": 1}
```

**Column** – Wide tables, analytics (Cassandra, Redshift)  
**Graph** – Relationships as first class (Neo4j)

---

## Message Queue
*Async communication between services*

```
Producer ──► [Queue] ──► Consumer
(OrderSvc)              (EmailSvc)
```

**Tools** – SQS, RabbitMQ, Kafka  
*(See 13-message-queues.md for full detail)*

---

## Reverse Proxy
*Intermediary between client and server*

```
Client ──► Reverse Proxy (Nginx) ──► App Server
```

**Responsibilities** – SSL termination, compression, caching, routing, security  
**Tools** – Nginx, Caddy, HAProxy, Traefik

```nginx
# Nginx reverse proxy config
server {
    listen 443 ssl;
    server_name api.myapp.com;

    location / {
        proxy_pass http://localhost:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

---

## Service Discovery
*How services find each other dynamically*

**Problem** – In microservices, IPs change constantly (containers restart)  
**Solution** – Services register themselves, others discover by name

```
Service A wants to call Service B:
  ❌ Hardcoded: http://192.168.1.10:8080  (IP can change)
  ✅ Discovery:  http://user-service/      (resolves dynamically)
```

**Tools** – AWS Service Discovery, Consul, Kubernetes DNS

---

## Key Architecture Decisions

| Need | Solution |
|---|---|
| High traffic | Load balancer + horizontal scaling |
| Slow DB reads | Cache (Redis) |
| Static assets | CDN |
| Service decoupling | Message queue |
| Single entry point | API Gateway |
| Flexible routing | Reverse proxy |
