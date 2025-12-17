import React from 'react';
import TaskCard from './TaskCard';

const KanbanColumn = ({ status, tasks, onTaskView, onTaskEdit, onQuickStatus, canEdit }) => {
  const statusLabels = {
    TODO: 'TO DO',
    IN_PROGRESS: 'IN PROGRESS',
    IN_QA: 'IN QA',
    DONE: 'DONE'
  };
  
  return (
    <div className="flex-1 min-w-[280px] bg-gray-850 rounded">
      <div className="p-3 border-b border-gray-700">
        <div className="flex items-center justify-between mb-1">
          <h3 className="text-xs font-semibold text-gray-300 uppercase tracking-wide">
            {statusLabels[status] || status}
          </h3>
          <span className="text-xs text-gray-500 bg-gray-700 px-2 py-0.5 rounded">
            {tasks.length}
          </span>
        </div>
      </div>
      
      <div className="p-2 max-h-[calc(100vh-280px)] overflow-y-auto">
        {tasks.length === 0 ? (
          <div className="text-center text-gray-500 text-sm py-8">
            No tasks
          </div>
        ) : (
          tasks.map((task) => (
            <TaskCard
              key={task.task_id}
              task={task}
              onView={onTaskView}
              onEdit={onTaskEdit}
              onQuickStatus={onQuickStatus}
              canEdit={canEdit}
            />
          ))
        )}
      </div>
    </div>
  );
};

export default KanbanColumn;