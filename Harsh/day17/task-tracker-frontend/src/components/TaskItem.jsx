
// TaskItem.jsx
import API from "../api";

export default function TaskItem({ task, refreshTasks }) {
  const toggleCompleted = async () => {
    await API.put(`/tasks/${task.id}`, {
      id: task.id,
      title: task.title,
      description: task.description,
      completed: !task.completed,
    });
    refreshTasks();
  };

  const deleteTask = async () => {
    await API.delete(`/tasks/${task.id}`);
    refreshTasks();
  };

  return (
    <div className="task-item">
      <h3>{task.title}</h3>
      <p>{task.description}</p>
      <p className={`status ${task.completed ? "completed" : "pending"}`}>
        {task.completed ? " Completed" : " Pending"}
      </p>
      <div className="task-actions">
        <button className="btn-secondary" onClick={toggleCompleted}>
          {task.completed ? "Mark Pending" : "Mark Completed"}
        </button>
        <button className="btn-danger" onClick={deleteTask}>Delete</button>
      </div>
    </div>
  );
}