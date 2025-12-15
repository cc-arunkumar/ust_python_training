
// TaskList.jsx
import TaskItem from "./TaskItem";

export default function TaskList({ tasks, refreshTasks }) {
  return (
    <>
      <h2 className="tasklist-title">Task List</h2>
      <div className="tasklist-container">
        {(!tasks || tasks.length === 0) ? (
          <div className="task-item">
            <h3>No tasks yet</h3>
            <p>Add a task using the form on the left.</p>
          </div>
        ) : (
          tasks.map((task) => (
            <TaskItem key={task.id} task={task} refreshTasks={refreshTasks} />
          ))
        )}
      </div>
    </>
  );
}
