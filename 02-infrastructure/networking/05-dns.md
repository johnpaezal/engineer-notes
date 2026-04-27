# DNS – Domain Name System
*Translates domain names to IP addresses*

## What is DNS
*The internet's phone book*

**DNS** – Distributed system that maps human-readable names to IP addresses  
**Domain** – Human-readable address (google.com, api.myapp.com)  
**Record** – Entry in DNS that maps a name to something

```
User types: google.com
DNS resolves: 142.250.80.46
Browser connects to: 142.250.80.46
```

---

## DNS Resolution Process
*How a domain gets resolved step by step*

```
Browser asks: "What's the IP for google.com?"

1. Check local cache → not found
2. Ask Recursive Resolver (ISP or 8.8.8.8)
3. Resolver asks Root Server → "ask .com nameserver"
4. Resolver asks .com TLD Server → "ask google's nameserver"
5. Resolver asks Google's Nameserver → "142.250.80.46"
6. Resolver returns IP to browser
7. Browser caches result (until TTL expires)
```

### DNS Hierarchy

```
.                       ← Root
└── com.                ← TLD (Top Level Domain)
    └── google.com.     ← Second-level domain
        └── mail.google.com.  ← Subdomain
```

---

## DNS Record Types
*Different types of information stored in DNS*

**A** – Maps domain to IPv4 address  
**AAAA** – Maps domain to IPv6 address  
**CNAME** – Alias from one domain to another  
**MX** – Mail server for the domain  
**TXT** – Text data (verification, SPF, DKIM)  
**NS** – Nameserver for the domain  
**PTR** – Reverse DNS (IP → domain)  
**SOA** – Start of Authority (zone info)

```
# A record
google.com.       300  IN  A      142.250.80.46

# AAAA record
google.com.       300  IN  AAAA   2607:f8b0:4004::200e

# CNAME record
www.myapp.com.    300  IN  CNAME  myapp.com.

# MX record
myapp.com.        300  IN  MX     10 mail.myapp.com.

# TXT record
myapp.com.        300  IN  TXT    "v=spf1 include:gmail.com ~all"
```

---

## TTL – Time To Live
*How long a DNS record is cached*

**TTL** – Seconds a record can be cached before re-querying  
**Low TTL** – Changes propagate fast (use during migrations)  
**High TTL** – Less DNS traffic (use for stable records)

```
TTL = 300   → cache for 5 minutes
TTL = 3600  → cache for 1 hour
TTL = 86400 → cache for 24 hours
```

---

## Common DNS Servers

**8.8.8.8** – Google Public DNS  
**8.8.4.4** – Google Public DNS (secondary)  
**1.1.1.1** – Cloudflare DNS (fastest)  
**9.9.9.9** – Quad9 (security-focused)

---

## DNS Commands

```bash
# Look up A record
nslookup google.com
dig google.com

# Look up specific record type
dig google.com MX
dig google.com AAAA

# Trace full resolution path
dig google.com +trace

# Reverse lookup (IP → domain)
dig -x 8.8.8.8

# Check DNS propagation
dig @8.8.8.8 myapp.com   # query Google's DNS
dig @1.1.1.1 myapp.com   # query Cloudflare's DNS
```

---

## DNS in AWS
*Route 53*

**Route 53** – AWS managed DNS service  
**Hosted Zone** – Container for DNS records of a domain  
**Routing Policies** – Simple, weighted, latency-based, failover, geolocation

```
Route 53 routing policies:
  Simple     → one record, one IP
  Weighted   → 80% to v1, 20% to v2 (canary)
  Latency    → route to nearest region
  Failover   → primary + backup (health checks)
  Geo        → route by user location
```
