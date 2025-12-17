import React, { useState } from 'react';
import { CheckCircle2, Circle, Clock, Eye } from 'lucide-react';
import { STATUS_COLORS } from '../../utils/constants';
import TaskCard from './TaskCard';

const TaskBoard = ({ tasks, onStatusChange, onAddRemark, userRole }) => {
  const canEditTasks = ['admin', 'manager', 'developer'].includes(userRole);
  const [draggedTask, setDraggedTask] = useState(null);

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

  const handleDragStart = (e, task) => {
    if (!canEditTasks) return;
    setDraggedTask(task);
    e.dataTransfer.effectAllowed = 'move';
  };

  const isValidTransition = (currentStatus, newStatus, role) => {
    console.log(role)
    // Can't move Done tasks anywhere
    if (currentStatus === 'Done') return false;
    
    // Can't move to the same status
    if (currentStatus === newStatus) return false;

    // Role-based rules
    if (role === 'developer') {
      // Developer: Only In Progress → Review
      return currentStatus === 'In Progress' && newStatus === 'Review';
    }
    
    if (role === 'manager') {
      // Manager: To Do → In Progress, Review → Done, Review → In Progress
      if (currentStatus === 'To Do' && newStatus === 'In Progress') return true;
      if (currentStatus === 'Review' && newStatus === 'Done') return true;
      if (currentStatus === 'Review' && newStatus === 'In Progress') return true;
      return false;
    }
    
    if (role === 'admin') {
      // Admin: Only To Do → In Progress
      return currentStatus === 'To Do' && newStatus === 'In Progress';
    }

    return false;
  };

  const handleDragOver = (e, status) => {
    if (!canEditTasks || !draggedTask) {
      e.preventDefault();
      return;
    }
    
    // Check if this is a valid drop target
    if (isValidTransition(draggedTask.status, status, userRole)) {
      e.preventDefault();
      e.dataTransfer.dropEffect = 'move';
    } else {
      e.dataTransfer.dropEffect = 'none';
    }
  };

  const handleDrop = (e, newStatus) => {
    e.preventDefault();
    if (!canEditTasks || !draggedTask) return;
    
    // Validate the transition before making the change
    if (isValidTransition(draggedTask.status, newStatus, userRole)) {
      onStatusChange(draggedTask._id, newStatus);
    }
    setDraggedTask(null);
  };

  const handleDragEnd = () => {
    setDraggedTask(null);
  };

  return (
    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
      {Object.entries(tasksByStatus).map(([status, statusTasks]) => {
        const isValidDropZone = draggedTask && isValidTransition(draggedTask.status, status, userRole);
        
        return (
          <div
            key={status}
            className={`rounded-xl border-2 ${STATUS_COLORS[status]} p-4 flex flex-col transition-all ${
              isValidDropZone ? 'ring-2 ring-green-400 ring-opacity-50 bg-green-50 bg-opacity-30' : ''
            } ${
              draggedTask && !isValidDropZone && draggedTask.status !== status ? 'opacity-50' : ''
            }`}
            onDragOver={(e) => handleDragOver(e, status)}
            onDrop={(e) => handleDrop(e, status)}
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
                  <div
                    key={task._id}
                    draggable={canEditTasks}
                    onDragStart={(e) => handleDragStart(e, task)}
                    onDragEnd={handleDragEnd}
                    className={`${canEditTasks ? 'cursor-move' : ''} ${
                      draggedTask?._id === task._id ? 'opacity-50' : ''
                    }`}
                  >
                    <TaskCard
                      task={task}
                      onStatusChange={onStatusChange}
                      onAddRemark={onAddRemark}
                      canEdit={canEditTasks}
                    />
                  </div>
                ))
              )}
            </div>
          </div>
        );
      })}
    </div>
  );
};

export default TaskBoard;