import React, { useState, useMemo } from "react";
import { Plus, Search, Filter } from "lucide-react";
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
  const [statusFilter, setStatusFilter] = useState("ALL");
  const [detailTask, setDetailTask] = useState(null);

  const filteredTasks = useMemo(() => {
    const q = (searchQuery || "").trim().toLowerCase();
    return (tasks || []).filter((t) => {
      if (statusFilter !== "ALL" && t.status !== statusFilter) return false;
      // Role-based visibility: developers see only tasks assigned to them,
      // managers see only tasks where they are the reviewer. Other roles see all.
      const roleUpper = (userRole || "").toUpperCase();
      const isDeveloper = roleUpper.includes("DEVELOPER");
      const isManager = roleUpper.includes("MANAGER");
      if (isDeveloper) {
        // If we don't know the current user's emp id, hide tasks for developer view
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
  }, [tasks, searchQuery, statusFilter]);

  const groupedTasks = STATUSES.reduce((acc, status) => {
    // sort tasks within a status by priority (CRITICAL, HIGH, MEDIUM, LOW)
    const list = filteredTasks.filter((t) => t.status === status);
    const priorityOrder = [...PRIORITIES].reverse(); // ['CRITICAL','HIGH','MEDIUM','LOW']
    const orderMap = priorityOrder.reduce((m, p, i) => ({ ...m, [p]: i }), {});
    list.sort((a, b) => {
      const ra = orderMap[a.priority] ?? orderMap["MEDIUM"] ?? 2;
      const rb = orderMap[b.priority] ?? orderMap["MEDIUM"] ?? 2;
      return ra - rb; // smaller index = higher priority (CRITICAL first)
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
              className="px-3 py-2 rounded-md border w-80 focus:outline-none focus:ring-2 focus:ring-indigo-300"
            />
          </div>

          <select
            value={statusFilter}
            onChange={(e) => setStatusFilter(e.target.value)}
            className="px-3 py-2 rounded-md border focus:outline-none focus:ring-2 focus:ring-indigo-300"
          >
            <option value="ALL">All Statuses</option>
            {STATUSES.map((s) => (
              <option key={s} value={s}>
                {STATUS_CONFIG[s].label}
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
            gridTemplateColumns: `repeat(${STATUSES.length}, minmax(250px, 1fr))`,
          }}
        >
          {STATUSES.map((status) => (
            <div key={status} className="kanban-column">
              <div className="sticky top-4 bg-white/90 backdrop-blur-sm px-3 py-2 rounded-md flex items-center justify-between shadow-sm mb-2">
                <div>
                  <div className="text-sm font-semibold">
                    {STATUS_CONFIG[status].label}
                  </div>
                  <div className="text-xs text-gray-500">
                    {(groupedTasks[status] || []).length} tasks
                  </div>
                </div>
                <div>
                  <span
                    className={`inline-block px-2 py-1 rounded text-xs ${STATUS_CONFIG[status].color} ${STATUS_CONFIG[status].textColor}`}
                  ></span>
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
                      />
                    </div>
                  ))
                ) : (
                  <div className="text-center text-sm text-gray-400 py-8">
                    No tasks
                  </div>
                )}
              </div>
            </div>
          ))}
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
