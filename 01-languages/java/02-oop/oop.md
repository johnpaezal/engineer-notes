# Object-Oriented Programming
*Organizing code around objects and their interactions*

## Core Concepts

**Object** – Entity combining data (state) and operations (behavior)

**Benefits**: Reusability, Maintainability, Modifiability, Reliability

**Four Pillars**: Abstraction, Encapsulation, Inheritance, Polymorphism

---

## Classes and Objects
*Blueprints and instances*

**Class** – Template defining structure and behavior
**Object** – Instance of a class with its own state

```java
class Car {
    String model;
    int year;

    Car(String model, int year) {
        this.model = model;
        this.year = year;
    }

    void drive() {
        System.out.println(model + " is driving");
    }
}

Car car1 = new Car("Tesla", 2024);
Car car2 = new Car("BMW", 2023);
car1.drive();
```

---

## Constructors
*Initialize objects when created*

**Rules** – Same name as class, no return type

```java
class Person {
    String name;
    int age;

    Person() {                          // default
        this.name = "Unknown";
        this.age = 0;
    }

    Person(String name, int age) {      // parameterized
        this.name = name;
        this.age = age;
    }

    Person(String name) {               // overloaded
        this.name = name;
        this.age = 18;
    }
}
```

---

## State and Behavior

**State** – Data stored in object
**Behavior** – Actions object performs

```java
class BankAccount {
    private double balance;      // STATE

    BankAccount() {
        this.balance = 0.0;
    }

    void deposit(double amount) {    // BEHAVIOR
        this.balance += amount;
    }

    double getBalance() {
        return this.balance;
    }
}
```

---

## Attributes and Methods

```java
class Example {
    // Instance - each object has its own
    public String name;
    private int age;

    // Static - shared by all instances
    public static int count;
    public static final int MAX = 100;

    Example(String name, int age) {
        this.name = name;
        this.age = age;
        count++;
    }

    // Instance method
    public void celebrate() {
        this.age++;
    }

    // Static method
    public static int getCount() {
        return count;
    }
}
```

---

## Packages
*Organize classes into namespaces*

**Package** – Folder-like grouping of related classes
**Import** – Bring a class from another package into scope

```java
// File: mypackage/User.java
package mypackage;

public class User {
    public String name;
}

// File: Main.java
import mypackage.User;          // single class
import mypackage.*;             // all classes in package

public class Main {
    public static void main(String[] args) {
        User u = new User();
    }
}
```

**Rules** – Folder path must match package name; only `public` classes are visible from other packages.

---

## Encapsulation
*Protecting and controlling data access*

**Access Modifiers**:
- `public` – accessible everywhere
- `private` – only within this class
- `protected` – within package + subclasses
- (default) – within package only

```java
class User {
    public String username;
    private String password;

    // Getter
    public String getPassword() {
        return password;
    }

    // Setter with validation
    public void setPassword(String password) {
        if (password.length() >= 8) {
            this.password = password;
        }
    }
}

User user = new User();
user.username = "alice";          // direct
user.setPassword("secret123");    // controlled
```

**Best Practice** – `private` attributes, `public` getters/setters

---

## `this` Keyword
*Reference to current object*

```java
class Product {
    String name;
    double price;

    Product(String name, double price) {
        this.name = name;       // distinguish parameter from attribute
        this.price = price;
    }

    Product(String name) {
        this(name, 0.0);        // call another constructor
    }

    Product setName(String name) {
        this.name = name;
        return this;            // method chaining
    }
}
```

---

## Relationships
*How classes connect and depend on each other*

**Association** – Independent existence
**Aggregation** – Weak ownership, child can exist alone
**Composition** – Strong ownership, child bound to parent

```java
// ASSOCIATION
class Student {
    Teacher teacher;

    Student(Teacher teacher) {
        this.teacher = teacher;  // teacher exists independently
    }
}

// AGGREGATION
class Car {
    Engine engine;

    Car(Engine engine) {
        this.engine = engine;  // engine created outside
    }
}

// COMPOSITION
class House {
    Room room;

    House() {
        this.room = new Room();  // room created inside
    }
}
```

**Summary**: Association → knows | Aggregation → has | Composition → owns

---

## Inheritance
*Reuse code through parent-child relationships*

**Extends** – Child inherits parent's attributes and methods
**Super** – Reference to parent class

```java
class Animal {
    String name;

    Animal(String name) {
        this.name = name;
    }

    void eat() {
        System.out.println(name + " is eating");
    }
}

class Dog extends Animal {
    String breed;

    Dog(String name, String breed) {
        super(name);  // call parent constructor
        this.breed = breed;
    }

    @Override
    void eat() {
        System.out.println(name + " is eating dog food");
    }

    void bark() {
        System.out.println(name + " is barking");
    }
}

Dog dog = new Dog("Max", "Golden");
dog.eat();   // "Max is eating dog food" (overridden)
dog.bark();  // "Max is barking"
```

**Method Overriding**:
- Same signature as parent method
- Use `@Override` annotation
- `super.method()` calls parent version

**Final** – Prevent inheritance or overriding
```java
final class CannotExtend { }
class Parent {
    final void cannotOverride() { }
}
```

**Abstract** – Force child classes to implement
```java
abstract class Shape {
    abstract double area();  // no implementation
}

class Circle extends Shape {
    double radius;

    @Override
    double area() {
        return Math.PI * radius * radius;
    }
}
```

---

## Polymorphism
*One interface, multiple implementations*

**Compile-time (Overloading)** – Same method name, different parameters
**Runtime (Overriding)** – Parent reference, child object

```java
// METHOD OVERLOADING (compile-time)
class Calculator {
    int add(int a, int b) { return a + b; }
    double add(double a, double b) { return a + b; }
    int add(int a, int b, int c) { return a + b + c; }
}

// RUNTIME POLYMORPHISM
class Animal {
    void sound() { System.out.println("Animal makes sound"); }
}

class Dog extends Animal {
    @Override
    void sound() { System.out.println("Dog barks"); }
}

class Cat extends Animal {
    @Override
    void sound() { System.out.println("Cat meows"); }
}

// Parent reference, child object
Animal animal1 = new Dog();
Animal animal2 = new Cat();
animal1.sound();  // "Dog barks"
animal2.sound();  // "Cat meows"

// Polymorphism with arrays
Animal[] animals = {new Dog(), new Cat(), new Dog()};
for (Animal a : animals) {
    a.sound();
}
```

**instanceof** – Check object type
```java
Animal animal = new Dog();

if (animal instanceof Dog) {
    Dog dog = (Dog) animal;  // safe cast
    dog.bark();
}

// Pattern matching (Java 16+)
if (animal instanceof Dog dog) {
    dog.bark();  // auto-cast
}
```

---

## Interfaces
*Contract for what a class must do*

**Purpose** – Define behavior without implementation
**Rules** – All methods public abstract by default, can have default/static methods

```java
// Basic interface
interface Drawable {
    void draw();
    void resize(int size);
}

class Circle implements Drawable {
    @Override
    public void draw() { System.out.println("Drawing circle"); }

    @Override
    public void resize(int size) { System.out.println("Resizing to " + size); }
}

// Multiple interfaces
class Player implements Drawable, Movable {
    @Override public void draw() { }
    @Override public void move(int x, int y) { }
}

// Default methods (Java 8+)
interface Vehicle {
    void start();

    default void stop() {
        System.out.println("Vehicle stopped");
    }
}

// Static methods
interface MathUtils {
    static int add(int a, int b) {
        return a + b;
    }
}

int result = MathUtils.add(5, 3);  // call without instance

// Constants (public static final by default)
interface Constants {
    int MAX_SIZE = 100;
    String APP_NAME = "MyApp";
}
```

**Interface vs Abstract Class**:
- Interface: multiple inheritance, no state
- Abstract: single inheritance, can have state

---

## Casting
*Converting one type into another*

```java
// Primitive casting

// Implicit (automatic)
int a = 10;
double b = a;        // int → double

// Explicit (manual)
double x = 10.5;
int y = (int) x;     // double → int

// Object casting (inheritance)

// Upcasting (automatic)
Animal a = new Dog();

// Downcasting (manual)
Dog d = (Dog) a;
```

---

## Object Class
*Root of all Java classes*

Every class implicitly extends `Object`. Key methods you can override:

```java
class Person {
    String name;
    int age;

    Person(String name, int age) {
        this.name = name;
        this.age = age;
    }

    // toString – called when printing object
    @Override
    public String toString() {
        return "Person{name=" + name + ", age=" + age + "}";
    }

    // equals – compare by value (not reference)
    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (!(obj instanceof Person other)) return false;
        return age == other.age && name.equals(other.name);
    }

    // hashCode – must be consistent with equals
    @Override
    public int hashCode() {
        return Objects.hash(name, age);
    }
}

Person p1 = new Person("Alice", 25);
Person p2 = new Person("Alice", 25);

p1.equals(p2);      // true (value comparison)
p1 == p2;           // false (reference comparison)
System.out.println(p1);  // "Person{name=Alice, age=25}"
p1.getClass();      // class Person
```

**Rule**: always override both `equals` and `hashCode` together — if two objects are equal, they must have the same hash code.

---

## Nested / Inner Classes
*Class defined inside another class*

```java
// Inner class (has access to outer class members)
class Outer {
    private int x = 10;

    class Inner {
        void show() {
            System.out.println(x);  // can access outer's private
        }
    }
}

Outer outer = new Outer();
Outer.Inner inner = outer.new Inner();
inner.show();

// Static nested class (no access to outer instance)
class Outer {
    static class StaticNested {
        void show() {
            System.out.println("static nested");
        }
    }
}

Outer.StaticNested nested = new Outer.StaticNested();

// Anonymous class (one-off implementation)
Runnable r = new Runnable() {
    @Override
    public void run() {
        System.out.println("running");
    }
};
// Modern equivalent with lambda:
Runnable r = () -> System.out.println("running");
```

---

## Sealed Classes (Java 17+)
*Restrict which classes can extend or implement a type*

```java
// sealed class – only listed classes can extend it
sealed class Shape permits Circle, Rectangle, Triangle { }

final class Circle extends Shape {
    double radius;
}

final class Rectangle extends Shape {
    double width, height;
}

non-sealed class Triangle extends Shape {
    // non-sealed: allows further extension
}

// Useful with pattern matching switch (Java 21)
double area = switch (shape) {
    case Circle c    -> Math.PI * c.radius * c.radius;
    case Rectangle r -> r.width * r.height;
    case Triangle t  -> 0.5 * t.base * t.height;
};
```

**Why use it**: compiler guarantees exhaustive handling — no unknown subtypes can appear.

---

## Static Initializer Blocks
*Run code once when the class is loaded*

```java
class Config {
    static final Map<String, String> DEFAULTS;
    static final List<String> ALLOWED_ROLES;

    // Static block – runs once when class is first loaded
    static {
        DEFAULTS = new HashMap<>();
        DEFAULTS.put("timeout", "30");
        DEFAULTS.put("retries", "3");
        DEFAULTS.put("host", "localhost");

        ALLOWED_ROLES = List.of("ADMIN", "USER", "GUEST");
    }
}

// Instance initializer block – runs before every constructor
class Counter {
    int count;

    {
        count = 0;
        System.out.println("instance created");
    }

    Counter() { }
    Counter(int start) { this.count = start; }
}
```

**When to use static blocks**: when initializing a `static final` field requires multiple statements or can throw exceptions.

---

## Decoupling
*Reducing dependency between classes*

```java
// ❌ Tightly coupled
class Car {
    Engine engine = new Engine();
}

// ✅ Decoupled (using interface)
interface Engine {
    void start();
}

class Car {
    private Engine engine;

    public Car(Engine engine) {
        this.engine = engine;
    }
}
```
