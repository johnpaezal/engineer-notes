# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Purpose

Personal learning repository for becoming an **AWS Engineer with full-stack backend focus**. Contains study notes, architecture prototypes, and Anki flashcard decks organized across 10 learning stages (see `ROADMAP.md`).

## Note Style

All notes follow the minimalist format defined in `CONTEXT.md`. Key rules:

- Title format: `# Technology Topic` (no "Notes" suffix)
- Every `##` and `###` section has a short italic description (3–6 words) directly below
- Definitions: `**Term** – Short definition (max 10 words)  ` — each line ends with two trailing spaces for line breaks
- Short inline lists for simple enumerations: `**Benefits**: A, B, C`
- Code blocks max 20–30 lines, one concept each, always include `# Usage` section
- `---` separator between every `##` section
- No verbose explanations, no redundant comments

## Concept Uniqueness

Each concept lives in exactly ONE file. Never duplicate a concept across notes — if it already exists elsewhere, do not copy it; omit it or reference the canonical file. Goal: clean notes with no repetition.

## Visual Elements Warning

If a concept requires a diagram that markdown cannot render well (2D matrices, diagrams with crossing arrows, wireframes, architecture diagrams with icons, sequence diagrams, ER diagrams, Gantt, burndown charts, journey maps, user story maps, impact maps, UML), **warn the user** instead of forcing an ugly text version. Suggest the right tool (Excalidraw, draw.io, Miro, Figma, Mermaid, PlantUML, dbdiagram.io) and recommend saving the image in a `diagrams/` folder next to the `.md`, referenced as `![title](diagrams/name.png)`. Keep markdown for: tables, lists, tree hierarchies (`├──`), linear flows (`A → B → C`), code blocks, text templates.

## Anki Cards (Automatic)

Every time a new topic is created or updated, immediately add the corresponding Anki cards to `anki-aws-engineer.txt`. Do not wait for the user to ask.

- Template and format reference: `.claude/PLANTILLA_ANKI.txt`
- Goal of the deck: **recognize that X exists and know its purpose** — not memorize syntax or details.

### Deck hierarchy

- **Mirror of the repo folder structure**, in English, PascalCase: `AwsEngineer::<Area>::<Topic>::<Subtopic>`
- One deck per note file. Examples:
  - `01-languages/python/01-core/control-flow.md` → `AwsEngineer::Languages::Python::Core::ControlFlow`
  - `06-cloud/aws/02-compute/ec2.md` → `AwsEngineer::Cloud::AWS::Compute::EC2`
- Top-level areas: `SoftwareEngineering`, `Languages`, `Infrastructure`, `Databases`, `Web`, `Tooling`, `Cloud`, `Automation`, `Career`, `SystemDesign`

### Card types

For each topic, generate **3–6 atomic cards** chosen from:

- **Existence** – `What is X?` → 1 line, what it is and what category
- **Purpose** – `What is X used for?` → the real problem it solves
- **Key Element** – `What is <element> of X?` → **one card per element** (never a bulk list)
- **When to use** – `When to use X vs Y?` → short `<table>` comparison
- **How it works** – `How does X work?` → 1-line mechanism (only if the internals matter)
- **Gotcha** – `Key gotcha about X?` → common pitfall, one line
- **Shape** – `What does X look like?` → minimal `<pre>` skeleton (not full code)

### Atomic rules (mandatory)

- **One idea per card.** If a concept has 5 sub-elements (e.g., DynamoDB: Partition Key, Sort Key, Item, Attribute, GSI/LSI), create **5 separate cards**, not one card with a bulleted list.
- **Lists with 4+ items are forbidden** — split into N atomic cards.
- **Tables only when the idea *is* the comparison** (X vs Y).

### Wording rules

- **All cards in English.** Front uses `What is...?` / `What does...?` / `When to use...?` / `How does...?`
- **Clarity over brevity**: if the concept name exists in multiple contexts (loop, class, list, lambda, mock, queue…), the question must include the language/domain. Examples:
  - ❌ `What is a class?` → ✅ `What is a class in Python?`
  - ❌ `What is a Lambda?` → ✅ `What is a Java lambda?` (and separately `What is AWS Lambda?`)
  - ❌ `What is a Queue?` → ✅ `What is a Queue (data structure)?` (and separately `What is AWS SQS?`)
- **Minimal answers**: 1–2 lines max. Use `<code>` for inline terms, `<pre>` for shape skeletons, `<table border="1" cellpadding="6">` for comparisons.

### Technical constraints (Anki TSV format)

- Format per line: `Deck::Path\tMiPlantilla\tFront\tBack` (tab-separated, exactly 4 columns).
- **No raw newlines inside `<pre>` blocks** — collapse multi-line code with `<br>` so each card is one physical line. A literal newline in the back will break the TSV import.
- HTML allowed: `<ul><li>`, `<table>`, `<pre>`, `<code>`, `<b>`, `<br>`. Always close every tag.
- Never use backticks `` ` `` in answers — use `<code>` instead.

### No-duplication rule

- Before adding a card, check if the concept already exists in another deck. If it does, **link via the note, don't duplicate in the deck.**
- Canonical placement priority for shared concepts:
  - AWS services → `Cloud::AWS::<Category>::<Service>` (not in certification decks)
  - Patterns (Circuit Breaker, Saga, Repository) → `SoftwareEngineering::Architecture::Patterns` or `SystemDesign::Patterns`, never both
  - Generic principles (SRP, DRY, KISS) → `SoftwareEngineering::Design::CleanCode` only

## Folder Structure Rules

- Numbered group folders: `01-grupo/`, `02-grupo/` (implies learning progression)
- Single-file topics go directly as `topic.md` inside the group — no subfolder
- Subfolders only when a topic has multiple files (e.g., `oop/notes.md` + `oop/example.py`)
- All names in `kebab-case` lowercase
- Each technology section has a `README.md` with an index table grouped by section

## Repository Map

Only folders that currently exist with content are listed. New stage folders are added on demand per `ROADMAP.md`.

| Folder | Content |
|--------|---------|
| `00-software-engineering/` | SE fundamentals: `01-process`, `02-design`, `03-architecture`, `04-quality`, `05-delivery`, `06-communication`, `07-global-example` |
| `01-languages/` | `python/` (core → fastapi, flask), `java/` (core → ecosystem) |
| `02-infrastructure/` | `docker/`, `networking/`, `linux/`, `bash/`, `kubernetes/` (linux, bash, kubernetes — pending notes) |
| `03-databases/` | `sql/`, `nosql/`, `data-modeling/` |
| `04-web/` | `angular/` (pending) |
| `05-tooling/` | `git/`, `json-yaml/`, `ci-cd/`, `testing/`, `best-practices/` (all pending) |
| `06-cloud/` | `aws/` (01-core → 08-security), `terraform/`, `cdk/` (all pending) |
| `07-automation/` | `claude-ai/`, `n8n/` |
| `08-career/` | `professional-profile/` (linkedin.md) |
| `09-system-design/` | `01-fundamentals/` → `04-case-studies/` (all pending) |
| `anki-aws-engineer.txt` | All Anki flashcard decks |
| `ROADMAP.md` | 10-stage learning plan with progress tracking |
| `CONTEXT.md` | Full style guide for notes and Anki format |

## Architecture Prototypes

`00-software-engineering/03-architecture/tipos-arquitecturas/` contains minimal Flask Todo apps showing architecture styles side by side:

- `01-capas/` — Layered: `repository.py` (data) → `service.py` (logic) → `routes.py` (HTTP) → `app.py` (entry)
- `02-monolito/` — Everything in a single `app.py`

Run any prototype with:
```bash
pip install flask
python app.py
```
