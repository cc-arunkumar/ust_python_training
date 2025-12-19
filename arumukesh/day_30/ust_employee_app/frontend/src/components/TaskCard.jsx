export default function TaskCard({ task }) {
  return (
    <div className="p-4 bg-white rounded shadow">
      <h2 className="font-semibold">{task.title}</h2>
      <p className="text-sm">{task.description}</p>
      <p className="text-xs text-gray-500">Status: {task.status}</p>
    </div>
  );
}
