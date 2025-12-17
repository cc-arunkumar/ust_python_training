export default function TaskCard({ task, children }) {
  return (
    <div className="card">
      <h3>{task.title}</h3>
      <p>{task.description}</p>
      <p><strong>Status:</strong> {task.status}</p>
      <div className="actions">{children}</div>
    </div>
  );
}
