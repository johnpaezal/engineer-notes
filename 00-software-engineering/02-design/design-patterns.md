# Software Design Patterns
*Reusable solutions to common software problems*

## What are Design Patterns
*Language-agnostic blueprints for solving recurring problems*

**Design Pattern** – Proven solution to a recurring design problem  
**GoF Patterns** – 23 patterns from "Gang of Four" book, organized in 3 categories

**Categories**:
- **Creational** – How objects are created
- **Structural** – How objects are composed
- **Behavioral** – How objects communicate

---

## Creational Patterns
*Control object creation*

### Singleton
*Only one instance exists globally*

```python
class Database:
    _instance = None

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

# Usage
db1 = Database.get_instance()
db2 = Database.get_instance()
# db1 is db2 → True
```

### Factory
*Create objects without specifying exact class*

```python
class NotificationFactory:
    @staticmethod
    def create(type: str):
        if type == "email":
            return EmailNotification()
        if type == "sms":
            return SMSNotification()
        raise ValueError(f"Unknown type: {type}")

# Usage
notification = NotificationFactory.create("email")
notification.send("Hello")
```

### Builder
*Construct complex objects step by step*

```python
class QueryBuilder:
    def __init__(self):
        self._table = ""
        self._conditions = []
        self._limit = None

    def from_table(self, table):
        self._table = table
        return self

    def where(self, condition):
        self._conditions.append(condition)
        return self

    def limit(self, n):
        self._limit = n
        return self

    def build(self):
        query = f"SELECT * FROM {self._table}"
        if self._conditions:
            query += " WHERE " + " AND ".join(self._conditions)
        if self._limit:
            query += f" LIMIT {self._limit}"
        return query

# Usage
query = QueryBuilder().from_table("users").where("age > 18").limit(10).build()
```

---

## Structural Patterns
*Compose objects into larger structures*

### Adapter
*Make incompatible interfaces work together*

```python
# External library with different interface
class ExternalPayment:
    def make_payment(self, amount_cents):
        print(f"Paying {amount_cents} cents")

# Our app expects dollars
class PaymentAdapter:
    def __init__(self, external):
        self._external = external

    def pay(self, amount_dollars):
        self._external.make_payment(amount_dollars * 100)

# Usage
adapter = PaymentAdapter(ExternalPayment())
adapter.pay(9.99)
```

### Decorator
*Add behavior to objects dynamically*

```python
class Logger:
    def __init__(self, service):
        self._service = service

    def process(self, data):
        print(f"Processing: {data}")
        result = self._service.process(data)
        print(f"Done: {result}")
        return result
```

---

## Behavioral Patterns
*Define how objects communicate*

### Strategy
*Swap algorithms at runtime*

```python
class Sorter:
    def __init__(self, strategy):
        self._strategy = strategy

    def sort(self, data):
        return self._strategy(data)

# Usage
sorter = Sorter(sorted)
sorter.sort([3, 1, 2])

sorter = Sorter(lambda x: sorted(x, reverse=True))
sorter.sort([3, 1, 2])
```

### Observer
*Notify multiple objects when state changes*

```python
class EventEmitter:
    def __init__(self):
        self._listeners = []

    def subscribe(self, listener):
        self._listeners.append(listener)

    def emit(self, event):
        for listener in self._listeners:
            listener(event)

# Usage
emitter = EventEmitter()
emitter.subscribe(lambda e: print(f"Email: {e}"))
emitter.subscribe(lambda e: print(f"Log: {e}"))
emitter.emit("user.created")
```

---

## MVC Pattern
*Separate data, logic, and presentation*

**Model** – Data and business logic  
**View** – User interface / presentation  
**Controller** – Handles input, coordinates Model and View

```
User Action
    ↓
Controller  →  Model (reads/writes data)
    ↓              ↓
   View  ←  Model data
```

```python
# Model – data and rules
class UserModel:
    def get_user(self, user_id):
        return db.query("SELECT * FROM users WHERE id = ?", user_id)

# View – presentation
class UserView:
    def render(self, user):
        return {"id": user.id, "name": user.name}

# Controller – coordinates
class UserController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def get_user(self, user_id):
        user = self.model.get_user(user_id)
        return self.view.render(user)
```

### MVC Variants
*Common adaptations*

**MVP** (Model-View-Presenter) – Presenter replaces Controller, no direct Model-View link  
**MVVM** (Model-View-ViewModel) – ViewModel exposes data bindings for the View (common in frontend)  
**MVC in web** – Controller = route handler, View = template/JSON response, Model = DB layer

---

## SOLID Principles
*Five principles for maintainable object-oriented design*

### S – Single Responsibility
*One class, one reason to change*

```python
# ❌ Does too many things
class User:
    def save(self): ...        # persistence
    def send_email(self): ...  # notification
    def generate_pdf(self): .. # reporting

# ✅ Each class has one job
class User: ...
class UserRepository:
    def save(self, user): ...
class EmailService:
    def send_welcome(self, user): ...
```

### O – Open/Closed
*Open for extension, closed for modification*

```python
# ❌ Add new type → modify existing code
def calculate_area(shape):
    if shape.type == "circle":
        return 3.14 * shape.radius ** 2
    if shape.type == "square":
        return shape.side ** 2

# ✅ Add new type → add new class, don't touch existing
class Circle:
    def area(self): return 3.14 * self.radius ** 2

class Square:
    def area(self): return self.side ** 2
```

### L – Liskov Substitution
*Subclasses must be substitutable for their parent*

```python
# ❌ Violates LSP — Square breaks Rectangle's contract
class Rectangle:
    def set_width(self, w): self.width = w
    def set_height(self, h): self.height = h
    def area(self): return self.width * self.height

class Square(Rectangle):
    def set_width(self, w):   # Square forces width == height
        self.width = self.height = w  # breaks Rectangle behavior

# ✅ Don't force inheritance where behavior differs
class Shape(ABC):
    @abstractmethod
    def area(self): ...
```

### I – Interface Segregation
*Many specific interfaces over one general interface*

```python
# ❌ Forces classes to implement methods they don't need
class Worker(ABC):
    def work(self): ...
    def eat(self): ...   # robots don't eat

# ✅ Split into specific interfaces
class Workable(ABC):
    def work(self): ...

class Eatable(ABC):
    def eat(self): ...

class Human(Workable, Eatable): ...
class Robot(Workable): ...          # only what it needs
```

### D – Dependency Inversion
*Depend on abstractions, not concrete implementations*

```python
# ❌ High-level module depends on low-level module
class OrderService:
    def __init__(self):
        self.db = PostgreSQLDatabase()  # hard dependency

# ✅ Depend on abstraction (interface)
class OrderService:
    def __init__(self, db: Database):  # inject the dependency
        self.db = db

# Can swap implementation without changing OrderService
service = OrderService(db=PostgreSQLDatabase())
service = OrderService(db=MockDatabase())     # for testing
```

---

## Best Practices

- Use patterns to solve real problems, not to show off
- Prefer composition over inheritance
- Don't force a pattern — if simple code works, use it
- Strategy: when behavior needs to change at runtime
- Observer: when multiple things react to one event
- Factory: when object creation is complex or varies
- Singleton: use sparingly (hard to test, global state)
- SOLID: apply as guidelines, not dogma
