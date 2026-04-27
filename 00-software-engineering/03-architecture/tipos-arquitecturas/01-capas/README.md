# Layered Architecture — Todo App

Arquitectura en capas: cada capa tiene una responsabilidad y solo habla con la capa inmediatamente inferior.

```
routes.py   ← Capa de Presentación (HTTP)
    ↓
service.py  ← Capa de Negocio (lógica)
    ↓
repository.py ← Capa de Datos (persistencia)
```

## Correr

```bash
pip install flask
python app.py
```

## Endpoints

```
GET    /tasks         → listar todas
POST   /tasks         → crear  { "title": "..." }
PUT    /tasks/<id>    → marcar completada
DELETE /tasks/<id>    → eliminar
```
