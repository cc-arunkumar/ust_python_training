import React, { useState } from 'react';
import TaskItem from './TaskItem';
import { Circle } from 'lucide-react';

function TaskList({ tasks, onUpdate, onDelete }) {
  const [editingTask, setEditingTask] = useState(null);

  const handleEdit = (task) => {
    setEditingTask(task);
  };

  const handleUpdate = (taskId, updates) => {
    onUpdate(taskId, updates);
    setEditingTask(null);
  };

  const handleCancelEdit = () => {
    setEditingTask(null);
  };

  if (tasks.length === 0) {
    return (
      <div className="text-center py-12">
        <Circle className="mx-auto text-gray-300 mb-4" size={48} />
        <p className="text-gray-500 text-lg">No tasks found</p>
        <p className="text-gray-400 text-sm">Create your first task to get started!</p>
      </div>
    );
  }

  return (
    <div className="space-y-3">
      {tasks.map((task) => (
        <TaskItem
          key={task.id}
          task={task}
          isEditing={editingTask?.id === task.id}
          editingTask={editingTask}
          onEdit={handleEdit}
          onUpdate={handleUpdate}
          onDelete={onDelete}
          onCancelEdit={handleCancelEdit}
          setEditingTask={setEditingTask}
        />
      ))}
    </div>
  );
}

export default TaskList;