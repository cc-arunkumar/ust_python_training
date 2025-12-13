import { useState } from "react";

export default function TaskListToggle() {
  const [tasks, setTasks] = useState([
    { id: 1, text: "Task 1", done: false },
    { id: 2, text: "Task 2", done: false },
    { id: 3, text: "Task 3", done: false },
  ]);

  const toggleTask = (id) => {
    setTasks(tasks.map(t => t.id === id ? { ...t, done: !t.done } : t));
  };

  return (
    <div >
      <h3>Task List Toggle</h3>
      <ul>
        {tasks.map(task => (
          <li key={task.id} style={{ textDecoration: task.done ? "line-through" : "none" }}>
            {task.text} <button onClick={() => toggleTask(task.id)}>Complete</button>
          </li>
        ))}
      </ul>
    </div>
  );
}
