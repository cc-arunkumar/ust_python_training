import React, { useState, useEffect } from "react";
import { Plus, Eye, Trash, AlertCircle, User, Bell } from "lucide-react";
import { useAuth } from "../../context/AuthContext";
import ApiService from "../../services/api";
import TaskModal from "./TaskModal";
import TaskDetailsModal from "./TaskDetailsModal";
import toast from "react-hot-toast";

const TasksPage = ({ initialTasks, initialEmployees, onTasksChanged }) => {
  const [tasks, setTasks] = useState(initialTasks ?? []);
  const [employees, setEmployees] = useState(initialEmployees ?? []);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");
  const [showModal, setShowModal] = useState(false);
  const [editingTask, setEditingTask] = useState(null);
  const [selectedTask, setSelectedTask] = useState(null);
  const [selectedNotificationsTask, setSelectedNotificationsTask] =
    useState(null);
  const { hasRole } = useAuth();

  const canCreate = hasRole("ADMIN") || hasRole("MANAGER");
  const canDelete = hasRole("ADMIN") || hasRole("MANAGER");

  useEffect(() => {
    // If parent provided initialTasks, use them and skip automatic fetch.
    if (initialTasks !== undefined) {
      setTasks(initialTasks);
      setLoading(false);
      setError("");
      // also set employees if provided
      if (initialEmployees !== undefined) setEmployees(initialEmployees);
      return;
    }

    fetchTasks();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [initialTasks]);

  const normalizeStatus = (task) => {
    if (!task) return task;
    if (task.status === "IN_PROGRESS") task.status = "ON_PROCESS";
    if (task.status === "IN_REVIEW") task.status = "REVIEW";
    return task;
  };

  const fetchTasks = async (force = false) => {
    try {
      setError("");
      // If initialTasks provided and not forcing, reuse them
      if (initialTasks !== undefined && !force) {
        return setTasks(initialTasks);
      }

      let data = await ApiService.getTasks();

      // Normalize statuses
      if (Array.isArray(data)) {
        data = data.map(normalizeStatus);
      } else if (data && data.status) {
        data = normalizeStatus(data);
      }

      setTasks(data);
    } catch (err) {
      setError(err.message);
      toast.error(err.message);
    } finally {
      setLoading(false);
    }
  };

  const formatDate = (dateString) => {
    if (!dateString) return "No deadline";
    return new Date(dateString).toLocaleDateString("en-US", {
      month: "short",
      day: "numeric",
      year: "numeric",
    });
  };

  const handleDelete = async (taskId) => {
    if (!canDelete) {
      toast.error("You don't have permission to delete tasks");
      return;
    }

    const confirm = window.confirm(
      "Are you sure you want to delete this task?"
    );
    if (!confirm) return;

    try {
      await ApiService.deleteTask(taskId);
      toast.success("Task deleted successfully");
      // update local list immediately
      setTasks((prev) => prev.filter((t) => t.task_id !== taskId));
      // Ask parent (Layout) to refresh role-filtered data so stats update
      if (onTasksChanged) onTasksChanged();
      else await fetchTasks(true);
    } catch (err) {
      toast.error(err.message || "Failed to delete task");
    }
  };

  if (loading) {
    return (
      <div className="flex flex-col items-center justify-center py-24">
        <div className="animate-spin rounded-full h-10 w-10 border-b-2 border-blue-500" />
        <p className="mt-4 text-slate-500">Fetching tasks…</p>
      </div>
    );
  }

  return (
    <div className="max-w-7xl mx-auto px-6 py-8">
      {/* PAGE HEADER */}
      <div className="flex flex-wrap items-center justify-between gap-4 mb-8">
        <div>
          <h1 className="text-3xl font-semibold text-slate-800">
            Task Overview
          </h1>
          <p className="text-slate-500 mt-1">
            Monitor assignments and team progress
          </p>
        </div>

        {canCreate && (
          <button
            onClick={() => {
              setEditingTask(null);
              setShowModal(true);
            }}
            className="flex items-center gap-2 bg-blue-600 text-white
                       px-5 py-2.5 rounded-xl shadow-sm
                       hover:bg-blue-700 transition"
          >
            <Plus size={18} />
            New Task
          </button>
        )}
      </div>

      {/* ERROR */}
      {error && (
        <div
          className="mb-6 flex items-center gap-2 bg-red-50
                        text-red-600 px-4 py-3 rounded-xl"
        >
          <AlertCircle size={18} />
          {error}
        </div>
      )}

      {/* EMPTY */}
      {tasks.length === 0 ? (
        <div className="bg-white rounded-2xl shadow-sm p-12 text-center">
          <p className="text-slate-500">No tasks have been created yet.</p>
          {canCreate && (
            <button
              onClick={() => setShowModal(true)}
              className="mt-4 text-blue-600 font-medium hover:underline"
            >
              Create your first task
            </button>
          )}
        </div>
      ) : (
        /* TASK CARDS */
        <div className="grid gap-6 sm:grid-cols-1 md:grid-cols-2 xl:grid-cols-3">
          {tasks.map((task) => (
            <div
              key={task.task_id}
              className="bg-white rounded-2xl shadow-sm
                         hover:shadow-md transition p-6 flex flex-col"
            >
              {/* HEADER: Title on left, bell + deadline on right */}
              <div className="flex items-start justify-between mb-3">
                <h3 className="text-lg font-semibold text-slate-800 line-clamp-1">
                  {task.title}
                </h3>
                <div className="flex flex-col items-end">
                  <div className="relative">
                    <button
                      onClick={() => setSelectedNotificationsTask(task)}
                      aria-label="Open notifications"
                      className="p-2 rounded-md text-slate-600 hover:bg-slate-100 transition"
                    >
                      <Bell size={18} />
                    </button>
                    {((task.notifications && task.notifications.length) || 0) +
                      ((task.remarks && task.remarks.length) || 0) >
                      0 && (
                      <span className="absolute -top-1 -right-1 bg-red-600 text-white text-[11px] rounded-full w-5 h-5 flex items-center justify-center">
                        {((task.notifications && task.notifications.length) ||
                          0) + ((task.remarks && task.remarks.length) || 0)}
                      </span>
                    )}
                  </div>
                  <div className="text-xs text-slate-500 mt-1">
                    {formatDate(task.expected_closure)}
                  </div>
                </div>
              </div>

              {/* DESC */}
              {task.description && (
                <p className="text-slate-500 text-sm line-clamp-2 mb-4">
                  {task.description}
                </p>
              )}

              {/* META */}
              <div className="space-y-2 text-sm text-slate-500">
                <div className="flex items-center gap-3">
                  {(() => {
                    const assigned = employees.find(
                      (e) => Number(e.emp_id) === Number(task.assigned_to)
                    );
                    return (
                      <div className="relative group">
                        <div className="w-9 h-9 rounded-full bg-slate-100 overflow-hidden flex items-center justify-center text-slate-700 font-semibold">
                          {assigned && assigned.avatar ? (
                            <img
                              src={assigned.avatar}
                              alt={assigned.emp_name || "avatar"}
                              className="w-full h-full object-cover"
                            />
                          ) : assigned && assigned.emp_name ? (
                            <span className="uppercase">
                              {assigned.emp_name.charAt(0)}
                            </span>
                          ) : (
                            <User size={14} />
                          )}
                        </div>

                        {assigned && (
                          <div className="absolute left-0 -top-2 transform -translate-y-full hidden group-hover:block text-xs bg-white border border-gray-200 rounded-md px-3 py-2 shadow z-10 w-48">
                            <div className="font-medium text-slate-700">
                              {assigned.emp_name}
                            </div>
                            <div className="text-slate-500 text-[12px]">
                              ID: {assigned.emp_id}
                            </div>
                            {assigned.email && (
                              <div className="text-slate-500 text-[12px] truncate">
                                {assigned.email}
                              </div>
                            )}
                          </div>
                        )}
                      </div>
                    );
                  })()}

                  {task.priority && (
                    <span
                      className={`inline-block px-2 py-1 rounded-full text-xs font-medium ${
                        task.priority ? "bg-gray-100 text-slate-700" : ""
                      }`}
                    >
                      {task.priority}
                    </span>
                  )}

                  {/* header bell moved to top; no bell here */}
                </div>

                {task.reviewer && (
                  <div className="flex items-center gap-2">
                    <User size={14} />
                    Reviewer: {task.reviewer}
                  </div>
                )}

                {/* deadline moved to header; duplicate calendar removed */}
              </div>

              {/* ACTION */}
              <div className="mt-6 flex gap-2">
                <button
                  onClick={() => setSelectedTask(task)}
                  className="flex-1 flex items-center justify-center gap-2
                             text-blue-600 text-sm font-medium
                             rounded-lg py-2
                             hover:bg-blue-50 transition"
                >
                  <Eye size={16} />
                  View details
                </button>

                {canDelete && (
                  <button
                    onClick={() => handleDelete(task.task_id)}
                    className="flex-1 flex items-center justify-center gap-2
                               text-red-600 text-sm font-medium
                               rounded-lg py-2
                               hover:bg-red-50 transition"
                  >
                    <Trash size={16} />
                    Delete
                  </button>
                )}
              </div>
            </div>
          ))}
        </div>
      )}

      {/* MODALS */}
      {showModal && (
        <TaskModal
          task={editingTask}
          onClose={() => setShowModal(false)}
          onSuccess={() => {
            setShowModal(false);
            toast.success("Task saved successfully");
            if (onTasksChanged) onTasksChanged();
            else fetchTasks(true);
          }}
        />
      )}

      {selectedTask && (
        <TaskDetailsModal
          task={selectedTask}
          assignedEmployee={employees.find(
            (e) => Number(e.emp_id) === Number(selectedTask.assigned_to)
          )}
          onClose={() => setSelectedTask(null)}
          onUpdate={() => {
            toast.success("Task updated successfully");
            if (onTasksChanged) onTasksChanged();
            else fetchTasks(true);
          }}
        />
      )}

      {selectedNotificationsTask && (
        <div className="fixed inset-0 z-50 flex items-center justify-center">
          <div
            className="absolute inset-0 bg-black/40"
            onClick={() => setSelectedNotificationsTask(null)}
          />
          <div className="relative bg-white rounded-lg p-6 shadow-lg w-full max-w-md z-10">
            <div className="flex justify-between items-center mb-4">
              <h4 className="text-lg font-semibold">Notifications</h4>
              <button
                onClick={() => setSelectedNotificationsTask(null)}
                className="text-slate-500"
              >
                Close
              </button>
            </div>
            <div className="space-y-3 max-h-56 overflow-auto">
              {selectedNotificationsTask.notifications &&
              selectedNotificationsTask.notifications.length > 0 ? (
                selectedNotificationsTask.notifications.map((n, i) => (
                  <div key={i} className="p-2 border rounded">
                    <p className="text-sm text-slate-700">{n}</p>
                  </div>
                ))
              ) : selectedNotificationsTask.remarks &&
                selectedNotificationsTask.remarks.length > 0 ? (
                selectedNotificationsTask.remarks.map((r, i) => (
                  <div key={i} className="p-2 border rounded">
                    <p className="text-sm text-slate-700">{r}</p>
                  </div>
                ))
              ) : (
                <p className="text-sm text-slate-500">No notifications</p>
              )}
            </div>
          </div>
        </div>
      )}
    </div>
  );
};

export default TasksPage;
