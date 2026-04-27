# Capa de Datos — solo maneja el almacenamiento

tasks = {}
next_id = 1


def get_all():
    return list(tasks.values())


def get_by_id(task_id):
    return tasks.get(task_id)


def save(task):
    global next_id
    task["id"] = next_id
    tasks[next_id] = task
    next_id += 1
    return task


def update(task_id, data):
    tasks[task_id].update(data)
    return tasks[task_id]


def delete(task_id):
    del tasks[task_id]
