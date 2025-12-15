import { useState } from "react";

export default function TaskList() {
  const [tasks, setTasks] = useState([
    { id: 1, text: "Task 1", done: false },
    { id: 2, text: "Task 2", done: false },
    { id: 3, text: "Task 3", done: false },
  ]);

  const completeTask = (id) =>
    setTasks(ts => ts.map(t => t.id === id ? { ...t, done: true } : t));

  return (
    <section className="card">
      <h3>Task List Toggle</h3>
      <ul>
        {tasks.map(t => (
          <li key={t.id} style={{ textDecoration: t.done ? "line-through" : "none" }}>
            {t.text}{" "}
            {!t.done && <button onClick={() => completeTask(t.id)}>Complete</button>}
          </li>
        ))}
      </ul>
    </section>
  );
}
