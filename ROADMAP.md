# AWS Engineer Roadmap

## Goal
Conseguir un puesto como **AWS Engineer** con perfil full-stack backend.

---

## Stage 0 — Ingeniería de Software (Transversal)
*Conceptos que aplican a todo lo demás*

- [x] **SDLC (Software Development Lifecycle)** → `00-software-engineering/01-process/sdlc.md`
- [x] **Requirements & User Stories** → `00-software-engineering/01-process/requirements.md`
- [x] **Scrum & Plataformas** → `00-software-engineering/01-process/scrum.md`
- [x] **REST API Design** → `00-software-engineering/02-design/rest-api.md`
- [x] **Design Patterns + MVC** → `00-software-engineering/02-design/design-patterns.md`
- [x] **Clean Code** → `00-software-engineering/02-design/clean-code.md`
- [x] **Architecture** → `00-software-engineering/03-architecture/`
  - Styles, Components, Diagrams, Patterns, Scalability
- [x] **Testing** → `00-software-engineering/04-quality/testing.md`
- [x] **Security – OWASP** → `00-software-engineering/04-quality/security-owasp.md`
- [x] **Observability** → `00-software-engineering/04-quality/observability.md`
- [x] **DevOps & CI/CD** → `00-software-engineering/05-delivery/devops-cicd.md`
- [x] **IaC & Terraform** → `00-software-engineering/05-delivery/iac-terraform.md`
- [x] **Git Workflow** → `00-software-engineering/05-delivery/git-workflow.md`
- [x] **Message Queues** → `00-software-engineering/06-communication/message-queues.md`
- [x] **Documentation** → `00-software-engineering/06-communication/documentation.md`

---

## Stage 1 — Fundamentos (Base de todo)
*Sin esto, nada de lo demás tiene sentido*

- [ ] **Linux** → `02-infrastructure/linux/`
  - Comandos esenciales, permisos, procesos, systemd
- [ ] **Bash** → `02-infrastructure/bash/`
  - Scripts, variables, condicionales, loops, cron
- [x] **Redes básicas** → `02-infrastructure/networking/`
  - Fundamentos, OSI, TCP/IP, IP+Subnets, DNS, HTTP/HTTPS, Puertos, Seguridad
- [ ] **Git + GitHub** → `05-tooling/git/`
  - Commits, branches, merge, rebase, pull requests
- [ ] **JSON / YAML** → `05-tooling/json-yaml/`
  - Sintaxis, validación, uso en configs

---

## Stage 2 — Contenedores y DevOps
*Lo que usan todos los equipos modernos*

- [ ] **Docker** → `02-infrastructure/docker/`
  - Imágenes, contenedores, Dockerfile, docker-compose
- [ ] **CI/CD** → `05-tooling/ci-cd/`
  - GitHub Actions, pipelines, deploy automático
- [ ] **Kubernetes** → `02-infrastructure/kubernetes/`
  - Pods, deployments, services, ingress

---

## Stage 3 — Backend
*El código que correrá en AWS*

- [ ] **Python avanzado** → `01-languages/python/` ✓ (notas completas)
  - Revisar y practicar con proyectos
- [ ] **FastAPI** → `01-languages/python/07-fastapi/`
  - Routing, modelos, autenticación, deploy
- [ ] **Java avanzado** → `01-languages/java/` ✓ (notas completas)
  - Revisar y practicar con proyectos
- [ ] **Spring Boot** → `01-languages/java/07-spring-boot/`
  - REST API, JPA, seguridad, testing, deploy

---

## Stage 4 — Bases de Datos
*Persistencia de datos*

- [x] **SQL** → `03-databases/sql/`
  - Fundamentals, queries, joins, indexes, transactions, views, normalization
- [x] **Data Modeling** → `03-databases/data-modeling/`
  - ER diagrams, relationships, normalization, schema patterns
- [x] **NoSQL** → `03-databases/nosql/`
  - DynamoDB, Redis, MongoDB overview, when to use each

---

## Stage 5 — AWS Core ⭐
*El corazón del perfil*

- [ ] **IAM + Core** → `06-cloud/aws/01-core/`
  - Usuarios, roles, policies, regiones, availability zones
- [ ] **Compute** → `06-cloud/aws/02-compute/`
  - EC2, Lambda, ECS, EKS
- [ ] **Storage** → `06-cloud/aws/03-storage/`
  - S3, EBS, EFS
- [ ] **Database** → `06-cloud/aws/04-database/`
  - RDS, DynamoDB, ElastiCache
- [ ] **Networking** → `06-cloud/aws/05-networking/`
  - VPC, subnets, security groups, ALB, Route53
- [ ] **Messaging** → `06-cloud/aws/06-messaging/`
  - SQS, SNS, EventBridge
- [ ] **DevOps AWS** → `06-cloud/aws/07-devops/`
  - CloudWatch, CodePipeline, CodeBuild
- [ ] **Security AWS** → `06-cloud/aws/08-security/`
  - IAM avanzado, KMS, Secrets Manager

---

## Stage 6 — Infrastructure as Code ⭐
*Diferenciador clave en entrevistas*

- [ ] **Terraform** → `06-cloud/terraform/`
  - Providers, resources, variables, modules, state
- [ ] **AWS CDK** → `06-cloud/cdk/`
  - Stacks, constructs, deploy con Python o Java

---

## Stage 7 — System Design
*Entrevistas técnicas y trabajo real*

- [ ] **Fundamentos** → `09-system-design/01-fundamentals/`
  - Escalabilidad, disponibilidad, latencia, CAP theorem
- [ ] **Componentes** → `09-system-design/02-components/`
  - Load balancer, cache, CDN, message queues, DB sharding
- [ ] **Patrones** → `09-system-design/03-patterns/`
  - Microservicios, event-driven, serverless, CQRS
- [ ] **Casos reales** → `09-system-design/04-case-studies/`
  - Diseñar: URL shortener, sistema de notificaciones, API escalable

---

## Stage 8 — Testing y Buenas Prácticas
*Código profesional y mantenible*

- [ ] **Testing** → `05-tooling/testing/`
  - Unit, integration, e2e, mocking
- [ ] **Best Practices** → `05-tooling/best-practices/`
  - .env, .gitignore, secrets, estructura de proyectos
- [ ] **README profesional** → `08-career/professional-profile/`

---

## Stage 9 — Certificación AWS ⭐
*Validación formal del perfil*

- [ ] **AWS Cloud Practitioner** (CLF-C02) — entry level, primero
- [ ] **AWS Solutions Architect Associate** (SAA-C03) — el real para engineer

---

## Stage 10 — Perfil y Proyectos
*Lo que te consigue el trabajo*

- [ ] **GitHub bien armado** → `08-career/professional-profile/`
  - README de perfil, repos organizados, proyectos destacados
- [ ] **LinkedIn** → `08-career/professional-profile/`
  - Headline, about, experiencia con keywords AWS
- [ ] **Proyecto 1** → API REST con FastAPI + PostgreSQL + Docker
- [ ] **Proyecto 2** → API REST con Spring Boot + RDS + deploy en AWS
- [ ] **Proyecto 3** → Infraestructura AWS con Terraform (VPC + EC2 + RDS)
- [ ] **Proyecto 4** → Sistema serverless (Lambda + API Gateway + DynamoDB)

---

## Frontend (paralelo, no bloqueante)

- [ ] **Angular** → `04-web/angular/`
  - Componentes, routing, servicios, HTTP, formularios

---

## Automation (cuando tengas tiempo)

- [ ] **N8N** → `07-automation/n8n/`
- [ ] **Claude AI** → `07-automation/claude-ai/` (notas básicas existentes)

---

## Progress

| Stage | Tema | Estado |
|---|---|---|
| 0 | Requirements & User Stories | ✅ Notas completas |
| 0 | Scrum & Plataformas | ✅ Notas completas |
| 0 | REST API Design | ✅ Notas completas |
| 0 | Design Patterns + MVC | ✅ Notas completas |
| 0 | Testing | ✅ Notas completas |
| 0 | DevOps & CI/CD | ✅ Notas completas |
| 0 | IaC & Terraform (conceptos) | ✅ Notas completas |
| 0 | Clean Code | ✅ Notas completas |
| 0 | Git Workflow | ✅ Notas completas |
| 0 | Security – OWASP | ✅ Notas completas |
| 0 | Observability | ✅ Notas completas |
| 0 | Documentation | ✅ Notas completas |
| 0 | Message Queues | ✅ Notas completas |
| 0 | Architecture | ✅ Notas completas |
| 1 | Linux | ⬜ Pendiente |
| 1 | Bash | ⬜ Pendiente |
| 1 | Redes | ✅ Notas completas |
| 1 | Git | ⬜ Pendiente |
| 1 | JSON/YAML | ⬜ Pendiente |
| 2 | Docker | ⬜ Pendiente |
| 2 | CI/CD | ⬜ Pendiente |
| 2 | Kubernetes | ⬜ Pendiente |
| 3 | Python | ✅ Notas completas |
| 3 | FastAPI | ⬜ Pendiente |
| 3 | Java | ✅ Notas completas |
| 3 | Spring Boot | ⬜ Pendiente |
| 4 | SQL | ✅ Notas completas |
| 4 | Data Modeling | ✅ Notas completas |
| 4 | NoSQL (DynamoDB, Redis) | ✅ Notas completas |
| 5 | AWS Core | ⬜ Pendiente |
| 6 | Terraform | ⬜ Pendiente |
| 6 | CDK | ⬜ Pendiente |
| 7 | System Design | ⬜ Pendiente |
| 8 | Testing | ⬜ Pendiente |
| 8 | Best Practices | ⬜ Pendiente |
| 9 | AWS Cloud Practitioner cert | ⬜ Pendiente |
| 9 | AWS SAA cert | ⬜ Pendiente |
| 10 | GitHub perfil | ⬜ Pendiente |
| 10 | LinkedIn | ⬜ Pendiente |
| 10 | Proyecto 1 — FastAPI | ⬜ Pendiente |
| 10 | Proyecto 2 — Spring Boot | ⬜ Pendiente |
| 10 | Proyecto 3 — Terraform | ⬜ Pendiente |
| 10 | Proyecto 4 — Serverless | ⬜ Pendiente |
