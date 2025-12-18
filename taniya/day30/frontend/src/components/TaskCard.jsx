import PriorityBadge from "./PriorityBadge";
import { apiService } from "../services/api";
import { useState } from "react";
import { useToast } from "./Toast";

const TaskCard = ({
  task,
  selectedRole,
  currentUser,
  authToken,
  onStatusChange,
}) => {
  const canEmployeeUpdate =
    selectedRole === "EMPLOYEE" && currentUser?.emp_id === task.assigned_to;
  const canManagerUpdate =
    selectedRole === "MANAGER" || selectedRole === "ADMIN";

  const nextForEmployee = () => {
    if (task.status === "TO_DO") return "IN_PROGRESS";
    if (task.status === "IN_PROGRESS") return "REVIEW";
    return null;
  };

  const [isUpdating, setIsUpdating] = useState(false);
  const toast = useToast();

  const handleChangeStatus = async (newStatus) => {
    if (!newStatus) return;
    setIsUpdating(true);
    try {
      const updated = await apiService.updateTaskStatus(
        task.id,
        newStatus,
        authToken
      );
      if (onStatusChange) onStatusChange(updated);
      toast.show("Task updated", "success");
    } catch (err) {
      console.error("Failed to update status", err);
      toast.show("Failed to update status: " + (err.message || ""), "error");
    } finally {
      setIsUpdating(false);
    }
  };

  return (
    <div className="bg-white rounded-lg p-4 shadow-sm hover:shadow-md transition-all cursor-pointer border border-gray-100">
      <div className="flex items-start justify-between gap-4">
        <div className="flex-1">
          <h4 className="font-medium text-gray-900 mb-1 line-clamp-1">
            {task.title}
          </h4>
          <p className="text-sm text-gray-600 mb-2 line-clamp-2">
            {task.description}
          </p>
          <div className="flex items-center gap-3 text-xs text-gray-500 mb-2">
            <span className="bg-gray-50 px-2 py-1 rounded">
              Assigned: {task.assigned_to}
            </span>
            {task.due_date && (
              <span className="bg-gray-50 px-2 py-1 rounded">
                Due: {new Date(task.due_date).toLocaleDateString()}
              </span>
            )}
          </div>

          <div className="flex items-center gap-2">
            <span className="text-xs px-2 py-1 rounded border bg-gray-50">
              {task.status}
            </span>
            {canEmployeeUpdate && nextForEmployee() && (
              <button
                onClick={() => handleChangeStatus(nextForEmployee())}
                className="px-3 py-1 text-sm bg-blue-600 text-white rounded"
                disabled={isUpdating}
              >
                {isUpdating
                  ? "Updating..."
                  : task.status === "TO_DO"
                  ? "Start"
                  : "Submit for Review"}
              </button>
            )}
          </div>
        </div>

        <div className="flex flex-col items-end gap-3">
          <PriorityBadge priority={task.priority} />

          {canManagerUpdate && task.status === "REVIEW" && (
            <div className="flex items-center gap-2">
              <button
                onClick={() => handleChangeStatus("IN_PROGRESS")}
                className="px-2 py-1 bg-yellow-500 text-white rounded text-sm"
                disabled={isUpdating}
              >
                {isUpdating ? "Updating..." : "Back to In Progress"}
              </button>
              <button
                onClick={() => handleChangeStatus("DONE")}
                className="px-2 py-1 bg-green-600 text-white rounded text-sm"
                disabled={isUpdating}
              >
                {isUpdating ? "Updating..." : "Mark Done"}
              </button>
            </div>
          )}
        </div>
      </div>
    </div>
  );
};

export default TaskCard;
