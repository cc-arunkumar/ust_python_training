import React from "react";
import { Clock, MessageSquare } from "lucide-react";
import { PRIORITY_COLORS } from "../../utils/constants";
import { formatDate } from "../../utils/helpers";

const TaskCard = ({ task, onStatusChange }) => {
  return (
    <div className="bg-white rounded-lg shadow-md p-4 hover:shadow-lg transition-shadow border border-gray-200">
      <div className="flex items-start justify-between mb-3">
        <h3 className="font-semibold text-gray-900 line-clamp-2">
          {task.title}
        </h3>
        <span
          className={`px-2 py-1 rounded-full text-xs font-semibold ${
            PRIORITY_COLORS[task.priority]
          }`}
        >
          {task.priority}
        </span>
      </div>

      <p className="text-sm text-gray-600 mb-3 line-clamp-2">
        {task.description}
      </p>

      <div className="flex items-center justify-between text-xs text-gray-500">
        <div className="flex items-center gap-1">
          <Clock className="w-3 h-3" />
          <span>{formatDate(task.expected_closure)}</span>
        </div>
        {task.remarks && task.remarks.length > 0 && (
          <div className="flex items-center gap-1">
            <MessageSquare className="w-3 h-3" />
            <span>{task.remarks.length}</span>
          </div>
        )}
      </div>

      {task.status !== "completed" && (
        <button
          onClick={() => onStatusChange(task)}
          className="mt-3 w-full py-2 bg-blue-50 text-blue-600 text-sm font-medium rounded hover:bg-blue-100 transition-colors"
        >
          Move Forward →
        </button>
      )}
    </div>
  );
};

export default TaskCard;
