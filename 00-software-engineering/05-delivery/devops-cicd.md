# DevOps & CI/CD
*Automating software delivery*

## DevOps Philosophy
*Culture of collaboration between Dev and Ops*

**DevOps** – Culture + practices that unify development and operations  
**Goal** – Deliver software faster, more reliably, with less manual work

### Core Principles

**Collaboration** – Dev and Ops work together, share responsibility  
**Automation** – Automate everything: testing, building, deploying  
**Continuous Improvement** – Measure, learn, iterate  
**Shift Left** – Catch problems early (testing, security in development, not after)  
**Feedback Loops** – Fast feedback at every stage

```
Traditional:                DevOps:
Dev → (wall) → Ops         Dev + Ops working together
"Works on my machine"      "Shared ownership of production"
```

---

## CI/CD Overview
*Automated pipeline from code to production*

**CI (Continuous Integration)** – Automatically build and test on every commit  
**CD (Continuous Delivery)** – Automatically prepare release (manual deploy trigger)  
**CD (Continuous Deployment)** – Automatically deploy to production (no human trigger)

```
Code Push → CI: Build + Test → CD: Deploy to Staging → CD: Deploy to Prod
```

---

## CI Pipeline
*Automated checks on every commit*

### Typical CI Steps

```yaml
# GitHub Actions example
name: CI

on: [push, pull_request]

jobs:
  build-and-test:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: "3.11"

      - name: Install dependencies
        run: pip install -r requirements.txt

      - name: Run linter
        run: flake8 .

      - name: Run tests
        run: pytest --cov=app

      - name: Build Docker image
        run: docker build -t myapp:${{ github.sha }} .
```

### CI Pipeline Stages
*Ordered checks*

```
1. Checkout code
2. Install dependencies
3. Lint / format check
4. Run unit tests
5. Run integration tests
6. Build artifact (Docker image, JAR, etc.)
7. Push artifact to registry
```

---

## CD Pipeline
*Automated deployment*

```yaml
  deploy:
    needs: build-and-test
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main'

    steps:
      - name: Deploy to staging
        run: |
          ssh deploy@staging "docker pull myapp:${{ github.sha }}"
          ssh deploy@staging "docker-compose up -d"

      - name: Run smoke tests
        run: curl -f https://staging.myapp.com/health

      - name: Deploy to production
        run: |
          ssh deploy@prod "docker pull myapp:${{ github.sha }}"
          ssh deploy@prod "docker-compose up -d"
```

---

## Popular Tools

### CI/CD Platforms

**GitHub Actions** – Native to GitHub, YAML-based, free for public repos  
**GitLab CI/CD** – Built into GitLab, powerful for self-hosted  
**Jenkins** – Open source, highly customizable, older standard  
**CircleCI** – Fast, Docker-first CI/CD

### Supporting Tools

**Docker** – Package app + dependencies into container  
**Docker Hub / ECR** – Store Docker images (registry)  
**SonarQube** – Code quality and security analysis  
**Trivy** – Container vulnerability scanning

---

## Environments
*Separate stages for safe deployment*

```
Development → Staging → Production

Development:  Local or shared dev environment
Staging:      Mirror of production, for final testing
Production:   Live environment, real users
```

### Deployment Strategies

**Blue/Green** – Two identical environments, switch traffic instantly

```
Blue (current) → 100% traffic
Green (new)    → deploy and test
Switch:          Green → 100% traffic
```

**Canary** – Gradually shift traffic to new version

```
v1: 90% traffic
v2: 10% traffic → monitor → increase if stable
```

**Rolling** – Replace instances one by one  
**Recreate** – Stop all, deploy new (downtime, simplest)

---

## Key Metrics
*Measuring DevOps performance (DORA metrics)*

**Deployment Frequency** – How often code is deployed to production  
**Lead Time** – Time from commit to production  
**Mean Time to Recovery (MTTR)** – How fast you recover from failures  
**Change Failure Rate** – % of deployments that cause incidents

```
Elite teams:
  Deployment frequency: Multiple times/day
  Lead time:            < 1 hour
  MTTR:                 < 1 hour
  Change failure rate:  0–15%
```

---

## Best Practices

- Every commit triggers the CI pipeline
- Never merge code that breaks the pipeline
- Keep pipeline fast (< 10 min for CI)
- Deploy to staging automatically, production manually at first
- Use feature flags to decouple deployment from release
- Monitor production after every deployment
- Rollback must be possible in under 5 minutes
