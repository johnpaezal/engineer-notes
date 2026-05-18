# HTTP API Deep
*Interview-depth HTTP, auth, CORS, pagination*

## Status Codes Interview Depth
*Families and the must-know ones*

**2xx Success** – Request succeeded  
**3xx Redirection** – More action needed (often caching/location)  
**4xx Client Error** – Caller's fault, do not retry as-is  
**5xx Server Error** – Server's fault, retry may help

| Code | Meaning | When to use |
|---|---|---|
| 200 | OK | GET/PUT/PATCH success with body |
| 201 | Created | POST created resource (return `Location`) |
| 204 | No Content | DELETE / PUT success, empty body |
| 301 | Moved Permanently | Resource URL changed forever (SEO, cache) |
| 302 | Found | Temporary redirect (keep old URL) |
| 304 | Not Modified | Conditional GET, client cache still valid |
| 400 | Bad Request | Malformed syntax / unparseable body |
| 401 | Unauthorized | Missing or invalid authentication |
| 403 | Forbidden | Authenticated but not allowed |
| 404 | Not Found | Resource does not exist (or hide 403) |
| 409 | Conflict | State conflict (duplicate, version clash) |
| 422 | Unprocessable Entity | Syntactically valid but fails validation |
| 429 | Too Many Requests | Rate limit exceeded (send `Retry-After`) |
| 500 | Internal Server Error | Unhandled server exception |
| 502 | Bad Gateway | Upstream returned invalid response |
| 503 | Service Unavailable | Overloaded / down for maintenance |
| 504 | Gateway Timeout | Upstream did not respond in time |

**400 vs 422** – 400 = cannot parse; 422 = parsed but invalid  
**401 vs 403** – 401 = who are you?; 403 = known but denied  
**502 vs 503 vs 504** – bad upstream reply / no capacity / upstream too slow

---

## Method Semantics
*Safe, idempotent, cacheable*

**Safe** – Read-only, no server state change (GET, HEAD)  
**Idempotent** – Same effect if called N times (GET, PUT, DELETE, HEAD)  
**Cacheable** – Response may be stored and reused

| Method | Safe | Idempotent | Cacheable |
|---|---|---|---|
| GET | yes | yes | yes |
| HEAD | yes | yes | yes |
| PUT | no | yes | no |
| DELETE | no | yes | no |
| POST | no | no | rarely |
| PATCH | no | no | no |

**Why POST is not idempotent** – Two POSTs create two resources  
**Why DELETE is idempotent** – Second delete still leaves it deleted (return 204/404)

---

## Idempotency Keys
*Safe retries for non-idempotent POST*

**Idempotency-Key** – Client-generated unique ID per logical operation  
**Behavior** – Server stores result by key; replays return cached response  
**Use case** – Payments, order creation under network retry/timeout

```http
POST /payments HTTP/1.1
Idempotency-Key: 7f3a9c1e-2b... (UUID, one per intent)

# Usage
# 1st request -> process, store (key -> response), return 201
# Retry same key -> return stored 201, do NOT charge twice
# Different key -> treated as new operation
```

---

## Authentication & Authorization
*Proving identity and granting access*

**Authentication** – Who you are  
**Authorization** – What you may do

| | Session-Cookie | JWT | OAuth2 |
|---|---|---|---|
| State | Server-side session store | Stateless (self-contained) | Token issued by auth server |
| Scale | Needs shared session store | Easy horizontal scale | Delegated to provider |
| Revoke | Delete session (instant) | Hard (needs blocklist/short TTL) | Refresh-token revoke |
| Best for | Classic web apps | APIs, microservices, SPAs | Third-party / delegated access |

### OAuth2 Authorization Code Flow
*Delegated access, no password sharing*

```
1. App redirects user to Auth Server (/authorize?client_id&redirect_uri&scope)
2. User logs in and consents
3. Auth Server redirects back with ?code=...
4. App exchanges code (+ client_secret) at /token  -> access_token (+ refresh_token)
5. App calls Resource Server with Authorization: Bearer <access_token>
6. access_token expires -> use refresh_token to get a new one
```

**+ PKCE** – Adds code_verifier/challenge for public clients (SPA, mobile)

### JWT Storage Trade-offs
*Where to keep the token client-side*

**localStorage** – Easy, but readable by JS → vulnerable to XSS  
**httpOnly cookie** – Hidden from JS (no XSS theft) → vulnerable to CSRF  
**Mitigation** – httpOnly + `SameSite` cookie + short TTL + CSRF token

---

## CORS
*Browser cross-origin request control*

**CORS** – Browser policy allowing cross-origin requests via server headers  
**Triggered when** – Page origin ≠ API origin (scheme/host/port differ)  
**Not enforced** – Server-to-server calls (CORS is a browser thing)

**Simple request** – GET/POST with safe headers → no preflight  
**Preflight (OPTIONS)** – Sent first for PUT/DELETE, custom headers, JSON content-type

```http
# Preflight request
OPTIONS /orders
Origin: https://app.example.com
Access-Control-Request-Method: PUT

# Server response (key headers)
Access-Control-Allow-Origin: https://app.example.com
Access-Control-Allow-Methods: GET, PUT, DELETE
Access-Control-Allow-Headers: Authorization, Content-Type
Access-Control-Allow-Credentials: true   # cannot use with Origin: *
Access-Control-Max-Age: 600              # cache preflight
```

---

## Pagination
*Splitting large collections*

**Offset/Limit** – `?page=3&limit=20` (skip N, take M)  
**Cursor/Keyset** – `?after=<opaque_cursor>` (where id > last seen)

| | Offset | Cursor / Keyset |
|---|---|---|
| Query | `OFFSET 40 LIMIT 20` | `WHERE id > ? LIMIT 20` |
| Deep page perf | Slow (scans skipped rows) | Fast (uses index) |
| Stable under inserts | No (items shift/skip) | Yes |
| Random page jump | Yes (`page=99`) | No (sequential only) |
| Best for | Small data, admin UIs | Infinite scroll, large/changing data |

---

## Rate Limiting (Contract Side)
*What the API exposes to clients*

**429 Too Many Requests** – Limit exceeded  
**Retry-After** – Seconds (or HTTP-date) to wait before retrying  
**X-RateLimit-*** – Limit / Remaining / Reset hints for clients

```http
HTTP/1.1 429 Too Many Requests
Retry-After: 30
X-RateLimit-Limit: 100
X-RateLimit-Remaining: 0
```

**Algorithms** – Token bucket, leaky bucket, sliding window: see `09-system-design/` patterns (not duplicated here)

---

## API Versioning
*Evolving without breaking clients*

| Strategy | Example | Trade-off |
|---|---|---|
| URI | `/api/v2/users` | Clearest, most common; not "pure REST" |
| Header | `Accept: application/vnd.api+json;version=2` | Clean URLs; harder to test/cache |
| Query param | `/users?version=2` | Easy; clutters URLs, cache risk |

---

## Best Practices

- Return precise status codes (404 not 200-with-error)
- Make writes idempotent or accept an `Idempotency-Key`
- Prefer cursor pagination for large/changing datasets
- Store JWT in httpOnly + SameSite cookie when in a browser
- Never use `Allow-Origin: *` with credentials
- Version from day one (URI versioning unless you need negotiation)
- Always send `Retry-After` with 429 / 503
