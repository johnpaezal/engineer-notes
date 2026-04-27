# Architecture Diagrams
*Visualizing software systems*

## Why Diagrams Matter
*A good diagram replaces 1000 words*

**Purpose** – Communicate architecture to team members, stakeholders, new developers  
**Rule** – A diagram should answer one specific question  
**Tools** – Mermaid (text-based), draw.io, Lucidchart, C4-PlantUML, Excalidraw

---

## C4 Model
*4 levels of zoom for architecture*

**C4** – Context, Containers, Components, Code  
**Key idea** – Each level zooms into more detail

### Level 1 – System Context
*Who uses the system and what external systems does it interact with*

```
┌──────────────────────────────────────────────┐
│                                              │
│  [User] ──────────────► [My App]             │
│                              │               │
│                         ┌────┘               │
│                         ▼                    │
│                    [Stripe API]               │
│                    [SendGrid]                 │
│                    [Google OAuth]             │
│                                              │
└──────────────────────────────────────────────┘
```

### Level 2 – Container
*Applications, databases, services that make up the system*

```
┌─────────────────────────────────────────────────────┐
│  My App                                             │
│                                                     │
│  [Browser] ──HTTPS──► [React SPA]                   │
│                              │                      │
│                         REST API                    │
│                              ▼                      │
│                       [FastAPI Backend]              │
│                        /           \                │
│                       ▼             ▼               │
│               [PostgreSQL]     [Redis Cache]         │
│                                     │               │
│                              [Celery Workers]        │
└─────────────────────────────────────────────────────┘
```

### Level 3 – Component
*Modules inside a container*

```
┌──────────────────────────────────────────────┐
│  FastAPI Backend                             │
│                                              │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐   │
│  │  Auth    │  │  Orders  │  │ Products │   │
│  │ Router   │  │ Router   │  │  Router  │   │
│  └────┬─────┘  └────┬─────┘  └────┬─────┘   │
│       │              │              │        │
│  ┌────▼─────┐  ┌────▼─────┐  ┌────▼─────┐  │
│  │  Auth    │  │  Orders  │  │ Products │  │
│  │ Service  │  │ Service  │  │  Service │  │
│  └────┬─────┘  └────┬─────┘  └────┬─────┘  │
│       │              │              │       │
│  ┌────▼──────────────▼──────────────▼────┐  │
│  │           Repositories                │  │
│  └───────────────────────────────────────┘  │
└──────────────────────────────────────────────┘
```

---

## Mermaid Diagrams
*Text-based diagrams in Markdown*

### Flowchart

```mermaid
graph TD
    A[User] -->|HTTP Request| B[API Gateway]
    B --> C{Auth OK?}
    C -->|Yes| D[Order Service]
    C -->|No| E[401 Unauthorized]
    D --> F[(Database)]
    D --> G[Queue]
    G --> H[Email Service]
```

### Sequence Diagram

```mermaid
sequenceDiagram
    participant U as User
    participant A as API
    participant D as Database
    participant E as Email Service

    U->>A: POST /orders
    A->>D: INSERT order
    D-->>A: order_id = 42
    A->>Queue: publish order.created
    A-->>U: 201 Created {order_id: 42}
    Queue->>E: order.created event
    E-->>U: confirmation email
```

### Architecture Diagram

```mermaid
graph LR
    subgraph Internet
        User
        CDN
    end

    subgraph AWS
        ALB[Load Balancer]
        subgraph ECS
            API1[API Instance 1]
            API2[API Instance 2]
        end
        RDS[(PostgreSQL RDS)]
        Redis[(ElastiCache)]
        S3[(S3 Bucket)]
    end

    User --> CDN
    User --> ALB
    CDN --> S3
    ALB --> API1
    ALB --> API2
    API1 --> RDS
    API1 --> Redis
    API2 --> RDS
    API2 --> Redis
```

### State Diagram

```mermaid
stateDiagram-v2
    [*] --> Pending
    Pending --> Processing : payment confirmed
    Processing --> Shipped : items packed
    Shipped --> Delivered : courier delivered
    Processing --> Cancelled : out of stock
    Pending --> Cancelled : user cancelled
    Delivered --> [*]
    Cancelled --> [*]
```

### ER Diagram

```mermaid
erDiagram
    USER {
        int id PK
        string name
        string email
        datetime created_at
    }

    ORDER {
        int id PK
        int user_id FK
        decimal total
        string status
        datetime created_at
    }

    ORDER_ITEM {
        int id PK
        int order_id FK
        int product_id FK
        int quantity
        decimal price
    }

    PRODUCT {
        int id PK
        string name
        decimal price
        int stock
    }

    USER ||--o{ ORDER : places
    ORDER ||--|{ ORDER_ITEM : contains
    PRODUCT ||--o{ ORDER_ITEM : included_in
```

---

## When to Use Each Diagram

| Diagram | Use for |
|---|---|
| C4 Context | Onboarding, stakeholder communication |
| C4 Container | Team architecture overview |
| C4 Component | Deep-dive into one service |
| Flowchart | Decision logic, process flows |
| Sequence | API interactions, event flows |
| State | Order/workflow lifecycle |
| ER Diagram | Database design |
| Architecture | Infrastructure overview |

---

## Best Practices

- One diagram = one question answered
- Include a title and brief description
- Keep it simple — remove anything that doesn't add clarity
- Version diagrams in git alongside code (use Mermaid or PlantUML)
- Update diagrams when architecture changes
- Use consistent shapes: rectangles = services, cylinders = databases, diamonds = decisions
