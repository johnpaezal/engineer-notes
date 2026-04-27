# TCP/IP Model
*The model that actually runs the internet*

## TCP/IP vs OSI
*Practical model vs theoretical model*

**TCP/IP Model** – 4-layer model used in practice (the real internet)  
**OSI Model** – 7-layer theoretical reference model  
**Relationship** – OSI is for understanding, TCP/IP is for implementation

```
OSI Model          TCP/IP Model
─────────────      ─────────────
7. Application  ┐
6. Presentation ├─ Application
5. Session      ┘
4. Transport    ── Transport
3. Network      ── Internet
2. Data Link    ┐
1. Physical     ┘─ Network Access
```

---

## The 4 Layers

### Layer 4 – Application
*User-facing protocols*

Combines OSI layers 5, 6, 7  
**Protocols** – HTTP, HTTPS, FTP, SSH, DNS, SMTP, WebSocket

### Layer 3 – Transport
*End-to-end communication*

**TCP** – Reliable, ordered, connection-based  
**UDP** – Fast, no guarantee, connectionless

### Layer 2 – Internet
*Routing packets across networks*

**IP** – Logical addressing and routing  
**ICMP** – Error messages and diagnostics (`ping` uses ICMP)  
**ARP** – Resolves IP addresses to MAC addresses

### Layer 1 – Network Access
*Physical transmission*

Combines OSI layers 1 and 2  
**Protocols** – Ethernet, Wi-Fi, fiber

---

## TCP – Transmission Control Protocol
*Reliable, ordered delivery*

### TCP Handshake (3-way)
*Establishing a connection*

```
Client          Server
  │──── SYN ────►│    "I want to connect"
  │◄─── SYN-ACK─│    "OK, I'm ready"
  │──── ACK ────►│    "Great, let's go"
  │              │
  │  [data transfer]
  │              │
  │──── FIN ────►│    "I'm done"
  │◄─── FIN-ACK─│    "Acknowledged"
```

### TCP Features

**Reliability** – Retransmits lost packets  
**Ordering** – Reassembles packets in correct order  
**Flow Control** – Prevents sender from overwhelming receiver  
**Congestion Control** – Slows down when network is congested

**Use cases** – HTTP, HTTPS, SSH, FTP, email (anything that needs reliability)

---

## UDP – User Datagram Protocol
*Fast, no delivery guarantee*

```
Client          Server
  │──── data ───►│    no acknowledgment
  │──── data ───►│    no retransmit if lost
  │──── data ───►│    no ordering
```

**Use cases** – Video streaming, online games, DNS, VoIP  
**Why** – Speed matters more than perfect reliability

---

## IP – Internet Protocol

### IPv4
*32-bit address, most common*

```
Format:  192.168.1.1
Bits:    32 bits (4 octets of 8 bits)
Range:   0.0.0.0 to 255.255.255.255
Total:   ~4.3 billion addresses (exhausted)
```

### IPv6
*128-bit address, the future*

```
Format:  2001:0db8:85a3:0000:0000:8a2e:0370:7334
Bits:    128 bits
Total:   340 undecillion addresses
Short:   2001:db8:85a3::8a2e:370:7334 (:: = consecutive zeros)
```

---

## ICMP – Internet Control Message Protocol
*Network diagnostics*

**ping** – Tests connectivity and round-trip time

```bash
ping google.com
# PING google.com: 64 bytes, time=12.4ms
```

**traceroute** – Shows path packets take to destination

```bash
traceroute google.com
# 1  192.168.1.1   1ms    (router)
# 2  10.0.0.1      5ms    (ISP)
# 3  72.14.0.1     12ms   (Google)
```

---

## ARP – Address Resolution Protocol
*Maps IP address to MAC address*

```
Device knows: IP = 192.168.1.5
Needs to find: MAC address of that IP

ARP Request:  "Who has 192.168.1.5?" (broadcast)
ARP Reply:    "I do! My MAC is AA:BB:CC:DD:EE:FF"

Result stored in ARP cache (temporary table)
```

```bash
arp -a    # view ARP cache
```
