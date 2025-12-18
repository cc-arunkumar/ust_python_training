import React, { useState } from "react";
import { Draggable } from "@hello-pangea/dnd";
import { Eye, Trash, Edit, User, Bell } from "lucide-react";
import { PRIORITY_COLORS } from "../../utils/constants";
import toast from "react-hot-toast";

const TaskCard = ({
  task,
  index,
  onView,
  onEdit,
  onDelete,
  assignedEmployee,
}) => {
  const [showNotes, setShowNotes] = useState(false);
  const handleDelete = () => {
    if (!onDelete) return;
    const confirm = window.confirm(
      "Are you sure you want to delete this task?"
    );
    if (!confirm) return;
    onDelete(task.task_id);
  };

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
      {(provided) => (
        <div
          ref={provided.innerRef}
          {...provided.draggableProps}
          {...provided.dragHandleProps}
          className="bg-white rounded-lg shadow-sm p-4 flex flex-col hover:shadow-md transition"
        >
          {/* Header: title left, bell (notifications) top-right */}
          <div className="flex justify-between items-start mb-2">
            <h4 className="text-sm font-semibold text-gray-800 line-clamp-1">
              {task.title}
            </h4>
            <div className="relative">
              <button
                onClick={() => setShowNotes(true)}
                aria-label={
                  task.remarks || task.notifications
                    ? "Has notifications"
                    : "No notifications"
                }
                className={`p-2 rounded-md transition-colors ${
                  (task.remarks && task.remarks.length > 0) ||
                  (task.notifications && task.notifications.length > 0)
                    ? "text-red-600 animate-pulse"
                    : "text-slate-400"
                }`}
              >
                <Bell size={18} />
              </button>
              {((task.notifications && task.notifications.length) || 0) +
                ((task.remarks && task.remarks.length) || 0) >
                0 && (
                <span className="absolute -top-1 -right-1 bg-red-600 text-white text-[11px] rounded-full w-5 h-5 flex items-center justify-center">
                  {((task.notifications && task.notifications.length) || 0) +
                    ((task.remarks && task.remarks.length) || 0)}
                </span>
              )}
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

          {/* Notifications modal (task-specific) */}
          {showNotes && (
            <div className="fixed inset-0 z-50 flex items-center justify-center">
              <div
                className="absolute inset-0 bg-black/40"
                onClick={() => setShowNotes(false)}
              />
              <div className="relative bg-white rounded-lg p-6 shadow-lg w-full max-w-md z-10">
                <div className="flex justify-between items-center mb-4">
                  <h4 className="text-lg font-semibold">Notifications</h4>
                  <button
                    onClick={() => setShowNotes(false)}
                    className="text-slate-500"
                  >
                    Close
                  </button>
                </div>
                <div className="space-y-3 max-h-56 overflow-auto">
                  {task.notifications && task.notifications.length > 0 ? (
                    task.notifications.map((n, i) => (
                      <div key={i} className="p-2 border rounded">
                        <p className="text-sm text-slate-700">{n}</p>
                      </div>
                    ))
                  ) : task.remarks && task.remarks.length > 0 ? (
                    task.remarks.map((r, i) => (
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
