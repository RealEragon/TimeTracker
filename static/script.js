async function fetchTasks() {
    const response = await fetch('/tasks');
    const tasks = await response.json();
    const taskList = document.getElementById('task-list');
    taskList.innerHTML = '';
    tasks.forEach(task => {
        const li = document.createElement('li');
        li.innerHTML = `
            <span>${task.name} (${task.start_time})</span>
            ${!task.end_time ? `<button onclick="stopTask(${task.id})">Stop</button>` : `<span>Completed (${task.duration})</span>`}
        `;
        taskList.appendChild(li);
    });
}

async function createTask() {
    const taskName = document.getElementById('task-name').value;
    if (!taskName) {
        alert('Please enter a task name');
        return;
    }
    await fetch('/tasks', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ name: taskName }),
    });
    document.getElementById('task-name').value = '';
    fetchTasks();
}

async function stopTask(taskId) {
    await fetch(`/tasks/${taskId}/stop`, { method: 'POST' });
    fetchTasks();
}

// Загружаем задачи при загрузке страницы
window.onload = fetchTasks;
