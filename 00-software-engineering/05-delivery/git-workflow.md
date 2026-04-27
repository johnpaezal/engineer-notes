# Git Workflow
*Branching strategies and collaboration conventions*

## Branching Strategies
*How teams organize branches*

### Gitflow
*Classic strategy for versioned releases*

```
main        ── production code, always stable
develop     ── integration branch
feature/*   ── new features (branch from develop)
release/*   ── release preparation (branch from develop)
hotfix/*    ── urgent prod fixes (branch from main)

Flow:
feature/login ──► develop ──► release/1.0 ──► main
                                                ↑
                              hotfix/fix-auth ──┘
```

**Use when** – Products with scheduled releases, versioning matters

### Trunk-Based Development
*Modern strategy for continuous delivery*

```
main        ── single source of truth, always deployable
feature/*   ── short-lived branches (max 1-2 days)

Flow:
feature/small-change ──► main (fast, frequent)
                          ↓
                     auto-deploy to prod
```

**Use when** – CI/CD, microservices, frequent releases (preferred in most modern teams)

### GitHub Flow
*Simple version of trunk-based*

```
1. Branch from main
2. Make changes
3. Open pull request
4. Review + CI passes
5. Merge to main
6. Deploy
```

---

## Branch Naming
*Clear, consistent branch names*

```
feature/user-authentication
feature/JIRA-123-password-reset
bugfix/fix-login-redirect
hotfix/critical-payment-error
chore/update-dependencies
refactor/extract-user-service
```

---

## Conventional Commits
*Standard format for commit messages*

**Format** – `type(scope): description`

```
feat(auth): add JWT authentication
fix(api): handle null response from payment service
docs(readme): update installation steps
refactor(user): extract validation logic
test(orders): add integration tests for checkout
chore(deps): update fastapi to 0.104
perf(db): add index on orders.created_at
ci(github): add deployment workflow
```

### Types

**feat** – New feature  
**fix** – Bug fix  
**docs** – Documentation only  
**refactor** – Code change, no new feature or fix  
**test** – Adding or fixing tests  
**chore** – Build process, dependencies, tooling  
**perf** – Performance improvement  
**ci** – CI/CD configuration  
**breaking change** – Add `!` after type: `feat!: remove deprecated endpoint`

---

## Semantic Versioning (SemVer)
*Standard for version numbers*

**Format** – `MAJOR.MINOR.PATCH`

```
1.0.0
│ │ └── PATCH: bug fix, backward compatible
│ └──── MINOR: new feature, backward compatible
└────── MAJOR: breaking change

Examples:
1.0.0 → 1.0.1   bug fix
1.0.1 → 1.1.0   new feature added
1.1.0 → 2.0.0   breaking API change
```

```
0.x.x  → unstable, initial development
1.0.0  → first stable release
```

---

## Pull Requests
*Code review workflow*

### PR Best Practices

```
✓ Small PRs (< 400 lines changed)
✓ One purpose per PR
✓ Clear title following conventional commits
✓ Description: what changed and why
✓ Link to ticket (Jira, Linear)
✓ CI must pass before review
✓ At least 1 approval before merge
✗ Never merge your own PR without review (unless solo project)
✗ Don't leave review comments unresolved
```

### PR Description Template

```markdown
## What
Brief description of the change.

## Why
Motivation — what problem does this solve?

## How
Technical approach taken.

## Testing
How was this tested?

Closes #123
```

---

## Git Commands for Workflow

```bash
# Start new feature
git checkout main && git pull
git checkout -b feature/my-feature

# Keep branch up to date with main
git fetch origin
git rebase origin/main

# Interactive rebase (clean up commits before PR)
git rebase -i HEAD~3

# Squash merge (clean history on main)
git merge --squash feature/my-feature

# Tag a release
git tag -a v1.2.0 -m "Release 1.2.0"
git push origin v1.2.0
```

---

## Monorepo vs Multirepo
*How to organize multiple projects in git*

**Monorepo** – All projects/services in a single repository  
**Multirepo** – Each service/project has its own repository  
**Polyrepo** – Another name for multirepo

### Monorepo

```
my-company/
├── services/
│   ├── user-service/
│   ├── order-service/
│   └── payment-service/
├── libraries/
│   ├── shared-models/
│   └── auth-utils/
└── infrastructure/
    └── terraform/
```

**Pros**:
- Shared code easy to reuse (no npm/pip package for every util)
- Atomic commits across services (one PR changes API + consumer)
- Single CI/CD pipeline configuration
- Easier refactoring across services

**Cons**:
- Repo grows large over time
- CI runs for everything on every commit (needs smart filtering)
- Requires tooling: Nx, Turborepo, Bazel, Pants

**Used by** – Google, Meta, Microsoft, Airbnb

### Multirepo

```
github.com/my-company/user-service
github.com/my-company/order-service
github.com/my-company/payment-service
github.com/my-company/shared-models  ← published as package
```

**Pros**:
- Independent CI/CD per service
- Teams fully autonomous
- Simpler per-repo tooling
- Fine-grained access control

**Cons**:
- Shared code requires versioned packages (overhead)
- Cross-service changes need multiple PRs
- Harder to keep dependencies in sync

**Used by** – Most companies with independent teams

### When to Choose Each

| Scenario | Use |
|---|---|
| Small team, shared codebase | Monorepo |
| Large org, independent teams | Multirepo |
| Lots of shared libraries | Monorepo |
| Services in different languages | Multirepo |
| Need atomic cross-service changes | Monorepo |
| Strict team autonomy needed | Multirepo |

---

## Best Practices

- Commit early and often (small, atomic commits)
- Never force-push to main or shared branches
- Delete branches after merging
- Write commit messages for the `git log` reader, not yourself
- Use `git stash` to context-switch without committing incomplete work
- Protect `main` branch: require PR + CI pass + approval
- In monorepos: use path filtering in CI to only run affected pipelines
