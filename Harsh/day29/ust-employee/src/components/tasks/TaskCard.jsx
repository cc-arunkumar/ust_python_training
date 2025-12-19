import React, { useState, useRef, useEffect } from "react";
import { Draggable } from "@hello-pangea/dnd";
import { Eye, Trash, Edit, User, Bell } from "lucide-react";
import { PRIORITY_COLORS } from "../../utils/constants";
import toast from "react-hot-toast";
import ApiService from "../../services/api";

const TaskCard = ({
  task,
  index,
  onView,
  onEdit,
  onDelete,
  assignedEmployee,
  onAttach,
}) => {
  const [showNotes, setShowNotes] = useState(false);
  const [notifications, setNotifications] = useState([]);
  const popoverRef = useRef(null);
  // attach handled in edit modal (TaskModal)

  useEffect(() => {
    if (!showNotes) return;

    const handleOutside = (e) => {
      if (popoverRef.current && !popoverRef.current.contains(e.target)) {
        setShowNotes(false);
      }
    };

    const handleKey = (e) => {
      if (e.key === "Escape") setShowNotes(false);
    };

    document.addEventListener("mousedown", handleOutside);
    document.addEventListener("keydown", handleKey);

    return () => {
      document.removeEventListener("mousedown", handleOutside);
      document.removeEventListener("keydown", handleKey);
    };
  }, [showNotes]);

  // Fetch notifications for this task (best-effort). Merge with any task.notifications
  useEffect(() => {
    let mounted = true;

    const loadNotifications = async () => {
      if (!task || !task.task_id) return;
      try {
        const remote = await ApiService.getNotificationsForTask(task.task_id);
        if (!mounted) return;

        // Prefer backend notifications if available; fallback to task.notifications
        if (Array.isArray(remote) && remote.length > 0) {
          setNotifications(remote);
        } else if (task.notifications && task.notifications.length > 0) {
          // If backend doesn't have notifications endpoint, use task.notifications array
          setNotifications(
            task.notifications.map((n) => ({ message: n, is_read: false }))
          );
        } else {
          setNotifications([]);
        }
      } catch (err) {
        // ignore
        setNotifications([]);
      }
    };

    loadNotifications();

    return () => {
      mounted = false;
    };
  }, [task]);

  const handleOpenNotes = async () => {
    setShowNotes(true);

    // Best-effort: mark notifications read in backend and update local state
    try {
      await ApiService.markNotificationsReadForTask(task.task_id);
      setNotifications((prev) => prev.map((n) => ({ ...n, is_read: true })));
    } catch (err) {
      // ignore failure
    }
  };
  const handleDelete = () => {
    if (!onDelete) return;
    const confirm = window.confirm(
      "Are you sure you want to delete this task?"
    );
    if (!confirm) return;
    onDelete(task.task_id);
  };

  // NOTE: Attach action moved to TaskModal (edit). Keeping placeholder prop for compatibility.

  const formatDate = (dateString) => {
    if (!dateString) return "No deadline";
    return new Date(dateString).toLocaleDateString("en-US", {
      month: "short",
      day: "numeric",
      year: "numeric",
    });
  };

  return (
    <Draggable draggableId={task.task_id.toString()} index={index}>
      {(provided, snapshot) => (
        <div
          ref={provided.innerRef}
          {...provided.draggableProps}
          {...provided.dragHandleProps}
          style={{ ...(provided.draggableProps?.style || {}) }}
          className={`relative bg-white rounded-lg shadow-sm p-4 flex flex-col transition-transform duration-150 ease-out ${
            snapshot.isDragging ? "scale-105 shadow-xl z-50" : "hover:shadow-md"
          }`}
        >
          {/* Header: title left, bell (notifications) top-right */}
          <div className="flex justify-between items-start mb-2">
            <h4 className="text-sm font-semibold text-gray-800 line-clamp-1">
              {task.title}
            </h4>
            <div className="relative">
              {
                (() => {
                  const remarksCount = (task.remarks && task.remarks.length) || 0;
                  const unreadNotifications = Array.isArray(notifications)
                    ? notifications.filter((n) => !n.is_read).length
                    : 0;
                  const totalBadge = unreadNotifications + remarksCount;

                  return (
                    <>
                      <button
                        onClick={handleOpenNotes}
                        aria-label={totalBadge > 0 ? "Has notifications" : "No notifications"}
                        className={`p-2 rounded-md transition-colors ${
                          totalBadge > 0 ? "text-red-600 animate-pulse" : "text-slate-400"
                        }`}
                      >
                        <Bell size={18} />
                      </button>

                      {totalBadge > 0 && (
                        <span className="absolute -top-1 -right-1 bg-red-600 text-white text-[11px] rounded-full w-5 h-5 flex items-center justify-center">
                          {totalBadge}
                        </span>
                      )}
                    </>
                  );
                })()
              }
            </div>
          </div>

          {/* Description */}
          {task.description && (
            <p className="text-gray-500 text-sm line-clamp-2 mb-2">
              {task.description}
            </p>
          )}

          {/* Avatar, Priority and Deadline */}
          <div className="flex items-center gap-3 mb-2 text-xs text-gray-500">
            <div className="w-9 h-9 rounded-full bg-slate-100 overflow-hidden flex items-center justify-center text-slate-700 font-semibold">
              {assignedEmployee && assignedEmployee.avatar ? (
                <img
                  src={assignedEmployee.avatar}
                  alt={assignedEmployee.emp_name || "avatar"}
                  className="w-full h-full object-cover"
                />
              ) : assignedEmployee && assignedEmployee.emp_name ? (
                <span className="uppercase">
                  {assignedEmployee.emp_name.charAt(0)}
                </span>
              ) : (
                <User size={14} />
              )}
            </div>

            {task.priority && (
              <span
                className={`inline-block px-2 py-1 rounded-full text-xs font-medium ${
                  PRIORITY_COLORS[task.priority.toLowerCase()]
                }`}
              >
                {task.priority}
              </span>
            )}

            {/* deadline shown after priority */}
            {task.priority && (
              <div className="ml-auto text-right">
                <div className="text-xs text-slate-500">
                  {formatDate(task.expected_closure)}
                </div>
              </div>
            )}
          </div>

          {/* Notifications popover (anchored to bell) */}
          {showNotes && (
            <div
              ref={popoverRef}
              className="absolute top-10 right-2 z-50 w-72 bg-white border border-slate-200 rounded-md shadow-lg p-3"
            >
              <div className="flex justify-between items-center mb-2">
                <h4 className="text-sm font-semibold">Notifications</h4>
                <button
                  onClick={() => setShowNotes(false)}
                  className="text-slate-500"
                >
                  Close
                </button>
              </div>
              <div className="space-y-2 max-h-44 overflow-auto">
                {notifications && notifications.length > 0 ? (
                  notifications.map((n, i) => (
                    <div key={`n-${i}`} className="p-2 border rounded flex items-start gap-2">
                      <div className={`w-2 h-2 rounded-full mt-1 ${n.is_read ? 'bg-slate-300' : 'bg-blue-500'}`} />
                      <div>
                        <p className="text-sm text-slate-700">{n.message || n.msg || n.text}</p>
                        <div className="text-xs text-slate-400">{n.created_at ? new Date(n.created_at).toLocaleString() : ''}</div>
                      </div>
                    </div>
                  ))
                ) : task.remarks && task.remarks.length > 0 ? (
                  task.remarks.map((r, i) => (
                    <div key={`r-${i}`} className="p-2 border rounded">
                      <p className="text-sm text-slate-700">{r}</p>
                    </div>
                  ))
                ) : (
                  <p className="text-sm text-slate-500">No notifications</p>
                )}
              </div>
            </div>
          )}

          {/* Actions */}
          <div className="mt-2 flex gap-2">
            {onView && (
              <button
                onClick={() => onView(task)}
                className="flex-1 flex items-center justify-center gap-1 text-blue-600 text-xs font-medium rounded-lg py-1 hover:bg-blue-50 transition"
              >
                <Eye size={14} /> View
              </button>
            )}

            {onEdit && (
              <button
                onClick={() => onEdit(task)}
                className="flex-1 flex items-center justify-center gap-1 text-green-600 text-xs font-medium rounded-lg py-1 hover:bg-green-50 transition"
              >
                <Edit size={14} /> Edit
              </button>
            )}

            {onDelete && (
              <button
                onClick={handleDelete}
                className="flex-1 flex items-center justify-center gap-1 text-red-600 text-xs font-medium rounded-lg py-1 hover:bg-red-50 transition"
              >
                <Trash size={14} /> Delete
              </button>
            )}
          </div>
        </div>
      )}
    </Draggable>
  );
};

export default TaskCard;
