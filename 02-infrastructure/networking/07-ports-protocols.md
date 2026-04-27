# Ports & Protocols
*How services are identified on a network*

## Ports
*Numbered endpoints that identify services*

**Port** – 16-bit number (0–65535) that identifies a specific service on a host  
**Socket** – Combination of IP + port: `192.168.1.10:443`

```
192.168.1.10:80   → HTTP server
192.168.1.10:443  → HTTPS server
192.168.1.10:22   → SSH server
192.168.1.10:5432 → PostgreSQL
```

### Port Ranges

```
0 – 1023       Well-known ports  (require root to bind)
1024 – 49151   Registered ports  (assigned to applications)
49152 – 65535  Dynamic/Ephemeral (used by clients temporarily)
```

---

## Common Ports & Protocols

| Port | Protocol | Description |
|---|---|---|
| 20, 21 | FTP | File Transfer Protocol |
| 22 | SSH | Secure Shell |
| 23 | Telnet | Unencrypted remote shell (insecure) |
| 25 | SMTP | Send email |
| 53 | DNS | Domain Name System |
| 67, 68 | DHCP | Dynamic IP assignment |
| 80 | HTTP | Web traffic |
| 110 | POP3 | Receive email |
| 143 | IMAP | Email access |
| 443 | HTTPS | Secure web traffic |
| 465 | SMTPS | Secure email send |
| 3306 | MySQL | MySQL database |
| 5432 | PostgreSQL | PostgreSQL database |
| 6379 | Redis | Redis cache |
| 27017 | MongoDB | MongoDB database |
| 8080 | HTTP alt | Alternative HTTP / dev servers |
| 8443 | HTTPS alt | Alternative HTTPS |

---

## Application Protocols

### SSH – Secure Shell
*Encrypted remote access to servers*

```bash
ssh user@192.168.1.10           # connect with password
ssh -i key.pem user@host        # connect with private key
ssh -p 2222 user@host           # non-default port
ssh -L 8080:localhost:80 user@host  # port forwarding
```

### FTP / SFTP
*File transfer*

**FTP** – Unencrypted file transfer (avoid)  
**SFTP** – SSH File Transfer Protocol (secure, use this)

```bash
sftp user@host
sftp> get remote_file.txt
sftp> put local_file.txt
sftp> ls
```

### SMTP / IMAP / POP3
*Email protocols*

**SMTP** – Sending email (port 25, 465, 587)  
**IMAP** – Access email on server, syncs across devices (port 143, 993)  
**POP3** – Download email to client, removes from server (port 110, 995)

---

## DHCP – Dynamic Host Configuration Protocol
*Automatic IP assignment*

**DHCP** – Protocol that automatically assigns IP configuration to devices  
**DHCP Server** – Usually the router  
**Lease** – Temporary IP assignment with expiration time

```
Device joins network:
  1. Device sends DHCP Discover (broadcast)
  2. DHCP server sends DHCP Offer (available IP)
  3. Device sends DHCP Request (accept the offer)
  4. Server sends DHCP Acknowledge (confirmed)

Device receives:
  - IP address:      192.168.1.50
  - Subnet mask:     255.255.255.0
  - Default gateway: 192.168.1.1
  - DNS server:      8.8.8.8
  - Lease time:      24 hours
```

---

## Firewall Rules
*Controlling traffic by port*

```bash
# Allow HTTP and HTTPS (ufw - Ubuntu)
ufw allow 80/tcp
ufw allow 443/tcp
ufw allow 22/tcp

# Block a port
ufw deny 23/tcp

# Allow from specific IP only
ufw allow from 192.168.1.0/24 to any port 5432

# AWS Security Group (same concept, different syntax)
Inbound:
  Type: HTTP,   Port: 80,   Source: 0.0.0.0/0
  Type: HTTPS,  Port: 443,  Source: 0.0.0.0/0
  Type: SSH,    Port: 22,   Source: MY_IP/32
```

---

## Key Commands

```bash
# See listening ports
ss -tlnp                 # modern (preferred)
netstat -tlnp            # older

# Check if port is open on remote host
nc -zv 192.168.1.10 80  # netcat
telnet 192.168.1.10 80  # telnet

# Scan ports
nmap 192.168.1.10        # basic scan
nmap -p 80,443 host      # specific ports

# Show active connections
ss -s                    # summary
ss -tp                   # with process info
```
