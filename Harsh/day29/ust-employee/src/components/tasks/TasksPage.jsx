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

  const formatDate = (dateString) => {
    if (!dateString) return 'No deadline';
    return new Date(dateString).toLocaleDateString('en-US', {
      month: 'short',
      day: 'numeric',
      year: 'numeric'
    });
  };

  /* ---------- LOADING ---------- */
  if (loading) {
    return (
      <div className="flex flex-col items-center justify-center py-24">
        <div className="animate-spin rounded-full h-10 w-10 border-b-2 border-blue-500" />
        <p className="mt-4 text-slate-500">Fetching tasks…</p>
      </div>
    );
  }

  return (
    <div className="max-w-7xl mx-auto px-6 py-8">

      {/* PAGE HEADER */}
      <div className="flex flex-wrap items-center justify-between gap-4 mb-8">
        <div>
          <h1 className="text-3xl font-semibold text-slate-800">
            Task Overview
          </h1>
          <p className="text-slate-500 mt-1">
            Monitor assignments and team progress
          </p>
        </div>

        {canCreate && (
          <button
            onClick={() => {
              setEditingTask(null);
              setShowModal(true);
            }}
            className="flex items-center gap-2 bg-blue-600 text-white
                       px-5 py-2.5 rounded-xl shadow-sm
                       hover:bg-blue-700 transition"
          >
            <Plus size={18} />
            New Task
          </button>
        )}
      </div>

      {/* ERROR */}
      {error && (
        <div className="mb-6 flex items-center gap-2 bg-red-50
                        text-red-600 px-4 py-3 rounded-xl">
          <AlertCircle size={18} />
          {error}
        </div>
      )}

      {/* EMPTY */}
      {tasks.length === 0 ? (
        <div className="bg-white rounded-2xl shadow-sm p-12 text-center">
          <p className="text-slate-500">No tasks have been created yet.</p>
          {canCreate && (
            <button
              onClick={() => setShowModal(true)}
              className="mt-4 text-blue-600 font-medium hover:underline"
            >
              Create your first task
            </button>
          )}
        </div>
      ) : (
        /* TASK CARDS */
        <div className="grid gap-6 sm:grid-cols-1 md:grid-cols-2 xl:grid-cols-3">
          {tasks.map((task) => (
            <div
              key={task.task_id}
              className="bg-white rounded-2xl shadow-sm
                         hover:shadow-md transition p-6 flex flex-col"
            >
              {/* HEADER */}
              <div className="flex items-start justify-between mb-3">
                <h3 className="text-lg font-semibold text-slate-800 line-clamp-1">
                  {task.title}
                </h3>
                <span
                  className={`px-3 py-1 rounded-full text-xs font-medium
                  ${STATUS_COLORS[task.status]}`}
                >
                  {task.status.replace('_', ' ')}
                </span>
              </div>

              {/* DESC */}
              {task.description && (
                <p className="text-slate-500 text-sm line-clamp-2 mb-4">
                  {task.description}
                </p>
              )}

              {/* META */}
              <div className="space-y-2 text-sm text-slate-500">
                <div className="flex items-center gap-2">
                  <User size={14} />
                  Assigned: {task.assigned_to || 'Unassigned'}
                </div>

                {task.reviewer && (
                  <div className="flex items-center gap-2">
                    <User size={14} />
                    Reviewer: {task.reviewer}
                  </div>
                )}

                <div className="flex items-center gap-2">
                  <Calendar size={14} />
                  {formatDate(task.expected_closure)}
                </div>
              </div>

              {/* ACTION */}
              <button
                onClick={() => setSelectedTask(task)}
                className="mt-6 flex items-center justify-center gap-2
                           text-blue-600 text-sm font-medium
                           rounded-lg py-2
                           hover:bg-blue-50 transition"
              >
                <Eye size={16} />
                View details
              </button>
            </div>
          ))}
        </div>
      )}

      {/* MODALS */}
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
