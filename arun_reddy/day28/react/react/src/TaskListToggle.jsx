import { useState } from "react";
import "./index.css";

export default function TaskListToggle() {
  const [tasks, setTasks] = useState([
    { id: 1, text: "Complete React tutorial", completed: false },
    { id: 2, text: "Build a todo app", completed: false },
    { id: 3, text: "Learn about useState", completed: false },
  ]);

  const toggleTask = (id) => {
    setTasks(
      tasks.map((task) =>
        task.id === id ? { ...task, completed: !task.completed } : task
      )
    );
  };

  return (
    <div className="task-list-container">
      <div className="task-list-card">
        <h2 className="task-list-title">My Tasks</h2>
        <ul className="task-list">
          {tasks.map((task) => (
            <li key={task.id} className="task-item">
              <span
                className={task.completed ? "task-text completed" : "task-text"}
              >
                {task.text}
              </span>
              <button onClick={() => toggleTask(task.id)} className="task-btn">
                {task.completed ? "Undo" : "Complete"}
              </button>
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
}
