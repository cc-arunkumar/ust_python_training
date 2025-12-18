import { useEffect, useMemo, useState } from "react";
import {
  listTasks,
  updateTaskStatus,
  createTask,
  updateTaskPriority,
} from "../api/tasks";
import { getUser } from "../api/users";
import toast from "react-hot-toast";
import { DragDropContext, Droppable, Draggable } from "@hello-pangea/dnd";

// Gradient color themes for each status column
const STATUS_COLUMNS = [
  {
    key: "TO_DO",
    label: "To Do",
    gradient: "bg-gradient-to-r from-blue-500 to-indigo-600 text-white",
  },
  {
    key: "IN_PROGRESS",
    label: "In Progress",
    gradient: "bg-gradient-to-r from-yellow-400 to-orange-500 text-white",
  },
  {
    key: "REVIEW",
    label: "Review",
    gradient: "bg-gradient-to-r from-purple-500 to-pink-600 text-white",
  },
  {
    key: "DONE",
    label: "Done",
    gradient: "bg-gradient-to-r from-green-500 to-emerald-600 text-white",
  },
];

// Priority order mapping
const priorityOrder = { HIGH: 1, MEDIUM: 2, LOW: 3 };

export default function Tasks() {
  const [tasks, setTasks] = useState([]);
  const [current, setCurrent] = useState(null);
  const [filterPriority, setFilterPriority] = useState("");

  const [showCreate, setShowCreate] = useState(false);

  useEffect(() => {
    const token = localStorage.getItem("token");
    const payload = JSON.parse(atob(token.split(".")[1]));
    getUser(payload.user_id).then(setCurrent);
    listTasks().then(setTasks);
  }, []);

  const visibleTasks = useMemo(() => {
    if (!current) return [];
    let filtered =
      current.role === "EMPLOYEE"
        ? tasks.filter((t) => t.assigned_to === current.emp_id)
        : tasks;

    // ✅ apply priority filter
    if (filterPriority) {
      filtered = filtered.filter(
        (t) => t.priority === filterPriority.toUpperCase()
      );
    }

    return filtered;
  }, [tasks, current, filterPriority]);

  const grouped = useMemo(() => {
    const g = { TO_DO: [], IN_PROGRESS: [], REVIEW: [], DONE: [] };
    visibleTasks.forEach((t) => g[t.status]?.push(t));

    // sort each column by priority order
    Object.keys(g).forEach((status) => {
      g[status].sort(
        (a, b) => priorityOrder[a.priority] - priorityOrder[b.priority]
      );
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

  // 🔑 Drag and Drop handler
  const handleDragEnd = async (result) => {
    const { destination, source, draggableId } = result;
    if (!destination) return;

    // same place → ignore
    if (
      destination.droppableId === source.droppableId &&
      destination.index === source.index
    ) {
      return;
    }

    const taskId = Number(draggableId);
    const newStatus = destination.droppableId;

    // If moved to a new column → update status in backend
    if (newStatus !== source.droppableId) {
      try {
        const updated = await updateTaskStatus(taskId, newStatus);
        setTasks((prev) => prev.map((t) => (t.id === taskId ? updated : t)));
        toast.success("Task moved!");
      } catch {
        toast.error("Failed to move task");
      }
    } else {
      // Reordering inside same column → update local state only
      const items = Array.from(grouped[source.droppableId]);
      const [moved] = items.splice(source.index, 1);
      items.splice(destination.index, 0, moved);

      setTasks((prev) => prev.map((t) => (t.id === moved.id ? { ...t } : t)));
    }
  };

  return (
    <div className="p-6 space-y-6 text-gray-800 dark:text-gray-200">
      <div className="flex gap-3 items-center">
        <label className="font-medium">Filter by Priority:</label>
        <select
          value={filterPriority}
          onChange={(e) => setFilterPriority(e.target.value)}
          className="p-2 border rounded dark:bg-gray-700 dark:text-gray-200"
        >
          <option value="">All</option>
          <option value="HIGH">HIGH</option>
          <option value="MEDIUM">MEDIUM</option>
          <option value="LOW">LOW</option>
        </select>
      </div>
      <div className="flex items-center justify-between">
        <h1 className="text-3xl font-extrabold tracking-wide text-transparent bg-clip-text bg-gradient-to-r from-cyan-400 to-blue-500">
          Tasks
        </h1>
        {current?.role !== "EMPLOYEE" && (
          <button
            onClick={() => setShowCreate(true)}
            className="px-4 py-2 rounded-lg bg-gradient-to-r from-blue-500 to-indigo-600 text-white font-medium shadow hover:scale-105 transform transition-all duration-200"
          >
            + Create Task
          </button>
        )}
      </div>

      {showCreate && (
        <form
          onSubmit={handleCreate}
          className="bg-white dark:bg-gray-800 p-6 rounded-xl shadow-lg space-y-4"
        >
          <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
            <input
              name="title"
              required
              placeholder="Title"
              className="p-2 border rounded dark:bg-gray-700 dark:text-gray-200"
            />
            <select
              name="priority"
              className="p-2 border rounded dark:bg-gray-700 dark:text-gray-200"
              defaultValue="MEDIUM"
            >
              <option value="HIGH">HIGH</option>
              <option value="MEDIUM">MEDIUM</option>
              <option value="LOW">LOW</option>
            </select>
          </div>
          <textarea
            name="description"
            placeholder="Description"
            className="p-2 border rounded w-full dark:bg-gray-700 dark:text-gray-200"
          />
          <input
            name="assigned_to"
            type="number"
            required
            placeholder="Assignee emp_id"
            className="p-2 border rounded w-full dark:bg-gray-700 dark:text-gray-200"
          />
          <div className="flex gap-3">
            <button
              type="submit"
              className="px-4 py-2 rounded-lg bg-gradient-to-r from-green-500 to-emerald-600 text-white font-medium shadow hover:scale-105 transition"
            >
              Save
            </button>
            <button
              type="button"
              onClick={() => setShowCreate(false)}
              className="px-4 py-2 rounded-lg border hover:bg-gray-100 dark:hover:bg-gray-700 transition"
            >
              Cancel
            </button>
          </div>
        </form>
      )}

      {/* 🔑 DragDropContext wrapper */}
      <DragDropContext onDragEnd={handleDragEnd}>
        <div className="grid grid-cols-1 md:grid-cols-4 gap-6">
          {STATUS_COLUMNS.map(({ key, label, gradient }) => (
            <Droppable droppableId={key} key={key}>
              {(provided) => (
                <div
                  ref={provided.innerRef}
                  {...provided.droppableProps}
                  className="bg-gray-50 dark:bg-gray-800 rounded-xl shadow-lg p-4"
                >
                  <h2
                    className={`text-lg font-semibold mb-3 px-3 py-2 rounded-lg ${gradient}`}
                  >
                    {label}
                  </h2>
                  <div className="space-y-3">
                    {grouped[key].map((t, index) => (
                      <Draggable
                        key={t.id}
                        draggableId={String(t.id)}
                        index={index}
                      >
                        {(provided) => (
                          <div
                            ref={provided.innerRef}
                            {...provided.draggableProps}
                            {...provided.dragHandleProps}
                            className="bg-white dark:bg-gray-900 p-4 rounded-lg shadow hover:scale-[1.02] transition"
                          >
                            <div className="flex items-center justify-between">
                              <p className="font-medium text-gray-800 dark:text-gray-200">
                                {t.title}
                              </p>
                              {current?.role === "EMPLOYEE" ? (
                                <span
                                  className={`text-xs px-2 py-1 rounded-full font-semibold ${
                                    t.priority === "HIGH"
                                      ? "bg-red-500 text-white"
                                      : t.priority === "MEDIUM"
                                      ? "bg-yellow-400 text-white"
                                      : "bg-green-500 text-white"
                                  }`}
                                >
                                  {t.priority}
                                </span>
                              ) : (
                                <select
                                  value={t.priority}
                                  onChange={(e) =>
                                    handlePriorityChange(t.id, e.target.value)
                                  }
                                  className="text-xs border rounded p-1 dark:bg-gray-700 dark:text-gray-200"
                                >
                                  <option value="HIGH">HIGH</option>
                                  <option value="MEDIUM">MEDIUM</option>
                                  <option value="LOW">LOW</option>
                                </select>
                              )}
                            </div>

                            <p className="text-xs text-gray-500 dark:text-gray-400">
                              Assignee emp_id: {t.assigned_to}
                            </p>

                            <div className="mt-2">
                              <select
                                value={t.status}
                                onChange={(e) =>
                                  handleStatusChange(t.id, e.target.value)
                                }
                                className="text-sm border rounded p-1 dark:bg-gray-700 dark:text-gray-200"
                                disabled={
                                  current?.role === "EMPLOYEE" &&
                                  current?.emp_id !== t.assigned_to
                                }
                              >
                                {STATUS_COLUMNS.map(({ key }) => (
                                  <option key={key} value={key}>
                                    {key}
                                  </option>
                                ))}
                              </select>
                            </div>
                          </div>
                        )}
                      </Draggable>
                    ))}
                    {grouped[key].length === 0 && (
                      <p className="text-sm text-gray-500 dark:text-gray-400">
                        No tasks
                      </p>
                    )}
                    {provided.placeholder}
                  </div>
                </div>
              )}
            </Droppable>
          ))}
        </div>
      </DragDropContext>
    </div>
  );
}
