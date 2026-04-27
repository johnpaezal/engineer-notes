# OSI Model
*The 7-layer framework for network communication*

## What is the OSI Model
*Conceptual framework that standardizes network communication*

**OSI (Open Systems Interconnection)** – 7-layer model that describes how data travels from one device to another  
**Purpose** – Standardize communication so different vendors/systems can interoperate  
**Key idea** – Each layer has a specific job and communicates only with the layers above and below it

```
Sender                          Receiver
┌─────────────┐                ┌─────────────┐
│ 7. Application│              │ 7. Application│
│ 6. Presentation│            │ 6. Presentation│
│ 5. Session  │                │ 5. Session  │
│ 4. Transport│                │ 4. Transport│
│ 3. Network  │                │ 3. Network  │
│ 2. Data Link│                │ 2. Data Link│
│ 1. Physical │──── cable ─────│ 1. Physical │
└─────────────┘                └─────────────┘
   Data goes DOWN ↓                Data goes UP ↑
```

---

## The 7 Layers

### Layer 7 – Application
*Closest to the user, interfaces with software*

**What it does** – Provides network services to applications  
**Protocols** – HTTP, HTTPS, FTP, SMTP, DNS, SSH, WebSocket  
**Examples** – Browser, email client, Slack

### Layer 6 – Presentation
*Translates, encrypts, and compresses data*

**What it does** – Formats data so the application layer can understand it  
**Handles** – Encryption (TLS/SSL), compression, encoding (UTF-8, ASCII)  
**Examples** – JPEG, MP3, TLS, SSL

### Layer 5 – Session
*Manages connections between applications*

**What it does** – Opens, maintains, and closes sessions between devices  
**Handles** – Authentication, session tokens, reconnection  
**Examples** – NetBIOS, RPC, SQL sessions

### Layer 4 – Transport
*End-to-end delivery and reliability*

**What it does** – Breaks data into segments, ensures delivery  
**Protocols** – TCP (reliable), UDP (fast, no guarantee)  
**Handles** – Port numbers, segmentation, flow control, error recovery

```
TCP  → reliable, ordered, connection-based (HTTP, SSH, FTP)
UDP  → fast, no guarantee, connectionless (video, DNS, games)
```

### Layer 3 – Network
*Routing packets across different networks*

**What it does** – Logical addressing and routing between networks  
**Protocols** – IP (IPv4, IPv6), ICMP, OSPF, BGP  
**Devices** – Router  
**Unit** – Packet

```
IP address lives here
Router reads Layer 3 to decide where to forward the packet
```

### Layer 2 – Data Link
*Node-to-node delivery on same network*

**What it does** – Physical addressing, error detection within a network  
**Protocols** – Ethernet, Wi-Fi (802.11), ARP  
**Devices** – Switch, Bridge  
**Unit** – Frame

```
MAC address lives here
Switch reads Layer 2 to forward frames within LAN
```

### Layer 1 – Physical
*Raw bits over physical medium*

**What it does** – Transmits raw bits (0s and 1s) over a physical medium  
**Mediums** – Copper cable, fiber optic, radio waves (Wi-Fi)  
**Devices** – Hub, repeater, cable, NIC  
**Unit** – Bit

---

## Quick Reference

| # | Layer | Unit | Device | Protocol |
|---|---|---|---|---|
| 7 | Application | Data | — | HTTP, DNS, SSH |
| 6 | Presentation | Data | — | TLS, JPEG |
| 5 | Session | Data | — | NetBIOS, RPC |
| 4 | Transport | Segment | — | TCP, UDP |
| 3 | Network | Packet | Router | IP, ICMP |
| 2 | Data Link | Frame | Switch | Ethernet, ARP |
| 1 | Physical | Bit | Hub, cable | — |

---

## Mnemonic
*Remember the layers top to bottom*

```
All People Seem To Need Data Processing
7-Application, 6-Presentation, 5-Session, 4-Transport, 3-Network, 2-Data Link, 1-Physical
```

---

## Encapsulation
*How data is wrapped as it goes down the layers*

```
Application data: "Hello"
    ↓ Layer 4 adds: [TCP header | "Hello"]           → Segment
    ↓ Layer 3 adds: [IP header | TCP header | "Hello"] → Packet
    ↓ Layer 2 adds: [MAC header | IP | TCP | "Hello" | trailer] → Frame
    ↓ Layer 1:       101001010101011010...              → Bits
```

Receiver unwraps in reverse (decapsulation).
