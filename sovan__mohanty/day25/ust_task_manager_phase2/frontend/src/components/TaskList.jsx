import React from "react";

export default function TaskList({ tasks, onUpdate, onDelete }) {
  if (!tasks?.length) {
    return (
      <div className="section empty">
        <div className="empty-icon"></div>
        <p>No tasks yet. Create one above.</p>
      </div>
    );
  }

  return (
    <div className="section">
      <h2>Your tasks</h2>
      <ul className="task-list">
        {tasks.map((t) => (
          <li className="task-item glass-item" key={t.id}>
            <div className="task-main">
              <h3 className={`task-title ${t.completed ? "done" : ""}`}>{t.title}</h3>
              <p className="task-desc">{t.description}</p>
            </div>
            <div className="task-actions">
              <button
                className={`btn ${t.completed ? "warning" : "success"}`}
                onClick={() => onUpdate(t.id, { completed: !t.completed })}
              >
                {t.completed ? "Mark pending" : "Mark done"}
              </button>
              <button className="btn danger" onClick={() => onDelete(t.id)}>
                Delete
              </button>
            </div>
          </li>
        ))}
      </ul>
    </div>
  );
}
