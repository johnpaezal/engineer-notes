# Prompt para Crear Notas Técnicas Minimalistas

Crea notas técnicas sobre **[TEMA]** siguiendo este estilo minimalista y universal:

---

## ESTRUCTURA GENERAL

### 1. Encabezado Principal

- Título: `# [Tecnología] [Tema]` — ej. `# Python OOP`, `# Python Testing`, `# React Hooks`
- **Sin** la palabra "Notes" al final
- Sin introducción larga, directo al contenido

### 2. Organización por Secciones

```markdown
## Sección Principal
*Descripción corta en cursiva (3-6 palabras)*

### Subsección
*Descripción corta en cursiva (3-6 palabras)*

Contenido...

---

## Siguiente Sección
```

---

## REGLAS DE FORMATO

### Descripciones

- **Cada sección y subsección** debe tener una línea en cursiva debajo del título, de 3 a 6 palabras máximo.
- **Propósito**: Responder "¿qué hace/es esto?" de forma inmediata.
- Ejemplos:
  - `*Storing and managing data*`
  - `*Execute code based on conditions*`
  - `*Ordered sequences with duplicates allowed*`

### Definiciones

- Formato obligatorio: `**Término** – Definición corta (max 10 palabras)`
- Sin explicaciones largas, solo lo esencial.
- **IMPORTANTE — Saltos de línea**: Cuando hay varias definiciones seguidas en vertical, cada línea DEBE terminar con **dos espacios** (`  `) para forzar el salto de línea en Markdown. Sin esto, las líneas se renderizan como texto continuo pegado.

Ejemplo correcto (cada línea termina con dos espacios):

```markdown
**int** – Whole numbers  
**float** – Decimal numbers  
**str** – Text (single or double quotes)  
**bool** – `True` / `False`  
**None** – Absence of value
```

Ejemplo incorrecto (sin dos espacios al final):

```markdown
**int** – Whole numbers
**float** – Decimal numbers
**str** – Text
```

Esto se renderiza como un solo párrafo continuo en lugar de líneas separadas.

### Listas de Características en Línea

Cuando se listan beneficios, pilares o propiedades cortas, usar una sola línea:

```markdown
**Benefits**: Reusability, Maintainability, Modifiability, Reliability

**Four Pillars**: Abstraction, Encapsulation, Inheritance, Polymorphism
```

NO hacer listas verticales largas con explicaciones para cada punto cuando la idea es simple.

### Separadores y Saltos de Línea

- `---` entre secciones mayores (entre cada `##`).
- **Dos espacios al final de línea** (`  `) para forzar saltos en listas de definiciones verticales (`**Term** – Def  `).
- NO usar líneas en blanco excesivas.
- Una línea en blanco entre conceptos relacionados dentro de la misma sección.

---

## ESTILO DE CÓDIGO

### Bloques de Código

```python
# Comentarios SOLO cuando agregan valor
# NO comentar lo obvio

class User:
    def __init__(self, name):
        self.name = name
    
    def greet(self):
        print(f"Hello, {self.name}")

# Usage
user = User("Alice")
user.greet()  # "Hello, Alice"
```

### Reglas para Código

1. **Ejemplos cortos**: Máximo 20-30 líneas por bloque.
2. **Un concepto por ejemplo**: No mezclar múltiples ideas.
3. **Comentarios inline**: Solo para clarificar salida o contexto (ej. `# "Hello, Alice"`).
4. **Sin código repetitivo**: Mostrar el patrón una sola vez.
5. **Nombres descriptivos**: `user`, `product`, `order` — nunca `x`, `y`, `foo`.
6. **Siempre incluir "# Usage"**: Mostrar cómo se usa después de definir.

### Mostrar Múltiples Variantes

Cuando existan varias formas de hacer algo, mostrarlas juntas con comentarios cortos:

```python
# Basic
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")

# Multiple catch
try:
    # code
except TypeError:
    # handle
except ValueError:
    # handle

# Finally
try:
    # code
finally:
    # always runs
```

---

## PRESENTACIÓN DE CONCEPTOS

### Comparaciones y Relaciones

Usar definiciones alineadas con `**Término** – Definición` (cada línea con dos espacios al final), seguidas de código si es necesario:

```markdown
**Inheritance** – "Is-a" relationship  
**Composition** – "Has-a" relationship (strong)  
**Aggregation** – "Has-a" relationship (weak)
```

### Tablas de Referencia Rápida

Usar tablas solo cuando hay 3+ columnas de información paralela:

```markdown
| Element    | Convention       | Example              |
|------------|------------------|----------------------|
| Class      | PascalCase       | `UserAccount`        |
| Variable   | snake_case       | `first_name`         |
| Constant   | UPPER_SNAKE_CASE | `MAX_SIZE`           |
```

### Niveles de Acceso y Similares

Usar listas con prefijo de código cuando se describen variantes:

```markdown
- `public` – normal attributes (no prefix)
- `_protected` – convention, use underscore prefix
- `__private` – name mangling, use double underscore prefix
```

---

## LO QUE NO HACER

### 1. Explicaciones Verbosas

```markdown
❌ "A constructor is a special method that is called when an object 
    is instantiated. It is used to initialize the object's attributes 
    with values that are passed as parameters..."

✅ **Constructor (`__init__`)** – Initialize objects when created
```

### 2. Ejemplos Largos y Complejos

```markdown
❌ 50+ líneas de código con múltiples conceptos mezclados

✅ 10-20 líneas enfocadas en un solo concepto + sección "# Usage"
```

### 3. Comentarios Redundantes

```python
❌ x = 5  # assign 5 to variable x

✅ count = 0  # tracks active users
```

### 4. Repetir Información

```markdown
❌ Explicar lo mismo en descripción, definición y código

✅ Definición breve + código que lo demuestra
```

### 5. Código Sin Contexto de Uso

```python
❌ Solo definir función sin mostrar cómo se usa

✅ Definir + "# Usage" con ejemplo práctico al final
```

---

## ESTRUCTURA POR TIPO DE TEMA

### Para Lenguajes de Programación

1. Setup / IDE / Tools
2. Shortcuts (si aplica)
3. Naming Conventions
4. Fundamentals (tipos, variables, operadores)
5. Control Flow
6. Collections / Data Structures
7. Functions / Methods
8. OOP (si aplica)
9. Advanced Topics
10. Best Practices

### Para Bases de Datos

1. Fundamentals (tipos, conceptos)
2. Basic Operations (CRUD)
3. Advanced Queries
4. Constraints & Indexes
5. Transactions
6. Design Patterns
7. Best Practices

### Para Frameworks / Libraries

1. Setup & Installation
2. Core Concepts
3. Basic Usage
4. Common Patterns
5. Advanced Features
6. Best Practices

---

## PRINCIPIOS CLAVE

**Minimalismo** – Una idea por sección, ejemplos que se leen en 10 segundos, sin relleno.

**Universalidad** – Código y términos en inglés, ejemplos genéricos (`User`, `Product`, `Order`), convenciones estándar de industria.

**Escaneabilidad** – Jerarquía visual clara con `##` y `###`, código destacado en bloques, información agrupada por concepto.

**Practicidad** – Ejemplos realistas, código que funciona al copiar-pegar, patrones que realmente se usan en desarrollo.

---

## PLANTILLA BASE

```markdown
# [Technology] [Topic]

## Section Name
*Short description in italics*

### Subsection Name
*Short description in italics*

**Key Term** – Brief definition (max 10 words)

```[language]
# Minimal code example
concept demonstration

# Usage
practical application
```

---

## Next Section
*Short description*

### Subsection
*Short description*

Content following same pattern...

---

## Best Practices

**Naming Conventions**:
- Classes: `PascalCase`
- Methods/attributes: `snake_case`
- Constants: `UPPER_SNAKE_CASE`

**Principles**:
- Single Responsibility – One class, one purpose
- Keep methods short and focused
- Use descriptive names
```

---

## ORGANIZACIÓN DE CARPETAS

### Estructura general

```
tecnologia/
├── README.md  
├── 01-grupo/  
│   ├── tema-a.md  
│   └── tema-b.md  
├── 02-grupo/  
│   ├── tema-c.md  
│   └── tema-con-archivos/      ← solo si tiene más de 1 archivo  
│       ├── notes.md  
│       └── example.py  
└── 03-grupo/  
    └── tema-d.md  
```

### Reglas de estructura

1. **Grupos numerados** — carpetas con prefijo `01-`, `02-`... para mantener orden visual en el explorador de archivos. El número implica progresión de aprendizaje.

2. **Archivos planos** — si un tema tiene un solo archivo, va directo como `tema.md` dentro del grupo. **No crear subcarpeta** solo para contener un `notes.md`.

3. **Subcarpeta solo si hay múltiples archivos** — ej. `oop/notes.md` + `oop/example.py` justifica una carpeta `oop/`.

4. **Nombres en `kebab-case` minúsculas** — `error-handling.md`, `design-patterns.md`, `env-config.md`. Sin mayúsculas, sin espacios.

5. **README por tecnología** — tabla de índice agrupada por sección, con una línea descriptiva en cursiva por grupo.

### Formato del README

```markdown
# [Tecnología] Notes

## Index

### 01 - Nombre del Grupo
*Descripción corta en cursiva*

| # | Topic | Path |
|---|-------|------|
| 1 | Tema A | `01-grupo/tema-a.md` |
| 2 | Tema B | `01-grupo/tema-b.md` |

### 02 - Siguiente Grupo
*Descripción corta en cursiva*

| # | Topic | Path |
|---|-------|------|
| 3 | Tema C | `02-grupo/tema-c.md` |
```

### Ejemplo real - Python Notes

```
python/
├── README.md
├── 01-core/       fundamentals.md, control-flow.md, functions.md, data-structures.md
├── 02-oop/        oop/ (notes.md + example.py), solid.md, design-patterns.md
├── 03-stdlib/     modules.md, error-handling.md, file-io.md, regex.md, logging.md, datetime.md, collections.md
├── 04-advanced/   language-features.md, stdlib-utils.md, concurrency.md
├── 05-tooling/    testing.md, debugging.md, packaging.md, env-config.md, cli.md
└── 06-ecosystem/  database.md, http.md, pydantic.md
```

---

## CHECKLIST FINAL

Antes de entregar las notas, verificar:

- [ ] Cada sección (`##`) y subsección (`###`) tiene descripción en cursiva
- [ ] Definiciones con formato `**Term** – Definition`
- [ ] Ejemplos de código < 30 líneas con sección `# Usage`
- [ ] Separadores `---` entre secciones mayores
- [ ] Sin explicaciones redundantes ni relleno
- [ ] Términos clave en negrita
- [ ] Jerarquía clara (`##` → `###`)
- [ ] Sin comentarios obvios en código
- [ ] Nombres descriptivos en ejemplos (`user`, `product`, no `x`, `foo`)
- [ ] Listas de definiciones verticales terminan con dos espacios por línea
- [ ] Listas de propiedades en línea cuando son cortas
- [ ] Best Practices al final del documento
- [ ] Título sin la palabra "Notes" — formato `# Tecnología Tema`

**Carpetas**:
- [ ] Grupos numerados (`01-`, `02-`...)
- [ ] Archivos planos (`tema.md`) salvo cuando hay múltiples archivos por tema
- [ ] Nombres en `kebab-case` minúsculas
- [ ] README con tabla por grupo y descripción en cursiva

**Regla de oro**: Si algo puede explicarse en menos palabras, hazlo.

---

## MAZOS DE ANKI

### Formato general

Los mazos de Anki se guardan como archivos `.txt` en la raíz del proyecto con el nombre `anki-<tema>.txt`.

La plantilla de referencia con ejemplos está en `.claude/PLANTILLA_ANKI.txt`.

Cada línea sigue este formato (separado por Tab):

```
Mazo::Submazo	MiPlantilla	Frente	Reverso
```

El archivo debe empezar con:

```
#separator:Tab
#html:true
#deck column:1
#notetype column:2
```

### Estructura de mazos

- **Mazo principal**: nombre del proyecto o área (ej. `AwsEngineer`)
- **Submazos**: `Mazo::Area::Tema::Subtema` (ej. `AwsEngineer::BaseDatos::SQL::Indexes`)
- **Profundidad**: la que necesite el tema — sin límite fijo

### Tipos de respuesta — variar según el contenido

El HTML se escribe inline en la columna del reverso. Mezclar tipos según lo que se enseña:

**Texto corto** — para definiciones y conceptos simples:
```
¿Qué es X?	Definición breve en una o dos líneas.
```

**Lista** — para enumeraciones y pilares:
```
¿Cuáles son los X?	<ul><li><b>A</b> – descripción</li><li><b>B</b> – descripción</li></ul>
```

**Tabla** — para comparaciones entre dos o más cosas:
```
¿Diferencia entre X e Y?	<table border="1" cellpadding="6"><tr><th>X</th><th>Y</th></tr><tr><td>...</td><td>...</td></tr></table>
```

**Código inline** — para sintaxis y comandos:
```
¿Cómo se hace X en Python?	<pre>código aquí</pre>
```

### Reglas para las tarjetas

- **Frente**: pregunta directa, breve, con `¿...?`
- **Reverso**: respuesta mínima — solo lo esencial, sin contexto extra
- Una idea por tarjeta
- Variar los tipos de respuesta para que el repaso sea dinámico
- No poner detalles muy específicos — solo lo que hay que tener claro para entender el concepto

### Flujo por defecto

Cada vez que el usuario pide crear o agregar un tema:

1. Crear/actualizar la nota `.md` con el contenido
2. Inmediatamente después, agregar las tarjetas Anki correspondientes al archivo `anki-aws-engineer.txt`

Esto es automático — no esperar a que el usuario lo pida por separado.