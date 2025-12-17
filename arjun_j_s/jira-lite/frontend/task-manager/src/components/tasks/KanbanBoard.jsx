import React, { useState, useEffect } from 'react';
import { Plus, Search, Filter, AlertCircle, ChevronDown } from 'lucide-react';
import { useAuth } from '../../context/AuthContext';
import ApiService from '../../services/api';
import TaskModal from './TaskModal';
import TaskDetailsModal from './TaskDetailsModal';
import QuickStatusModal from './QuickStatusModal';
import KanbanColumn from './KanbanColumn';
import { TASK_STATUSES } from '../../utils/constants';

const KanbanBoard = () => {
  const [tasks, setTasks] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const [selectedTask, setSelectedTask] = useState(null);
  const [editingTask, setEditingTask] = useState(null);
  const [quickStatusTask, setQuickStatusTask] = useState(null);
  const [showCreateModal, setShowCreateModal] = useState(false);
  const [searchQuery, setSearchQuery] = useState('');
  const { hasRole } = useAuth();
  
  const canEdit = hasRole('ADMIN') || hasRole('MANAGER');

  useEffect(() => {
    fetchTasks();
  }, []);

  const fetchTasks = async () => {
    try {
      setError('');
      const data = await ApiService.getTasks();
      setTasks(data);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };
  
  const getTasksByStatus = (status) => {
    let filtered = tasks.filter(task => task.status === status);
    
    if (searchQuery) {
      filtered = filtered.filter(task => 
        task.title.toLowerCase().includes(searchQuery.toLowerCase()) ||
        task.description?.toLowerCase().includes(searchQuery.toLowerCase()) ||
        task.task_id.toString().includes(searchQuery)
      );
    }
    
    return filtered;
  };

  const handleEdit = (task) => {
    setEditingTask(task);
  };

  const handleView = (task) => {
    setSelectedTask(task);
  };

  const handleQuickStatus = (task) => {
    setQuickStatusTask(task);
  };

  const handleModalClose = () => {
    setEditingTask(null);
    setShowCreateModal(false);
  };

  const handleModalSuccess = () => {
    setEditingTask(null);
    setShowCreateModal(false);
    fetchTasks();
  };

  if (loading) {
    return (
      <div className="min-h-screen bg-gray-900 flex items-center justify-center">
        <div className="text-center">
          <div className="inline-block animate-spin rounded-full h-8 w-8 border-b-2 border-blue-500"></div>
          <p className="mt-2 text-gray-400">Loading board...</p>
        </div>
      </div>
    );
  }
  
  return (
    <div className="min-h-screen bg-gray-900 text-white">
      {/* Header */}
      <div className="border-b border-gray-800 bg-gray-850 px-6 py-3">
        <div className="flex items-center justify-between">
          <div className="flex items-center gap-4">
            <h1 className="text-lg font-semibold">Board</h1>
            <div className="flex items-center gap-2">
              <div className="relative">
                <input
                  type="text"
                  placeholder="Search tasks..."
                  value={searchQuery}
                  onChange={(e) => setSearchQuery(e.target.value)}
                  className="bg-gray-800 border border-gray-700 rounded px-3 py-1.5 text-sm w-64 focus:ring-2 focus:ring-blue-500 outline-none"
                />
                <Search className="absolute right-3 top-2 text-gray-500 pointer-events-none" size={16} />
              </div>
            </div>
          </div>
          
          <div className="flex items-center gap-3">
            <button className="flex items-center gap-1 px-3 py-1.5 text-sm text-gray-300 hover:bg-gray-800 rounded transition">
              <Filter size={16} />
              Filter
            </button>
            <button className="flex items-center gap-1 px-3 py-1.5 text-sm text-gray-300 hover:bg-gray-800 rounded transition">
              Group by
              <ChevronDown size={16} />
            </button>
            {canEdit && (
              <button
                onClick={() => setShowCreateModal(true)}
                className="flex items-center gap-1 px-3 py-1.5 text-sm bg-blue-600 hover:bg-blue-700 rounded transition"
              >
                <Plus size={16} />
                Create
              </button>
            )}
          </div>
        </div>
      </div>

      {/* Error Message */}
      {error && (
        <div className="mx-6 mt-4 bg-red-900 bg-opacity-50 border border-red-700 text-red-200 px-4 py-3 rounded flex items-center gap-2">
          <AlertCircle size={20} />
          <span>{error}</span>
        </div>
      )}
      
      {/* Kanban Board */}
      <div className="p-6">
        <div className="flex gap-4 overflow-x-auto pb-4">
          {Object.values(TASK_STATUSES).map((status) => (
            <KanbanColumn
              key={status}
              status={status}
              tasks={getTasksByStatus(status)}
              onTaskView={handleView}
              onTaskEdit={canEdit ? handleEdit : null}
              onQuickStatus={canEdit ? handleQuickStatus : null}
              canEdit={canEdit}
            />
          ))}
        </div>
      </div>
      
      {/* Modals */}
      {selectedTask && (
        <TaskDetailsModal
          task={selectedTask}
          onClose={() => setSelectedTask(null)}
          onUpdate={fetchTasks}
        />
      )}
      
      {quickStatusTask && (
        <QuickStatusModal
          task={quickStatusTask}
          onClose={() => setQuickStatusTask(null)}
          onUpdate={fetchTasks}
        />
      )}
      
      {(editingTask || showCreateModal) && (
        <TaskModal
          task={editingTask}
          onClose={handleModalClose}
          onSuccess={handleModalSuccess}
        />
      )}
    </div>
  );
};

export default KanbanBoard;