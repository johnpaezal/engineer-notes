# Software Testing
*Verifying software works correctly*

## Testing Pyramid
*Balance of test types by speed and cost*

```
        /\
       /  \
      / E2E \          ← Few, slow, expensive
     /--------\
    /Integration\      ← Some, medium speed
   /--------------\
  /   Unit Tests   \   ← Many, fast, cheap
 /------------------\
```

**Unit** – Test a single function/class in isolation  
**Integration** – Test how components work together  
**E2E (End-to-End)** – Test full user flows through the system

---

## Unit Testing
*Testing smallest pieces of code*

```python
# Function to test
def calculate_discount(price, percent):
    if percent < 0 or percent > 100:
        raise ValueError("Invalid percent")
    return price * (1 - percent / 100)

# Unit tests
def test_basic_discount():
    assert calculate_discount(100, 20) == 80

def test_zero_discount():
    assert calculate_discount(100, 0) == 100

def test_invalid_percent_raises():
    with pytest.raises(ValueError):
        calculate_discount(100, -5)
```

### AAA Pattern
*Structure of a unit test*

```python
def test_user_creation():
    # Arrange – set up data
    name = "Alice"
    email = "alice@example.com"

    # Act – execute the thing being tested
    user = create_user(name, email)

    # Assert – verify result
    assert user.name == name
    assert user.email == email
    assert user.id is not None
```

---

## Integration Testing
*Testing components working together*

**Purpose** – Verify that modules, services, or layers interact correctly  
**Scope** – More than one unit (e.g., controller + service + database)

```python
# Integration test: API endpoint + database
def test_create_user_endpoint(client, db):
    # Arrange
    payload = {"name": "Alice", "email": "alice@example.com"}

    # Act – real HTTP request to the app
    response = client.post("/users", json=payload)

    # Assert
    assert response.status_code == 201
    assert response.json()["name"] == "Alice"

    # Also check it was actually saved in DB
    user = db.query(User).filter_by(email="alice@example.com").first()
    assert user is not None
```

### What to Test in Integration
*Key integration points*

```
✓ API endpoint → service → database
✓ Service A → Service B (HTTP/gRPC)
✓ Application → external API (mocked)
✓ Background job → database
✓ Authentication middleware → protected route
```

---

## Mocking
*Replacing real dependencies with fakes*

**Mock** – Fake object that simulates behavior  
**Stub** – Returns fixed values  
**Spy** – Records calls to real function

```python
from unittest.mock import Mock, patch

# Mock an external service
def test_send_welcome_email():
    email_service = Mock()
    user_service = UserService(email_service)

    user_service.register("alice@example.com")

    email_service.send.assert_called_once_with(
        to="alice@example.com",
        subject="Welcome!"
    )

# Patch external call
@patch("requests.get")
def test_fetch_weather(mock_get):
    mock_get.return_value.json.return_value = {"temp": 22}

    result = fetch_weather("London")

    assert result["temp"] == 22
```

---

## E2E Testing
*Testing the full system from user perspective*

**Tools**: Cypress (web), Playwright (web), Selenium (web), Postman (API)

```javascript
// Cypress E2E example
describe("Login flow", () => {
  it("logs in with valid credentials", () => {
    cy.visit("/login");
    cy.get("[data-cy=email]").type("alice@example.com");
    cy.get("[data-cy=password]").type("secret123");
    cy.get("[data-cy=submit]").click();
    cy.url().should("include", "/dashboard");
  });
});
```

---

## Test Coverage
*Measuring how much code is tested*

**Line coverage** – % of lines executed during tests  
**Branch coverage** – % of if/else branches covered

```bash
# Python
pytest --cov=app --cov-report=term

# Output
Name          Stmts   Miss  Cover
app/users.py     45      5    89%
app/orders.py    30      0   100%
TOTAL            75      5    93%
```

**Target**: 80%+ coverage is a common minimum; 100% is not always practical

---

## Testing Strategies

### When to Use Each Type

| Scenario | Test Type |
|---|---|
| Pure function with no dependencies | Unit |
| Controller + service + DB | Integration |
| External API call | Unit with mock |
| Full user login/checkout flow | E2E |
| Critical business rule | Unit + Integration |

---

## Best Practices

- Test behavior, not implementation details
- Tests should be independent (order shouldn't matter)
- One assertion per test when possible
- Use real databases in integration tests (avoid mocking the DB)
- Name tests clearly: `test_[what]_when_[condition]_should_[result]`
- Run tests before every merge (CI/CD)
- Fix failing tests immediately — never comment them out
