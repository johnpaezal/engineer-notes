# IP Addressing & Subnets
*How devices are addressed and networks are divided*

## IP Address Structure
*32 bits divided into network and host portions*

```
IP Address:  192  . 168  .  1   .  10
Bits:       11000000.10101000.00000001.00001010
            ──────────────────────────────────
            Network part        │  Host part
```

**Network part** – Identifies the network  
**Host part** – Identifies the device within that network

---

## Subnet Mask
*Defines which part of the IP is network vs host*

```
IP:      192.168.1.10
Mask:    255.255.255.0
Binary:  11111111.11111111.11111111.00000000
                                    └── host bits (0s)
         └──────────────────────── network bits (1s)
```

**255** = 11111111 = all network bits  
**0** = 00000000 = all host bits

---

## CIDR Notation
*Shorthand for subnet mask*

**CIDR** – Classless Inter-Domain Routing  
**Format** – `IP/prefix` where prefix = number of network bits

```
192.168.1.0/24  →  mask: 255.255.255.0   (24 network bits)
192.168.1.0/16  →  mask: 255.255.0.0     (16 network bits)
192.168.1.0/8   →  mask: 255.0.0.0       (8 network bits)
10.0.0.0/30     →  mask: 255.255.255.252 (30 network bits)
```

### Common CIDR Values

| CIDR | Mask | Hosts | Use case |
|---|---|---|---|
| /8 | 255.0.0.0 | 16,777,214 | Large organization |
| /16 | 255.255.0.0 | 65,534 | Medium organization |
| /24 | 255.255.255.0 | 254 | Small network |
| /28 | 255.255.255.240 | 14 | Small subnet |
| /30 | 255.255.255.252 | 2 | Point-to-point link |
| /32 | 255.255.255.255 | 1 | Single host |

---

## Calculating Subnets
*How many hosts fit in a subnet*

```
Formula: hosts = 2^(host bits) - 2
         (-2 for network address and broadcast)

/24 → 32 - 24 = 8 host bits → 2^8 - 2 = 254 hosts
/28 → 32 - 28 = 4 host bits → 2^4 - 2 = 14 hosts
/30 → 32 - 30 = 2 host bits → 2^2 - 2 = 2 hosts
```

### Key Addresses in a Subnet

```
Network: 192.168.1.0/24

Network address:   192.168.1.0    ← identifies the subnet (not usable)
First host:        192.168.1.1    ← first assignable
Last host:         192.168.1.254  ← last assignable
Broadcast:         192.168.1.255  ← sends to all hosts (not usable)
```

---

## Private vs Public IPs
*Which addresses can reach the internet*

### Private Ranges (RFC 1918)
*Not routable on the internet — for internal use only*

```
10.0.0.0/8        →  10.0.0.0    – 10.255.255.255
172.16.0.0/12     →  172.16.0.0  – 172.31.255.255
192.168.0.0/16    →  192.168.0.0 – 192.168.255.255
```

### Special Addresses

```
127.0.0.1         → localhost (loopback, always "this device")
0.0.0.0           → any address / default route
255.255.255.255   → limited broadcast
169.254.x.x       → APIPA (auto-assigned when DHCP fails)
```

---

## NAT – Network Address Translation
*Translates private IPs to public IP*

**Problem** – Private IPs can't communicate directly with internet  
**Solution** – Router translates private → public IP on outgoing packets

```
Home Network                  Internet
192.168.1.10 ─┐
192.168.1.11 ─┤── Router (NAT) ── 203.0.113.5 ──► google.com
192.168.1.12 ─┘
                ↑
        one public IP for all devices
```

---

## Subnetting in Practice (AWS VPC)
*Real-world example*

```
VPC CIDR: 10.0.0.0/16  (65,534 hosts)

├── Public Subnet:   10.0.1.0/24  (254 hosts) ← internet accessible
├── Private Subnet:  10.0.2.0/24  (254 hosts) ← internal only
└── Database Subnet: 10.0.3.0/24  (254 hosts) ← DB layer
```

---

## Default Gateway
*Router that leads to other networks*

**Default Gateway** – IP of the router on your local network  
**Role** – When a packet's destination is outside the local subnet, it's sent to the gateway

```
Your IP:         192.168.1.10
Subnet:          192.168.1.0/24
Default Gateway: 192.168.1.1   ← your router

Destination 192.168.1.50 → same subnet, send directly
Destination 8.8.8.8      → different network, send to gateway
```
