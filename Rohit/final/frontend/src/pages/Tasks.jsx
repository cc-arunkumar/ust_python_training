import { useEffect, useMemo, useState } from "react";
import { listTasks, updateTaskStatus, createTask, updateTaskPriority } from "../api/tasks"; 
import { getUser } from "../api/users";
import toast from "react-hot-toast";

const STATUS_COLUMNS = [
  { key: "TO_DO", label: "TO_DO", color: "bg-blue-200 text-blue-800 dark:bg-blue-900 dark:text-blue-200" },
  { key: "IN_PROGRESS", label: "IN_PROGRESS", color: "bg-yellow-200 text-yellow-800 dark:bg-yellow-900 dark:text-yellow-200" },
  { key: "REVIEW", label: "REVIEW", color: "bg-purple-200 text-purple-800 dark:bg-purple-900 dark:text-purple-200" },
  { key: "DONE", label: "DONE", color: "bg-green-200 text-green-800 dark:bg-green-900 dark:text-green-200" },
];

// Priority order mapping
const priorityOrder = { HIGH: 1, MEDIUM: 2, LOW: 3 };

export default function Tasks() {
  const [tasks, setTasks] = useState([]);
  const [current, setCurrent] = useState(null);
  const [showCreate, setShowCreate] = useState(false);

  useEffect(() => {
    const token = localStorage.getItem("token");
    const payload = JSON.parse(atob(token.split(".")[1]));
    getUser(payload.user_id).then(setCurrent);
    listTasks().then(setTasks);
  }, []);

  const visibleTasks = useMemo(() => {
    if (!current) return [];
    return current.role === "EMPLOYEE"
      ? tasks.filter((t) => t.assigned_to === current.emp_id)
      : tasks;
  }, [tasks, current]);

  const grouped = useMemo(() => {
    const g = { TO_DO: [], IN_PROGRESS: [], REVIEW: [], DONE: [] };
    visibleTasks.forEach((t) => g[t.status]?.push(t));

    // sort each column by priority order
    Object.keys(g).forEach((status) => {
      g[status].sort((a, b) => priorityOrder[a.priority] - priorityOrder[b.priority]);
    });

    return g;
  }, [visibleTasks]);

  const handleStatusChange = async (taskId, status) => {
    try {
      const updated = await updateTaskStatus(taskId, status);
      setTasks((prev) => prev.map((t) => (t.id === taskId ? updated : t)));
      toast.success("Task status updated!");
    } catch {
      toast.error("Failed to update status");
    }
  };

  const handlePriorityChange = async (taskId, priority) => {
    try {
      const updated = await updateTaskPriority(taskId, priority);
      setTasks((prev) => prev.map((t) => (t.id === taskId ? updated : t)));
      toast.success("Task priority updated!");
    } catch {
      toast.error("Failed to update priority");
    }
  };

  const handleCreate = async (e) => {
    e.preventDefault();
    const form = new FormData(e.currentTarget);
    const payload = {
      title: form.get("title"),
      description: form.get("description"),
      assigned_to: Number(form.get("assigned_to")),
      priority: form.get("priority"),
    };
    try {
      const task = await createTask(payload);
      setTasks((prev) => [task, ...prev]);
      setShowCreate(false);
      e.currentTarget.reset();
      toast.success("Task created successfully!");
    } catch {
      toast.error("Failed to create task");
    }
  };

  return (
    <div className="p-6 space-y-4 text-gray-800 dark:text-gray-200">
      <div className="flex items-center justify-between">
        <h1 className="text-2xl font-bold">Tasks</h1>
        {current?.role !== "EMPLOYEE" && (
          <button
            onClick={() => setShowCreate(true)}
            className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700"
          >
            Create task
          </button>
        )}
      </div>

      {showCreate && (
        <form onSubmit={handleCreate} className="bg-white dark:bg-gray-800 p-4 rounded shadow space-y-3">
          <div className="grid grid-cols-1 md:grid-cols-2 gap-3">
            <input name="title" required placeholder="Title" className="p-2 border rounded dark:bg-gray-700 dark:text-gray-200" />
            <select name="priority" className="p-2 border rounded dark:bg-gray-700 dark:text-gray-200" defaultValue="MEDIUM">
              <option value="HIGH">HIGH</option>
              <option value="MEDIUM">MEDIUM</option>
              <option value="LOW">LOW</option>
            </select>
          </div>
          <textarea name="description" placeholder="Description" className="p-2 border rounded w-full dark:bg-gray-700 dark:text-gray-200" />
          <input name="assigned_to" type="number" required placeholder="Assignee emp_id" className="p-2 border rounded w-full dark:bg-gray-700 dark:text-gray-200" />
          <div className="flex gap-2">
            <button type="submit" className="bg-green-600 text-white px-4 py-2 rounded hover:bg-green-700">Save</button>
            <button type="button" onClick={() => setShowCreate(false)} className="px-4 py-2 rounded border">Cancel</button>
          </div>
        </form>
      )}

      <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
        {STATUS_COLUMNS.map(({ key, label, color }) => (
          <div key={key} className="bg-gray-100 dark:bg-gray-800 rounded-lg p-2">
            <h2 className={`text-lg font-semibold mb-2 px-2 py-1 rounded ${color}`}>{label}</h2>
            <div className="space-y-2">
              {grouped[key].map((t) => (
                <div key={t.id} className="bg-white dark:bg-gray-900 p-3 rounded shadow">
                  <div className="flex items-center justify-between">
                    <p className="font-medium text-gray-800 dark:text-gray-200">{t.title}</p>
                    {current?.role === "EMPLOYEE" ? (
                      <span
                        className={`text-xs px-2 py-1 rounded ${
                          t.priority === "HIGH"
                            ? "bg-red-100 text-red-600 dark:bg-red-900 dark:text-red-300"
                            : t.priority === "MEDIUM"
                            ? "bg-yellow-100 text-yellow-700 dark:bg-yellow-900 dark:text-yellow-300"
                            : "bg-green-100 text-green-600 dark:bg-green-900 dark:text-green-300"
                        }`}
                      >
                        {t.priority}
                      </span>
                    ) : (
                      <select
                        value={t.priority}
                        onChange={(e) => handlePriorityChange(t.id, e.target.value)}
                        className="text-xs border rounded p-1 dark:bg-gray-700 dark:text-gray-200"
                      >
                        <option value="HIGH">HIGH</option>
                        <option value="MEDIUM">MEDIUM</option>
                        <option value="LOW">LOW</option>
                      </select>
                    )}
                  </div>
                  <p className="text-xs text-gray-500 dark:text-gray-400">Assignee emp_id: {t.assigned_to}</p>
                  <div className="mt-2">
                    <select
                      value={t.status}
                      onChange={(e) => handleStatusChange(t.id, e.target.value)}
                      className="text-sm border rounded p-1 dark:bg-gray-700 dark:text-gray-200"
                      disabled={current?.role === "EMPLOYEE" && current?.emp_id !== t.assigned_to}
                    >
                      {STATUS_COLUMNS.map(({ key }) => (
                        <option key={key} value={key}>{key}</option>
                      ))}
                    </select>
                  </div>
                </div>
              ))}
              {grouped[key].length === 0 && (
                <p className="text-sm text-gray-500 dark:text-gray-400">No tasks</p>
              )}
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
