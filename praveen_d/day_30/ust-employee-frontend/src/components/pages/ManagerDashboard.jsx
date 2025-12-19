import { useState, useMemo } from "react";
import PerformanceBarChart from "../ui/PerformanceBarChart";  // Assume this exists for team performance
import {
  DndContext,
  PointerSensor,
  useSensor,
  useSensors,
  useDroppable,
  pointerWithin,
} from "@dnd-kit/core";
import { Users, LogOut, AlertCircle, Plus } from "lucide-react";
import { api } from "../../services/api";
import TaskCard from "../ui/TaskCard";

/* ================= STATUS CONFIG ================= */
const STATUS_ORDER = ["TO_DO", "IN_PROGRESS", "REVIEW", "DONE"];

const STATUS_META = {
  TO_DO: { label: "To Do", bg: "bg-blue-50", ring: "ring-blue-300" },
  IN_PROGRESS: { label: "In Progress", bg: "bg-amber-50", ring: "ring-amber-300" },
  REVIEW: { label: "Review", bg: "bg-purple-50", ring: "ring-purple-300" },
  DONE: { label: "Done", bg: "bg-emerald-50", ring: "ring-emerald-300" },
};

/* ================= DROPPABLE COLUMN ================= */
const DroppableColumn = ({ status, count, children }) => {
  const { setNodeRef, isOver } = useDroppable({
    id: status,
  });

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
const ManagerDashboard = ({
  user,
  tasks,
  token,
  onLogout,
  onSwitchRole,
  onError,
  onUpdateTasks,
  onCreateTask,
  error,
}) => {
  const [viewMode, setViewMode] = useState("KANBAN");
  const [showCreateTask, setShowCreateTask] = useState(false);
  const [taskForm, setTaskForm] = useState({
    task_id: '',
    name: '',
    description: '',
    assigned_to: '',
    priority: 'MEDIUM',
    expected_closure: '',
  });
  const [localLoading, setLocalLoading] = useState(false);

  const sensors = useSensors(
    useSensor(PointerSensor, {
      activationConstraint: { distance: 5 },
    })
  );

  /* MANAGER'S TEAM TASKS */
  const managerTasks = tasks.filter(
    (t) =>
      String(t.assigned_by).trim().toUpperCase() ===
      String(user?.emp_id).trim().toUpperCase()
  );

  const tasksByStatus = {
    TO_DO: managerTasks.filter((t) => t.status === "TO_DO"),
    IN_PROGRESS: managerTasks.filter((t) => t.status === "IN_PROGRESS"),
    REVIEW: managerTasks.filter((t) => t.status === "REVIEW"),
    DONE: managerTasks.filter((t) => t.status === "DONE"),
  };

  const sortedTasksByDate = useMemo(() => {
    return [...managerTasks].sort((a, b) => {
      const aDate = new Date(a.expected_closure || a.created_at || 0);
      const bDate = new Date(b.expected_closure || b.created_at || 0);
      return aDate - bDate;
    });
  }, [managerTasks]);

  /* ================= DRAG END (Manager-Specific) ================= */
  const handleDragEnd = async ({ active, over }) => {
    try {
      if (!over) return;

      const taskId = active.id;
      const newStatus = over.id;

      const draggedTask = tasks.find((t) => t.task_id === taskId);
      if (!draggedTask || draggedTask.status === newStatus) return;

      // Manager ALLOWED: Full forward + limited backward (REVIEW → IN_PROGRESS only)
      const ALLOWED = {
        TO_DO: ["IN_PROGRESS"],
        IN_PROGRESS: ["REVIEW"],
        REVIEW: ["DONE", "IN_PROGRESS"],  // Backward enabled for REVIEW
        DONE: [],
      };

      if (!ALLOWED[draggedTask.status].includes(newStatus)) return;

      // Optimistic update
      onUpdateTasks({ ...draggedTask, status: newStatus });

      // API call
      await api.updateTaskStatus(taskId, newStatus, "", token);
    } catch (err) {
      onError(err.message);
    }
  };

  /* ================= CREATE TASK ================= */
  const handleCreateTask = async (e) => {
    e.preventDefault();
    setLocalLoading(true);
    try {
      const newTask = {
        ...taskForm,
        status: 'TO_DO',
        assigned_by: user?.emp_id,
        created_by: user?.emp_id,
      };
      const created = await api.createTask(newTask, token);
      onCreateTask(created);
      setShowCreateTask(false);
      setTaskForm({
        task_id: '',
        name: '',
        description: '',
        assigned_to: '',
        priority: 'MEDIUM',
        expected_closure: '',
      });
    } catch (err) {
      onError(err.message);
    } finally {
      setLocalLoading(false);
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
              <h1 className="font-bold">Manager Dashboard</h1>
              <p className="text-sm text-gray-600">{user?.emp_id}</p>
            </div>
          </div>
          <div className="flex items-center gap-4">
            {user?.role === 'ADMIN' && (
              <button
                onClick={onSwitchRole}
                className="text-gray-600 hover:text-gray-900"
              >
                Switch Role
              </button>
            )}
            <button
              onClick={onLogout}
              className="flex items-center gap-2 bg-red-500 hover:bg-red-600 text-white px-4 py-2 rounded-lg"
            >
              <LogOut size={16} /> Logout
            </button>
          </div>
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

        {/* CREATE TASK BUTTON (Always Visible) */}
        <div className="mb-6">
          <button
            onClick={() => setShowCreateTask(true)}
            className="bg-green-600 text-white px-4 py-2 rounded-lg hover:bg-green-700 flex items-center gap-2"
          >
            <Plus className="w-5 h-5" />
            <span>Create New Task</span>
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
                  <th className="px-4 py-3 text-left">Assigned To</th>
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
                    <td className="px-4 py-3">{task.assigned_to}</td>
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
          <PerformanceBarChart tasksByStatus={tasksByStatus} />  // Team-based chart
        )}

        {/* CREATE TASK MODAL */}
        {showCreateTask && (
          <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center p-4 z-50">
            <div className="bg-white rounded-lg max-w-2xl w-full p-6">
              <h3 className="text-xl font-bold mb-4">Create New Task</h3>
              <form onSubmit={handleCreateTask} className="space-y-4">
                <div className="grid grid-cols-2 gap-4">
                  <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">
                      Task ID
                    </label>
                    <input
                      type="text"
                      value={taskForm.task_id}
                      onChange={(e) =>
                        setTaskForm({ ...taskForm, task_id: e.target.value })
                      }
                      className="w-full px-3 py-2 border border-gray-300 rounded-lg"
                      required
                    />
                  </div>
                  <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">
                      Priority
                    </label>
                    <select
                      value={taskForm.priority}
                      onChange={(e) =>
                        setTaskForm({ ...taskForm, priority: e.target.value })
                      }
                      className="w-full px-3 py-2 border border-gray-300 rounded-lg"
                    >
                      <option value="HIGH">High</option>
                      <option value="MEDIUM">Medium</option>
                      <option value="LOW">Low</option>
                    </select>
                  </div>
                </div>
                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-1">
                    Task Name
                  </label>
                  <input
                    type="text"
                    value={taskForm.name}
                    onChange={(e) =>
                      setTaskForm({ ...taskForm, name: e.target.value })
                    }
                    className="w-full px-3 py-2 border border-gray-300 rounded-lg"
                    required
                  />
                </div>
                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-1">
                    Description
                  </label>
                  <textarea
                    value={taskForm.description}
                    onChange={(e) =>
                      setTaskForm({ ...taskForm, description: e.target.value })
                    }
                    className="w-full px-3 py-2 border border-gray-300 rounded-lg"
                    rows="3"
                    required
                  />
                </div>
                <div className="grid grid-cols-2 gap-4">
                  <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">
                      Assign To (Employee ID)
                    </label>
                    <input
                      type="text"
                      value={taskForm.assigned_to}
                      onChange={(e) =>
                        setTaskForm({ ...taskForm, assigned_to: e.target.value })
                      }
                      className="w-full px-3 py-2 border border-gray-300 rounded-lg"
                      required
                    />
                  </div>
                  <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">
                      Expected Closure
                    </label>
                    <input
                      type="date"
                      value={taskForm.expected_closure}
                      onChange={(e) =>
                        setTaskForm({ ...taskForm, expected_closure: e.target.value })
                      }
                      className="w-full px-3 py-2 border border-gray-300 rounded-lg"
                      required
                    />
                  </div>
                </div>
                <div className="flex justify-end space-x-3 pt-4">
                  <button
                    type="button"
                    onClick={() => setShowCreateTask(false)}
                    className="px-4 py-2 border border-gray-300 rounded-lg hover:bg-gray-50"
                  >
                    Cancel
                  </button>
                  <button
                    type="submit"
                    disabled={localLoading}
                    className="px-4 py-2 bg-green-600 text-white rounded-lg hover:bg-green-700 disabled:opacity-50"
                  >
                    {localLoading ? 'Creating...' : 'Create Task'}
                  </button>
                </div>
              </form>
            </div>
          </div>
        )}
      </main>
    </div>
  );
};

export default ManagerDashboard;