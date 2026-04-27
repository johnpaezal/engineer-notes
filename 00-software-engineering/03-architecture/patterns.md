# Architecture Patterns
*Proven solutions to recurring system-level problems*

## Repository Pattern
*Abstracts data access from business logic*

```python
# Interface (port)
class UserRepository(ABC):
    @abstractmethod
    def find_by_id(self, user_id: int) -> User: ...

    @abstractmethod
    def save(self, user: User) -> User: ...

# Implementation (adapter)
class PostgreSQLUserRepository(UserRepository):
    def find_by_id(self, user_id: int) -> User:
        row = db.query("SELECT * FROM users WHERE id = %s", user_id)
        return User(id=row.id, name=row.name)

    def save(self, user: User) -> User:
        db.execute("INSERT INTO users ...", user)
        return user

# Service uses the interface, not the implementation
class UserService:
    def __init__(self, repo: UserRepository):
        self.repo = repo  # can be PostgreSQL, MongoDB, or Mock
```

---

## CQRS – Command Query Responsibility Segregation
*Separate read and write models*

```
Write side:                     Read side:
  Command: CreateOrder            Query: GetOrderSummary
  Handler: validates + saves      Handler: reads optimized view
  Model: normalized DB            Model: denormalized read model

Commands → Write DB ──► events ──► Read DB (projections)
                                        ↑
                                   Queries read here
```

**Use when** – High read/write ratio difference, complex queries, event sourcing

---

## Event Sourcing
*Store events, not current state*

```
Traditional:
  DB stores: {order_id: 1, status: "shipped", total: 99}

Event Sourcing:
  DB stores events:
    order.created  {order_id: 1, total: 99}
    order.paid     {order_id: 1, amount: 99}
    order.shipped  {order_id: 1, tracking: "XYZ"}

Current state = replay all events
```

**Pros** – Full audit trail, time travel, replay events  
**Cons** – Complex, eventual consistency, schema evolution hard

---

## Saga Pattern
*Manage distributed transactions across services*

**Problem** – No single transaction across microservices  
**Solution** – Sequence of local transactions with compensation on failure

```
Choreography (events):
  OrderService: order.created ──►
  PaymentService: payment.processed ──►
  InventoryService: stock.reserved ──►
  ShippingService: shipment.created

On failure:
  ShippingService fails → shipment.failed ──►
  InventoryService: stock.released ──►
  PaymentService: payment.refunded ──►
  OrderService: order.cancelled
```

---

## Circuit Breaker
*Stop calling failing services, fail fast*

```
States:
  CLOSED   → normal, requests pass through
  OPEN     → too many failures, reject all requests immediately
  HALF-OPEN → test if service recovered

CLOSED ──(5 failures in 10s)──► OPEN
OPEN ──(30s timeout)──► HALF-OPEN
HALF-OPEN ──(success)──► CLOSED
HALF-OPEN ──(failure)──► OPEN
```

```python
# Without circuit breaker
def get_user(user_id):
    return external_api.get(f"/users/{user_id}")  # hangs 30s if down

# With circuit breaker
@circuit_breaker(failure_threshold=5, timeout=30)
def get_user(user_id):
    return external_api.get(f"/users/{user_id}")
# If open: raises CircuitOpenError immediately
```

**Libraries** – `pybreaker` (Python), Hystrix (Java), Resilience4j (Java)

---

## Strangler Fig Pattern
*Gradually replace legacy system*

```
Phase 1: Legacy handles everything
  All requests ──► Legacy App

Phase 2: Proxy routes some to new services
  New feature ──► New Service
  Old feature ──► Legacy App (via proxy/API gateway)

Phase 3: Legacy retired
  All requests ──► New Services
```

**Use when** – Migrating from monolith to microservices incrementally

---

## Sidecar Pattern
*Attach helper container to main service*

```
Pod / Task:
  ┌──────────────────────────────┐
  │  Main Container (API)        │
  │  + Sidecar (log collector)   │
  │  + Sidecar (service mesh)    │
  └──────────────────────────────┘
```

**Use cases** – Log shipping, metrics collection, service mesh (Envoy)  
**Common in** – Kubernetes, ECS

---

## BFF – Backend for Frontend
*Separate API per client type*

```
Mobile App ──► Mobile BFF ──► Microservices
Web App    ──► Web BFF    ──────────────────
Third Party──► Public API ──────────────────
```

**Why** – Mobile needs different data shape than web; avoids over/under-fetching  
**Use when** – Multiple different clients with different data needs

---

## Pattern Selection Guide

| Problem | Pattern |
|---|---|
| Coupled data access | Repository |
| High read/write difference | CQRS |
| Full audit trail needed | Event Sourcing |
| Distributed transactions | Saga |
| External service failures | Circuit Breaker |
| Legacy migration | Strangler Fig |
| Cross-cutting concerns | Sidecar |
| Multiple client types | BFF |
