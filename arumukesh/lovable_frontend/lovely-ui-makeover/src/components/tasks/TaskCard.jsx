import React from "react";
import { Calendar, User, Clock } from "lucide-react";
import {
  formatDate,
  getDaysRemaining,
  truncateText,
} from "../../utils/helpers";
import { PRIORITY_COLORS } from "../../utils/constants";
import Badge from "../common/Badge";

const TaskCard = ({ task, onClick }) => {
  const daysInfo = getDaysRemaining(task.expected_closure);

  const getPriorityBadgeVariant = (priority) => {
    switch (priority) {
      case "high":
        return "danger";
      case "medium":
        return "warning";
      case "low":
        return "success";
      default:
        return "default";
    }
  };

  // Compact card: show title, due, priority. Expand on hover to show assignee & reviewer.
  return (
    <div
      onClick={onClick}
      className={`group bg-white p-3 rounded-none border border-gray-200 cursor-pointer transition-shadow duration-200 hover:shadow-md ${
        PRIORITY_COLORS[task.priority]
      }`}
      style={{ overflow: "hidden" }}
    >
      <div className="flex items-center justify-between">
        <h4 className="font-semibold text-gray-900 truncate max-w-[150px]">
          {task.title}
        </h4>
        <Badge variant={getPriorityBadgeVariant(task.priority)} size="small">
          {task.priority.toUpperCase()}
        </Badge>
      </div>

      <div className="mt-2 text-xs text-gray-500 flex items-center justify-between">
        <div
          className={`flex items-center gap-2 ${
            daysInfo?.isOverdue
              ? "text-red-600 font-medium"
              : daysInfo?.isDueToday
              ? "text-yellow-600 font-medium"
              : ""
          }`}
        >
          <Clock className="w-3 h-3" />
          <span>{daysInfo ? daysInfo.text : "No due date"}</span>
        </div>
      </div>

      {/* Hidden extra info: reveal on hover */}
      <div className="mt-2 text-xs text-gray-500 max-h-0 overflow-hidden group-hover:max-h-28 transition-all duration-200">
        <div className="flex items-center gap-2 mt-2">
          <User className="w-3 h-3" />
          <span>Assignee: {task.assigned_to}</span>
        </div>
        <div className="flex items-center gap-2 mt-1">
          <User className="w-3 h-3" />
          <span>Reviewer: {task.reviewer}</span>
        </div>
      </div>
    </div>
  );
};

export default TaskCard;
