import React from 'react';
import { CheckCircle, Circle, Trash2, Edit2 } from 'lucide-react';

export const TaskItem = ({ task, onToggle, onEdit, onDelete }) => {
  return (
    <div className="bg-white rounded-xl shadow-sm border border-gray-200 p-4 hover:shadow-md transition-shadow">
      <div className="flex items-start gap-3">
        <button
          onClick={() => onToggle(task)}
          className="mt-1 flex-shrink-0"
        >
          {task.completed ? (
            <CheckCircle className="text-green-500" size={24} />
          ) : (
            <Circle className="text-gray-400" size={24} />
          )}
        </button>
        
        <div className="flex-1 min-w-0">
          <h3 className={`font-semibold text-gray-800 ${task.completed ? 'line-through text-gray-500' : ''}`}>
            {task.title}
          </h3>
          <p className={`text-sm mt-1 ${task.completed ? 'line-through text-gray-400' : 'text-gray-600'}`}>
            {task.description}
          </p>
        </div>
        
        <div className="flex gap-2 flex-shrink-0">
          <button
            onClick={() => onEdit(task)}
            className="p-2 text-blue-600 hover:bg-blue-50 rounded-lg transition-colors"
          >
            <Edit2 size={18} />
          </button>
          <button
            onClick={() => onDelete(task.id)}
            className="p-2 text-red-600 hover:bg-red-50 rounded-lg transition-colors"
          >
            <Trash2 size={18} />
          </button>
        </div>
      </div>
    </div>
  );
};