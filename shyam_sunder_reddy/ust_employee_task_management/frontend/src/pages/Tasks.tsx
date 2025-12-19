import { useEffect, useState } from "react";
import { useAuth } from "../context/AuthContext";
import { taskAPI } from "../services/api";
import {
  Plus,
  Search,
  X as XIcon,
  MessageSquare,
  Eye,
  User as UserIcon,
  Edit as EditIcon,
} from "lucide-react";
import api, { employeeAPI, userAPI, remarkAPI } from "../services/api";
import { useNavigate } from "react-router-dom";
import type { Task, User } from "../types";

// Card-level border + shadow based on priority (module-level so it can be used
// by the Tasks component and nested TaskColumn renderer)
const getCardPriorityClass = (priority?: string) => {
  if (!priority) return "border border-gray-100 shadow-sm";
  switch (priority.toLowerCase()) {
    case "high":
      // stronger red border and shadow
      return "border border-red-300 bg-red-50 shadow-md hover:shadow-lg";
    case "medium":
      // stronger yellow border and shadow
      return "border border-yellow-300 bg-yellow-50 shadow-md hover:shadow-lg";
    case "low":
      return "border border-green-200 bg-green-50 shadow-sm hover:shadow-md";
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
  // sort tasks by priority: high -> medium -> low
  const priorityRank: Record<string, number> = {
    high: 0,
    medium: 1,
    low: 2,
  };

  const sortByPriority = (arr: Task[]) =>
    arr.slice().sort((a, b) => {
      const pa = (a.priority || "").toLowerCase();
      const pb = (b.priority || "").toLowerCase();
      const ra = priorityRank[pa] ?? 99;
      const rb = priorityRank[pb] ?? 99;
      if (ra !== rb) return ra - rb;
      // fallback: newer tasks first if created/updated timestamps exist
      if ((a as any).updated_at && (b as any).updated_at) {
        return (
          new Date((b as any).updated_at).getTime() -
          new Date((a as any).updated_at).getTime()
        );
      }
      return 0;
    });

  const columns = {
    TO_DO: sortByPriority(
      filteredTasks.filter((t) => normalizeStatus(t.status) === "TO_DO")
    ),
    IN_PROGRESS: sortByPriority(
      filteredTasks.filter((t) => normalizeStatus(t.status) === "IN_PROGRESS")
    ),
    REVIEW: sortByPriority(
      filteredTasks.filter((t) => normalizeStatus(t.status) === "REVIEW")
    ),
    DONE: sortByPriority(
      filteredTasks.filter((t) => normalizeStatus(t.status) === "DONE")
    ),
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
  // Remark modal state
  const [showRemarkModal, setShowRemarkModal] = useState(false);
  const [remarkTask, setRemarkTask] = useState<Task | null>(null);
  // Task detail modal state
  const [showDetailModal, setShowDetailModal] = useState(false);
  const [detailTask, setDetailTask] = useState<Task | null>(null);
  // Used to force reload of remarks inside TaskDetailModal when a remark is added
  const [remarksReloadKey, setRemarksReloadKey] = useState(0);

  const handlePriorityChange = async (task: Task, newPriority: string) => {
    if (!activeRole || !task.t_id) return;
    // Developers are not permitted to change priority
    if (activeRole === "Developer") {
      alert("You are not authorized to change task priority.");
      return;
    }
    try {
      await taskAPI.patchPriority(task.t_id, newPriority, activeRole as string);
      updateTaskInState({ ...task, priority: newPriority as any });
    } catch (error) {
      console.error("Error updating priority:", error);
      alert("Failed to update priority");
    }
  };

  const handleAddRemark = async (task: Task) => {
    if (!task.t_id) return;
    // Only allow when task is IN_PROGRESS or REVIEW
    const status = normalizeStatus(task.status);
    if (!(status === "IN_PROGRESS" || status === "REVIEW")) {
      alert("Remarks can only be added when task is In Progress or in Review.");
      return;
    }
    // Determine required role for this status
    const requiredRole = status === "IN_PROGRESS" ? "Developer" : "Manager";

    // Disallow Admin from adding remarks explicitly in the UI
    const userRoles: any = user?.role || [];
    const hasRequired = Array.isArray(userRoles)
      ? userRoles.includes(requiredRole)
      : String(userRoles).includes(requiredRole);
    const isAdmin = Array.isArray(userRoles)
      ? userRoles.includes("Admin")
      : String(userRoles).includes("Admin");

    if (!hasRequired || isAdmin) {
      // If the activeRole matches the requiredRole we can allow (covers role switch)
      if (activeRole !== requiredRole) {
        alert("You are not authorized to add remarks for this task.");
        return;
      }
    }

    // Open remark modal for in-place remark creation
    setRemarkTask(task);
    setShowRemarkModal(true);
  };

  const handleStatusChange = async (task: Task, newStatus: string) => {
    if (!activeRole || !task.t_id) return;
    if (normalizeStatus(task.status) === newStatus) return;
    // Developers have a limited ability to change status via drag/drop:
    // allow Developer to move their assigned task from IN_PROGRESS -> REVIEW.
    if (activeRole === "Developer") {
      const from = normalizeStatus(task.status);
      const to = newStatus;
      const allowedForDev =
        (from === "IN_PROGRESS" && to === "REVIEW") ||
        (from === "TO_DO" && to === "IN_PROGRESS");
      if (!allowedForDev) {
        alert("You are not authorized to change task status.");
        return;
      }
    }
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
          activeRole={activeRole}
          onAddRemark={handleAddRemark}
          onViewDetails={(t: Task) => {
            setDetailTask(t);
            setShowDetailModal(true);
          }}
          onCreateClick={() => setShowCreateModal(true)}
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
          activeRole={activeRole}
          onAddRemark={handleAddRemark}
          onViewDetails={(t: Task) => {
            setDetailTask(t);
            setShowDetailModal(true);
          }}
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
          activeRole={activeRole}
          onAddRemark={handleAddRemark}
          onViewDetails={(t: Task) => {
            setDetailTask(t);
            setShowDetailModal(true);
          }}
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
          activeRole={activeRole}
          onAddRemark={handleAddRemark}
          onViewDetails={(t: Task) => {
            setDetailTask(t);
            setShowDetailModal(true);
          }}
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

      {showRemarkModal && remarkTask && (
        <RemarkModal
          task={remarkTask}
          onClose={() => {
            setShowRemarkModal(false);
            setRemarkTask(null);
          }}
          onSuccess={() => {
            setShowRemarkModal(false);
            setRemarkTask(null);
            // bump reload key so TaskDetailModal (if open) refreshes remarks
            setRemarksReloadKey((k) => k + 1);
            // small feedback
            alert("Remark added.");
          }}
          user={user}
          activeRole={activeRole}
        />
      )}
      {showDetailModal && detailTask && (
        <TaskDetailModal
          task={detailTask}
          onClose={() => {
            setShowDetailModal(false);
            setDetailTask(null);
          }}
          activeRole={activeRole}
          user={user}
          reloadKey={remarksReloadKey}
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
  onAddRemark?: (task: Task) => void;
  onViewDetails?: (task: Task) => void;
  onCreateClick?: () => void;
  draggedTask: Task | null;
  setDraggedTask: (task: Task | null) => void;
  onEditClick?: (task: Task) => void;
  activeRole?: string | null;
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
  onAddRemark,
  onViewDetails,
  activeRole,
  onCreateClick,
}: TaskColumnProps) => {
  const [employeeDetails, setEmployeeDetails] = useState<Record<number, any>>(
    {}
  );
  const [showEmployeeFor, setShowEmployeeFor] = useState<number | null>(null);
  const [showEmployeeRole, setShowEmployeeRole] = useState<string | null>(null);

  const handleAssigneeClick = async (
    e: React.MouseEvent,
    assigneeId?: number,
    roleType?: "Assignee" | "Reviewer"
  ) => {
    e.stopPropagation();
    if (!assigneeId) return;
    // toggle if already shown
    if (showEmployeeFor === assigneeId) {
      setShowEmployeeFor(null);
      setShowEmployeeRole(null);
      return;
    }
    // if we already fetched, just show and set the role label
    if (employeeDetails[assigneeId]) {
      setShowEmployeeFor(assigneeId);
      setShowEmployeeRole(roleType || null);
      return;
    }
    try {
      const roleToUse = activeRole || "";
      const emp = await employeeAPI.getById(assigneeId, roleToUse);
      setEmployeeDetails((prev) => ({ ...prev, [assigneeId]: emp }));
      setShowEmployeeFor(assigneeId);
      setShowEmployeeRole(roleType || null);
    } catch (err) {
      console.error("Error fetching employee:", err);
      alert("Failed to load employee details");
    }
  };
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
          {onCreateClick && (
            <button
              onClick={(e) => {
                e.stopPropagation();
                onCreateClick();
              }}
              title="Create task"
              className="p-1 rounded text-primary-600 hover:bg-primary-100"
            >
              <Plus size={14} />
            </button>
          )}
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
          tasks.map((task) => {
            // compute days remaining for expected_closure
            const remainingDays = task.expected_closure
              ? Math.ceil(
                  (new Date(task.expected_closure).getTime() - Date.now()) /
                    (1000 * 60 * 60 * 24)
                )
              : null;

            const dueText =
              remainingDays === null
                ? "-"
                : remainingDays < 0
                ? `Overdue: ${Math.abs(remainingDays)}d`
                : remainingDays === 0
                ? `Due today`
                : `Due in ${remainingDays}d`;

            // Make tasks that are due in 1 day much more prominent:
            // stronger red border, slightly darker background, red text, shadow and a subtle pop animation
            // Urgent: due in 1 day OR already overdue -> make card pop
            const isUrgent =
              remainingDays !== null &&
              (remainingDays <= 2 || remainingDays < 0);
            const urgencyClass = isUrgent
              ? "border-2 border-red-500 bg-red-300 text-red-800 shadow-lg transform scale-105 animate-pulse"
              : "";

            return (
              <button
                key={task.t_id}
                onClick={() =>
                  onViewDetails
                    ? onViewDetails(task)
                    : navigate(`/tasks/${task.t_id}`)
                }
                className={`w-full text-left rounded-xl ${getCardPriorityClass(
                  task.priority
                )} ${urgencyClass} px-3 py-3 hover:border-primary-200 transition-all duration-200 overflow-hidden`}
                draggable
                onDragStart={() => setDraggedTask(task)}
                onDragEnd={() => setDraggedTask(null)}
              >
                {/* Top row: task id, eye (details), remark, priority */}
                <div className="flex items-center gap-2 mb-2">
                  <p className="text-xs text-gray-400 mb-0.5 flex-shrink-0">
                    #{task.t_id ?? ""}
                  </p>

                  <button
                    onClick={(e) => {
                      e.stopPropagation();
                      onViewDetails && onViewDetails(task);
                    }}
                    className="p-1 rounded-full text-gray-500 hover:bg-gray-100 transition-colors flex-shrink-0"
                    title="View task details & remarks"
                  >
                    <Eye size={14} />
                  </button>

                  <button
                    onClick={(e) => {
                      e.stopPropagation();
                      onAddRemark && onAddRemark(task);
                    }}
                    className={`p-1 rounded-full text-gray-500 hover:bg-gray-100 transition-colors flex-shrink-0 ${
                      (task.status || "TO_DO") === "IN_PROGRESS" ||
                      (task.status || "TO_DO") === "REVIEW"
                        ? "cursor-pointer"
                        : "opacity-40 pointer-events-none"
                    }`}
                    title={
                      (task.status || "TO_DO") === "IN_PROGRESS" ||
                      (task.status || "TO_DO") === "REVIEW"
                        ? "Add remark"
                        : "Remarks disabled for this status"
                    }
                  >
                    <MessageSquare size={14} />
                  </button>

                  <button
                    className={`inline-flex items-center whitespace-nowrap px-2 py-0.5 rounded-full text-[11px] font-medium border ${getPriorityColor(
                      task.priority
                    )} max-w-[72px] truncate overflow-hidden ml-1 flex-shrink-0`}
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
                    disabled={activeRole === "Developer"}
                    title="Click to change priority"
                  >
                    {task.priority}
                  </button>
                </div>

                <h3 className="text-sm font-semibold text-gray-800 line-clamp-2 mb-1">
                  {task.title}
                </h3>

                <p className="text-xs text-gray-500 mb-3 line-clamp-2">
                  {task.description}
                </p>

                <div className="flex items-center justify-between text-[11px] text-gray-400">
                  <div className="flex items-center gap-3">
                    {task.expected_closure && <span>{dueText}</span>}
                  </div>

                  <div className="flex items-center gap-2 relative">
                    {/* Assignee icon: click to fetch and show employee details inline */}
                    {task.assigned_to ? (
                      <button
                        onClick={(e) =>
                          handleAssigneeClick(e, task.assigned_to, "Assignee")
                        }
                        title={`Assignee: ${task.assigned_to}`}
                        className="p-1 rounded-md text-gray-500 hover:bg-gray-100 transition-colors"
                      >
                        <UserIcon size={14} />
                      </button>
                    ) : (
                      <div className="text-gray-300 text-[11px]">—</div>
                    )}

                    {/* Reviewer icon: click to view reviewer employee details */}
                    {task.reviewer ? (
                      <button
                        onClick={(e) =>
                          handleAssigneeClick(e, task.reviewer, "Reviewer")
                        }
                        title={`Reviewer: ${task.reviewer}`}
                        className="p-1 rounded-md text-gray-500 hover:bg-gray-100 transition-colors"
                      >
                        <UserIcon size={14} />
                      </button>
                    ) : null}

                    {/* Inline edit icon: open inline editor when allowed (not for Developers) */}
                    {activeRole !== "Developer" ? (
                      <button
                        onClick={(e) => {
                          e.stopPropagation();
                          onEditClick && onEditClick(task);
                        }}
                        title="Edit task inline"
                        className="p-1 rounded-md text-gray-500 hover:bg-gray-100 transition-colors"
                      >
                        <EditIcon size={14} />
                      </button>
                    ) : (
                      <div
                        title="You are not authorized to edit tasks"
                        className="p-1 rounded-md text-gray-300"
                      >
                        <EditIcon size={14} />
                      </div>
                    )}

                    {/* (Popup moved out) */}
                  </div>
                </div>
              </button>
            );
          })
        )}
      </div>

      {/* Employee detail modal popup (renders once per column) */}
      {showEmployeeFor !== null && (
        <div className="fixed inset-0 z-50 flex items-center justify-center p-4">
          <div
            className="absolute inset-0 bg-black/30"
            onClick={() => setShowEmployeeFor(null)}
          />
          <div
            className="relative z-10 bg-white rounded-lg shadow-xl w-full max-w-sm p-4 animate-scale-in"
            onClick={(e) => e.stopPropagation()}
          >
            <div className="flex items-center justify-between">
              <div>
                <p className="text-sm font-medium text-gray-800">
                  {showEmployeeRole
                    ? `${showEmployeeRole} — Employee ${showEmployeeFor}`
                    : `Employee ${showEmployeeFor}`}
                </p>
                <p className="text-xs text-gray-500">Profile</p>
              </div>
              <button
                onClick={() => setShowEmployeeFor(null)}
                className="text-gray-400 hover:text-gray-600 ml-2"
                title="Close"
              >
                <XIcon size={16} />
              </button>
            </div>
            <div className="mt-3 text-sm text-gray-700">
              {employeeDetails[showEmployeeFor as number] ? (
                <div className="space-y-1">
                  <div className="text-sm font-semibold">
                    {(employeeDetails[showEmployeeFor as number] as any).name}
                  </div>
                  <div className="text-xs text-gray-500">
                    {
                      (employeeDetails[showEmployeeFor as number] as any)
                        .designation
                    }
                  </div>
                  <div className="text-xs text-gray-500">
                    {(employeeDetails[showEmployeeFor as number] as any).email}
                  </div>
                  <div className="text-xs text-gray-500">
                    Manager ID:{" "}
                    {(employeeDetails[showEmployeeFor as number] as any)
                      .mgr_id ?? "-"}
                  </div>
                </div>
              ) : (
                <div className="text-xs text-gray-500">Loading...</div>
              )}
            </div>
          </div>
        </div>
      )}
    </div>
  );
};

const CreateTaskModal: React.FC<{
  onClose: () => void;
  onSuccess: () => void;
}> = ({ onClose, onSuccess }) => {
  const { user, activeRole } = useAuth();
  const [employees, setEmployees] = useState<
    {
      e_id?: number;
      name?: string;
    }[]
  >([]);

  const [managers, setManagers] = useState<
    {
      e_id?: number;
      name?: string;
    }[]
  >([]);

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

  useEffect(() => {
    let mounted = true;
    // fetch users for Assigned To and Reviewer via userAPI, then resolve names
    (async () => {
      try {
        let devUsers = await userAPI.getByRole("Developer");
        if (!mounted) return;
        // If backend route didn't return developers, fall back to fetching all users
        // and filtering client-side (handles cases where roles are stored as JSON strings)
        if (!devUsers || devUsers.length === 0) {
          try {
            const all = await userAPI.getAll("");
            if (!mounted) return;
            const roleIncludes = (r: any, target: string) => {
              if (Array.isArray(r)) return r.includes(target);
              if (typeof r === "string") {
                const trimmed = r.trim();
                if (trimmed.startsWith("[") && trimmed.endsWith("]")) {
                  try {
                    const parsed = JSON.parse(trimmed);
                    return Array.isArray(parsed) && parsed.includes(target);
                  } catch (_e) {
                    return trimmed.includes(target);
                  }
                }
                return trimmed.includes(target);
              }
              return false;
            };
            devUsers = all.filter((u: any) =>
              roleIncludes((u as any).role, "Developer")
            );
          } catch (_e) {
            /* ignore fallback errors */
          }
        }
        // resolve names from Employee table when available
        const devs = await Promise.all(
          devUsers.map(async (u) => {
            try {
              const emp = await employeeAPI.getById(u.e_id, "Developer");
              return { e_id: u.e_id, name: emp?.name };
            } catch (_e) {
              return { e_id: u.e_id, name: undefined };
            }
          })
        );
        if (!mounted) return;
        setEmployees(devs || []);

        let mgrUsers = await userAPI.getByRole("Manager");
        if (!mounted) return;
        if (!mgrUsers || mgrUsers.length === 0) {
          try {
            const all = await userAPI.getAll("");
            if (!mounted) return;
            const roleIncludes = (r: any, target: string) => {
              if (Array.isArray(r)) return r.includes(target);
              if (typeof r === "string") {
                const trimmed = r.trim();
                if (trimmed.startsWith("[") && trimmed.endsWith("]")) {
                  try {
                    const parsed = JSON.parse(trimmed);
                    return Array.isArray(parsed) && parsed.includes(target);
                  } catch (_e) {
                    return trimmed.includes(target);
                  }
                }
                return trimmed.includes(target);
              }
              return false;
            };
            mgrUsers = all.filter((u: any) =>
              roleIncludes((u as any).role, "Manager")
            );
          } catch (_e) {
            /* ignore fallback errors */
          }
        }
        const mgrs = await Promise.all(
          mgrUsers.map(async (u) => {
            try {
              const emp = await employeeAPI.getById(u.e_id, "Manager");
              return { e_id: u.e_id, name: emp?.name };
            } catch (_e) {
              return { e_id: u.e_id, name: undefined };
            }
          })
        );
        if (!mounted) return;
        setManagers(mgrs || []);
      } catch (err) {
        console.debug("failed to load users for dropdowns:", err);
      }
    })();

    return () => {
      mounted = false;
    };
  }, []);

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4">
      <div
        className="absolute inset-0 bg-black/30 backdrop-blur-sm"
        onClick={onClose}
      />
      <div
        className="relative z-10 bg-white rounded-lg shadow-xl w-full max-w-md max-h-[90vh] overflow-y-auto animate-scale-in"
        onClick={(e) => e.stopPropagation()}
      >
        <div className="flex items-center justify-between px-4 py-3 border-b">
          <h2 className="text-lg font-medium text-gray-800">Create Task</h2>
          <button
            type="button"
            onClick={onClose}
            className="text-gray-500 hover:text-gray-700 p-1 rounded"
            aria-label="Close"
          >
            <XIcon size={16} />
          </button>
        </div>
        <form
          onSubmit={handleSubmit}
          className="flex-1 overflow-y-auto px-3 py-2 space-y-2 text-xs"
        >
          <div>
            <label className="block font-medium text-gray-600 mb-0.5">
              Title
            </label>
            <input
              type="text"
              required
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
              required
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
              <select
                value={formData.assigned_to}
                onChange={(e) =>
                  setFormData({ ...formData, assigned_to: e.target.value })
                }
                className="input-field h-8 px-2 py-1 text-xs"
              >
                <option value="">-- Unassigned --</option>
                {employees.map((emp) => (
                  <option key={emp.e_id} value={String(emp.e_id)}>
                    {emp.name
                      ? String(emp.name)
                          .replace(/[.,\s]+$/g, "")
                          .trim()
                      : `#${emp.e_id}`}
                  </option>
                ))}
              </select>
            </div>

            <div>
              <label className="block text-xs font-medium text-gray-600 mb-0.5">
                Reviewer
              </label>
              <select
                value={formData.reviewer}
                onChange={(e) =>
                  setFormData({ ...formData, reviewer: e.target.value })
                }
                className="input-field h-8 px-2 py-1 text-xs"
              >
                <option value="">-- Select reviewer --</option>
                {managers.map((m) => (
                  <option key={m.e_id} value={String(m.e_id)}>
                    {m.name
                      ? String(m.name)
                          .replace(/[.,\s]+$/g, "")
                          .trim()
                      : `#${m.e_id}`}
                  </option>
                ))}
              </select>
            </div>

            <div>
              <label className="block text-xs font-medium text-gray-600 mb-0.5">
                Priority
              </label>
              <select
                required
                value={formData.priority}
                onChange={(e) =>
                  setFormData({ ...formData, priority: e.target.value })
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
                disabled={activeRole === "Developer"}
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
              type="datetime-local"
              required
              value={formData.expected_closure}
              onChange={(e) =>
                setFormData({ ...formData, expected_closure: e.target.value })
              }
              className="input-field h-8 px-2 py-1 text-xs"
            />
          </div>

          <div className="flex gap-2 pt-2">
            <button
              type="submit"
              className="btn-primary flex-1 text-xs h-8"
              disabled={isSubmitting}
            >
              {isSubmitting ? "Creating..." : "Create"}
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

const EditTaskInline: React.FC<{
  task: Task;
  onClose: () => void;
  onSaved: (updated: Task) => void;
  activeRole: string | null;
  user: User | null;
}> = ({ task, onClose, onSaved, activeRole, user }) => {
  const [employees, setEmployees] = useState<
    {
      e_id?: number;
      name?: string;
    }[]
  >([]);

  const [managers, setManagers] = useState<
    {
      e_id?: number;
      name?: string;
    }[]
  >([]);
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

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!task.t_id) return;
    setIsSubmitting(true);
    try {
      const roleToUse = user?.role?.includes("Manager")
        ? "Manager"
        : activeRole || user?.role?.[0] || "";

      // Disallow Developer role from performing task updates
      if (roleToUse === "Developer") {
        alert("You are not authorized to update tasks.");
        setIsSubmitting(false);
        return;
      }

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

  useEffect(() => {
    let mounted = true;
    // fetch users via userAPI.getByRole then resolve display names from Employee table
    (async () => {
      try {
        let devUsers = await userAPI.getByRole("Developer");
        if (!mounted) return;
        if (!devUsers || devUsers.length === 0) {
          try {
            const all = await userAPI.getAll("");
            if (!mounted) return;
            const roleIncludes = (r: any, target: string) => {
              if (Array.isArray(r)) return r.includes(target);
              if (typeof r === "string") {
                const trimmed = r.trim();
                if (trimmed.startsWith("[") && trimmed.endsWith("]")) {
                  try {
                    const parsed = JSON.parse(trimmed);
                    return Array.isArray(parsed) && parsed.includes(target);
                  } catch (_e) {
                    return trimmed.includes(target);
                  }
                }
                return trimmed.includes(target);
              }
              return false;
            };
            devUsers = all.filter((u: any) =>
              roleIncludes((u as any).role, "Developer")
            );
          } catch (_e) {
            /* ignore fallback errors */
          }
        }

        const devs = await Promise.all(
          devUsers.map(async (u) => {
            try {
              const emp = await employeeAPI.getById(u.e_id, "Developer");
              return { e_id: u.e_id, name: emp?.name };
            } catch (_e) {
              return { e_id: u.e_id, name: undefined };
            }
          })
        );
        if (!mounted) return;
        setEmployees(devs || []);

        let mgrUsers = await userAPI.getByRole("Manager");
        if (!mounted) return;
        if (!mgrUsers || mgrUsers.length === 0) {
          try {
            const all = await userAPI.getAll("");
            if (!mounted) return;
            const roleIncludes = (r: any, target: string) => {
              if (Array.isArray(r)) return r.includes(target);
              if (typeof r === "string") {
                const trimmed = r.trim();
                if (trimmed.startsWith("[") && trimmed.endsWith("]")) {
                  try {
                    const parsed = JSON.parse(trimmed);
                    return Array.isArray(parsed) && parsed.includes(target);
                  } catch (_e) {
                    return trimmed.includes(target);
                  }
                }
                return trimmed.includes(target);
              }
              return false;
            };
            mgrUsers = all.filter((u: any) =>
              roleIncludes((u as any).role, "Manager")
            );
          } catch (_e) {
            /* ignore fallback errors */
          }
        }

        const mgrs = await Promise.all(
          mgrUsers.map(async (u) => {
            try {
              const emp = await employeeAPI.getById(u.e_id, "Manager");
              return { e_id: u.e_id, name: emp?.name };
            } catch (_e) {
              return { e_id: u.e_id, name: undefined };
            }
          })
        );
        if (!mounted) return;
        setManagers(mgrs || []);
      } catch (err) {
        console.debug("failed to load users for dropdowns:", err);
      }
    })();

    return () => {
      mounted = false;
    };
  }, []);

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4">
      <div
        className="absolute inset-0 bg-black/30 backdrop-blur-sm"
        onClick={onClose}
      />
      <div
        className="relative z-10 bg-white w-full max-w-md rounded-lg shadow-md border border-gray-200 flex flex-col max-h-[90vh]"
        onClick={(e) => e.stopPropagation()}
      >
        {/* Header */}
        <div className="flex items-center justify-between px-3 py-2 border-b">
          <h3 className="text-sm font-semibold">Edit Task {task.t_id}</h3>
          <button
            onClick={onClose}
            className="text-gray-500 hover:text-gray-700 p-1 rounded"
            aria-label="Close"
          >
            <XIcon size={16} />
          </button>
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
              <select
                value={formData.assigned_to}
                onChange={(e) =>
                  setFormData({ ...formData, assigned_to: e.target.value })
                }
                className="input-field h-8 px-2 py-1 text-xs"
              >
                <option value="">-- Unassigned --</option>
                {employees.map((emp) => (
                  <option key={emp.e_id} value={String(emp.e_id)}>
                    {emp.name
                      ? String(emp.name)
                          .replace(/[.,\s]+$/g, "")
                          .trim()
                      : `#${emp.e_id}`}
                  </option>
                ))}
              </select>
            </div>

            <div>
              <label className="block text-xs font-medium text-gray-600 mb-0.5">
                Reviewer
              </label>
              <select
                value={formData.reviewer}
                onChange={(e) =>
                  setFormData({ ...formData, reviewer: e.target.value })
                }
                className="input-field h-8 px-2 py-1 text-xs"
              >
                <option value="">-- Select reviewer --</option>
                {managers.map((m) => (
                  <option key={m.e_id} value={String(m.e_id)}>
                    {m.name
                      ? String(m.name)
                          .replace(/[.,\s]+$/g, "")
                          .trim()
                      : `#${m.e_id}`}
                  </option>
                ))}
              </select>
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
                disabled={activeRole === "Developer"}
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

const RemarkModal: React.FC<{
  task: Task;
  onClose: () => void;
  onSuccess: () => void;
  activeRole: string | null;
  user: User | null;
}> = ({ task, onClose, onSuccess, activeRole, user }) => {
  const [comment, setComment] = useState("");
  const [file, setFile] = useState<File | null>(null);
  const [isSubmitting, setIsSubmitting] = useState(false);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!task.t_id) return;
    if (!comment && !file) {
      alert("Please enter a comment or attach a file.");
      return;
    }
    setIsSubmitting(true);
    try {
      // Choose role based on task status: IN_PROGRESS -> Developer, REVIEW -> Manager
      const status = task?.status || "TO_DO";
      const requiredRole = status === "IN_PROGRESS" ? "Developer" : "Manager";

      const userRoles: any = user?.role || [];
      const hasRequired = Array.isArray(userRoles)
        ? userRoles.includes(requiredRole)
        : String(userRoles).includes(requiredRole);

      // prefer the required role if the user has it, otherwise fall back to activeRole or first role
      const roleToUse = hasRequired
        ? requiredRole
        : activeRole === requiredRole
        ? requiredRole
        : activeRole ||
          (Array.isArray(userRoles) ? userRoles[0] : userRoles) ||
          "";

      const resp = await remarkAPI.create(
        task.t_id,
        comment,
        roleToUse,
        file || undefined
      );
      if (import.meta.env.DEV) console.log("remark.create resp:", resp);
      onSuccess();
    } catch (err) {
      console.error("Failed to add remark:", err);
      alert("Failed to add remark. See console for details.");
    } finally {
      setIsSubmitting(false);
    }
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4">
      <div
        className="absolute inset-0 bg-black/30 backdrop-blur-sm"
        onClick={onClose}
      />
      <div
        className="relative z-10 bg-white rounded-lg shadow-xl w-full max-w-md max-h-[80vh] overflow-y-auto animate-scale-in"
        onClick={(e) => e.stopPropagation()}
      >
        <div className="flex items-center justify-between px-4 py-3 border-b">
          <h2 className="text-lg font-medium text-gray-800">Add Remark</h2>
          <button
            type="button"
            onClick={onClose}
            className="text-gray-500 hover:text-gray-700 p-1 rounded"
            aria-label="Close"
          >
            <XIcon size={16} />
          </button>
        </div>

        <form onSubmit={handleSubmit} className="px-4 py-3 space-y-3 text-sm">
          <div>
            <label className="block text-xs font-medium text-gray-600 mb-1">
              Comment
            </label>
            <textarea
              value={comment}
              onChange={(e) => setComment(e.target.value)}
              rows={4}
              className="input-field w-full text-sm px-2 py-1"
              placeholder="Write a remark..."
            />
          </div>

          <div>
            <label className="block text-xs font-medium text-gray-600 mb-1">
              Attachment (optional)
            </label>
            <input
              type="file"
              onChange={(e) =>
                setFile(e.target.files ? e.target.files[0] : null)
              }
              className="text-xs"
            />
          </div>

          <div className="flex gap-2 pt-2">
            <button
              type="submit"
              className="btn-primary flex-1 text-xs h-8"
              disabled={isSubmitting}
            >
              {isSubmitting ? "Adding..." : "Add Remark"}
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

const TaskDetailModal: React.FC<{
  task: Task;
  onClose: () => void;
  activeRole: string | null;
  user: User | null;
  reloadKey?: number;
}> = ({ task, onClose, activeRole, user, reloadKey }) => {
  const [remarks, setRemarks] = useState<any[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    let mounted = true;
    (async () => {
      if (!task?.t_id) {
        if (mounted) {
          setRemarks([]);
          setLoading(false);
        }
        return;
      }

      // Try multiple roles: prefer activeRole, then any roles the user has.
      const tried = new Set<string>();
      const rolesToTry: string[] = [];
      if (activeRole) {
        rolesToTry.push(activeRole);
        tried.add(activeRole);
      }
      if (user?.role && Array.isArray(user.role)) {
        user.role.forEach((r: string) => {
          if (r && !tried.has(r)) {
            rolesToTry.push(r);
            tried.add(r);
          }
        });
      } else if (user?.role) {
        rolesToTry.push(String(user.role));
      }

      let lastError: any = null;
      if (import.meta.env.DEV)
        console.debug(
          "TaskDetailModal: rolesToTry=",
          rolesToTry,
          "taskId=",
          task.t_id
        );
      for (const role of rolesToTry) {
        try {
          if (import.meta.env.DEV)
            console.debug("TaskDetailModal: trying role=", role);
          const data = await remarkAPI.getByTask(task.t_id as number, role);
          if (!mounted) return;
          if (import.meta.env.DEV)
            console.debug(
              "TaskDetailModal: got remarks count=",
              (data || []).length
            );
          setRemarks(data || []);
          lastError = null;
          break; // success
        } catch (err: any) {
          if (import.meta.env.DEV)
            console.error(
              "TaskDetailModal: getByTask error for role=",
              role,
              err?.response?.status,
              err?.response?.data || err
            );
          lastError = err;
          const status = err?.response?.status;
          // If it's not an auth error, stop and surface
          if (status && status !== 400 && status !== 403) {
            console.error("Failed to load remarks:", err);
            break;
          }
          // otherwise try next role
        }
      }

      if (lastError && mounted) {
        // failed for all tried roles
        console.error(
          "Failed to load remarks with available roles:",
          lastError
        );
        setRemarks([]);
      }

      if (mounted) setLoading(false);
    })();
    return () => {
      mounted = false;
    };
  }, [task.t_id, activeRole, user, reloadKey]);

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4">
      <div
        className="absolute inset-0 bg-black/30 backdrop-blur-sm"
        onClick={onClose}
      />
      <div
        className="relative z-10 bg-white rounded-lg shadow-xl w-full max-w-xl max-h-[80vh] overflow-y-auto animate-scale-in"
        onClick={(e) => e.stopPropagation()}
      >
        <div className="flex items-center justify-between px-4 py-3 border-b">
          <h2 className="text-lg font-medium text-gray-800">Task Details</h2>
          <button
            type="button"
            onClick={onClose}
            className="text-gray-500 hover:text-gray-700 p-1 rounded"
            aria-label="Close"
          >
            <XIcon size={16} />
          </button>
        </div>
        <div className="px-4 py-3 text-sm space-y-3">
          <div>
            <h3 className="text-sm font-semibold">{task.title}</h3>
            <p className="text-xs text-gray-600">#{task.t_id}</p>
            <p className="text-sm text-gray-700 mt-1">{task.description}</p>
          </div>
          <div className="grid grid-cols-2 gap-3 text-xs text-gray-600">
            <div>Priority: {task.priority}</div>
            <div>Status: {task.status}</div>
            <div>Assignee: {task.assigned_to ?? "-"}</div>
            <div>Reviewer: {task.reviewer ?? "-"}</div>
            <div>
              Expected:{" "}
              {task.expected_closure
                ? new Date(task.expected_closure).toLocaleString()
                : "-"}
            </div>
          </div>

          <hr />

          <div>
            <h4 className="text-sm font-medium">Remarks</h4>
            {loading ? (
              <div className="text-xs text-gray-500 py-4">
                Loading remarks...
              </div>
            ) : remarks.length === 0 ? (
              <div className="text-xs text-gray-500 py-4">No remarks</div>
            ) : (
              <ul className="space-y-2 mt-2">
                {remarks.map((r) => (
                  <li key={r._id} className="border rounded p-2 text-xs">
                    <div className="text-gray-700">{r.comment}</div>
                    <div className="text-gray-500 text-[11px] mt-1">
                      {/* By: {r.created_by ?? "-"} •{" "} */}
                      {r.created_at
                        ? new Date(r.created_at).toLocaleString()
                        : "-"}
                    </div>
                    {r.file_name && (
                      <div className="text-xs mt-1">
                        {r.file_id ? (
                          <button
                            onClick={async (e) => {
                              e.stopPropagation();
                              try {
                                const resp = await api.get(
                                  `/Remark/file/${r.file_id}`,
                                  { responseType: "blob" }
                                );
                                const blob = new Blob([resp.data], {
                                  type:
                                    resp.headers["content-type"] ||
                                    "application/octet-stream",
                                });
                                const url = URL.createObjectURL(blob);
                                const a = document.createElement("a");
                                a.href = url;
                                a.download = r.file_name || "file";
                                document.body.appendChild(a);
                                a.click();
                                a.remove();
                                URL.revokeObjectURL(url);
                              } catch (err) {
                                console.error("Failed to download file:", err);
                                alert(
                                  "Failed to download attachment. Make sure you are logged in."
                                );
                              }
                            }}
                            className="text-blue-600 underline"
                          >
                            Attachment: {r.file_name}
                          </button>
                        ) : (
                          <span className="text-blue-600">
                            Attachment: {r.file_name}
                          </span>
                        )}
                      </div>
                    )}
                  </li>
                ))}
              </ul>
            )}
          </div>
        </div>
      </div>
    </div>
  );
};

export default Tasks;
