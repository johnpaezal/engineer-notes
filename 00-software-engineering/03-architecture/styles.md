# Architecture Styles
*High-level patterns for structuring a system*

## Monolith
*Single deployable unit containing everything*

```
┌─────────────────────────────┐
│         Monolith            │
│  ┌──────┐ ┌──────┐ ┌──────┐│
│  │ Auth │ │Orders│ │Email ││
│  └──────┘ └──────┘ └──────┘│
│         Single DB           │
└─────────────────────────────┘
         │
    deploy as one
```

**Pros** – Simple to develop, test, deploy; low latency (in-process calls)  
**Cons** – Hard to scale independently; one failure can crash all; slow deploys as it grows

**Use when** – Starting out, small team, simple domain

---

## Microservices
*System split into small, independent services*

```
         API Gateway
        /     |      \
   Auth   Orders   Inventory
   Service Service  Service
     │        │         │
   Auth DB  Orders DB  Inv DB
```

**Pros** – Independent scaling, deploy, and tech stack per service; fault isolation  
**Cons** – Distributed system complexity; network latency; harder to debug; operational overhead

**Use when** – Large team, clear domain boundaries, need independent scaling

---

## Layered Architecture (N-Tier)
*Code organized in horizontal layers*

```
┌──────────────────┐
│ Presentation     │  Controllers, API endpoints
├──────────────────┤
│ Business Logic   │  Services, use cases
├──────────────────┤
│ Data Access      │  Repositories, DB queries
├──────────────────┤
│ Database         │  PostgreSQL, MongoDB
└──────────────────┘
```

**Rule** – Each layer only talks to the layer directly below it  
**Use when** – Most web applications, clear CRUD domains

---

## Hexagonal Architecture (Ports & Adapters)
*Business logic isolated from external concerns*

```
        [ REST API ]  [ CLI ]  [ Tests ]
               ↓         ↓        ↓
          ┌────────────────────┐
          │    Application     │
          │   (Business Logic) │  ← no framework, no DB knowledge
          └────────────────────┘
               ↓         ↓
        [ PostgreSQL ] [ Email API ]
```

**Port** – Interface the business logic defines (e.g., `UserRepository`)  
**Adapter** – Implementation that plugs into the port (e.g., `PostgreSQLUserRepository`)  
**Benefit** – Business logic testable without DB or HTTP framework

---

## Event-Driven Architecture
*Services communicate through events*

```
OrderService ──publishes──► order.placed ──► EmailService
                                        └──► InventoryService
```

**Pros** – Decoupled, resilient, scalable  
**Cons** – Complex to debug, eventual consistency  
**Use when** – High throughput, services with different scaling needs

---

## Serverless
*Run code without managing servers*

```
HTTP Request ──► API Gateway ──► Lambda Function ──► DynamoDB
                                 (runs only when triggered)
```

**Pros** – No server management, auto-scaling, pay per invocation  
**Cons** – Cold starts, stateless, limited execution time  
**Use when** – Sporadic/unpredictable traffic, event-driven tasks

---

## Comparison

| Style | Team Size | Complexity | Scalability |
|---|---|---|---|
| Monolith | Small | Low | Limited |
| Layered | Any | Medium | Vertical |
| Microservices | Large | High | Horizontal |
| Hexagonal | Any | Medium | Flexible |
| Serverless | Any | Medium | Automatic |

---

## Best Practices

- Start with a monolith, extract microservices only when needed
- Don't over-engineer for scale you don't have yet
- Define clear boundaries between layers/services
- Each service/module should be independently testable
