# Network Security
*Protecting networks from unauthorized access and attacks*

## Firewall
*Controls incoming and outgoing traffic*

**Firewall** – System that filters traffic based on rules  
**Stateful** – Tracks connection state (modern, smarter)  
**Stateless** – Filters each packet independently (simpler, faster)

```
Types:
  Host-based   → software on a single machine (ufw, Windows Firewall)
  Network-based → hardware/software at network perimeter
  Cloud        → AWS Security Groups, AWS WAF
```

### Firewall Rules Logic

```
Rule evaluation: top to bottom, first match wins

Priority | Source          | Port | Action
---------|-----------------|------|--------
1        | 203.0.113.5/32  | 22   | ALLOW   (my IP, SSH)
2        | 0.0.0.0/0       | 80   | ALLOW   (everyone, HTTP)
3        | 0.0.0.0/0       | 443  | ALLOW   (everyone, HTTPS)
999      | 0.0.0.0/0       | ANY  | DENY    (block everything else)
```

---

## VPN – Virtual Private Network
*Encrypted tunnel over public network*

**VPN** – Creates secure, encrypted connection between two points  
**Tunnel** – Encapsulates packets inside another protocol  
**Use cases** – Remote workers accessing company network, privacy

```
Remote Worker                    Corporate Network
Laptop ──── encrypted tunnel ──── VPN Gateway ──── Internal servers
       public internet                              (private IPs)
```

### VPN Protocols

**OpenVPN** – Open source, widely used, very secure  
**WireGuard** – Modern, fast, simple configuration  
**IPSec** – Standard protocol, used in site-to-site VPNs  
**SSL/TLS VPN** – Works through browser (no client needed)

---

## Common Network Attacks
*What attackers do and how to defend*

### Man-in-the-Middle (MITM)
*Attacker intercepts communication*

```
Normal:  Client ──────────────────── Server
MITM:    Client ── Attacker ──────── Server
                   ↑ reads/modifies data
```

**Defense** – HTTPS/TLS, certificate pinning, VPN

### DDoS – Distributed Denial of Service
*Overwhelming a server with traffic*

```
Botnet (thousands of infected devices)
  └── floods server with requests → server crashes
```

**Defense** – Rate limiting, CDN, AWS Shield, WAF, auto-scaling

### DNS Spoofing / Poisoning
*Fake DNS responses redirect users*

```
Attacker poisons DNS cache:
  google.com → 203.0.113.99 (attacker's server)
User connects to fake server → credentials stolen
```

**Defense** – DNSSEC, use trusted DNS (1.1.1.1, 8.8.8.8), HTTPS

### Port Scanning
*Discovering open ports and services*

```bash
nmap -sV target.com   # service version detection
nmap -O target.com    # OS detection
```

**Defense** – Close unused ports, change default ports, IDS/IPS

### Packet Sniffing
*Capturing network traffic*

```bash
tcpdump -i eth0           # capture all traffic
tcpdump -i eth0 port 80   # capture HTTP traffic
wireshark                 # GUI packet analyzer
```

**Defense** – Encrypt all traffic (HTTPS, SSH, VPN)

---

## Network Security Tools

**nmap** – Port scanner and network discovery  
**Wireshark** – Packet capture and analysis  
**tcpdump** – CLI packet capture  
**fail2ban** – Ban IPs with too many failed attempts  
**ufw** – Uncomplicated Firewall (Ubuntu)  
**snort** – Intrusion Detection System (IDS)

```bash
# fail2ban - auto-ban brute force
fail2ban-client status sshd

# Check who's connected to your server
who
ss -tp

# Check failed SSH attempts
grep "Failed password" /var/log/auth.log
```

---

## Zero Trust Security
*"Never trust, always verify"*

**Zero Trust** – No user or device is trusted by default, even inside the network  
**Principles**:
- Verify every user and device
- Least privilege access (minimum permissions needed)
- Assume breach (monitor everything)

```
Traditional:  Trusted inside network → full access
Zero Trust:   Everyone verified → only what they need
```

---

## TLS/SSL Best Practices

```
✓ Use TLS 1.2 minimum, prefer TLS 1.3
✓ Use strong cipher suites (AES-256, ChaCha20)
✓ Redirect HTTP → HTTPS (301)
✓ HSTS header: Strict-Transport-Security: max-age=31536000
✓ Renew certificates before expiry (Let's Encrypt auto-renews)
✗ Never use SSL 2.0, SSL 3.0, TLS 1.0, TLS 1.1 (deprecated)
✗ Never use self-signed certs in production
```
