# Capa de Presentación — solo maneja HTTP

from flask import Blueprint, request, jsonify
import service

tasks_bp = Blueprint("tasks", __name__)


@tasks_bp.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(service.get_tasks())


@tasks_bp.route("/tasks", methods=["POST"])
def create_task():
    data = request.get_json()
    try:
        task = service.create_task(data.get("title"))
        return jsonify(task), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


@tasks_bp.route("/tasks/<int:task_id>", methods=["PUT"])
def complete_task(task_id):
    try:
        task = service.complete_task(task_id)
        return jsonify(task)
    except LookupError as e:
        return jsonify({"error": str(e)}), 404


@tasks_bp.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    try:
        service.delete_task(task_id)
        return "", 204
    except LookupError as e:
        return jsonify({"error": str(e)}), 404
