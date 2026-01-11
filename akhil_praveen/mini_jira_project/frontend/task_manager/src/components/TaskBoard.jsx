import React, { useState, useMemo, useEffect } from "react";
import { Plus, Search, RefreshCw, Filter } from "lucide-react";
import TaskCard from "./TaskCard";
import TaskFormModal from "./TaskFormModel";
import TaskDetailModal from "./TaskDetailModal";
import { STATUS_CONFIG, STATUSES, PRIORITIES } from "../utils/constants";

function TaskBoard({
  tasks = [],
  employees = [],
  onRefresh,
  canCreateTasks,
  onUpdateStatus,
  onSaveTask,
  userRole = "",
  currentEmpId = null,
}) {
  const ALLOWED_TRANSITIONS = {
    TO_DO: ["IN_PROGRESS"],
    IN_PROGRESS: ["REVIEW"],
    REVIEW: ["IN_PROGRESS", "DONE"],
    DONE: [],
  };
  const [showTaskForm, setShowTaskForm] = useState(false);
  const [editingTask, setEditingTask] = useState(null);
  const [searchQuery, setSearchQuery] = useState("");
  const [priorityFilter, setPriorityFilter] = useState("ALL");
  const [detailTask, setDetailTask] = useState(null);
  const [dragOverStatus, setDragOverStatus] = useState(null);
  const [isRefreshing, setIsRefreshing] = useState(false);

  const canMarkDone =
    (userRole || "").toUpperCase().includes("ADMIN") ||
    (userRole || "").toUpperCase().includes("MANAGER");

  const filteredTasks = useMemo(() => {
    const q = (searchQuery || "").trim().toLowerCase();
    return (tasks || []).filter((t) => {
      if (priorityFilter !== "ALL" && t.priority !== priorityFilter)
        return false;

      const roleUpper = (userRole || "").toUpperCase();
      const isDeveloper = roleUpper.includes("DEVELOPER");
      const isManager = roleUpper.includes("MANAGER");

      if (isDeveloper) {
        if (currentEmpId == null) return false;
        if (Number(t.assigned_to) !== Number(currentEmpId)) return false;
      } else if (isManager) {
        if (currentEmpId == null) return false;
        if (Number(t.reviewer) !== Number(currentEmpId)) return false;
      }

      if (!q) return true;
      return (
        String(t.title || "")
          .toLowerCase()
          .includes(q) ||
        String(t.description || "")
          .toLowerCase()
          .includes(q) ||
        String(t.dept_name || "")
          .toLowerCase()
          .includes(q)
      );
    });
  }, [tasks, searchQuery, priorityFilter, userRole, currentEmpId]);

  const groupedTasks = STATUSES.reduce((acc, status) => {
    const priorityOrder = [...PRIORITIES].reverse();
    const orderMap = priorityOrder.reduce((m, p, i) => ({ ...m, [p]: i }), {});
    const list = (filteredTasks || []).filter((t) => t.status === status);
    list.sort(
      (a, b) => (orderMap[a.priority] ?? 2) - (orderMap[b.priority] ?? 2)
    );
    acc[status] = list;
    return acc;
  }, {});

  const handleEditTask = (task) => {
    setEditingTask(task);
    setShowTaskForm(true);
  };

  const handleCloseForm = () => {
    setShowTaskForm(false);
    setEditingTask(null);
  };

  const handleSaveTask = async (taskData) => {
    await onSaveTask(editingTask, taskData);
    handleCloseForm();
  };

  const handleRefresh = async () => {
    setIsRefreshing(true);
    await onRefresh();
    setTimeout(() => setIsRefreshing(false), 500);
  };

  const handleDragOver = (e, status) => {
    e.preventDefault();
    e.dataTransfer.dropEffect = "move";
    setDragOverStatus(status);
  };

  const handleDragLeave = () => {
    setDragOverStatus(null);
  };

  const handleDrop = async (e, newStatus) => {
    e.preventDefault();
    setDragOverStatus(null);

    const taskId = parseInt(e.dataTransfer.getData("taskId"));
    const currentStatus = e.dataTransfer.getData("currentStatus");

    if (currentStatus === newStatus) return;

    const task = tasks.find((t) => t.task_id === taskId);
    if (!task) return;

    // Do not allow changing status of a DONE task
    if (task.status === "DONE") {
      alert("This task is already DONE and its status cannot be changed.");
      return;
    }

    // Enforce allowed sequential transitions
    const allowed = ALLOWED_TRANSITIONS[task.status] || [];
    if (!allowed.includes(newStatus)) {
      alert(
        `Invalid transition: ${task.status} -> ${newStatus}. Tasks must progress sequentially.`
      );
      return;
    }

    // Only Admin/Manager can mark as DONE (frontend hint)
    if (newStatus === "DONE" && !canMarkDone) {
      alert("Only Managers and Admins can mark tasks as Done");
      return;
    }

    const isReviewer =
      currentEmpId != null && Number(currentEmpId) === Number(task.reviewer);

    // Determine if current user is a manager/reviewer role
    const roleUpper = (userRole || "").toUpperCase();
    const isManagerRole = roleUpper.includes("MANAGER") || roleUpper.includes("ADMIN");

    if (newStatus === "REVIEW") {
      console.debug("TaskBoard.handleDrop -> REVIEW requested", {
        taskId,
        currentStatus,
        newStatus,
        isReviewer,
        isManagerRole,
        currentEmpId,
        reviewer: task.reviewer,
      });

      // Prompt for remarks - determine if it's reviewer or developer remarks
      const promptText = isReviewer || isManagerRole
        ? `Add reviewer remarks for changing status to ${STATUS_CONFIG[newStatus].label}:`
        : `Add developer remarks for submitting to ${STATUS_CONFIG[newStatus].label}:`;
      
      const remarks = prompt(promptText);
      console.debug("TaskBoard.handleDrop -> prompt result", { remarks });
      
      await onUpdateStatus(taskId, newStatus, remarks || null);
    } else if (newStatus === "DONE") {
      // For DONE status, always treat as reviewer remarks if user has permission
      const remarks = prompt(
        `Add reviewer remarks for marking task as ${STATUS_CONFIG[newStatus].label}:`
      );
      await onUpdateStatus(taskId, newStatus, remarks || null);
    } else if (newStatus === "IN_PROGRESS") {
      const remarks = prompt(
        `Add remarks for changing status to ${STATUS_CONFIG[newStatus].label} (optional):`
      );
      await onUpdateStatus(taskId, newStatus, remarks || null);
    } else {
      await onUpdateStatus(taskId, newStatus, null);
    }
  };

  // Keep the detailTask object in sync with the latest `tasks` array.
  useEffect(() => {
    if (!detailTask || !tasks || !tasks.length) return;
    try {
      const updated = tasks.find((t) => t.task_id === detailTask.task_id);
      if (updated && JSON.stringify(updated) !== JSON.stringify(detailTask)) {
        setDetailTask(updated);
      }
    } catch (e) {
      // ignore
    }
  }, [tasks]);

  return (
    <div className="container mx-auto px-4 py-4">
      {/* Header Controls */}
      <div className="flex items-center justify-between mb-4 gap-3 bg-white rounded-xl p-3 shadow-sm border border-gray-100">
        <div className="flex items-center gap-2 flex-1">
          <div className="relative flex-1 max-w-md">
            <Search
              className="absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-400"
              size={16}
            />
            <input
              type="search"
              placeholder="Search tasks..."
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
              className="pl-9 pr-3 py-2 text-sm rounded-lg border border-gray-200 w-full focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-transparent transition-all"
            />
          </div>

          <div className="relative">
            <Filter
              className="absolute left-2.5 top-1/2 transform -translate-y-1/2 text-gray-400"
              size={14}
            />
            <select
              value={priorityFilter}
              onChange={(e) => setPriorityFilter(e.target.value)}
              className="pl-8 pr-6 py-2 text-sm rounded-lg border border-gray-200 focus:outline-none focus:ring-2 focus:ring-indigo-500 appearance-none bg-white cursor-pointer font-medium text-gray-700"
            >
              <option value="ALL">All</option>
              {PRIORITIES.map((p) => (
                <option key={p} value={p}>
                  {p}
                </option>
              ))}
            </select>
          </div>
        </div>

        <div className="flex items-center gap-2">
          <button
            onClick={() => {
              setEditingTask(null);
              setShowTaskForm(true);
            }}
            className={`px-3 py-2 text-sm rounded-lg text-white font-semibold bg-gradient-to-r from-indigo-600 to-purple-600 hover:shadow-lg hover:scale-105 active:scale-95 transition-all flex items-center gap-1.5 ${
              !canCreateTasks ? "opacity-60 cursor-not-allowed" : ""
            }`}
            disabled={!canCreateTasks}
          >
            <Plus size={16} />
            New Task
          </button>

          <button
            onClick={handleRefresh}
            className={`px-2.5 py-2 rounded-lg border border-gray-200 hover:bg-gray-50 transition-all ${
              isRefreshing ? "animate-spin" : ""
            }`}
            title="Refresh"
          >
            <RefreshCw size={16} className="text-gray-600" />
          </button>
        </div>
      </div>

      {/* Kanban Board */}
      <div className="w-full">
        <div
          className="grid gap-3 grid-kanban"
          style={{
            gridTemplateColumns: `repeat(${STATUSES.length}, minmax(280px, 1fr))`,
          }}
        >
          {STATUSES.map((status) => {
            const config = STATUS_CONFIG[status];
            const isDragOver = dragOverStatus === status;
            const taskCount = (groupedTasks[status] || []).length;

            return (
              <div
                key={status}
                onDragOver={(e) => handleDragOver(e, status)}
                onDragLeave={handleDragLeave}
                onDrop={(e) => handleDrop(e, status)}
                className={`kanban-column rounded-xl ${
                  config.columnBg
                } p-3 transition-all border-2 ${
                  isDragOver
                    ? "border-indigo-400 shadow-lg scale-[1.02]"
                    : "border-transparent"
                }`}
              >
                {/* Column Header */}
                <div
                  className="sticky top-2 bg-white rounded-lg px-3 py-2.5 shadow-sm mb-3 border-l-4 transition-all hover:shadow-md"
                  style={{ borderColor: config.color.replace("bg-", "#") }}
                >
                  <div className="flex items-center justify-between">
                    <div className="flex-1">
                      <div
                        className={`text-sm font-bold ${config.textColor} flex items-center gap-2`}
                      >
                        {config.label}
                      </div>
                      <div className="text-[10px] text-gray-500 mt-0.5 font-medium">
                        {taskCount} task{taskCount !== 1 ? "s" : ""}
                      </div>
                    </div>
                    <div
                      className={`w-7 h-7 rounded-lg ${config.color} flex items-center justify-center shadow-sm`}
                    >
                      <span className="text-white text-xs font-bold">
                        {taskCount}
                      </span>
                    </div>
                  </div>
                </div>

                {/* Task List - Scrollable */}
                <div className="kanban-list">
                  {groupedTasks[status] && groupedTasks[status].length ? (
                    groupedTasks[status].map((task) => (
                      <div
                        key={task.task_id}
                        onClick={() => setDetailTask(task)}
                      >
                        <TaskCard
                          task={task}
                          employees={employees}
                          userRole={userRole}
                          currentEmpId={currentEmpId}
                          onUpdateStatus={onUpdateStatus}
                          onEdit={(t) => handleEditTask(t)}
                          statusConfig={config}
                        />
                      </div>
                    ))
                  ) : (
                    <div
                      className={`text-center text-xs text-gray-400 py-12 bg-white/70 rounded-lg transition-all border-2 border-dashed ${
                        isDragOver
                          ? "bg-indigo-50/50 border-indigo-300 scale-105"
                          : "border-gray-200"
                      }`}
                    >
                      {isDragOver ? (
                        <div className="text-indigo-600 font-semibold">
                          Drop here
                        </div>
                      ) : (
                        <div>No tasks</div>
                      )}
                    </div>
                  )}
                </div>
              </div>
            );
          })}
        </div>
      </div>

      {showTaskForm && (
        <TaskFormModal
          task={editingTask}
          employees={employees}
          onClose={handleCloseForm}
          onSave={handleSaveTask}
        />
      )}

      {detailTask && (
        <TaskDetailModal
          task={detailTask}
          employees={employees}
          onClose={() => setDetailTask(null)}
          onEdit={() => {
            setEditingTask(detailTask);
            setShowTaskForm(true);
            setDetailTask(null);
          }}
          currentEmpId={currentEmpId}
        />
      )}
    </div>
  );
}

export default TaskBoard;