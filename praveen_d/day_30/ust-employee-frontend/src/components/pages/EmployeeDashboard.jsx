import { useState, useMemo } from "react";
import PerformanceBarChart from "../ui/PerformanceBarChart";
import {
  DndContext,
  PointerSensor,
  useSensor,
  useSensors,
  useDroppable,
  pointerWithin,
} from "@dnd-kit/core";
import { Users, LogOut, AlertCircle } from "lucide-react";
import { api } from "../../services/api";
import TaskCard from "../ui/TaskCard";

/* ================= STATUS CONFIG ================= */
const STATUS_ORDER = ["TO_DO", "IN_PROGRESS", "REVIEW", "DONE"];

const STATUS_META = {
  TO_DO: { label: "To Do", bg: "bg-blue-50", ring: "ring-blue-300" },
  IN_PROGRESS: {
    label: "In Progress",
    bg: "bg-amber-50",
    ring: "ring-amber-300",
  },
  REVIEW: { label: "Review", bg: "bg-purple-50", ring: "ring-purple-300" },
  DONE: { label: "Done", bg: "bg-emerald-50", ring: "ring-emerald-300" },
};

/* ================= DROPPABLE COLUMN ================= */
const DroppableColumn = ({ status, count, children }) => {
  const { setNodeRef, isOver } = useDroppable({ id: status });
  const meta = STATUS_META[status];

  return (
    <div className="flex flex-col">
      <div className="flex justify-between mb-2 px-1">
        <h3 className="font-semibold text-gray-700">{meta.label}</h3>
        <span className="text-xs bg-white px-2 py-0.5 rounded-full shadow">
          {count}
        </span>
      </div>

      <div
        ref={setNodeRef}
        className={`min-h-[420px] p-4 rounded-2xl border transition
          ${meta.bg}
          ${isOver ? `ring-2 ${meta.ring}` : ""}`}
      >
        <div className="space-y-3">{children}</div>
      </div>
    </div>
  );
};

/* ================= MAIN DASHBOARD ================= */
const EmployeeDashboard = ({
  user,
  tasks,
  token,
  onLogout,
  onError,
  onUpdateTasks,
  error,
}) => {
  const [viewMode, setViewMode] = useState("KANBAN");

  const sensors = useSensors(
    useSensor(PointerSensor, { activationConstraint: { distance: 5 } })
  );

  /* USER TASKS */
  const myTasks = tasks.filter(
    (t) =>
      String(t.assigned_to).trim().toUpperCase() ===
      String(user?.emp_id).trim().toUpperCase()
  );

  const tasksByStatus = {
    TO_DO: myTasks.filter((t) => t.status === "TO_DO"),
    IN_PROGRESS: myTasks.filter((t) => t.status === "IN_PROGRESS"),
    REVIEW: myTasks.filter((t) => t.status === "REVIEW"),
    DONE: myTasks.filter((t) => t.status === "DONE"),
  };

  const sortedTasksByDate = useMemo(() => {
    return [...myTasks].sort((a, b) => {
      const aDate = new Date(a.expected_closure || a.created_at || 0);
      const bDate = new Date(b.expected_closure || b.created_at || 0);
      return aDate - bDate;
    });
  }, [myTasks]);

  /* ================= DRAG END ================= */
  const handleDragEnd = async ({ active, over }) => {
    try {
      if (!over) return;

      const taskId = active.id;
      const newStatus = over.id;

      const draggedTask = tasks.find((t) => t.task_id === taskId);
      if (!draggedTask || draggedTask.status === newStatus) return;

      const ALLOWED = {
        TO_DO: ["IN_PROGRESS"],
        IN_PROGRESS: ["REVIEW"],
        REVIEW: ["DONE"],
        DONE: [],
      };

      if (!ALLOWED[draggedTask.status].includes(newStatus)) return;

      onUpdateTasks({ ...draggedTask, status: newStatus });
      await api.updateTaskStatus(taskId, newStatus, "", token);
    } catch (err) {
      onError(err.message);
    }
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-100 to-gray-200">
      {/* HEADER */}
      <header className="bg-white shadow-sm border-b">
        <div className="max-w-7xl mx-auto px-6 py-4 flex justify-between">
          <div className="flex items-center gap-3">
            <Users className="text-emerald-600" />
            <div>
              <h1 className="font-bold">Employee Dashboard</h1>
              <p className="text-sm text-gray-600">{user?.emp_id}</p>
            </div>
          </div>

          <button
            onClick={onLogout}
            className="flex items-center gap-2 bg-red-500 hover:bg-red-600 text-white px-4 py-2 rounded-lg"
          >
            <LogOut size={16} /> Logout
          </button>
        </div>
      </header>

      {/* MAIN */}
      <main className="max-w-7xl mx-auto px-6 py-6">
        {error && (
          <div className="mb-4 bg-red-50 border border-red-300 text-red-700 p-3 rounded-lg flex items-center gap-2">
            <AlertCircle size={16} />
            {error}
          </div>
        )}

        {/* VIEW TOGGLE */}
        <div className="flex justify-end mb-4 gap-2">
          <button
            onClick={() => setViewMode("KANBAN")}
            className={`px-4 py-2 rounded-lg text-sm font-medium ${
              viewMode === "KANBAN"
                ? "bg-emerald-600 text-white"
                : "bg-white border"
            }`}
          >
            Kanban
          </button>

          <button
            onClick={() => setViewMode("LIST")}
            className={`px-4 py-2 rounded-lg text-sm font-medium ${
              viewMode === "LIST"
                ? "bg-indigo-600 text-white"
                : "bg-white border"
            }`}
          >
            List
          </button>

          <button
            onClick={() => setViewMode("PERFORMANCE")}
            className={`px-4 py-2 rounded-lg text-sm font-medium ${
              viewMode === "PERFORMANCE"
                ? "bg-orange-600 text-white"
                : "bg-white border"
            }`}
          >
            Performance
          </button>
        </div>

        {/* KANBAN */}
        {viewMode === "KANBAN" && (
          <DndContext
            sensors={sensors}
            collisionDetection={pointerWithin}
            onDragEnd={handleDragEnd}
          >
            <div className="grid grid-cols-4 gap-6">
              {STATUS_ORDER.map((status) => (
                <DroppableColumn
                  key={status}
                  status={status}
                  count={tasksByStatus[status].length}
                >
                  {tasksByStatus[status].map((task) => (
                    <TaskCard
                      key={task.task_id}
                      task={task}
                      token={token}
                      onUpdateTask={(updated) => onUpdateTasks(updated)}
                    />
                  ))}
                </DroppableColumn>
              ))}
            </div>
          </DndContext>
        )}

        {/* LIST */}
        {viewMode === "LIST" && (
          <div className="bg-white rounded-xl shadow border overflow-x-auto">
            <table className="w-full text-sm">
              <thead className="bg-gray-100">
                <tr>
                  <th className="px-4 py-3 text-left">Task</th>
                  <th className="px-4 py-3 text-left">Status</th>
                  <th className="px-4 py-3 text-left">Priority</th>
                  <th className="px-4 py-3 text-left">Created</th>
                  <th className="px-4 py-3 text-left">Deadline</th>
                </tr>
              </thead>
              <tbody>
                {sortedTasksByDate.map((task) => (
                  <tr key={task.task_id} className="border-t">
                    <td className="px-4 py-3">{task.name}</td>
                    <td className="px-4 py-3">{task.status}</td>
                    <td className="px-4 py-3">{task.priority}</td>
                    <td className="px-4 py-3">
                      {task.created_at
                        ? new Date(task.created_at).toLocaleDateString()
                        : "—"}
                    </td>
                    <td className="px-4 py-3">
                      {task.expected_closure
                        ? new Date(task.expected_closure).toLocaleDateString()
                        : "—"}
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}

        {/* PERFORMANCE */}
        {viewMode === "PERFORMANCE" && (
          <PerformanceBarChart tasksByStatus={tasksByStatus} />
        )}
      </main>
    </div>
  );
};

export default EmployeeDashboard;
