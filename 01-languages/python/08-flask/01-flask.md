# Flask
*Micro-framework web minimalista para Python*

## ¿Qué es Flask?

**Flask** es un micro-framework web para Python, diseñado para ser **simple, ligero y fácil de aprender**.

A diferencia de Django (que viene con todo incluido), Flask te da lo mínimo necesario para levantar una aplicación web y tú decides qué agregar.

### Flask vs FastAPI vs Django

| | Flask | FastAPI | Django |
|---|---|---|---|
| Complejidad | Muy baja | Media | Alta |
| Velocidad de aprendizaje | Rápida | Media | Lenta |
| Rendimiento | Medio | Alto (async) | Medio |
| Validación automática | No | Sí (Pydantic) | Parcial |
| Documentación automática | No | Sí (Swagger) | No |
| Ideal para | Proyectos simples, prototipos, scripts web | APIs modernas | Aplicaciones grandes con todo integrado |

**Usa Flask cuando**:
- Quieres algo simple y rápido de levantar
- El proyecto es pequeño o mediano
- Estás aprendiendo desarrollo web con Python
- Necesitas una API sencilla o un prototipo
- No necesitas las capas extras de Django o FastAPI

**No uses Flask cuando**:
- Necesitas validación automática de datos (usa FastAPI)
- El proyecto es grande y necesita estructura clara desde el inicio (usa Django)
- Necesitas alto rendimiento con código async (usa FastAPI)

---

## Instalación

```bash
pip install flask
```

---

## Hola Mundo

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hola Mundo'

if __name__ == '__main__':
    app.run(debug=True)
```

```bash
python app.py
# → http://localhost:5000
```

`debug=True` → recarga automática al guardar cambios, muestra errores detallados. **Nunca usar en producción.**

---

## Rutas (Routes)

```python
from flask import Flask

app = Flask(__name__)

# Ruta básica
@app.route('/users')
def get_users():
    return 'Lista de usuarios'

# Parámetro en URL
@app.route('/users/<int:user_id>')
def get_user(user_id):
    return f'Usuario {user_id}'

# Parámetro de texto
@app.route('/products/<string:slug>')
def get_product(slug):
    return f'Producto: {slug}'

# Múltiples métodos HTTP
@app.route('/users', methods=['GET', 'POST'])
def users():
    if request.method == 'POST':
        return 'Crear usuario'
    return 'Listar usuarios'
```

### Tipos de parámetros en URL

| Tipo | Ejemplo | Convierte a |
|---|---|---|
| `<string:name>` | `/users/alice` | str |
| `<int:id>` | `/users/42` | int |
| `<float:value>` | `/price/9.99` | float |
| `<path:subpath>` | `/files/a/b/c` | str con "/" |

---

## Request – Leer datos de la petición

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

    return f'Usuario creado: {name}'
```

---

## Response – Devolver datos

```python
from flask import Flask, jsonify, make_response

app = Flask(__name__)

# Devolver JSON
@app.route('/users/<int:user_id>')
def get_user(user_id):
    user = {'id': user_id, 'name': 'Alice', 'email': 'alice@example.com'}
    return jsonify(user)

# Devolver con status code explícito
@app.route('/users', methods=['POST'])
def create_user():
    user = {'id': 1, 'name': 'Alice'}
    return jsonify(user), 201

# Respuesta personalizada (headers, cookies, etc.)
@app.route('/custom')
def custom():
    response = make_response(jsonify({'message': 'ok'}), 200)
    response.headers['X-Custom-Header'] = 'value'
    return response
```

---

## API REST completa (ejemplo)

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

# Base de datos en memoria (solo para ejemplo)
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

## Manejo de Errores

```python
from flask import Flask, jsonify
from werkzeug.exceptions import NotFound

app = Flask(__name__)

# Manejador para 404
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404

# Manejador para 400
@app.errorhandler(400)
def bad_request(error):
    return jsonify({'error': 'Bad request'}), 400

# Manejador para 500
@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error'}), 500

# Lanzar error desde una ruta
@app.route('/users/<int:user_id>')
def get_user(user_id):
    user = db.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    return jsonify(user)
```

---

## Blueprints
*Organizar rutas en módulos separados*

```
proyecto/
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

## Variables de Entorno y Configuración

```python
import os
from flask import Flask

app = Flask(__name__)

# Cargar configuración desde variables de entorno
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-secret')
app.config['DATABASE_URL'] = os.getenv('DATABASE_URL')
app.config['DEBUG'] = os.getenv('FLASK_ENV') == 'development'
```

```bash
# .env
SECRET_KEY=mi-clave-secreta
DATABASE_URL=postgresql://user:pass@localhost/mydb
FLASK_ENV=development
```

```bash
# Instalar python-dotenv para cargar .env
pip install python-dotenv
```

```python
from dotenv import load_dotenv
load_dotenv()  # cargar .env antes de iniciar la app
```

---

## Conectar con Base de Datos (SQLAlchemy)

```bash
pip install flask-sqlalchemy
```

```python
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'  # o postgresql://...
db = SQLAlchemy(app)

# Modelo
class User(db.Model):
    id    = db.Column(db.Integer, primary_key=True)
    name  = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)

    def to_dict(self):
        return {'id': self.id, 'name': self.name, 'email': self.email}

# Crear tablas
with app.app_context():
    db.create_all()

# CRUD con SQLAlchemy
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

## Estructura de Proyecto Recomendada

```
mi-api/
├── app.py              ← punto de entrada
├── config.py           ← configuración
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

## Correr en Producción

```bash
# Instalar Gunicorn (servidor WSGI para producción)
pip install gunicorn

# Correr con Gunicorn (4 workers)
gunicorn -w 4 -b 0.0.0.0:8000 app:app
```

**Nunca usar `app.run(debug=True)` en producción.**

---

## Comandos útiles

```bash
# Instalar dependencias
pip install flask flask-sqlalchemy python-dotenv

# Guardar dependencias
pip freeze > requirements.txt

# Instalar dependencias desde archivo
pip install -r requirements.txt

# Correr en desarrollo
flask run
# o
python app.py

# Especificar puerto
flask run --port 8080
```

---

## Resumen

Flask es el framework más fácil de aprender en Python para hacer APIs y aplicaciones web. Es ideal cuando:
- Quieres construir algo rápido sin complicarte
- Estás aprendiendo
- El proyecto es pequeño o un prototipo

Para proyectos más serios donde necesitas validación automática de datos, documentación automática y mejor rendimiento, considera migrar a **FastAPI**.
