# Monolithic Architecture — Todo App

Todo en un solo archivo. Sin separación de responsabilidades.

```
app.py  ← datos + lógica + rutas todo junto
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
