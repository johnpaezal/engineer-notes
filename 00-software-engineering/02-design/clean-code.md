# Clean Code
*Writing code that humans can read and maintain*

## Core Principles
*Rules that guide clean code*

**DRY** – Don't Repeat Yourself: every piece of knowledge has one place  
**KISS** – Keep It Simple, Stupid: simplest solution that works  
**YAGNI** – You Aren't Gonna Need It: don't build what isn't needed yet  
**SRP** – Single Responsibility: one reason to change per module

---

## Naming
*Names should reveal intent*

```python
# ❌ Bad
def calc(x, y, z):
    return x * y * (1 - z)

d = calc(100, 3, 0.1)

# ✅ Good
def calculate_total_price(unit_price, quantity, discount_rate):
    return unit_price * quantity * (1 - discount_rate)

total = calculate_total_price(unit_price=100, quantity=3, discount_rate=0.1)
```

### Naming Rules

```
Variables:   descriptive nouns        → user_count, active_orders
Booleans:    question form            → is_active, has_permission, can_edit
Functions:   verbs                    → get_user(), calculate_total(), send_email()
Classes:     nouns, PascalCase        → UserRepository, OrderService
Constants:   UPPER_SNAKE_CASE         → MAX_RETRY_COUNT, DEFAULT_TIMEOUT
```

---

## Functions
*Small, focused, one job*

```python
# ❌ Bad – does too many things
def process_order(order):
    # validate
    if not order.user_id:
        raise ValueError("Missing user")
    # calculate
    total = sum(item.price for item in order.items)
    tax = total * 0.19
    # save
    db.save(order)
    # notify
    send_email(order.user.email, f"Order total: {total + tax}")

# ✅ Good – each function does one thing
def validate_order(order):
    if not order.user_id:
        raise ValueError("Missing user")

def calculate_total(order):
    subtotal = sum(item.price for item in order.items)
    return subtotal + subtotal * 0.19

def process_order(order):
    validate_order(order)
    total = calculate_total(order)
    db.save(order)
    send_email(order.user.email, f"Order total: {total}")
```

### Function Rules

```
✓ Max 20 lines (ideally under 10)
✓ Max 3 parameters (use objects for more)
✓ One level of abstraction per function
✓ No side effects (predictable output for same input)
✗ No flags as parameters (bool param = two functions in one)
```

---

## Comments
*Code should explain itself; comments explain why*

```python
# ❌ Bad – explains what (code already does that)
x = x + 1  # increment x by 1

# ❌ Bad – outdated comment
# Returns user by email
def get_user_by_id(user_id):  # function was renamed
    ...

# ✅ Good – explains why
# Retry 3 times: external API occasionally returns 503 on first call
for attempt in range(3):
    response = external_api.call()
    if response.ok:
        break
```

---

## Error Handling
*Handle errors explicitly, not silently*

```python
# ❌ Bad – swallows the error
try:
    result = process(data)
except:
    pass

# ❌ Bad – returns None (caller doesn't know what happened)
def get_user(user_id):
    try:
        return db.find(user_id)
    except:
        return None

# ✅ Good – raise specific, meaningful exceptions
def get_user(user_id):
    user = db.find(user_id)
    if user is None:
        raise UserNotFoundError(f"User {user_id} not found")
    return user
```

---

## Code Structure
*Organizing code for readability*

```python
# ❌ Bad – mixed levels of abstraction
def checkout(cart):
    total = 0
    for item in cart.items:
        if item.discount:
            total += item.price * (1 - item.discount)
        else:
            total += item.price
    if total > 1000:
        total *= 0.95
    db.execute("INSERT INTO orders VALUES (?)", total)
    requests.post("https://email-api.com/send", json={"to": cart.user.email})

# ✅ Good – consistent level of abstraction
def checkout(cart):
    total = calculate_discounted_total(cart)
    total = apply_bulk_discount(total)
    save_order(cart.user, total)
    notify_user(cart.user, total)
```

---

## Code Smells
*Signals that code needs refactoring*

**Long method** – Function doing too much, split it  
**Long parameter list** – More than 3 params, use an object  
**Duplicate code** – Same logic in multiple places, extract it  
**Dead code** – Unused variables/functions, delete them  
**Magic numbers** – Unexplained literals, use named constants  
**God class** – One class knowing/doing everything, split it

```python
# ❌ Magic number
if age > 18:
    ...

# ✅ Named constant
LEGAL_AGE = 18
if age > LEGAL_AGE:
    ...
```

---

## Best Practices

- Write code for the next developer (which might be you in 6 months)
- Leave the code cleaner than you found it (Boy Scout Rule)
- Small commits with meaningful messages
- Refactor continuously, not in big bang sessions
- Tests are the safety net that allows refactoring
