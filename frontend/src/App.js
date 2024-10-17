import React, { useEffect, useState } from 'react';
import { getTasks, createTask } from './services/api';

function App() {
    const [tasks, setTasks] = useState([]);

    useEffect(() => {
        loadTasks();
    }, []);

    const loadTasks = async () => {
        const data = await getTasks();
        setTasks(data);
    };

    const handleCreateTask = async () => {
        const newTask = { title: 'New Task', description: 'Task description', due_date: '2024-10-31T12:00' };
        await createTask(newTask);
        loadTasks();
    };

    return (
        <div>
            <h1>Task Management</h1>
            <ul>
                {tasks.map(task => (
                    <li key={task.id}>{task.title} - {task.due_date}</li>
                ))}
            </ul>
            <button onClick={handleCreateTask}>Add Task</button>
        </div>
    );
}

export default App;
