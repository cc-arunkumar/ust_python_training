import React, { useState, useEffect } from 'react';
import { Plus, AlertCircle } from 'lucide-react';
import { useAuth } from '../../context/AuthContext';
import ApiService from '../../services/api';
import TaskModal from './TaskModal';
import TaskDetailsModal from './TaskDetailsModal';
import KanbanColumn from './KanbanColumn';
import { TASK_STATUSES } from '../../utils/constants';
import toast, { Toaster } from 'react-hot-toast';
import { DragDropContext } from '@hello-pangea/dnd';

// Priority order for sorting
const PRIORITY_ORDER = { high: 3, medium: 2, low: 1 };

const KanbanBoard = () => {
  const { hasRole } = useAuth();
  const canEdit = hasRole('ADMIN') || hasRole('MANAGER');

  const [tasks, setTasks] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  const [selectedTask, setSelectedTask] = useState(null);
  const [editingTask, setEditingTask] = useState(null);
  const [showCreateModal, setShowCreateModal] = useState(false);
  const [sortOption, setSortOption] = useState('priority'); // default sort

  useEffect(() => {
    fetchTasks();
  }, []);

  const fetchTasks = async () => {
    try {
      const data = await ApiService.getTasks();
      setTasks(data);
    } catch (err) {
      setError(err.message);
      toast.error(err.message);
    } finally {
      setLoading(false);
    }
  };

  const handleDelete = async (taskId) => {
    try {
      await ApiService.deleteTask(taskId);
      toast.success('Task deleted successfully');
      fetchTasks();
    } catch (err) {
      toast.error(err.message);
    }
  };

  // Restrict movement: only ON_PROCESS <-> REVIEW
  const canMove = (from, to) => {
    return (from === 'ON_PROCESS' && to === 'REVIEW') ||
           (from === 'REVIEW' && to === 'ON_PROCESS');
  };

  const onDragEnd = async (result) => {
    const { source, destination, draggableId } = result;
    if (!destination || source.droppableId === destination.droppableId) return;

    const fromStatus = source.droppableId;
    const toStatus = destination.droppableId;

    if (!canMove(fromStatus, toStatus)) {
      toast.error('Tasks can only move between ON_PROCESS and REVIEW');
      return;
    }

    try {
      await ApiService.updateTaskStatus(draggableId, toStatus);
      toast.success(`Task moved to ${toStatus}`);
      fetchTasks();
    } catch {
      toast.error('Failed to update task');
    }
  };

  // Group tasks by status and apply sorting
  const groupedTasks = {};
  Object.values(TASK_STATUSES).forEach(status => {
    groupedTasks[status] = tasks
      .filter(t => t.status === status)
      .sort((a, b) => {
        if (sortOption === 'priority') {
          const aPriority = a.priority ? PRIORITY_ORDER[a.priority.toLowerCase()] || 0 : 0;
          const bPriority = b.priority ? PRIORITY_ORDER[b.priority.toLowerCase()] || 0 : 0;
          return bPriority - aPriority; // high → low
        } else if (sortOption === 'date') {
          const aDate = a.expected_closure ? new Date(a.expected_closure) : new Date(0);
          const bDate = b.expected_closure ? new Date(b.expected_closure) : new Date(0);
          return aDate - bDate; // earliest first
        }
        return 0;
      });
  });

  if (loading) {
    return <div className="min-h-screen flex items-center justify-center">Loading...</div>;
  }

  return (
    <div className="min-h-screen bg-gray-50">
      <Toaster position="top-right" />

      {/* HEADER */}
      <div className="bg-white px-6 py-4 shadow-sm flex justify-between items-center">
        <h1 className="text-xl font-semibold">Task Board</h1>

        <div className="flex gap-4 items-center">
          {/* Sort dropdown */}
          <select
            value={sortOption}
            onChange={(e) => setSortOption(e.target.value)}
            className="border rounded px-3 py-1 text-sm"
          >
            <option value="priority">Sort by Priority</option>
            <option value="date">Sort by Deadline</option>
          </select>

          {canEdit && (
            <button
              onClick={() => setShowCreateModal(true)}
              className="bg-blue-600 text-white px-4 py-2 rounded-lg text-sm flex items-center gap-1"
            >
              <Plus size={16} /> New Task
            </button>
          )}
        </div>
      </div>

      {/* ERROR */}
      {error && (
        <div className="m-6 bg-red-50 text-red-700 px-4 py-3 rounded-lg flex gap-2">
          <AlertCircle size={18} />
          {error}
        </div>
      )}

      {/* BOARD */}
      <DragDropContext onDragEnd={onDragEnd}>
        <div className="p-6 flex gap-6 overflow-x-auto">
          {Object.entries(groupedTasks).map(([status, list]) => (
            <KanbanColumn
              key={status}
              status={status}
              tasks={list}
              onTaskView={setSelectedTask}
              onTaskEdit={canEdit ? setEditingTask : null}
              onTaskDelete={handleDelete}
            />
          ))}
        </div>
      </DragDropContext>

      {/* MODALS */}
      {selectedTask && (
        <TaskDetailsModal
          task={selectedTask}
          onClose={() => setSelectedTask(null)}
        />
      )}

      {(editingTask || showCreateModal) && (
        <TaskModal
          task={editingTask}
          onClose={() => {
            setEditingTask(null);
            setShowCreateModal(false);
          }}
          onSuccess={() => {
            setEditingTask(null);
            setShowCreateModal(false);
            fetchTasks();
          }}
        />
      )}
    </div>
  );
};

export default KanbanBoard;
