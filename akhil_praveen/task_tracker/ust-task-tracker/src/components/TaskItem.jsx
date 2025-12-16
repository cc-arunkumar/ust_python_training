import React from 'react';
import { CheckCircle2, Circle, Edit2, Trash2 } from 'lucide-react';

function TaskItem({
  task,
  isEditing,
  editingTask,
  onEdit,
  onUpdate,
  onDelete,
  onCancelEdit,
  setEditingTask
}) {
  const toggleComplete = () => {
    onUpdate(task.id, {
      title: task.title,
      description: task.description,
      completed: !task.completed
    });
  };

  if (isEditing) {
    return (
      <div className="bg-white border-2 border-indigo-300 rounded-lg p-5">
        <div className="space-y-3">
          <input
            type="text"
            value={editingTask.title}
            onChange={(e) => setEditingTask({ ...editingTask, title: e.target.value })}
            className="w-full px-4 py-2 rounded-lg border border-gray-300 focus:ring-2 focus:ring-indigo-500"
          />
          <textarea
            value={editingTask.description}
            onChange={(e) => setEditingTask({ ...editingTask, description: e.target.value })}
            className="w-full px-4 py-2 rounded-lg border border-gray-300 focus:ring-2 focus:ring-indigo-500 resize-none"
            rows="2"
          />
          <div className="flex gap-2">
            <button
              onClick={() => onUpdate(editingTask.id, {
                title: editingTask.title,
                description: editingTask.description,
                completed: editingTask.completed
              })}
              className="px-4 py-2 bg-indigo-600 text-white rounded-lg hover:bg-indigo-700 transition-colors text-sm font-medium"
            >
              Save
            </button>
            <button
              onClick={onCancelEdit}
              className="px-4 py-2 bg-gray-200 text-gray-700 rounded-lg hover:bg-gray-300 transition-colors text-sm font-medium"
            >
              Cancel
            </button>
          </div>
        </div>
      </div>
    );
  }

  return (
    <div
      className={`group bg-white border-2 rounded-lg p-5 transition-all hover:shadow-lg ${
        task.completed
          ? 'border-green-200 bg-green-50'
          : 'border-gray-200 hover:border-indigo-300'
      }`}
    >
      <div className="flex items-start gap-4">
        <button
          onClick={toggleComplete}
          className="mt-1 shrink-0 transition-transform hover:scale-110"
        >
          {task.completed ? (
            <CheckCircle2 className="text-green-600" size={24} />
          ) : (
            <Circle className="text-gray-400 hover:text-indigo-500" size={24} />
          )}
        </button>
        
        <div className="flex-1">
          <h3
            className={`text-lg font-semibold mb-1 ${
              task.completed ? 'text-gray-500 line-through' : 'text-gray-800'
            }`}
          >
            {task.title}
          </h3>
          <p className={`text-sm ${task.completed ? 'text-gray-400' : 'text-gray-600'}`}>
            {task.description || 'No description'}
          </p>
        </div>
        
        <div className="flex gap-2 opacity-0 group-hover:opacity-100 transition-opacity">
          <button
            onClick={() => onEdit(task)}
            className="p-2 text-indigo-600 hover:bg-indigo-100 rounded-lg transition-colors"
          >
            <Edit2 size={18} />
          </button>
          <button
            onClick={() => onDelete(task.id)}
            className="p-2 text-red-600 hover:bg-red-100 rounded-lg transition-colors"
          >
            <Trash2 size={18} />
          </button>
        </div>
      </div>
    </div>
  );
}

export default TaskItem;