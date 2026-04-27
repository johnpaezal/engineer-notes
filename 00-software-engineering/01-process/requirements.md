# Software Engineering Requirements
*Capturing and managing what software must do*

## User Needs
*What the user actually wants*

### Classification

**Articulated** – What people say and think  
**Observable** – What people do and use  
**Tacit** – Conscious, but hard to express  
**Latent** – Not conscious or not recognized  

### Collection Tips

- Listen, observe, and empathize
- Clarify and confirm requirements
- Focus on the current user
- Faithfully record what the user conveys

### Elicitation Techniques
*Formal ways to gather requirements*

**Interviews** – One-on-one with stakeholders; deep insight but slow  
**Surveys** – Wide reach, shallow data; good for many users  
**Observation** – Watch users in their real context; captures tacit needs  
**Document Analysis** – Review existing manuals, reports, and contracts  

---

## User Goals
*Desires expressed as an "I want"*

**Soft Goal** – Does not meet SMART criteria; emerges naturally in conversations

### Goal Types

| Type | Description | Example |
|---|---|---|
| Achieve / Eliminate | Reach a desired state | I want the system to send me notifications |
| Maintain / Avoid | Preserve a condition | I want the system to run 24/7 |
| Optimize | Compare current vs desired state | I want to minimize expenses by 10% |

### From Soft Goal to Requirement

```
Soft goal:
  I want the system to send me notifications.

Concrete requirement:
  Implement a system that sends email or SMS notifications
  about itinerary changes within 3 months.
```

---

## User Experience Scenarios
*Situation, emotions, and context of the user*

### Elements

**Title** – Descriptive and related to the scenario  
**Introduction & situation** – Presents the user and context  
**Result** – Success metrics and satisfaction conditions  

### Characteristics

- Story with a beginning and end
- Personal details of the customer
- Includes emotions and environment
- Explores user needs
- Based on research
- Does not mention any implementation

### Example

```
Title: Time-tracking app for professionals

Introduction: Marta, a freelance designer, feels stressed at work and needs to organize her time across projects.

Result: The app improves her time management by 40%, letting her deliver projects on time and reduce stress.
```

---

## Requirements
*What the system must do*

**Requirement** – Description of what a program must do to meet user needs
- **Functional Requirement** – Specific behavior or function the system must perform
- **Non-Functional Requirement** – Quality attributes (performance, security, scalability)

```
Functional:     "User can log in with email and password"
Non-Functional: "Login must respond in under 2 seconds"
```

### Types of Requirements

**Business** – Organizational goals (e.g. reduce costs)  
**User** – Specific needs or goals of users  
**Product / Process** – Expected behaviors or attributes of the software  

### Non-Functional Requirements (NFRs)
*Quality attributes the system must meet*

| Type | Example |
|---|---|
| Performance | API responds in under 200 ms |
| Security | Passwords hashed with bcrypt |
| Scalability | Support 10k concurrent users |
| Availability | 99.9% uptime |
| Usability | New user completes signup in under 2 min |
| Reliability | No data loss on crash |

### Requirements Lifecycle

```
Elicitation → Analysis → Validation
```

| Phase | Description |
|---|---|
| Elicitation | Collect user needs |
| Analysis | Interpret and define requirements |
| Validation | Verify they meet expectations |

### Prioritization (MoSCoW)
*Decide what goes into each release*

**Must have** – Critical, release fails without it  
**Should have** – Important, but not release-blocking  
**Could have** – Nice to have if time permits  
**Won't have** – Excluded from this release  

---

## Use Cases
*Alternative to user stories — actor-driven flows*

Common in plan-driven projects. More formal than a user story.

**Actor** – Who interacts with the system (user, admin, external system)  
**Main Flow** – Happy path, step by step  
**Alternate Flow** – What happens when something goes wrong  

```
Use Case: Reset Password
Actor: User

Main Flow:
  1. User clicks "Forgot password"
  2. System asks for email
  3. User enters email
  4. System sends reset link
  5. User clicks link and sets new password

Alternate Flow (email not registered):
  3a. System shows "email not found" error
```

---

## User Stories
*Requirements from the user's perspective*

**Format**: `As a [role], I want [goal], so that [benefit]`

```
✓ As a customer, I want to filter products by price,
  so that I can find items within my budget.

✓ As an admin, I want to export user data to CSV,
  so that I can generate monthly reports.

✗ As a seller, I want to publish my products easily
  to increase my earnings.
  (bad: "easily" is ambiguous)
```

### Acceptance Criteria
*Conditions that define "done"*

**Template 1**: Checklist of rules the story must meet.

```
Story: User can reset password

Criteria:
- User receives email within 2 minutes
- Link expires after 24 hours
- New password must be at least 8 characters
- Old password no longer works after reset
```

**Template 2**: `Given [precondition], when [event], then [response].`

```
Given an employee is on payroll and single,
when the paycheck is created,
then federal single tax tables are used.
```

### Quality Criteria

**SMART** – Specific, Measurable, Achievable, Relevant, Time-bound  
**INVEST** – Independent, Negotiable, Valuable, Estimable, Small, Testable  

---

## System Features
*Expected functionalities*

### Templates

- `The [system] shall [response].`
- `If [preconditions], then the [system] shall [response].`
- `When [trigger], the [system] shall [response].`
- `While [state], the [system] shall [response].`
- `If the [feature] is enabled, the [system] shall [response].`

### Example

```
When there is a change in the flight schedule,
the system shall send a notification using the communication
mode specified in the traveler's preferences.
```

---

## Story Points
*Estimating effort, not time*

**Story Point** – Relative unit of effort/complexity, not hours  
**Velocity** – Average story points **completed (DONE)** per sprint — partially finished stories don't count

### Fibonacci Scale
*Non-linear scale reflects uncertainty*

```
1 – Trivial (fix a typo)
2 – Simple (add a field to a form)
3 – Small (new CRUD endpoint)
5 – Medium (feature with some complexity)
8 – Large (feature with significant complexity)
13 – Very large (consider breaking it down)
21+ – Too big, must be split
```

### Planning Poker
*Team estimation technique*

```
1. Present user story
2. Each member picks a card (secretly)
3. Reveal simultaneously
4. Discuss differences
5. Re-estimate until consensus
```

---

## Best Practices

- Write stories from the user's perspective, not the developer's
- One story = one unit of value
- Define acceptance criteria before development starts
- Estimate as a team, never alone
- Stories > 8 points should be split

---

## Summary
*All concepts in one glance*

**User Need** – What the user actually wants  
**User Goal** – Desire expressed as an "I want"  
**UX Scenario** – Situation, emotions, and context of the user  
**Requirement** – What the system must do to meet a need  
**Functional Requirement** – Specific behavior or function of the system  
**Non-Functional Requirement** – Quality attribute (performance, security, etc.)  
**Use Case** – Actor-driven flow of interaction with the system  
**User Story** – Requirement from the user's perspective  
**Acceptance Criteria** – Conditions that define "done" for a story  
**System Feature** – Expected functionality written with a fixed template  
**Story Point** – Relative unit of effort/complexity, not hours  
**Velocity** – Average story points completed per sprint

### Flow

```
Need → Goal → Scenario → Requirement (FR / NFR) → Use Case → User Story → Acceptance Criteria
```

### Common Confusions
*Pairs that students mix up — short distinction*

| Pair | Difference |
|---|---|
| Need vs Requirement | Need is the user's problem; requirement is the system's response to it |
| Goal vs Requirement | Goal is what the user *wants*; requirement is what the system *must do* |
| Functional vs Non-Functional | FR = what it does; NFR = how well it does it |
| Feature vs Requirement | Feature is a capability the user sees; requirement is the formal spec behind it |
| User Story vs Use Case | Story = short, user perspective; Use Case = detailed actor-driven flow |
| User Story vs Requirement | Same content, different audience (user-facing vs system-facing) |
| Acceptance Criteria vs Definition of Done | AC is per-story; DoD applies to every story in the team |
| Story Points vs Hours | Points = relative effort; hours = time estimate (avoid) |
| Epic vs Story | Epic is a large story that must be split into smaller ones |
