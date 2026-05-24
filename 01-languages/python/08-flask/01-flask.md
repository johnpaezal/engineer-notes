# Flask
*Minimalist Python web micro-framework*

## What is Flask?

**Flask** is a Python web micro-framework designed to be **simple, lightweight, and easy to learn**.

Unlike Django (batteries-included), Flask gives you the bare minimum to spin up a web app and lets you choose what to add.

### Flask vs FastAPI vs Django

| | Flask | FastAPI | Django |
|---|---|---|---|
| Complexity | Very low | Medium | High |
| Learning curve | Fast | Medium | Slow |
| Performance | Medium | High (async) | Medium |
| Auto validation | No | Yes (Pydantic) | Partial |
| Auto docs | No | Yes (Swagger) | No |
| Best for | Simple projects, prototypes, web scripts | Modern APIs | Large all-in-one apps |

**Use Flask when**:
- You want something simple and quick to set up
- The project is small or medium
- You're learning Python web development
- You need a simple API or a prototype
- You don't need the extra layers of Django or FastAPI

**Don't use Flask when**:
- You need automatic data validation (use FastAPI)
- The project is large and needs clear structure from day one (use Django)
- You need high performance with async code (use FastAPI)

---

## Install

```bash
pip install flask
```

---

## Hello World

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello World'

if __name__ == '__main__':
    app.run(debug=True)
```

```bash
python app.py
# → http://localhost:5000
```

`debug=True` → auto-reload on save, detailed error pages. **Never use in production.**

---

## Routes

```python
from flask import Flask

app = Flask(__name__)

# Basic route
@app.route('/users')
def get_users():
    return 'User list'

# URL parameter
@app.route('/users/<int:user_id>')
def get_user(user_id):
    return f'User {user_id}'

# String parameter
@app.route('/products/<string:slug>')
def get_product(slug):
    return f'Product: {slug}'

# Multiple HTTP methods
@app.route('/users', methods=['GET', 'POST'])
def users():
    if request.method == 'POST':
        return 'Create user'
    return 'List users'
```

### URL parameter types

| Type | Example | Converts to |
|---|---|---|
| `<string:name>` | `/users/alice` | str |
| `<int:id>` | `/users/42` | int |
| `<float:value>` | `/price/9.99` | float |
| `<path:subpath>` | `/files/a/b/c` | str with "/" |

---

## Request – Read request data

```python
from flask import Flask, request

app = Flask(__name__)

@app.route('/users', methods=['POST'])
def create_user():
    # JSON body
    data = request.get_json()
    name = data['name']
    email = data['email']

    # Query params: /users?page=2&limit=10
    page = request.args.get('page', 1, type=int)
    limit = request.args.get('limit', 10, type=int)

    # Form data (HTML forms)
    name = request.form.get('name')

    # Headers
    token = request.headers.get('Authorization')

    return f'User created: {name}'
```

---

## Response – Return data

```python
from flask import Flask, jsonify, make_response

app = Flask(__name__)

# Return JSON
@app.route('/users/<int:user_id>')
def get_user(user_id):
    user = {'id': user_id, 'name': 'Alice', 'email': 'alice@example.com'}
    return jsonify(user)

# Return with explicit status code
@app.route('/users', methods=['POST'])
def create_user():
    user = {'id': 1, 'name': 'Alice'}
    return jsonify(user), 201

# Custom response (headers, cookies, etc.)
@app.route('/custom')
def custom():
    response = make_response(jsonify({'message': 'ok'}), 200)
    response.headers['X-Custom-Header'] = 'value'
    return response
```

---

## Complete REST API (example)

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory database (example only)
users = {}
next_id = 1

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(list(users.values()))

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = users.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    return jsonify(user)

@app.route('/users', methods=['POST'])
def create_user():
    global next_id
    data = request.get_json()

    if not data or not data.get('name'):
        return jsonify({'error': 'Name is required'}), 400

    user = {'id': next_id, 'name': data['name'], 'email': data.get('email')}
    users[next_id] = user
    next_id += 1
    return jsonify(user), 201

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    if user_id not in users:
        return jsonify({'error': 'User not found'}), 404

    data = request.get_json()
    users[user_id].update(data)
    return jsonify(users[user_id])

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_id not in users:
        return jsonify({'error': 'User not found'}), 404

    del users[user_id]
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
```

---

## Error Handling

```python
from flask import Flask, jsonify
from werkzeug.exceptions import NotFound

app = Flask(__name__)

# Handler for 404
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404

# Handler for 400
@app.errorhandler(400)
def bad_request(error):
    return jsonify({'error': 'Bad request'}), 400

# Handler for 500
@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error'}), 500

# Raise error from a route
@app.route('/users/<int:user_id>')
def get_user(user_id):
    user = db.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    return jsonify(user)
```

---

## Blueprints
*Organize routes into separate modules*

```
project/
├── app.py
└── routes/
    ├── __init__.py
    ├── users.py
    └── products.py
```

```python
# routes/users.py
from flask import Blueprint, jsonify

users_bp = Blueprint('users', __name__, url_prefix='/users')

@users_bp.route('/')
def get_users():
    return jsonify([])

@users_bp.route('/<int:user_id>')
def get_user(user_id):
    return jsonify({'id': user_id})
```

```python
# routes/products.py
from flask import Blueprint, jsonify

products_bp = Blueprint('products', __name__, url_prefix='/products')

@products_bp.route('/')
def get_products():
    return jsonify([])
```

```python
# app.py
from flask import Flask
from routes.users import users_bp
from routes.products import products_bp

app = Flask(__name__)
app.register_blueprint(users_bp)
app.register_blueprint(products_bp)

if __name__ == '__main__':
    app.run(debug=True)
```

---

## Environment Variables and Config

```python
import os
from flask import Flask

app = Flask(__name__)

# Load config from environment variables
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-secret')
app.config['DATABASE_URL'] = os.getenv('DATABASE_URL')
app.config['DEBUG'] = os.getenv('FLASK_ENV') == 'development'
```

```bash
# .env
SECRET_KEY=my-secret-key
DATABASE_URL=postgresql://user:pass@localhost/mydb
FLASK_ENV=development
```

```bash
# Install python-dotenv to load .env
pip install python-dotenv
```

```python
from dotenv import load_dotenv
load_dotenv()  # load .env before starting the app
```

---

## Connecting to a Database (SQLAlchemy)

```bash
pip install flask-sqlalchemy
```

```python
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'  # or postgresql://...
db = SQLAlchemy(app)

# Model
class User(db.Model):
    id    = db.Column(db.Integer, primary_key=True)
    name  = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)

    def to_dict(self):
        return {'id': self.id, 'name': self.name, 'email': self.email}

# Create tables
with app.app_context():
    db.create_all()

# CRUD with SQLAlchemy
@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([u.to_dict() for u in users])

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    user = User(name=data['name'], email=data['email'])
    db.session.add(user)
    db.session.commit()
    return jsonify(user.to_dict()), 201

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return '', 204
```

---

## Recommended Project Structure

```
my-api/
├── app.py              ← entry point
├── config.py           ← configuration
├── models/
│   ├── __init__.py
│   └── user.py
├── routes/
│   ├── __init__.py
│   └── users.py
├── requirements.txt
└── .env
```

---

## Running in Production

```bash
# Install Gunicorn (WSGI server for production)
pip install gunicorn

# Run with Gunicorn (4 workers)
gunicorn -w 4 -b 0.0.0.0:8000 app:app
```

**Never use `app.run(debug=True)` in production.**

---

## Useful Commands

```bash
# Install dependencies
pip install flask flask-sqlalchemy python-dotenv

# Save dependencies
pip freeze > requirements.txt

# Install from file
pip install -r requirements.txt

# Run in development
flask run
# or
python app.py

# Specify port
flask run --port 8080
```

---

## Summary

Flask is the easiest Python framework to learn for building APIs and web apps. Ideal when:
- You want to build something quickly without overhead
- You're learning
- The project is small or a prototype

For more serious projects that need automatic data validation, auto-generated docs, and better performance, consider migrating to **FastAPI**.
