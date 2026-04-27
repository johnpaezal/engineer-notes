# REST API Design
*Designing and documenting HTTP APIs*

## HTTP Basics
*Protocol for communication between client and server*

**HTTP** – Protocol for transferring data between client and server  
**Request** – Client sends to server (method + URL + headers + body)  
**Response** – Server replies (status code + headers + body)

### Methods
*Actions performed on resources*

**GET** – Read resource (no body)  
**POST** – Create resource  
**PUT** – Replace resource completely  
**PATCH** – Update resource partially  
**DELETE** – Remove resource

### Status Codes
*Server response meaning*

```
2xx – Success
  200 OK              – Request succeeded
  201 Created         – Resource created
  204 No Content      – Success, no body

4xx – Client Error
  400 Bad Request     – Invalid input
  401 Unauthorized    – Not authenticated
  403 Forbidden       – Authenticated but no permission
  404 Not Found       – Resource doesn't exist
  422 Unprocessable   – Validation failed

5xx – Server Error
  500 Internal Server Error – Unexpected server failure
  503 Service Unavailable   – Server temporarily down
```

---

## REST Principles
*Constraints that make an API RESTful*

**Stateless** – Each request contains all needed info (no session on server)  
**Resource-based** – URLs represent nouns, not actions  
**Uniform interface** – Consistent URL and method conventions

---

## URL Design
*Naming and structuring endpoints*

```
# Resources are nouns, plural
GET    /users              # list all users
POST   /users              # create user
GET    /users/{id}         # get one user
PUT    /users/{id}         # replace user
PATCH  /users/{id}         # update user
DELETE /users/{id}         # delete user

# Nested resources
GET    /users/{id}/orders  # orders for a user
GET    /orders/{id}/items  # items in an order

# Filtering, sorting, pagination (query params)
GET    /users?role=admin
GET    /products?sort=price&order=asc
GET    /products?page=2&limit=20
```

```
# ❌ Wrong – verbs in URL
POST   /createUser
GET    /getUserById/5
POST   /deleteUser/5

# ✅ Correct – nouns + HTTP methods
POST   /users
GET    /users/5
DELETE /users/5
```

---

## Request & Response
*Structure of data exchange*

### Request
```http
POST /users HTTP/1.1
Host: api.example.com
Content-Type: application/json
Authorization: Bearer <token>

{
  "name": "Alice",
  "email": "alice@example.com"
}
```

### Response
```http
HTTP/1.1 201 Created
Content-Type: application/json

{
  "id": 42,
  "name": "Alice",
  "email": "alice@example.com",
  "createdAt": "2025-01-15T10:30:00Z"
}
```

### Error Response
```json
{
  "error": "Validation failed",
  "details": [
    { "field": "email", "message": "Invalid email format" },
    { "field": "name", "message": "Name is required" }
  ]
}
```

---

## API Documentation
*OpenAPI / Swagger standard*

**OpenAPI** – Standard format to describe REST APIs (YAML or JSON)  
**Swagger UI** – Visual interface generated from OpenAPI spec

```yaml
# openapi.yaml
openapi: 3.0.0
info:
  title: Users API
  version: 1.0.0

paths:
  /users:
    get:
      summary: List all users
      responses:
        '200':
          description: Success
    post:
      summary: Create user
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CreateUser'
      responses:
        '201':
          description: Created
        '422':
          description: Validation error

components:
  schemas:
    CreateUser:
      type: object
      required: [name, email]
      properties:
        name:
          type: string
        email:
          type: string
          format: email
```

---

## Versioning
*Managing API changes without breaking clients*

```
# URL versioning (most common)
/api/v1/users
/api/v2/users

# Header versioning
Accept: application/vnd.api+json;version=2
```

---

## Authentication
*Identifying who is making the request*

**API Key** – Simple key sent in header (for server-to-server)  
**JWT** – Signed token with user info (for user sessions)  
**OAuth 2.0** – Delegated authorization (login with Google)

```http
# API Key
Authorization: ApiKey abc123xyz

# JWT Bearer token
Authorization: Bearer eyJhbGciOiJIUzI1NiJ9...
```

---

## GraphQL
*Alternative to REST for flexible data fetching*

**GraphQL** – Query language where the client specifies exactly what data it needs  
**Single endpoint** – All requests go to `/graphql` (vs REST's many endpoints)

### REST vs GraphQL

```
REST:
  GET /users/1          → {id, name, email, address, orders, ...}  ← over-fetching
  GET /users/1/orders   → second request needed                     ← under-fetching

GraphQL:
  POST /graphql
  query {
    user(id: 1) {
      name              ← only what you need
      orders {
        id
        total
      }
    }
  }
  → {name: "Alice", orders: [{id: 42, total: 99}]}
```

### Basic Syntax

```graphql
# Query (read)
query {
  user(id: 1) {
    name
    email
  }
}

# Mutation (write)
mutation {
  createUser(name: "Alice", email: "alice@example.com") {
    id
    name
  }
}

# Subscription (real-time)
subscription {
  orderUpdated(orderId: 42) {
    status
  }
}
```

### When to Use GraphQL vs REST

| Scenario | Use |
|---|---|
| Public API, simple CRUD | REST |
| Multiple clients (web, mobile) needing different data | GraphQL |
| Rapid frontend iteration | GraphQL |
| Microservices with well-defined contracts | REST |
| Real-time data needs | GraphQL (subscriptions) |
| Team unfamiliar with GraphQL | REST |

**Tools** – Apollo Server, Strawberry (Python), Spring GraphQL (Java)

---

## Best Practices

- Use nouns in URLs, HTTP methods as verbs
- Return appropriate status codes (don't always return 200)
- Version your API from day one
- Always return consistent error structure
- Paginate list endpoints
- Document with OpenAPI
- Never expose internal IDs that reveal implementation details
- Prefer REST for simple APIs; GraphQL when clients need flexibility
