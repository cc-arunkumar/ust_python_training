import React, { useState, useEffect } from "react";
import { Plus, AlertCircle, Users, Search } from "lucide-react";
import { useAuth } from "../../context/AuthContext";
import ApiService from "../../services/api";
import TaskModal from "./TaskModal";
import TaskDetailsModal from "./TaskDetailsModal";
import KanbanColumn from "./KanbanColumn";
import { TASK_STATUSES } from "../../utils/constants";
import toast, { Toaster } from "react-hot-toast";
import { DragDropContext } from "@hello-pangea/dnd";

// Priority order for sorting
const PRIORITY_ORDER = { high: 3, medium: 2, low: 1 };

const KanbanBoard = ({ initialTasks, initialEmployees, onTasksChanged }) => {
  const { hasRole } = useAuth();
  const canEdit = hasRole("ADMIN") || hasRole("MANAGER");

  const [tasks, setTasks] = useState(initialTasks ?? []);
  const [employees, setEmployees] = useState(initialEmployees ?? []);
  const [searchQuery, setSearchQuery] = useState("");
  const [priorityFilter, setPriorityFilter] = useState("ALL");
  const [showEmployeesModal, setShowEmployeesModal] = useState(false);
  const [selectedEmployeeId, setSelectedEmployeeId] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  const [selectedTask, setSelectedTask] = useState(null);
  const [editingTask, setEditingTask] = useState(null);
  const [showCreateModal, setShowCreateModal] = useState(false);
  const [sortOption, setSortOption] = useState("priority");

  useEffect(() => {
    if (initialTasks !== undefined) {
      setTasks(initialTasks);
      setLoading(false);
      setError("");
      // also set employees when provided
      if (initialEmployees !== undefined) setEmployees(initialEmployees);
      return;
    }

    fetchTasks();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [initialTasks, initialEmployees]);

  const fetchTasks = async (force = false) => {
    try {
      if (initialTasks !== undefined && !force) {
        setTasks(initialTasks);
        return;
      }

      const data = await ApiService.getTasks();
      setTasks(data);
    } catch (err) {
      setError(err.message);
      toast.error(err.message);
    } finally {
      setLoading(false);
    }
  };

  const handleDelete = async (taskId) => {
    try {
      await ApiService.deleteTask(taskId);
      toast.success("Task deleted successfully");
      // update local list immediately
      setTasks((prev) => prev.filter((t) => t.task_id !== taskId));
      // Ask parent (Layout) to refresh role-filtered data so stats update
      if (onTasksChanged) onTasksChanged();
      else await fetchTasks(true);
    } catch (err) {
      toast.error(err.message);
    }
  };

  /* =========================
     STATUS MOVEMENT RULES
     ========================= */
  const canMove = (from, to) => {
    const allowedTransitions = {
      TODO: ["ON_PROCESS"],
      ON_PROCESS: ["REVIEW"],
      REVIEW: ["ON_PROCESS", "DONE"],
      DONE: [],
    };

    return allowedTransitions[from]?.includes(to);
  };

  const onDragEnd = async (result) => {
    const { source, destination, draggableId } = result;

    if (!destination) return;
    if (source.droppableId === destination.droppableId) return;

    const fromStatus = source.droppableId;
    const toStatus = destination.droppableId;

    if (!canMove(fromStatus, toStatus)) {
      toast.error(`Cannot move task from ${fromStatus} to ${toStatus}`);
      return;
    }

    try {
      await ApiService.updateTaskStatus(draggableId, toStatus);
      toast.success(`Task moved to ${toStatus.replace("_", " ")}`);
      // update local task status to keep filtered view
      setTasks((prev) =>
        prev.map((t) =>
          t.task_id.toString() === draggableId.toString()
            ? { ...t, status: toStatus }
            : t
        )
      );
      if (onTasksChanged) onTasksChanged();
      else await fetchTasks(true);
    } catch {
      toast.error("Failed to update task");
    }
  };

  // Apply search / priority / employee filters first
  const filteredTasks = tasks.filter((t) => {
    // priority filter
    if (priorityFilter && priorityFilter !== "ALL") {
      if (!t.priority) return false;
      if (t.priority.toString().toLowerCase() !== priorityFilter.toLowerCase())
        return false;
    }

    // search filter (task title)
    if (searchQuery && searchQuery.trim() !== "") {
      const q = searchQuery.trim().toLowerCase();
      if (!t.title || !t.title.toLowerCase().includes(q)) return false;
    }

    // employee filter (assigned_to)
    if (selectedEmployeeId) {
      const assigned = t.assigned_to == null ? null : Number(t.assigned_to);
      if (assigned !== Number(selectedEmployeeId)) return false;
    }

    return true;
  });

  // Group tasks by status and apply sorting
  const groupedTasks = {};
  Object.values(TASK_STATUSES).forEach((status) => {
    groupedTasks[status] = filteredTasks
      .filter((t) => t.status === status)
      .sort((a, b) => {
        if (sortOption === "priority") {
          const aPriority = a.priority
            ? PRIORITY_ORDER[a.priority.toLowerCase()] || 0
            : 0;
          const bPriority = b.priority
            ? PRIORITY_ORDER[b.priority.toLowerCase()] || 0
            : 0;
          return bPriority - aPriority;
        } else {
          const aDate = a.expected_closure
            ? new Date(a.expected_closure)
            : new Date(0);
          const bDate = b.expected_closure
            ? new Date(b.expected_closure)
            : new Date(0);
          return aDate - bDate;
        }
      });
  });

  if (loading) {
    return (
      <div className="min-h-screen flex items-center justify-center">
        Loading...
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-gray-50">
      <Toaster position="top-right" />

      {/* HEADER */}
      <div className="bg-white px-6 py-4 shadow-sm flex justify-between items-center">
        <h1 className="text-xl font-semibold">Task Board</h1>

        <div className="flex gap-3 items-center">
          {/* Employee button (shows employee modal) */}
          <button
            onClick={() => setShowEmployeesModal(true)}
            className="flex items-center gap-2 px-3 py-2 rounded-lg bg-slate-100 border border-slate-200 text-sm"
          >
            <Users size={16} /> Employees
          </button>

          {/* Search */}
          <div className="relative">
            <input
              type="search"
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
              placeholder="Search tasks by name..."
              className="px-3 py-2 border border-slate-300 rounded-lg text-sm w-64"
            />
            <div className="absolute right-2 top-1/2 -translate-y-1/2 text-slate-400 pointer-events-none">
              <Search size={14} />
            </div>
          </div>

          {/* Sort */}
          <select
            value={sortOption}
            onChange={(e) => setSortOption(e.target.value)}
            className="border rounded px-3 py-1 text-sm"
          >
            <option value="priority">Sort by Priority</option>
            <option value="date">Sort by Deadline</option>
          </select>

          {canEdit && (
            <button
              onClick={() => setShowCreateModal(true)}
              className="bg-blue-600 text-white px-4 py-2 rounded-lg text-sm flex items-center gap-1"
            >
              <Plus size={16} /> New Task
            </button>
          )}

          {/* Priority filter on extreme right */}
          <select
            value={priorityFilter}
            onChange={(e) => setPriorityFilter(e.target.value)}
            className="border rounded px-3 py-1 text-sm"
          >
            <option value="ALL">All priorities</option>
            <option value="HIGH">High</option>
            <option value="MEDIUM">Medium</option>
            <option value="LOW">Low</option>
          </select>
        </div>
      </div>

      {/* ERROR */}
      {error && (
        <div className="m-6 bg-red-50 text-red-700 px-4 py-3 rounded-lg flex gap-2">
          <AlertCircle size={18} />
          {error}
        </div>
      )}

      {/* BOARD */}
      <DragDropContext onDragEnd={onDragEnd}>
        <div className="p-6 flex gap-6 overflow-x-auto">
          {Object.entries(groupedTasks).map(([status, list]) => (
            <KanbanColumn
              key={status}
              status={status}
              tasks={list}
              employees={employees}
              onTaskView={setSelectedTask}
              onTaskEdit={canEdit ? setEditingTask : null}
              onTaskDelete={handleDelete}
            />
          ))}
        </div>
      </DragDropContext>

      {/* Employees modal */}
      {showEmployeesModal && (
        <div className="fixed inset-0 z-50 flex items-center justify-center">
          <div
            className="absolute inset-0 bg-black/40"
            onClick={() => setShowEmployeesModal(false)}
          />
          <div className="relative bg-white rounded-lg p-6 shadow-lg w-full max-w-md z-10">
            <div className="flex justify-between items-center mb-4">
              <h4 className="text-lg font-semibold">Employees</h4>
              <button
                onClick={() => setShowEmployeesModal(false)}
                className="text-slate-500"
              >
                Close
              </button>
            </div>
            <div className="space-y-2 max-h-64 overflow-auto">
              {employees && employees.length > 0 ? (
                employees.map((emp) => (
                  <div
                    key={emp.emp_id}
                    className="p-2 border rounded flex items-center justify-between"
                  >
                    <div>
                      <div className="font-medium">{emp.emp_name}</div>
                      <div className="text-xs text-slate-500">
                        ID: {emp.emp_id}
                      </div>
                    </div>
                    <div>
                      <button
                        onClick={() => {
                          setSelectedEmployeeId(emp.emp_id);
                          setShowEmployeesModal(false);
                        }}
                        className="px-2 py-1 text-sm bg-slate-100 rounded"
                      >
                        Filter
                      </button>
                    </div>
                  </div>
                ))
              ) : (
                <p className="text-sm text-slate-500">No employees available</p>
              )}
            </div>
            {selectedEmployeeId && (
              <div className="mt-4 text-right">
                <button
                  onClick={() => setSelectedEmployeeId(null)}
                  className="px-3 py-1 text-sm bg-red-50 text-red-600 rounded"
                >
                  Clear Employee Filter
                </button>
              </div>
            )}
          </div>
        </div>
      )}

      {/* MODALS */}
      {selectedTask && (
        <TaskDetailsModal
          task={selectedTask}
          assignedEmployee={employees.find(
            (e) => Number(e.emp_id) === Number(selectedTask.assigned_to)
          )}
          onClose={() => setSelectedTask(null)}
          onUpdate={async () => {
            toast.success("Task updated successfully");
            if (onTasksChanged) onTasksChanged();
            else await fetchTasks(true);
          }}
        />
      )}

      {(editingTask || showCreateModal) && (
        <TaskModal
          task={editingTask}
          onClose={() => {
            setEditingTask(null);
            setShowCreateModal(false);
          }}
          onSuccess={async () => {
            setEditingTask(null);
            setShowCreateModal(false);
            // Let parent reload filtered lists (so stats update). If not provided, refresh locally.
            if (onTasksChanged) onTasksChanged();
            else await fetchTasks(true);
          }}
        />
      )}
    </div>
  );
};

export default KanbanBoard;
