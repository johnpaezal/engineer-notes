# Security – OWASP
*Common vulnerabilities and how to prevent them*

## OWASP Top 10
*Most critical web application security risks*

**OWASP** – Open Web Application Security Project  
**OWASP Top 10** – Annual list of most critical security vulnerabilities

---

## 1. Injection (SQL, NoSQL, Command)
*Untrusted data sent as part of a command or query*

```python
# ❌ SQL Injection – attacker controls the query
user_input = "'; DROP TABLE users; --"
query = f"SELECT * FROM users WHERE name = '{user_input}'"

# ✅ Parameterized queries – input treated as data, not code
cursor.execute("SELECT * FROM users WHERE name = %s", (user_input,))
```

```python
# ❌ Command injection
filename = request.args.get("file")
os.system(f"cat {filename}")  # attacker: "file; rm -rf /"

# ✅ Never pass user input to shell commands
# Use safe libraries instead of shell execution
```

---

## 2. Broken Authentication
*Weak login, session, or credential management*

```
❌ Weak passwords allowed
❌ No rate limiting on login (brute force possible)
❌ Session tokens not invalidated on logout
❌ Passwords stored in plain text

✅ Enforce strong passwords
✅ Rate limit login attempts (fail2ban, throttling)
✅ Invalidate tokens on logout
✅ Hash passwords: bcrypt, argon2 (never MD5 or SHA1)
✅ Multi-factor authentication (MFA)
```

```python
# ✅ Hash passwords with bcrypt
import bcrypt

hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
bcrypt.checkpw(input_password.encode(), hashed)  # verify
```

---

## 3. Sensitive Data Exposure
*Unprotected sensitive data in transit or at rest*

```
❌ Passwords/tokens in logs
❌ API keys in code or git history
❌ HTTP instead of HTTPS
❌ Database backups unencrypted

✅ HTTPS everywhere
✅ Encrypt sensitive data at rest (AES-256)
✅ Never log passwords, tokens, or PII
✅ Use environment variables for secrets
✅ .gitignore for .env files
```

```python
# ❌ Secret in code
API_KEY = "sk-abc123xyz"

# ✅ Secret from environment
import os
API_KEY = os.environ["API_KEY"]
```

---

## 4. Broken Access Control
*Users can act outside their intended permissions*

```
❌ User accesses /admin without being admin
❌ User 1 can view/edit User 2's data by changing ID in URL
❌ API doesn't check ownership of resource

✅ Validate permissions on every request (server-side)
✅ Principle of least privilege
✅ Check resource ownership, not just authentication
```

```python
# ❌ Only checks login, not ownership
@app.get("/orders/{order_id}")
def get_order(order_id: int, user=Depends(get_current_user)):
    return db.get_order(order_id)

# ✅ Checks ownership
@app.get("/orders/{order_id}")
def get_order(order_id: int, user=Depends(get_current_user)):
    order = db.get_order(order_id)
    if order.user_id != user.id:
        raise HTTPException(403, "Forbidden")
    return order
```

---

## 5. XSS – Cross-Site Scripting
*Injecting malicious scripts into web pages*

```javascript
// ❌ Reflected XSS – user input rendered as HTML
const name = req.query.name
res.send(`<h1>Hello ${name}</h1>`)
// attacker: ?name=<script>steal(document.cookie)</script>

// ✅ Escape output
const name = escapeHtml(req.query.name)

// ✅ Content Security Policy header
Content-Security-Policy: default-src 'self'
```

---

## 6. CSRF – Cross-Site Request Forgery
*Tricking users into making unintended requests*

```
Scenario:
  User is logged into bank.com
  User visits attacker.com
  Attacker page sends POST to bank.com/transfer
  Bank executes transfer (user is authenticated via cookie)

Defense:
  ✅ CSRF tokens (hidden form field, server validates)
  ✅ SameSite cookie attribute
  ✅ Check Origin/Referer headers
```

```python
# Cookie with SameSite
Set-Cookie: session=abc123; SameSite=Strict; Secure; HttpOnly
```

---

## 7. Security Misconfiguration
*Insecure default settings, exposed error details*

```
❌ Default credentials (admin/admin)
❌ Debug mode enabled in production
❌ Stack traces returned to users
❌ Unnecessary services/ports open
❌ Directory listing enabled

✅ Disable debug in production
✅ Generic error messages to users, full details in logs only
✅ Close all unused ports
✅ Change default credentials
✅ Security headers on all responses
```

```python
# ❌ Exposes internal error
@app.exception_handler(Exception)
async def error_handler(request, exc):
    return JSONResponse({"error": str(exc), "traceback": traceback.format_exc()})

# ✅ Generic message, log internally
@app.exception_handler(Exception)
async def error_handler(request, exc):
    logger.error(f"Unhandled error: {exc}", exc_info=True)
    return JSONResponse({"error": "Internal server error"}, status_code=500)
```

---

## 8. Insecure Deserialization
*Untrusted data used to reconstruct objects*

```python
# ❌ Never deserialize untrusted data with pickle
import pickle
data = pickle.loads(user_provided_bytes)  # can execute arbitrary code

# ✅ Use safe formats: JSON, protobuf
import json
data = json.loads(user_provided_string)
```

---

## Security Headers
*HTTP headers that improve browser security*

```http
Strict-Transport-Security: max-age=31536000; includeSubDomains
Content-Security-Policy: default-src 'self'
X-Content-Type-Options: nosniff
X-Frame-Options: DENY
Referrer-Policy: strict-origin-when-cross-origin
Permissions-Policy: geolocation=(), microphone=()
```

---

## Best Practices Summary

```
Authentication:   hash passwords (bcrypt), use MFA, expire sessions
Authorization:    check permissions server-side on every request
Data:             HTTPS, encrypt at rest, never log secrets
Input:            validate and sanitize all user input
Dependencies:     keep updated, audit with safety/snyk
Secrets:          environment variables, never in code or git
Errors:           generic to users, detailed in logs
```
