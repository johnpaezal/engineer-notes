# HTTP & HTTPS
*Protocol for web communication*

## HTTP
*HyperText Transfer Protocol*

**HTTP** – Application-layer protocol for transferring data on the web  
**Stateless** – Each request is independent, no memory of previous requests  
**Port** – 80 (default)

### Request Structure

```http
GET /users/42 HTTP/1.1
Host: api.example.com
Accept: application/json
Authorization: Bearer eyJ...
```

```
Method   Path         Version
  ↓        ↓            ↓
GET    /users/42    HTTP/1.1
Host: api.example.com        ← required header
Accept: application/json     ← optional headers
```

### Response Structure

```http
HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: 52

{"id": 42, "name": "Alice", "email": "alice@example.com"}
```

---

## HTTP Methods
*Actions performed on resources*

**GET** – Retrieve data (no body, idempotent)  
**POST** – Create resource (has body, not idempotent)  
**PUT** – Replace resource completely (idempotent)  
**PATCH** – Update resource partially  
**DELETE** – Remove resource (idempotent)  
**HEAD** – Same as GET but no body (check if resource exists)  
**OPTIONS** – Returns allowed methods (used in CORS preflight)

**Idempotent** – Multiple identical requests = same result as one

---

## Status Codes
*Server's response to the request*

```
1xx – Informational
  100 Continue

2xx – Success
  200 OK
  201 Created
  204 No Content

3xx – Redirection
  301 Moved Permanently
  302 Found (temporary redirect)
  304 Not Modified (use cache)

4xx – Client Error
  400 Bad Request
  401 Unauthorized (not authenticated)
  403 Forbidden (authenticated, no permission)
  404 Not Found
  405 Method Not Allowed
  409 Conflict
  422 Unprocessable Entity (validation error)
  429 Too Many Requests (rate limited)

5xx – Server Error
  500 Internal Server Error
  502 Bad Gateway
  503 Service Unavailable
  504 Gateway Timeout
```

---

## HTTP Headers
*Metadata sent with requests and responses*

### Common Request Headers

```http
Content-Type: application/json       # body format
Accept: application/json             # expected response format
Authorization: Bearer <token>        # auth credentials
User-Agent: Mozilla/5.0 ...         # client info
Cache-Control: no-cache              # caching behavior
Origin: https://myapp.com           # where request comes from (CORS)
```

### Common Response Headers

```http
Content-Type: application/json       # body format
Content-Length: 128                  # body size in bytes
Cache-Control: max-age=3600          # cache for 1 hour
Set-Cookie: session=abc123; HttpOnly
Access-Control-Allow-Origin: *       # CORS policy
X-RateLimit-Remaining: 99           # rate limit info
```

---

## HTTPS
*HTTP with encryption*

**HTTPS** – HTTP + TLS (Transport Layer Security)  
**Port** – 443 (default)  
**TLS** – Cryptographic protocol that encrypts the connection  
**SSL** – Older predecessor to TLS (term still used colloquially)

### TLS Handshake
*Establishing an encrypted connection*

```
Client                    Server
  │── ClientHello ────────►│  (TLS version, cipher suites)
  │◄─── ServerHello ───────│  (chosen cipher, certificate)
  │◄─── Certificate ───────│  (public key + identity)
  │── ClientKeyExchange ──►│  (session key, encrypted)
  │── ChangeCipherSpec ───►│
  │◄── ChangeCipherSpec ───│
  │  [encrypted data] ↔   │
```

### SSL/TLS Certificate

**Certificate** – Digital document that proves server identity  
**CA (Certificate Authority)** – Trusted entity that signs certificates (Let's Encrypt, DigiCert)  
**Self-signed** – Certificate signed by yourself (not trusted by browsers)

```bash
# Check certificate info
openssl s_client -connect google.com:443
curl -v https://google.com 2>&1 | grep "SSL"
```

---

## HTTP Versions

**HTTP/1.1** – One request at a time per connection, keep-alive  
**HTTP/2** – Multiplexing (multiple requests per connection), header compression, faster  
**HTTP/3** – Uses QUIC (UDP-based), faster connection setup, resilient to packet loss

```
HTTP/1.1  →  one request at a time
HTTP/2    →  multiple requests simultaneously (multiplexing)
HTTP/3    →  same as HTTP/2 but over UDP (faster, more resilient)
```

---

## CORS – Cross-Origin Resource Sharing
*Browser security policy for cross-domain requests*

**Same-Origin Policy** – Browser blocks requests to different origin by default  
**CORS** – Server headers that allow specific cross-origin requests  
**Origin** – Protocol + domain + port (`https://myapp.com:443`)

```
Frontend: https://myapp.com
API:      https://api.myapp.com   ← different origin → blocked by default

# Server must respond with:
Access-Control-Allow-Origin: https://myapp.com
Access-Control-Allow-Methods: GET, POST, PUT
Access-Control-Allow-Headers: Authorization, Content-Type
```

---

## Cookies vs Tokens
*Session management approaches*

**Cookie** – Server sets, browser stores and sends automatically  
**JWT Token** – Client stores (localStorage/memory), sent manually in header

```
Cookie:         Set-Cookie: session=abc; HttpOnly; Secure
JWT in header:  Authorization: Bearer eyJhbGc...
```

---

## Caching
*Storing responses to avoid repeated requests*

```http
# Server response: cache for 1 hour
Cache-Control: max-age=3600

# Server response: never cache
Cache-Control: no-store

# Client revalidate before using cache
Cache-Control: no-cache

# Browser cached, server says nothing changed
304 Not Modified
```
