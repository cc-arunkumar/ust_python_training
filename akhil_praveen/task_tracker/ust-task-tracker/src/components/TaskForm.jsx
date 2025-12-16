import React, { useState } from 'react';

function TaskForm({ onSubmit, onCancel, loading, initialTask = null }) {
  const [task, setTask] = useState(
    initialTask || { title: '', description: '', completed: false }
  );

  const handleSubmit = () => {
    if (!task.title.trim()) return;
    onSubmit(task);
  };

  const handleKeyPress = (e) => {
    if (e.key === 'Enter' && e.ctrlKey) {
      handleSubmit();
    }
  };

  return (
    <div className="bg-gradient-to-r from-indigo-50 to-purple-50 p-6 rounded-lg mb-6 border-2 border-indigo-200">
      <h3 className="text-lg font-semibold text-gray-800 mb-4">
        {initialTask ? 'Edit Task' : 'Create New Task'}
      </h3>
      <div className="space-y-4">
        <input
          type="text"
          placeholder="Task title..."
          value={task.title}
          onChange={(e) => setTask({ ...task, title: e.target.value })}
          onKeyPress={handleKeyPress}
          className="w-full px-4 py-3 rounded-lg border border-gray-300 focus:ring-2 focus:ring-indigo-500 focus:border-transparent"
        />
        <textarea
          placeholder="Task description..."
          value={task.description}
          onChange={(e) => setTask({ ...task, description: e.target.value })}
          onKeyPress={handleKeyPress}
          className="w-full px-4 py-3 rounded-lg border border-gray-300 focus:ring-2 focus:ring-indigo-500 focus:border-transparent resize-none"
          rows="3"
        />
        <div className="flex gap-3">
          <button
            onClick={handleSubmit}
            disabled={loading}
            className="px-6 py-2 bg-indigo-600 text-white rounded-lg font-semibold hover:bg-indigo-700 transition-colors disabled:opacity-50"
          >
            {initialTask ? 'Update Task' : 'Create Task'}
          </button>
          <button
            onClick={onCancel}
            className="px-6 py-2 bg-gray-200 text-gray-700 rounded-lg font-semibold hover:bg-gray-300 transition-colors"
          >
            Cancel
          </button>
        </div>
      </div>
    </div>
  );
}

export default TaskForm;