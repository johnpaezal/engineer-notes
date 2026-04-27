# Scrum
*Agile framework for iterative delivery*

**Scrum** – Framework to deliver software in short cycles called sprints  
**Agile** – Mindset and set of values defined in the Agile Manifesto (2001)

---

## Roles
*Who does what in a Scrum team*

**Product Owner (PO)** – Owns the backlog, defines priorities, represents stakeholders  
**Scrum Master** – Facilitates process, removes blockers, protects the team  
**Developers** – Self-organizing team that builds the product (renamed from "Development Team" in Scrum Guide 2020)

---

## Ceremonies
*Regular meetings in Scrum*

**Backlog Refinement** – Ongoing ceremony to clarify and estimate upcoming stories before Planning  
**Sprint Planning** – Team selects already-estimated stories and defines the Sprint Goal  
**Daily Scrum** – 15-min daily sync to inspect progress toward the Sprint Goal and adjust the plan  
**Sprint Review** – Demo completed work to stakeholders at end of sprint  
**Retrospective** – Team reflects: what went well, what to improve

```
Sprint cycle (1-2 weeks):

Backlog Refinement → Sprint Planning → Daily Scrums → Sprint Review → Retrospective
        ↑                                                                    |
        └──────────────────────── next sprint ──────────────────────────────┘
```

---

## Sprint
*Fixed time box for delivering value*

**Sprint** – Fixed time period (usually 1–2 weeks) where the team delivers a set of stories

```
Sprint 1 (2 weeks):
  ├── Story: User can register        (3 pts) ✓
  ├── Story: User can log in          (2 pts) ✓
  └── Story: User can reset password  (5 pts) ✓
  Total: 10 pts → Velocity = 10

Sprint 2:
  Plan stories up to ~10 pts (based on velocity)
```

---

## Backlog
*Ordered list of work to be done*

**Product Backlog** – All stories for the product (ordered by priority)  
**Sprint Backlog** – Stories committed for current sprint  
**Epic** – Large user story broken into smaller ones

```
Epic: User Authentication
  ├── Story: User can register        (3 pts)
  ├── Story: User can log in          (2 pts)
  ├── Story: User can reset password  (5 pts)
  └── Story: User can log out         (1 pt)
```

---

## Definition of Ready
*Criteria a story must meet to enter a sprint*

```
A story is READY when:
  ✓ Clear user story format (As a... I want... so that...)
  ✓ Acceptance criteria defined
  ✓ Estimated in story points
  ✓ No blocking dependencies
  ✓ Small enough to fit in one sprint
```

---

## Definition of Done
*Shared agreement on what "done" means*

```
A story is DONE when:
  ✓ Code is written and reviewed
  ✓ Tests pass (unit + integration)
  ✓ Deployed to staging
  ✓ Acceptance criteria met
  ✓ No known bugs introduced
```

---

## Tools & Platforms
*Where teams manage requirements and sprints*

**Jira** – Industry standard for Agile/Scrum. Backlog, sprints, epics, story points, reports. Used in most companies.  
**Linear** – Modern, fast alternative to Jira. Popular in startups.  
**Trello** – Kanban boards, simple and visual. Good for small teams.  
**GitHub Projects** – Kanban + issues directly in GitHub. Good for dev-focused teams.  
**Notion** – Flexible docs + databases. Used for lightweight project tracking.  
**Azure DevOps** – Microsoft's full suite: boards, repos, pipelines.

### Jira – Scrum Features

```
Backlog        → prioritized list of all stories
Sprint Board   → kanban view of current sprint
Epics          → group stories by feature
Story Points   → estimate field per issue
Velocity Chart → points completed per sprint over time
Burndown Chart → remaining work vs time in sprint
```

---

## Best Practices

- Keep Daily Standups short — blockers only, no deep discussion
- Retrospectives must produce concrete action items, not just complaints
- PO must be available during the sprint, not only at review
- Never add stories mid-sprint without removing others
- Demo real working software at Sprint Review, not slides
