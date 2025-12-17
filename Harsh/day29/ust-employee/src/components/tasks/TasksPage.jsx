import React, { useState, useEffect } from 'react';
import { Plus, Eye, AlertCircle, Calendar, User } from 'lucide-react';
import { useAuth } from '../../context/AuthContext';
import ApiService from '../../services/api';
import TaskModal from './TaskModal';
import TaskDetailsModal from './TaskDetailsModal';
import { STATUS_COLORS } from '../../utils/constants';

const TasksPage = () => {
  const [tasks, setTasks] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const [showModal, setShowModal] = useState(false);
  const [editingTask, setEditingTask] = useState(null);
  const [selectedTask, setSelectedTask] = useState(null);
  const { hasRole } = useAuth();

  const canCreate = hasRole('ADMIN') || hasRole('MANAGER');

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

  const handleAdd = () => {
    setEditingTask(null);
    setShowModal(true);
  };

  const handleView = (task) => {
    setSelectedTask(task);
  };

  const formatDate = (dateString) => {
    if (!dateString) return 'No deadline';
    return new Date(dateString).toLocaleDateString('en-US', {
      year: 'numeric',
      month: 'short',
      day: 'numeric'
    });
  };

  if (loading) {
    return (
      <div className="p-8 text-center">
        <div className="inline-block animate-spin rounded-full h-8 w-8 border-b-2 border-blue-500"></div>
        <p className="mt-2 text-gray-400">Loading tasks...</p>
      </div>
    );
  }

  return (
    <div className="p-8">
      <div className="flex justify-between items-center mb-6">
        <div>
          <h1 className="text-3xl font-bold text-white">Tasks</h1>
          <p className="text-gray-400 mt-1">Manage and track your team's tasks</p>
        </div>
        {canCreate && (
          <button
            onClick={handleAdd}
            className="bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700 transition flex items-center gap-2 shadow-lg"
          >
            <Plus size={20} />
            Create Task
          </button>
        )}
      </div>

      {error && (
        <div className="bg-red-900 bg-opacity-50 border border-red-700 text-red-200 px-4 py-3 rounded mb-4 flex items-center gap-2">
          <AlertCircle size={20} />
          <span>{error}</span>
        </div>
      )}

      {tasks.length === 0 ? (
        <div className="bg-gray-800 rounded-lg shadow-xl border border-gray-700 p-8 text-center">
          <p className="text-gray-400">No tasks found</p>
          {canCreate && (
            <button
              onClick={handleAdd}
              className="mt-4 text-blue-400 hover:text-blue-300 font-medium"
            >
              Create your first task
            </button>
          )}
        </div>
      ) : (
        <div className="grid gap-4">
          {tasks.map((task) => (
            <div
              key={task.task_id}
              className="bg-gray-800 rounded-lg shadow-xl border border-gray-700 hover:border-gray-600 transition-all p-6"
            >
              <div className="flex justify-between items-start">
                <div className="flex-1">
                  <div className="flex items-start justify-between mb-2">
                    <h3 className="text-lg font-semibold text-white">
                      {task.title}
                    </h3>
                    <span className={`px-3 py-1 rounded-full text-xs font-medium ml-4 ${STATUS_COLORS[task.status]}`}>
                      {task.status.replace('_', ' ')}
                    </span>
                  </div>
                  
                  {task.description && (
                    <p className="text-gray-400 mb-3 line-clamp-2">
                      {task.description}
                    </p>
                  )}
                  
                  <div className="flex flex-wrap gap-4 text-sm text-gray-400">
                    <div className="flex items-center gap-1">
                      <User size={16} />
                      <span>
                        Assigned: {task.assigned_to ? `#${task.assigned_to}` : 'Unassigned'}
                      </span>
                    </div>
                    
                    {task.reviewer && (
                      <div className="flex items-center gap-1">
                        <User size={16} />
                        <span>Reviewer: #{task.reviewer}</span>
                      </div>
                    )}
                    
                    <div className="flex items-center gap-1">
                      <Calendar size={16} />
                      <span>{formatDate(task.expected_closure)}</span>
                    </div>
                  </div>
                </div>
                
                <button
                  onClick={() => handleView(task)}
                  className="ml-4 text-blue-400 hover:text-blue-300 transition p-2 hover:bg-gray-700 rounded-lg"
                  title="View details"
                >
                  <Eye size={20} />
                </button>
              </div>
            </div>
          ))}
        </div>
      )}

      {showModal && (
        <TaskModal
          task={editingTask}
          onClose={() => setShowModal(false)}
          onSuccess={() => {
            setShowModal(false);
            fetchTasks();
          }}
        />
      )}

      {selectedTask && (
        <TaskDetailsModal
          task={selectedTask}
          onClose={() => setSelectedTask(null)}
          onUpdate={fetchTasks}
        />
      )}
    </div>
  );
};

export default TasksPage;