import React, { useState } from 'react';
import { MoreHorizontal } from 'lucide-react';

const PRIORITY_COLORS = {
  high: 'bg-red-500',
  medium: 'bg-yellow-400',
  low: 'bg-green-500'
};

const TaskCard = ({ task, onView, onEdit, canEdit }) => {
  const [showMenu, setShowMenu] = useState(false);

  return (
    <div
      className="bg-gray-900 rounded-xl shadow-md hover:shadow-lg transition-shadow p-4 sm:p-5 cursor-pointer relative
                 flex flex-col justify-between min-h-[120px] sm:min-h-[140px] w-full sm:w-auto"
    >
      {/* Top Row */}
      <div className="flex items-start justify-between mb-3">
        <span className="text-xs sm:text-sm text-gray-400 font-semibold">#{task.task_id}</span>

        {canEdit && (
          <div className="relative">
            <button
              onClick={(e) => {
                e.stopPropagation();
                setShowMenu(!showMenu);
              }}
              className="text-gray-400 hover:text-white transition-colors"
            >
              <MoreHorizontal size={18} />
            </button>

            {showMenu && (
              <>
                <div
                  className="fixed inset-0 z-10"
                  onClick={() => setShowMenu(false)}
                />
                <div className="absolute right-0 mt-2 w-36 bg-gray-800 rounded-xl shadow-lg border border-gray-700 z-20">
                  <button
                    onClick={(e) => {
                      e.stopPropagation();
                      onEdit(task);
                      setShowMenu(false);
                    }}
                    className="w-full text-left px-4 py-2 text-sm text-gray-200 hover:bg-gray-700 rounded-t-lg transition-colors"
                  >
                    Edit
                  </button>
                  <button
                    onClick={(e) => {
                      e.stopPropagation();
                      onView(task);
                      setShowMenu(false);
                    }}
                    className="w-full text-left px-4 py-2 text-sm text-gray-200 hover:bg-gray-700 rounded-b-lg transition-colors"
                  >
                    View Details
                  </button>
                </div>
              </>
            )}
          </div>
        )}
      </div>

      {/* Title */}
      <h4
        className="text-sm sm:text-base font-semibold text-white mb-3 line-clamp-2"
        onClick={() => onView(task)}
      >
        {task.title}
      </h4>

      {/* Bottom Row */}
      <div className="flex items-center justify-between">
        {/* Priority Badge */}
        {task.priority && (
          <span
            className={`text-xs sm:text-sm font-semibold text-white px-2 py-1 rounded-full ${PRIORITY_COLORS[task.priority]}`}
          >
            {task.priority.toUpperCase()}
          </span>
        )}

        {/* Assigned User */}
        {task.assigned_to && (
          <div className="flex items-center gap-2">
            <div className="w-7 h-7 sm:w-8 sm:h-8 rounded-full bg-gradient-to-br from-indigo-500 to-purple-600
                            flex items-center justify-center text-xs sm:text-sm text-white font-medium">
              {String(task.assigned_to).substring(0, 1).toUpperCase()}
            </div>
            <span className="hidden sm:block text-gray-300 text-sm">
              {task.assigned_to}
            </span>
          </div>
        )}
      </div>
    </div>
  );
};

export default TaskCard;
