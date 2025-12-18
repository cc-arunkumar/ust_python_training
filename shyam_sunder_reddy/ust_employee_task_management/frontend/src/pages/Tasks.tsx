import { useEffect, useState } from "react";
import { useAuth } from "../context/AuthContext";
import { taskAPI } from "../services/api";
import { Plus, Search } from "lucide-react";
import { remarkAPI } from "../services/api";
import { useNavigate } from "react-router-dom";
import type { Task, User } from "../types";

// Card-level border + shadow based on priority (module-level so it can be used
// by the Tasks component and nested TaskColumn renderer)
const getCardPriorityClass = (priority?: string) => {
  if (!priority) return "border border-gray-100 shadow-sm";
  switch (priority.toLowerCase()) {
    case "high":
      // stronger red border and shadow
      return "border border-red-300 shadow-md hover:shadow-lg";
    case "medium":
      // stronger yellow border and shadow
      return "border border-yellow-300 shadow-md hover:shadow-lg";
    case "low":
      return "border border-green-200 shadow-sm hover:shadow-md";
    default:
      return "border border-gray-100 shadow-sm";
  }
};
const Tasks = () => {
  const { activeRole, user } = useAuth();
  const navigate = useNavigate();
  const [tasks, setTasks] = useState<Task[]>([]);
  const [filteredTasks, setFilteredTasks] = useState<Task[]>([]);
  const [isLoading, setIsLoading] = useState(true);
  const [searchTerm, setSearchTerm] = useState("");
  const [statusFilter, setStatusFilter] = useState<string>("all");
  const [priorityFilter, setPriorityFilter] = useState<string>("all");
  const [showCreateModal, setShowCreateModal] = useState(false);
  const [draggedTask, setDraggedTask] = useState<Task | null>(null);

  useEffect(() => {
    const fetchTasks = async () => {
      if (!activeRole) return;

      try {
        const role = activeRole;
        const data = await taskAPI.getAll(role);
        setTasks(data);
        setFilteredTasks(data);
      } catch (error) {
        console.error("Error fetching tasks:", error);
      } finally {
        setIsLoading(false);
      }
    };

    fetchTasks();
  }, [activeRole]);

  useEffect(() => {
    const applyFilters = async () => {
      // If a specific status is selected, prefer the server-side endpoint
      // which can return role-aware results. Otherwise use the cached `tasks` list.
      try {
        let sourceTasks: Task[] = [];

        if (statusFilter !== "all") {
          if (!activeRole) return;
          // Call backend to get tasks filtered by status and role
          sourceTasks = await taskAPI.getByStatus(
            statusFilter,
            activeRole as string
          );
        } else {
          sourceTasks = tasks;
        }

        let filtered = sourceTasks;

        if (searchTerm) {
          filtered = filtered.filter(
            (task) =>
              task.title.toLowerCase().includes(searchTerm.toLowerCase()) ||
              task.description.toLowerCase().includes(searchTerm.toLowerCase())
          );
        }

        if (priorityFilter !== "all") {
          filtered = filtered.filter(
            (task) => task.priority.toLowerCase() === priorityFilter
          );
        }

        setFilteredTasks(filtered);
      } catch (error) {
        console.error("Error applying filters:", error);
        setFilteredTasks([]);
      }
    };

    applyFilters();
  }, [searchTerm, statusFilter, priorityFilter, tasks, activeRole]);

  // status colors removed — status pill is not shown on cards

  const getPriorityColor = (priority: string) => {
    switch (priority.toLowerCase()) {
      case "high":
        return "bg-red-100 text-red-800 border-red-200";
      case "medium":
        return "bg-yellow-100 text-yellow-800 border-yellow-200";
      case "low":
        return "bg-green-100 text-green-800 border-green-200";
      default:
        return "bg-gray-100 text-gray-800 border-gray-200";
    }
  };

  // Group tasks by status for Kanban-style board
  const normalizeStatus = (status?: string) => status || "TO_DO";
  const columns = {
    TO_DO: filteredTasks.filter((t) => normalizeStatus(t.status) === "TO_DO"),
    IN_PROGRESS: filteredTasks.filter(
      (t) => normalizeStatus(t.status) === "IN_PROGRESS"
    ),
    REVIEW: filteredTasks.filter((t) => normalizeStatus(t.status) === "REVIEW"),
    DONE: filteredTasks.filter((t) => normalizeStatus(t.status) === "DONE"),
  };

  const updateTaskInState = (updated: Task) => {
    setTasks((prev) =>
      prev.map((t) => (t.t_id === updated.t_id ? updated : t))
    );
    setFilteredTasks((prev) =>
      prev.map((t) => (t.t_id === updated.t_id ? updated : t))
    );
  };

  // Inline editor state
  const [editingTask, setEditingTask] = useState<Task | null>(null);

  const handlePriorityChange = async (task: Task, newPriority: string) => {
    if (!activeRole || !task.t_id) return;
    try {
      await taskAPI.patchPriority(task.t_id, newPriority, activeRole as string);
      updateTaskInState({ ...task, priority: newPriority as any });
    } catch (error) {
      console.error("Error updating priority:", error);
      alert("Failed to update priority");
    }
  };

  const handleStatusChange = async (task: Task, newStatus: string) => {
    if (!activeRole || !task.t_id) return;
    if (normalizeStatus(task.status) === newStatus) return;
    try {
      await taskAPI.patchStatus(task.t_id, newStatus, activeRole as string);
      updateTaskInState({ ...task, status: newStatus });
    } catch (error: any) {
      console.error("Error updating status:", error);
      const detail =
        error?.response?.data?.detail ||
        "You are not allowed to move this task to that status.";
      alert(detail);
    }
  };

  if (isLoading) {
    return (
      <div className="flex items-center justify-center h-64">
        <div className="animate-spin rounded-full h-12 w-12 border-t-2 border-b-2 border-primary-500"></div>
      </div>
    );
  }

  return (
    <div className="space-y-6 animate-fade-in">
      {/* Page header */}
      <div className="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-4">
        <div>
          <h1 className="text-3xl font-bold text-gray-800 mb-1">Task Board</h1>
          <p className="text-gray-600">
            Manage and track all tasks across the team
          </p>
        </div>
        <button
          onClick={() => setShowCreateModal(true)}
          className="btn-primary flex items-center gap-2"
        >
          <Plus size={20} />
          Create Task
        </button>
      </div>

      {/* Filters / search */}
      <div className="card">
        <div className="flex flex-col lg:flex-row lg:items-center gap-4">
          <div className="flex-1 relative">
            <Search
              className="absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-400"
              size={18}
            />
            <input
              type="text"
              placeholder="Search tasks..."
              value={searchTerm}
              onChange={(e) => setSearchTerm(e.target.value)}
              className="input-field pl-9 text-sm"
            />
          </div>
          <div className="flex flex-wrap gap-2">
            <select
              value={priorityFilter}
              onChange={(e) => setPriorityFilter(e.target.value)}
              className="input-field text-sm w-40"
            >
              <option value="all">All Priorities</option>
              <option value="high">High</option>
              <option value="medium">Medium</option>
              <option value="low">Low</option>
            </select>
            <select
              value={statusFilter}
              onChange={(e) => setStatusFilter(e.target.value)}
              className="input-field text-sm w-40"
            >
              <option value="all">All Status</option>
              <option value="TO_DO">To Do</option>
              <option value="IN_PROGRESS">In Progress</option>
              <option value="REVIEW">Review</option>
              <option value="DONE">Done</option>
            </select>
          </div>
        </div>
      </div>

      {/* Kanban columns */}
      <div className="grid grid-cols-1 lg:grid-cols-4 gap-4 lg:gap-6">
        {/* To Do */}
        <TaskColumn
          title="To Do"
          count={columns.TO_DO.length}
          statusValue="TO_DO"
          bgColor="bg-blue-50"
          dotColor="bg-blue-500"
          tasks={columns.TO_DO}
          navigate={navigate}
          getPriorityColor={getPriorityColor}
          onPriorityChange={handlePriorityChange}
          onStatusChange={handleStatusChange}
          draggedTask={draggedTask}
          setDraggedTask={setDraggedTask}
          onEditClick={(t: Task) => setEditingTask(t)}
        />

        {/* In Progress */}
        <TaskColumn
          title="In Progress"
          count={columns.IN_PROGRESS.length}
          statusValue="IN_PROGRESS"
          bgColor="bg-yellow-50"
          dotColor="bg-yellow-500"
          tasks={columns.IN_PROGRESS}
          navigate={navigate}
          getPriorityColor={getPriorityColor}
          onPriorityChange={handlePriorityChange}
          onStatusChange={handleStatusChange}
          draggedTask={draggedTask}
          setDraggedTask={setDraggedTask}
          onEditClick={(t: Task) => setEditingTask(t)}
        />

        {/* Review */}
        <TaskColumn
          title="Review"
          count={columns.REVIEW.length}
          statusValue="REVIEW"
          bgColor="bg-indigo-50"
          dotColor="bg-indigo-500"
          tasks={columns.REVIEW}
          navigate={navigate}
          getPriorityColor={getPriorityColor}
          onPriorityChange={handlePriorityChange}
          onStatusChange={handleStatusChange}
          draggedTask={draggedTask}
          setDraggedTask={setDraggedTask}
          onEditClick={(t: Task) => setEditingTask(t)}
        />

        {/* Done */}
        <TaskColumn
          title="Done"
          count={columns.DONE.length}
          statusValue="DONE"
          bgColor="bg-green-50"
          dotColor="bg-green-500"
          tasks={columns.DONE}
          navigate={navigate}
          getPriorityColor={getPriorityColor}
          onPriorityChange={handlePriorityChange}
          onStatusChange={handleStatusChange}
          draggedTask={draggedTask}
          setDraggedTask={setDraggedTask}
          onEditClick={(t: Task) => setEditingTask(t)}
        />
      </div>

      {/* Inline edit panel (appears when a task is selected) */}
      {editingTask && (
        <EditTaskInline
          task={editingTask}
          onClose={() => setEditingTask(null)}
          onSaved={(updated) => {
            updateTaskInState(updated);
            setEditingTask(null);
          }}
          activeRole={activeRole}
          user={user}
        />
      )}

      {showCreateModal && (
        <CreateTaskModal
          onClose={() => setShowCreateModal(false)}
          onSuccess={() => {
            setShowCreateModal(false);
            window.location.reload();
          }}
        />
      )}
    </div>
  );
};

interface TaskColumnProps {
  title: string;
  count: number;
  statusValue: string;
  bgColor: string;
  dotColor: string;
  tasks: Task[];
  navigate: ReturnType<typeof useNavigate>;
  getPriorityColor: (priority: string) => string;
  onPriorityChange: (task: Task, newPriority: string) => void;
  onStatusChange: (task: Task, newStatus: string) => void;
  draggedTask: Task | null;
  setDraggedTask: (task: Task | null) => void;
  onEditClick?: (task: Task) => void;
}

const TaskColumn = ({
  title,
  count,
  statusValue,
  bgColor,
  dotColor,
  tasks,
  navigate,
  getPriorityColor,
  onPriorityChange,
  onStatusChange,
  draggedTask,
  setDraggedTask,
  onEditClick,
}: TaskColumnProps) => {
  return (
    <div
      className={`flex flex-col rounded-2xl border border-gray-100 ${bgColor} p-3 sm:p-4 min-h-[260px]`}
      onDragOver={(e) => {
        if (draggedTask) {
          e.preventDefault();
        }
      }}
      onDrop={(e) => {
        e.preventDefault();
        if (draggedTask) {
          onStatusChange(draggedTask, statusValue);
          setDraggedTask(null);
        }
      }}
    >
      {/* Column header */}
      <div className="flex items-center justify-between mb-3">
        <div className="flex items-center gap-2">
          <span className={`w-2 h-2 rounded-full ${dotColor}`} />
          <h2 className="text-sm font-semibold text-gray-800">{title}</h2>
          <span className="text-xs px-2 py-0.5 rounded-full bg-white text-gray-600 border border-gray-200">
            {count}
          </span>
        </div>
      </div>

      {/* Cards */}
      <div className="space-y-3 flex-1">
        {tasks.length === 0 ? (
          <div className="flex items-center justify-center h-32 text-xs text-gray-400">
            No tasks
          </div>
        ) : (
          tasks.map((task) => (
            <button
              key={task.t_id}
              onClick={() =>
                onEditClick
                  ? onEditClick(task)
                  : navigate(`/tasks/${task.t_id}`)
              }
              className={`w-full text-left bg-white rounded-xl ${getCardPriorityClass(
                task.priority
              )} px-3 py-3 hover:border-primary-200 transition-all duration-200 overflow-hidden`}
              draggable
              onDragStart={() => setDraggedTask(task)}
              onDragEnd={() => setDraggedTask(null)}
            >
              <div className="flex items-start justify-between mb-2 gap-2 min-w-0">
                <div className="flex-1">
                  <p className="text-xs text-gray-400 mb-0.5">
                    #{task.t_id ?? ""}
                  </p>
                  <h3 className="text-sm font-semibold text-gray-800 line-clamp-2">
                    {task.title}
                  </h3>
                </div>
                <div className="flex flex-col items-end gap-1">
                  <div className="flex flex-col items-end gap-1">
                    {/* status pill removed as requested */}
                    <button
                      className={`inline-flex items-center whitespace-nowrap px-2 py-0.5 rounded-full text-[11px] font-medium border ${getPriorityColor(
                        task.priority
                      )}`}
                      onClick={(e) => {
                        e.stopPropagation();
                        const next =
                          task.priority === "high"
                            ? "medium"
                            : task.priority === "medium"
                            ? "low"
                            : "high";
                        onPriorityChange(task, next);
                      }}
                      title="Click to change priority"
                    >
                      {task.priority}
                    </button>
                  </div>
                </div>
              </div>

              <p className="text-xs text-gray-500 mb-3 line-clamp-2">
                {task.description}
              </p>

              <div className="flex items-center justify-between text-[11px] text-gray-400">
                <div className="flex items-center gap-3">
                  {task.expected_closure && (
                    <span>
                      {new Date(task.expected_closure).toLocaleDateString()}
                    </span>
                  )}
                  {task.assigned_to && (
                    <span>Assignee: {task.assigned_to}</span>
                  )}
                </div>
              </div>
            </button>
          ))
        )}
      </div>
    </div>
  );
};

const CreateTaskModal: React.FC<{
  onClose: () => void;
  onSuccess: () => void;
}> = ({ onClose, onSuccess }) => {
  const { user, activeRole } = useAuth();
  const [formData, setFormData] = useState({
    title: "",
    description: "",
    assigned_to: "",
    priority: "medium",
    status: "TO_DO",
    reviewer: "",
    expected_closure: "",
  });
  const [isSubmitting, setIsSubmitting] = useState(false);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!user && !activeRole) return;

    setIsSubmitting(true);
    try {
      // Use Manager role when the user has it, even if it's not the first role in the array
      const roleToUse = user?.role?.includes("Manager")
        ? "Manager"
        : activeRole || user?.role?.[0] || "Developer";
      await taskAPI.create(roleToUse, {
        ...formData,
        assigned_to: formData.assigned_to
          ? parseInt(formData.assigned_to)
          : undefined,
        reviewer: formData.reviewer ? parseInt(formData.reviewer) : undefined,
        expected_closure: new Date(formData.expected_closure).toISOString(),
      } as any);
      onSuccess();
    } catch (error) {
      console.error("Error creating task:", error);
      alert("Failed to create task. Please try again.");
    } finally {
      setIsSubmitting(false);
    }
  };

  return (
    <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50 p-4 animate-fade-in">
      <div className="bg-white rounded-xl shadow-xl max-w-2xl w-full max-h-[90vh] overflow-y-auto animate-scale-in">
        <div className="p-6 border-b border-gray-200">
          <h2 className="text-2xl font-bold text-gray-800">Create New Task</h2>
        </div>
        <form onSubmit={handleSubmit} className="p-6 space-y-4">
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-2">
              Title *
            </label>
            <input
              type="text"
              required
              value={formData.title}
              onChange={(e) =>
                setFormData({ ...formData, title: e.target.value })
              }
              className="input-field"
            />
          </div>
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-2">
              Description *
            </label>
            <textarea
              required
              value={formData.description}
              onChange={(e) =>
                setFormData({ ...formData, description: e.target.value })
              }
              className="input-field"
              rows={4}
            />
          </div>
          <div className="grid grid-cols-2 gap-4">
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-2">
                Assigned To
              </label>
              <input
                type="number"
                value={formData.assigned_to}
                onChange={(e) =>
                  setFormData({ ...formData, assigned_to: e.target.value })
                }
                className="input-field"
                placeholder="Employee ID"
              />
            </div>
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-2">
                Reviewer
              </label>
              <input
                type="number"
                value={formData.reviewer}
                onChange={(e) =>
                  setFormData({ ...formData, reviewer: e.target.value })
                }
                className="input-field"
                placeholder="Employee ID"
              />
            </div>
          </div>
          <div className="grid grid-cols-2 gap-4">
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-2">
                Priority *
              </label>
              <select
                required
                value={formData.priority}
                onChange={(e) =>
                  setFormData({ ...formData, priority: e.target.value })
                }
                className="input-field"
              >
                <option value="low">Low</option>
                <option value="medium">Medium</option>
                <option value="high">High</option>
              </select>
            </div>
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-2">
                Expected Closure *
              </label>
              <input
                type="datetime-local"
                required
                value={formData.expected_closure}
                onChange={(e) =>
                  setFormData({ ...formData, expected_closure: e.target.value })
                }
                className="input-field"
              />
            </div>
          </div>
          <div className="flex gap-3 pt-4">
            <button
              type="submit"
              className="btn-primary flex-1"
              disabled={isSubmitting}
            >
              {isSubmitting ? "Creating..." : "Create Task"}
            </button>
            <button type="button" onClick={onClose} className="btn-secondary">
              Cancel
            </button>
          </div>
        </form>
      </div>
    </div>
  );
};

const EditTaskInline: React.FC<{
  task: Task;
  onClose: () => void;
  onSaved: (updated: Task) => void;
  activeRole: string | null;
  user: User | null;
}> = ({ task, onClose, onSaved, activeRole, user }) => {
  const [formData, setFormData] = useState<{
    title: string;
    description: string;
    assigned_to: string;
    reviewer: string;
    priority: Task["priority"];
    status: string;
    expected_closure: string;
  }>({
    title: task.title || "",
    description: task.description || "",
    assigned_to: task.assigned_to ? String(task.assigned_to) : "",
    reviewer: task.reviewer ? String(task.reviewer) : "",
    priority: (task.priority as Task["priority"]) || "medium",
    status: task.status || "TO_DO",
    expected_closure: task.expected_closure
      ? new Date(task.expected_closure).toISOString().slice(0, 16)
      : "",
  });
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [remarkText, setRemarkText] = useState("");
  const [remarkFile, setRemarkFile] = useState<File | null>(null);
  const [isAddingRemark, setIsAddingRemark] = useState(false);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!task.t_id) return;
    setIsSubmitting(true);
    try {
      const roleToUse = user?.role?.includes("Manager")
        ? "Manager"
        : activeRole || user?.role?.[0] || "";

      const updates: any = {
        title: formData.title,
        description: formData.description,
        assigned_to: formData.assigned_to
          ? parseInt(formData.assigned_to)
          : undefined,
        reviewer: formData.reviewer ? parseInt(formData.reviewer) : undefined,
        priority: formData.priority,
        status: formData.status,
      };
      if (formData.expected_closure) {
        updates.expected_closure = new Date(
          formData.expected_closure
        ).toISOString();
      }

      const resp = await taskAPI.update(task.t_id, roleToUse, updates as any);
      // backend responds with { detail, task }
      const updatedTask: Task = resp?.task
        ? resp.task
        : { ...task, ...updates };
      onSaved(updatedTask);
    } catch (err) {
      console.error("Failed to update task:", err);
      alert("Failed to update task. See console for details.");
    } finally {
      setIsSubmitting(false);
    }
  };

  const handleAddRemark = async () => {
    if (!task.t_id) return;
    if (!remarkText && !remarkFile) {
      alert("Please enter a comment or attach a file for the remark.");
      return;
    }
    setIsAddingRemark(true);
    try {
      const roleToUse = user?.role?.includes("Manager")
        ? "Manager"
        : activeRole || user?.role?.[0] || "";
      await remarkAPI.create(
        task.t_id,
        remarkText,
        roleToUse,
        remarkFile || undefined
      );
      setRemarkText("");
      setRemarkFile(null);
      alert("Remark added.");
    } catch (err) {
      console.error("Failed to add remark:", err);
      alert("Failed to add remark. See console for details.");
    } finally {
      setIsAddingRemark(false);
    }
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/30">
  <div className="bg-white w-full max-w-md rounded-lg shadow-md border border-gray-200 flex flex-col max-h-[90vh]">

    {/* Header */}
    <div className="flex items-center justify-between px-3 py-2 border-b">
      <h3 className="text-sm font-semibold">
        Edit Task {task.t_id}
      </h3>
      {/* <button onClick={onClose} className="text-xs text-gray-500">
        Close
      </button> */}
    </div>

    {/* Scrollable Body */}
    <form
      onSubmit={handleSubmit}
      className="flex-1 overflow-y-auto px-3 py-2 space-y-2 text-xs"
    >
      <div>
        <label className="block font-medium text-gray-600 mb-0.5">
          Title
        </label>
        <input
          value={formData.title}
          onChange={(e) =>
            setFormData({ ...formData, title: e.target.value })
          }
          className="input-field h-8 px-2 py-1 text-xs"
        />
      </div>

      <div>
        <label className="block font-medium text-gray-600 mb-0.5">
          Description
        </label>
        <textarea
          value={formData.description}
          onChange={(e) =>
            setFormData({ ...formData, description: e.target.value })
          }
          className="input-field px-2 py-1 text-xs"
          rows={3}
        />
      </div>

      <div className="grid grid-cols-4 gap-1.5">
        <div>
          <label className="block text-xs font-medium text-gray-600 mb-0.5">
            Assigned To
          </label>
          <input
            value={formData.assigned_to}
            onChange={(e) =>
              setFormData({ ...formData, assigned_to: e.target.value })
            }
            className="input-field h-8 px-2 py-1 text-xs"
            type="number"
          />
        </div>

        <div>
          <label className="block text-xs font-medium text-gray-600 mb-0.5">
            Reviewer
          </label>
          <input
            value={formData.reviewer}
            onChange={(e) =>
              setFormData({ ...formData, reviewer: e.target.value })
            }
            className="input-field h-8 px-2 py-1 text-xs"
            type="number"
          />
        </div>

        <div>
          <label className="block text-xs font-medium text-gray-600 mb-0.5">
            Priority
          </label>
          <select
            value={formData.priority}
            onChange={(e) =>
              setFormData({
                ...formData,
                priority: e.target.value as Task["priority"],
              })
            }
            className="input-field h-8 px-2 py-1 text-xs"
          >
            <option value="low">Low</option>
            <option value="medium">Medium</option>
            <option value="high">High</option>
          </select>
        </div>

        <div>
          <label className="block text-xs font-medium text-gray-600 mb-0.5">
            Status
          </label>
          <select
            value={formData.status}
            onChange={(e) =>
              setFormData({ ...formData, status: e.target.value })
            }
            className="input-field h-8 px-2 py-1 text-xs"
          >
            <option value="TO_DO">To Do</option>
            <option value="IN_PROGRESS">In Progress</option>
            <option value="REVIEW">Review</option>
            <option value="DONE">Done</option>
          </select>
        </div>
      </div>

      <div>
        <label className="block font-medium text-gray-600 mb-0.5">
          Expected Closure
        </label>
        <input
          value={formData.expected_closure}
          onChange={(e) =>
            setFormData({ ...formData, expected_closure: e.target.value })
          }
          className="input-field h-8 px-2 py-1 text-xs"
          type="datetime-local"
        />
      </div>

      {/* Remarks */}
      <div className="pt-1">
        <label className="block font-medium text-gray-600 mb-0.5">
          Add Remark
        </label>
        <textarea
          placeholder="Add a comment or note"
          value={remarkText}
          onChange={(e) => setRemarkText(e.target.value)}
          className="input-field px-2 py-1 text-xs mb-1"
          rows={2}
        />
        <input
          type="file"
          onChange={(e) =>
            setRemarkFile(e.target.files ? e.target.files[0] : null)
          }
          className="text-xs mb-1"
        />
        <div className="flex gap-1.5">
          <button
            type="button"
            onClick={handleAddRemark}
            className="btn-primary text-xs px-2 py-1 h-7"
            disabled={isAddingRemark}
          >
            {isAddingRemark ? "Adding..." : "Add"}
          </button>
          <button
            type="button"
            onClick={() => {
              setRemarkText("");
              setRemarkFile(null);
            }}
            className="btn-secondary text-xs px-2 py-1 h-7"
          >
            Clear
          </button>
        </div>
      </div>

      {/* Footer buttons */}
      <div className="flex gap-2 pt-2">
        <button
          type="submit"
          className="btn-primary flex-1 text-xs h-8"
          disabled={isSubmitting}
        >
          {isSubmitting ? "Saving..." : "Save"}
        </button>
        <button
          type="button"
          onClick={onClose}
          className="btn-secondary text-xs h-8"
        >
          Cancel
        </button>
      </div>
    </form>
  </div>
</div>

  );
};

export default Tasks;
