# **Ingeniería de Software II**  


***

# 1. Systems Thinking (Pensamiento Sistémico)

### 1.1 ¿Qué es un sistema?

Un sistema es un conjunto de elementos interrelacionados que trabajan para un objetivo común.  
Incluye:

- Entradas  
- Procesos  
- Salidas  

### 1.2 ¿Qué es el análisis de sistemas?

Es el proceso de entender un sistema e identificar:

- Sus componentes  
- Sus interacciones  
- Sus objetivos  
- Cómo mejorarlo  
---

- Modelado de datos  
- Modelado de procesos  
- Análisis de requisitos  

***

# 2. Object-Oriented Design (Diseño Orientado a Objetos)

### 2.9 CRC Cards (Class–Responsibility–Collaboration)

Tarjetas que describen:

- Clase  
- Responsabilidades  
- Colaboradores  

Se usan para el diseño inicial del sistema antes de codificar.

***

     

Regla de oro:

- Composición sobre herencia  
- Programar contra interfaces (no clases concretas)  

***

# 4. Domain-Driven Design (DDD)

### 4.1 Objetivo de DDD

Diseñar software alineado con el negocio real.

### 4.2 Conceptos clave

- Context → ambiente en el que opera un concepto  
- Model → representación del dominio  
- Ubiquitous Language → lenguaje común entre devs y expertos del negocio  
- Bounded Context → límites claros del modelo  

Business Logic Layers:

- Domain Layer  
- Application Layer  
- Presentation Layer  
- Infrastructure Layer  

### 4.3 Modelos de procesos

- Diagramas de flujo  
- DFD  
- BPMN  
- UML (actividades, estados, etc.)  

***

# 5. Reference Architectures

### 5.1 Diseño antes del código

- Primero requisitos  
- Luego diseño  
- Después implementación  

Nunca al revés.

### 5.2 Tipos de arquitecturas

Monolítica:

- Todo junto en un sistema único  
- Fácil de desarrollar  
- Mala escalabilidad  

Client–Server:

- Cliente interactúa con un servidor  
- Más compleja  
- Escalable  

Distributed / Peer-to-Peer:

- Tareas repartidas  
- Alta disponibilidad  

### 5.3 Arquitecturas de software

Layered Architecture (arquitectura por capas):

- Presentation  
- Business  
- Persistence  
- Database  

Muy común en proyectos tradicionales.

Microservices:

- Sistema dividido en servicios independientes  
- Escalan fácil  
- Comunicación por APIs  
- Ejemplo: Uber  

Comparación clásica:

- Monolito → simple, difícil de escalar  
- Microservicios → complejo, pero muy escalable  

***

# 6. Design Patterns (GoF)

### 6.1 ¿Qué son?

Soluciones probadas y reutilizables a problemas comunes.

### 6.2 Creational Patterns

**Builder:** Construir objetos complejos paso a paso.

**Prototype:** Clonar objetos (incluyendo atributos privados).

**Singleton:** Una única instancia en toda la aplicación.

**Factory Method:** Crear objetos sin exponer la lógica de creación.

**Abstract Factory:** Crear familias de objetos relacionados.

### 6.3 Structural Patterns

Ayudan a organizar clases y objetos.

**Adapter:** Hace compatibles interfaces distintas.

**Bridge:** Separa abstracción de implementación.

**Composite:** Árbol de objetos (ejemplo: carpetas y archivos).

**Decorator:** Agregar comportamiento dinámicamente.

**Facade:** Proveer una interfaz simple a un sistema complejo.

**Proxy:** Representar un objeto y controlar su acceso.

### 6.4 Behavioral Patterns

Describen comportamientos y comunicación.

**Strategy:** Cambiar algoritmos dinámicamente.

**Observer:** Suscripción / notificación (por ejemplo, eventos).

**Command:** Encapsular operaciones.

**Template Method:** Definir el esqueleto de un algoritmo.

**Mediator:** Centralizar la comunicación entre objetos.

**State:** El comportamiento depende del estado interno.

**Iterator:** Recorrer colecciones sin exponer la estructura.

***

# 7. Anti-Patterns y Code Smells

### 7.1 Code Smells (malos olores)

Indican problemas en el diseño:

- Métodos gigantes  
- Clases con demasiadas responsabilidades  
- Duplicación de código  
- Dependencias innecesarias  
- Nombres mal elegidos  

### 7.2 Anti-Patterns más comunes

- God Object: objeto gigante que hace todo  
- Spaghetti code: sin estructura clara  
- Golden hammer: utilizar un patrón para todos los problemas  
- Lava flow: código viejo que nadie toca  

***

# 8. Práctica para el parcial

Se pueden generar:

- 50 preguntas tipo examen  
- Ejercicios de diseño (UML, CRC Cards, SOLID, patrones)  
- Casos prácticos para identificar patrones  
- Preguntas teóricas, opción múltiple y verdadero/falso  

Puedes indicar si quieres ahora preguntas tipo parcial, ejercicios u otro tipo de guía específica.