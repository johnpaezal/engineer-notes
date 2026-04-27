# Global Example — Requirements Flow
*From user need to sprint planning, end to end*

Example project: **"TravelMate"** — app that notifies travelers about flight changes.

Format based on IEEE 830 SRS style (used in Microsoft, Google, Amazon specs).

**ID prefixes**:
- `UN` – User Need
- `UG` – User Goal
- `FR` – Functional Requirement
- `NFR` – Non-Functional Requirement
- `UC` – Use Case
- `US` – User Story
- `AC` – Acceptance Criterion

---

## 1. User Needs
*Raw needs from research*

| ID | Type | Need |
|---|---|---|
| UN-01 | Articulated | "I want to know immediately if my flight changes." |
| UN-02 | Observable | Users check airline websites manually several times a day. |
| ... | ... | ... |

---

## 2. User Goals
*Needs expressed as "I want"*

| ID | Type | Goal |
|---|---|---|
| UG-01 | Achieve | I want to receive real-time flight change notifications. |
| UG-02 | Maintain | I want the app to work 24/7. |
| ... | ... | ... |

---

## 3. UX Scenario

```
Title: Frequent business traveler

Introduction: Carlos, sales executive, travels twice a week.
He misses connections when airlines delay flights without notice.

Result: With TravelMate, Carlos receives notifications within
2 minutes of any schedule change, avoiding 95% of missed flights.
```

---

## 4. Requirements
*Formal spec derived from needs and goals*

### Functional Requirements

| ID | Requirement | Source |
|---|---|---|
| FR-01 | **The system shall** allow users to configure the notification channel (email / SMS / push). | UN-01 |
| FR-02 | **When** a flight schedule changes, **the system shall** send a notification to the affected traveler. | UN-01, UG-01 |
| FR-03 | **If** the user has no preference set, **then the system shall** send the notification via email. | UN-01 |
| ... | ... | ... |

### Non-Functional Requirements

| ID | Type | Requirement |
|---|---|---|
| NFR-01 | Performance | **The system shall** deliver notifications within 2 minutes of the change. |
| NFR-02 | Availability | **The system shall** maintain 99.9% uptime. |
| ... | ... | ... |

### Prioritization (MoSCoW)

| Priority | Requirements |
|---|---|
| Must | FR-01, FR-02, NFR-01 |
| Should | ... |
| Could | ... |
| Won't | ... |

---

## 5. Use Case

```
UC-01: Notify Flight Change
Actor: Traveler
Related: FR-01, FR-02

Main Flow:
  1. Airline system reports a schedule change
  2. TravelMate detects the change
  3. System looks up user notification preferences
  4. System sends notification through preferred channel
  5. User receives notification within 2 minutes

Alternate Flow (user has no preference set):
  3a. System sends notification via email (default)
```

---

## 6. User Stories
*Same requirements, written from the user's perspective*

| ID | Story | Points | Related |
|---|---|---|---|
| US-01 | **As a** traveler, **I want** to receive flight change notifications **so that** I don't miss my flight. | 5 | FR-01 |
| US-02 | **As a** traveler, **I want** to choose my notification channel **so that** I'm reached in the way that works best for me. | 3 | FR-02 |
| ... | ... | ... | ... |

---

## 7. Acceptance Criteria

### For US-01

**Template 1 — Checklist**:
- User receives notification within 2 minutes of the change
- Notification includes new flight time and gate
- Notification is sent only for the user's active trips

**Template 2 — Given/When/Then**:
```
AC-01: **Given** a traveler has an active trip,
       **when** the airline changes the flight schedule,
       **then** the system shall send a notification within 2 minutes.

AC-02: **Given** the traveler has no notification preference set,
       **when** a change occurs,
       **then** the system shall send the notification via email.
```

---

## 8. Story Points & Estimation

### Fibonacci estimate (from Planning Poker)

| Story | Estimate | Rationale |
|---|---|---|
| US-01 | 5 | Medium complexity — requires integration with airline API |
| US-02 | 3 | Small CRUD feature for user preferences |
| ... | ... | ... |

### Planning Poker round

```
Round 1:
  Dev A: 5
  Dev B: 8
  Dev C: 3

Discussion: Dev B was counting airline API setup (already done).
Dev C was missing the retry-on-failure logic.

Round 2: consensus at 5 pts.
```

---

## 9. Backlog

```
Epic: Flight Notifications
  ├── US-01  Receive flight change notification  (5 pts)  [Must]
  ├── US-02  Choose notification channel         (3 pts)  [Must]
  └── ...
  Sprint 1 velocity target: 10 pts
```

---

## Summary — End-to-End Traceability

```
UN-01 / UG-01
     ↓
FR-01, NFR-01
     ↓
UC-01
     ↓
US-01  (5 pts)
     ↓
AC-01, AC-02
     ↓
Sprint 1 Backlog
```

Each ID can be traced back to the original user need — this is the backbone of a traceability matrix in formal SRS documents.
