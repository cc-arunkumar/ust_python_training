import React from 'react';
import { CheckCircle2, Circle, Clock, Eye } from 'lucide-react';
import { STATUS_COLORS } from '../../utils/constants';
import TaskCard from './TaskCard';

const TaskBoard = ({ tasks, onStatusChange, onAddRemark, userRole }) => {
  const canEditTasks = ['admin', 'manager', 'developer'].includes(userRole);

  const tasksByStatus = {
    'To Do': tasks.filter(t => t.status === 'To Do'),
    'In Progress': tasks.filter(t => t.status === 'In Progress'),
    'Review': tasks.filter(t => t.status === 'Review'),
    'Done': tasks.filter(t => t.status === 'Done')
  };

  const statusIcons = {
    'To Do': <Circle className="text-gray-400" size={20} />,
    'In Progress': <Clock className="text-blue-500" size={20} />,
    'Review': <Eye className="text-purple-500" size={20} />,
    'Done': <CheckCircle2 className="text-green-500" size={20} />
  };

  return (
    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
      {Object.entries(tasksByStatus).map(([status, statusTasks]) => (
        <div
          key={status}
          className={`rounded-xl border-2 ${STATUS_COLORS[status]} p-4 flex flex-col`}
        >
          {/* Header */}
          <div className="flex items-center justify-between mb-4">
            <div className="flex items-center gap-2">
              {statusIcons[status]}
              <h2 className="font-bold text-gray-900">{status}</h2>
            </div>
            <span className="bg-white px-2 py-1 rounded-full text-sm font-semibold text-gray-700">
              {statusTasks.length}
            </span>
          </div>

          {/* Task list (flexible height, no scrollbars) */}
          <div className="space-y-3">
            {statusTasks.length === 0 ? (
              <div className="text-center py-8 text-gray-400">
                <Circle size={32} className="mx-auto mb-2 opacity-50" />
                <p className="text-sm">No tasks</p>
              </div>
            ) : (
              statusTasks.map(task => (
                <TaskCard
                  key={task._id}
                  task={task}
                  onStatusChange={onStatusChange}
                  onAddRemark={onAddRemark}
                  canEdit={canEditTasks}
                />
              ))
            )}
          </div>
        </div>
      ))}
    </div>
  );
};

export default TaskBoard;