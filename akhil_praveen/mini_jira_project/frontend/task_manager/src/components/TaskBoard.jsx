import React, { useState } from 'react';
import { Plus, Search, Filter } from 'lucide-react';
import TaskCard from './TaskCard';
import TaskFormModal from './TaskFormModel';
import { STATUS_CONFIG, STATUSES } from '../utils/constants';

function TaskBoard({ tasks, employees, onRefresh, canCreateTasks, onUpdateStatus, onSaveTask, userRole }) {
  const [showTaskForm, setShowTaskForm] = useState(false);
  const [editingTask, setEditingTask] = useState(null);
  const [searchQuery, setSearchQuery] = useState('');
  const [statusFilter, setStatusFilter] = useState('ALL');

  const filteredTasks = tasks.filter((task) => {
    const matchesSearch =
      task.title.toLowerCase().includes(searchQuery.toLowerCase()) ||
      task.description?.toLowerCase().includes(searchQuery.toLowerCase());
    const matchesStatus = statusFilter === 'ALL' || task.status === statusFilter;
    return matchesSearch && matchesStatus;
  });

  const groupedTasks = STATUSES.reduce((acc, status) => {
    acc[status] = filteredTasks.filter((t) => t.status === status);
    return acc;
  }, {});

  const handleEditTask = (task) => {
    setEditingTask(task);
    setShowTaskForm(true);
  };

  const handleCloseForm = () => {
    setShowTaskForm(false);
    setEditingTask(null);
  };

  const handleSaveTask = async (taskData) => {
    await onSaveTask(editingTask, taskData);
    handleCloseForm();
  };

  return (
    <div className="p-6">
      {/* Header */}
      <div className="flex justify-between items-center mb-6">
        <h2 className="text-2xl font-bold">Tasks</h2>
        {canCreateTasks && (
          <button
            onClick={() => setShowTaskForm(true)}
            className="bg-blue-600 text-white px-4 py-2 rounded-lg flex items-center gap-2 hover:bg-blue-700"
          >
            <Plus size={20} />
            New Task
          </button>
        )}
      </div>

      {/* Filters */}
      <div className="flex gap-4 mb-6">
        <div className="relative flex-1">
          <Search className="absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-400" size={20} />
          <input
            type="text"
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
            placeholder="Search tasks..."
            className="w-full pl-10 pr-4 py-2 border rounded-lg focus:ring-2 focus:ring-blue-500"
          />
        </div>

        <div className="flex items-center gap-2">
          <Filter size={20} className="text-gray-600" />
          <select
            value={statusFilter}
            onChange={(e) => setStatusFilter(e.target.value)}
            className="px-3 py-2 border rounded-lg focus:ring-2 focus:ring-blue-500"
          >
            <option value="ALL">All Status</option>
            {STATUSES.map((status) => (
              <option key={status} value={status}>
                {STATUS_CONFIG[status].label}
              </option>
            ))}
          </select>
        </div>
      </div>

      {/* Kanban Board */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
        {STATUSES.map((status) => (
          <div key={status} className="bg-gray-50 rounded-lg p-4">
            <div className="flex items-center justify-between mb-4">
              <h3 className="font-semibold text-gray-700">
                {STATUS_CONFIG[status].label}
              </h3>
              <span className="bg-gray-200 text-gray-700 px-2 py-1 rounded-full text-xs font-medium">
                {groupedTasks[status].length}
              </span>
            </div>

            <div className="space-y-3">
              {groupedTasks[status].map((task) => (
                <TaskCard
                  key={task.task_id}
                  task={task}
                  employees={employees}
                  userRole={userRole}
                  onUpdateStatus={onUpdateStatus}
                  onEdit={() => handleEditTask(task)}
                />
              ))}
              
              {groupedTasks[status].length === 0 && (
                <div className="text-center text-gray-400 py-8 text-sm">
                  No tasks
                </div>
              )}
            </div>
          </div>
        ))}
      </div>

      {/* Task Form Modal */}
      {showTaskForm && (
        <TaskFormModal
          task={editingTask}
          employees={employees}
          onClose={handleCloseForm}
          onSave={handleSaveTask}
        />
      )}
    </div>
  );
}

export default TaskBoard;