from flask import Flask, request, jsonify

app = Flask(__name__)

# Datos, lógica y rutas — todo en el mismo lugar
tasks = {}
next_id = 1


@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(list(tasks.values()))


@app.route("/tasks", methods=["POST"])
def create_task():
    global next_id
    data = request.get_json()

    if not data or not data.get("title"):
        return jsonify({"error": "Title is required"}), 400

    task = {"id": next_id, "title": data["title"], "done": False}
    tasks[next_id] = task
    next_id += 1
    return jsonify(task), 201


@app.route("/tasks/<int:task_id>", methods=["PUT"])
def complete_task(task_id):
    if task_id not in tasks:
        return jsonify({"error": "Task not found"}), 404

    tasks[task_id]["done"] = True
    return jsonify(tasks[task_id])


@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    if task_id not in tasks:
        return jsonify({"error": "Task not found"}), 404

    del tasks[task_id]
    return "", 204


if __name__ == "__main__":
    app.run(debug=True)
