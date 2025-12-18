import React, { useState, useMemo } from "react";
import { Plus, Search } from "lucide-react";
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
  const [showTaskForm, setShowTaskForm] = useState(false);
  const [editingTask, setEditingTask] = useState(null);
  const [searchQuery, setSearchQuery] = useState("");
  const [priorityFilter, setPriorityFilter] = useState("ALL");
  const [detailTask, setDetailTask] = useState(null);
  const [dragOverStatus, setDragOverStatus] = useState(null);

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
    const list = filteredTasks.filter((t) => t.status === status);
    const priorityOrder = [...PRIORITIES].reverse();
    const orderMap = priorityOrder.reduce((m, p, i) => ({ ...m, [p]: i }), {});
    list.sort((a, b) => {
      const ra = orderMap[a.priority] ?? orderMap["MEDIUM"] ?? 2;
      const rb = orderMap[b.priority] ?? orderMap["MEDIUM"] ?? 2;
      return ra - rb;
    });
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

  // Drag and Drop handlers
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

    // If dropped in the same column, do nothing
    if (currentStatus === newStatus) {
      return;
    }

    // Find the task being dropped
    const task = tasks.find((t) => t.task_id === taskId);
    if (!task) return;

    // Check permission for DONE status
    if (newStatus === "DONE" && !canMarkDone) {
      alert("Only Managers and Admins can mark tasks as Done");
      return;
    }

    // Check if user is the reviewer for REVIEW/DONE
    const isReviewer = currentEmpId != null && Number(currentEmpId) === Number(task.reviewer);

    // For REVIEW or DONE, ask for remarks if user is reviewer
    if ((newStatus === "REVIEW" || newStatus === "DONE") && isReviewer) {
      const remarks = prompt(`Add reviewer remarks for changing status to ${STATUS_CONFIG[newStatus].label}:`);
      await onUpdateStatus(taskId, newStatus, remarks || null);
    } else if (newStatus === "IN_PROGRESS") {
      const remarks = prompt(`Add remarks for changing status to ${STATUS_CONFIG[newStatus].label} (optional):`);
      await onUpdateStatus(taskId, newStatus, remarks || null);
    } else {
      // For other status changes, update directly
      await onUpdateStatus(taskId, newStatus, null);
    }
  };

  return (
    <div className="container mx-auto px-4 py-6">
      <div className="flex items-center justify-between mb-4 gap-4">
        <div className="flex items-center gap-3">
          <div className="relative">
            <Search
              className="absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-400"
              size={18}
            />
            <input
              type="search"
              placeholder="Search tasks, dept or description..."
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
              className="pl-10 pr-4 py-2 rounded-md border w-80 focus:outline-none focus:ring-2 focus:ring-indigo-300"
            />
          </div>

          <select
            value={priorityFilter}
            onChange={(e) => setPriorityFilter(e.target.value)}
            className="px-3 py-2 rounded-md border focus:outline-none focus:ring-2 focus:ring-indigo-300"
          >
            <option value="ALL">All Priorities</option>
            {PRIORITIES.map((p) => (
              <option key={p} value={p}>
                {p}
              </option>
            ))}
          </select>
        </div>

        <div className="flex items-center gap-3">
          <button
            onClick={() => {
              setEditingTask(null);
              setShowTaskForm(true);
            }}
            className={`px-4 py-2 rounded-md text-white bg-indigo-600 hover:bg-indigo-700 ${
              !canCreateTasks ? "opacity-60 cursor-not-allowed" : ""
            }`}
            disabled={!canCreateTasks}
          >
            <Plus size={16} className="inline mr-2" /> New Task
          </button>

          <button
            onClick={onRefresh}
            className="px-3 py-2 rounded-md border hover:bg-gray-50"
          >
            Refresh
          </button>
        </div>
      </div>

      <div className="w-full">
        <div
          className="grid gap-4 grid-kanban"
          style={{
            gridTemplateColumns: `repeat(${STATUSES.length}, minmax(280px, 1fr))`,
          }}
        >
          {STATUSES.map((status) => {
            const config = STATUS_CONFIG[status];
            const isDragOver = dragOverStatus === status;
            
            return (
              <div
                key={status}
                onDragOver={(e) => handleDragOver(e, status)}
                onDragLeave={handleDragLeave}
                onDrop={(e) => handleDrop(e, status)}
                className={`kanban-column rounded-lg ${config.columnBg} p-3 transition-all ${
                  isDragOver ? 'ring-2 ring-indigo-400 ring-offset-2' : ''
                }`}
              >
                <div className="sticky top-4 bg-white rounded-lg px-4 py-3 shadow-sm mb-3 border-l-4" style={{ borderColor: config.color.replace('bg-', '#') }}>
                  <div className="flex items-center justify-between">
                    <div>
                      <div className={`text-sm font-bold ${config.textColor}`}>
                        {config.label}
                      </div>
                      <div className="text-xs text-gray-500 mt-0.5">
                        {(groupedTasks[status] || []).length} task{(groupedTasks[status] || []).length !== 1 ? 's' : ''}
                      </div>
                    </div>
                    <div className={`w-8 h-8 rounded-full ${config.color} flex items-center justify-center`}>
                      <span className="text-white text-xs font-bold">
                        {(groupedTasks[status] || []).length}
                      </span>
                    </div>
                  </div>
                </div>

                <div className="kanban-list">
                  {groupedTasks[status] && groupedTasks[status].length ? (
                    groupedTasks[status].map((task) => (
                      <div key={task.task_id} onClick={() => setDetailTask(task)}>
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
                    <div className={`text-center text-sm text-gray-400 py-12 bg-white/50 rounded-lg transition-all ${
                      isDragOver ? 'bg-white/80 border-2 border-dashed border-indigo-300' : ''
                    }`}>
                      {isDragOver ? 'Drop here' : 'No tasks'}
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