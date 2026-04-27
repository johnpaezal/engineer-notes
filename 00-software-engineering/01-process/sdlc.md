# Software Development Lifecycle
*Phases from idea to production*

## Phases
*Sequence of work to build software*

```
Planning → Analysis → Design → Development → Testing → Deployment → Maintenance
```

| Phase | Description |
|---|---|
| Planning | Define scope, goals, feasibility, resources |
| Analysis | Gather requirements, understand what to build |
| Design | Architecture, database schema, UI wireframes |
| Development | Write code following the design |
| Testing | Unit, integration, QA — verify it works |
| Deployment | Release to production |
| Maintenance | Bug fixes, updates, new features |

---

## Common Models
*Different ways to move through the phases*

### Waterfall
*Sequential, phase by phase*

Each phase ends before the next starts. Predictable but inflexible.

- **Flow**: Planning → Analysis → Design → Development → Testing → Deployment
- **Delivery**: Only at the end
- **Change cost**: Very high once a phase is closed
- **Best for**: Fixed-scope projects, regulated industries

### Agile
*Iterative, adapts to change*

Short cycles (sprints) deliver working software early and often.

- **Flow**: Repeat → Plan → Build → Test → Release → Feedback
- **Delivery**: Every sprint (1–4 weeks)
- **Change cost**: Low — requirements evolve
- **Best for**: Products with unclear or changing requirements

### Scrum
*Agile framework with structure*

Concrete implementation of Agile with fixed roles, ceremonies, and artifacts.

- **Delivery**: Each sprint (1–4 weeks)
- **Best for**: Teams that need discipline around Agile

### Kanban
*Continuous flow, visual board*

No sprints. Pull work as capacity frees up.

- **Flow**: To Do → In Progress → Done (columns on a board)
- **Delivery**: Continuous, whenever an item is ready
- **Key metric**: WIP limits (Work In Progress)
- **Best for**: Support, maintenance, ops teams

### Comparison

| Model | Flexibility | Delivery | Best for |
|---|---|---|---|
| Waterfall | Low | End only | Fixed-scope projects |
| Agile/Scrum | High | Each sprint | Evolving requirements |
| Kanban | High | Continuous | Support / maintenance |

---

## Best Practices

- Match the model to the project — fixed-scope → Waterfall, evolving → Agile
- Don't skip phases, even if short (a 10-min design beats no design)
- Maintenance is where most of the lifetime cost lives — plan for it
