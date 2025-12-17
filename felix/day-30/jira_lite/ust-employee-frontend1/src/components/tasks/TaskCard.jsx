import React from 'react';
import { User, Calendar } from 'lucide-react';
import { PRIORITY_COLORS } from '../../utils/constants';
import { formatDate } from '../../utils/helpers';

const TaskCard = ({ task, onStatusChange, canEdit }) => {
  return (
    <div className="bg-white rounded-lg border border-gray-200 p-4 hover:shadow-md transition-all cursor-pointer">
      <div className="flex justify-between items-start mb-3">
        <h3 className="font-semibold text-gray-800 flex-1 pr-2">{task.title}</h3>
        <span className={`text-xs px-2 py-1 rounded-full border ${PRIORITY_COLORS[task.priority]} whitespace-nowrap`}>
          {task.priority}
        </span>
      </div>
      
      <p className="text-sm text-gray-600 mb-3 line-clamp-2">{task.description}</p>
      
      <div className="space-y-2">
        <div className="flex items-center gap-2 text-xs text-gray-500">
          <User className="w-3 h-3 flex-shrink-0" />
          <span className="truncate">{task.assignee_name || `ID: ${task.assigned_to}`}</span>
        </div>
        
        <div className="flex items-center gap-2 text-xs text-gray-500">
          <Calendar className="w-3 h-3 flex-shrink-0" />
          <span>Due: {formatDate(task.expected_completion_date)}</span>
        </div>
      </div>
      
      {canEdit && (
        <div className="mt-3 pt-3 border-t border-gray-100">
          <select
            value={task.status}
            onChange={(e) => onStatusChange(task._id, e.target.value)}
            className="text-xs w-full px-2 py-1.5 border border-gray-300 rounded focus:ring-2 focus:ring-blue-500 outline-none"
            onClick={(e) => e.stopPropagation()}
          >
            <option value="todo">To Do</option>
            <option value="in_progress">In Progress</option>
            <option value="completed">Completed</option>
          </select>
        </div>
      )}

      {task.actual_completion_date && (
        <div className="mt-2 text-xs text-green-600 flex items-center gap-1">
          <span>✓</span>
          <span>Completed: {formatDate(task.actual_completion_date)}</span>
        </div>
      )}
    </div>
  );
};

export default TaskCard;