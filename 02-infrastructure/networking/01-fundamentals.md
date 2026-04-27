# Networking Fundamentals
*Core concepts of how computers communicate*

## What is a Network
*Computers connected to share resources and data*

**Network** – Two or more devices connected to exchange data  
**Node** – Any device on a network (computer, router, switch, phone)  
**Protocol** – Set of rules for how data is sent and received  
**Bandwidth** – Maximum data transfer rate (Mbps, Gbps)  
**Latency** – Time for data to travel from source to destination (ms)  
**Packet** – Small unit of data sent over a network

---

## Types of Networks
*Scope of the network*

**LAN (Local Area Network)** – Small area: home, office, building  
**WAN (Wide Area Network)** – Large area: cities, countries (internet is a WAN)  
**MAN (Metropolitan Area Network)** – City-scale network  
**VPN (Virtual Private Network)** – Encrypted tunnel over public network  
**WLAN** – Wireless LAN (Wi-Fi)

---

## Network Devices
*Hardware that builds and connects networks*

**Router** – Connects different networks, directs packets between them (e.g., home router connects LAN to internet)  
**Switch** – Connects devices within the same network (LAN), forwards frames using MAC addresses  
**Hub** – Old device, broadcasts to all ports (replaced by switches)  
**Access Point (AP)** – Provides Wi-Fi wireless connectivity  
**Modem** – Converts digital ↔ analog signal (connects to ISP)  
**Firewall** – Filters traffic based on rules (hardware or software)  
**Load Balancer** – Distributes traffic across multiple servers

```
Internet
    │
  Modem
    │
  Router  ←── Firewall
    │
  Switch
  ├── PC 1
  ├── PC 2
  └── Access Point ──── Phone (Wi-Fi)
```

---

## MAC Address
*Physical hardware identifier*

**MAC (Media Access Control)** – Unique hardware ID burned into every network interface card  
**Format** – 48-bit, written as 6 pairs of hex: `AA:BB:CC:DD:EE:FF`  
**Scope** – Works at Layer 2 (local network only, not routed)

```
FF:FF:FF:FF:FF:FF  ← broadcast (send to everyone)
00:1A:2B:3C:4D:5E  ← unicast (specific device)
```

---

## Transmission Types
*How data is sent to recipients*

**Unicast** – One sender → one receiver  
**Broadcast** – One sender → all devices on network  
**Multicast** – One sender → group of receivers  
**Anycast** – One sender → nearest receiver (used in CDN, DNS)

---

## Key Concepts

**Full Duplex** – Send and receive simultaneously (modern ethernet)  
**Half Duplex** – Send or receive, not both at once (old hubs, walkie-talkie)  
**Encapsulation** – Wrapping data with headers at each layer  
**MTU (Maximum Transmission Unit)** – Largest packet size allowed (typically 1500 bytes for ethernet)
