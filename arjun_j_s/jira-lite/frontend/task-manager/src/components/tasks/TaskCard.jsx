import React, { useState } from 'react';
import { MoreHorizontal } from 'lucide-react';

const PRIORITY_COLORS = {
  high: 'bg-red-600 text-red-100',
  medium: 'bg-yellow-600 text-yellow-100',
  low: 'bg-green-600 text-green-100'
};

const TaskCard = ({ task, onView, onEdit, onQuickStatus, canEdit }) => {
  const [showMenu, setShowMenu] = useState(false);
  
  return (
    <div className="bg-gray-800 rounded border border-gray-700 hover:border-gray-600 transition-all p-3 mb-2 cursor-pointer group">
      <div className="flex items-start justify-between mb-2">
        <span className="text-xs text-gray-400 font-medium">#{task.task_id}</span>
        <div className="relative">
          {canEdit && (
            <>
              <button
                onClick={(e) => {
                  e.stopPropagation();
                  setShowMenu(!showMenu);
                }}
                className="text-gray-500 hover:text-gray-300 opacity-0 group-hover:opacity-100 transition-opacity"
              >
                <MoreHorizontal size={16} />
              </button>
              {showMenu && (
                <>
                  <div 
                    className="fixed inset-0 z-10" 
                    onClick={() => setShowMenu(false)}
                  />
                  <div className="absolute right-0 mt-1 w-40 bg-gray-700 rounded shadow-lg border border-gray-600 z-20">
                    <button
                      onClick={(e) => {
                        e.stopPropagation();
                        onQuickStatus(task);
                        setShowMenu(false);
                      }}
                      className="w-full text-left px-3 py-2 text-sm text-gray-200 hover:bg-gray-600 rounded-t"
                    >
                      Update Status
                    </button>
                    <button
                      onClick={(e) => {
                        e.stopPropagation();
                        onEdit(task);
                        setShowMenu(false);
                      }}
                      className="w-full text-left px-3 py-2 text-sm text-gray-200 hover:bg-gray-600"
                    >
                      Edit Task
                    </button>
                    <button
                      onClick={(e) => {
                        e.stopPropagation();
                        onView(task);
                        setShowMenu(false);
                      }}
                      className="w-full text-left px-3 py-2 text-sm text-gray-200 hover:bg-gray-600 rounded-b"
                    >
                      View Details
                    </button>
                  </div>
                </>
              )}
            </>
          )}
        </div>
      </div>
      
      <h4 
        className="text-sm text-white mb-3 line-clamp-2 leading-snug"
        onClick={() => onView(task)}
      >
        {task.title}
      </h4>
      
      <div className="flex items-center justify-between">
        <span className={`text-xs font-semibold px-2 py-1 rounded ${PRIORITY_COLORS[task.priority || 'medium']}`}>
          {(task.priority || 'medium').toUpperCase()}
        </span>
        
        {task.assigned_to && (
          <div className="w-6 h-6 rounded-full bg-gradient-to-br from-blue-500 to-purple-600 flex items-center justify-center text-xs text-white font-medium">
            {String(task.assigned_to).substring(0, 1).toUpperCase()}
          </div>
        )}
      </div>
    </div>
  );
};

export default TaskCard;