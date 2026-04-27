# Capa de Negocio — solo contiene lógica

import repository


def get_tasks():
    return repository.get_all()


def create_task(title):
    if not title:
        raise ValueError("Title is required")
    task = {"title": title, "done": False}
    return repository.save(task)


def complete_task(task_id):
    task = repository.get_by_id(task_id)
    if not task:
        raise LookupError("Task not found")
    return repository.update(task_id, {"done": True})


def delete_task(task_id):
    task = repository.get_by_id(task_id)
    if not task:
        raise LookupError("Task not found")
    repository.delete(task_id)
