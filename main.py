from flask import Flask, request, jsonify, render_template
from datetime import datetime

app = Flask(__name__)

# Список задач
tasks = []

@app.route('/')
def index():
    # Рендер главной страницы
    return render_template('index.html')

@app.route('/tasks', methods=['GET', 'POST'])
def manage_tasks():
    if request.method == 'POST':
        # Создание новой задачи
        data = request.json
        task = {
            "id": len(tasks) + 1,
            "name": data.get('name', 'Unnamed Task'),
            "start_time": datetime.now().isoformat(),
            "end_time": None,
            "duration": None
        }
        tasks.append(task)
        return jsonify(task), 201
    # Получение списка задач
    return jsonify(tasks), 200

@app.route('/tasks/<int:task_id>/stop', methods=['POST'])
def stop_task(task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["end_time"] = datetime.now().isoformat()
            task["duration"] = str(datetime.fromisoformat(task["end_time"]) - datetime.fromisoformat(task["start_time"]))
            return jsonify(task), 200
    return jsonify({"error": "Task not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
