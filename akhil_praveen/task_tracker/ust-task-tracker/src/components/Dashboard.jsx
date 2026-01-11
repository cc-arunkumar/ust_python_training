import React, { useState, useEffect } from 'react';
import Navbar from './Navbar';
import StatsCards from './StatsCards';
import TaskFilters from './TaskFilters';
import TaskForm from './TaskForm';
import TaskList from './TaskList';
import { getTasks, createTask, updateTask, deleteTask } from '../api/taskApi';

function Dashboard({ onLogout }) {
  const [tasks, setTasks] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const [showAddTask, setShowAddTask] = useState(false);
  const [searchTerm, setSearchTerm] = useState('');
  const [filterStatus, setFilterStatus] = useState('all');

  useEffect(() => {
    fetchTasks();
  }, []);

  const fetchTasks = async () => {
    try {
      const data = await getTasks();
      setTasks(data);
    } catch (err) {
      setError(err.message);
    }
  };

  const handleCreateTask = async (newTask) => {
    setLoading(true);
    setError('');
    try {
      await createTask(newTask);
      await fetchTasks();
      setShowAddTask(false);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  const handleUpdateTask = async (taskId, updates) => {
    setError('');
    try {
      await updateTask(taskId, updates);
      await fetchTasks();
    } catch (err) {
      setError(err.message);
    }
  };

  const handleDeleteTask = async (taskId) => {
    setError('');
    try {
      await deleteTask(taskId);
      await fetchTasks();
    } catch (err) {
      setError(err.message);
    }
  };

  const filteredTasks = tasks.filter(task => {
    const matchesSearch = task.title.toLowerCase().includes(searchTerm.toLowerCase()) ||
                         task.description.toLowerCase().includes(searchTerm.toLowerCase());
    const matchesFilter = filterStatus === 'all' ||
                         (filterStatus === 'completed' && task.completed) ||
                         (filterStatus === 'active' && !task.completed);
    return matchesSearch && matchesFilter;
  });

  const stats = {
    total: tasks.length,
    completed: tasks.filter(t => t.completed).length,
    active: tasks.filter(t => !t.completed).length
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-indigo-50 via-purple-50 to-pink-50">
      <Navbar onLogout={onLogout} />
      
      <div className="max-w-7xl mx-auto px-4 py-8">
        <StatsCards stats={stats} />
        
        <div className="bg-white rounded-xl shadow-lg p-6 mb-6">
          <TaskFilters
            searchTerm={searchTerm}
            setSearchTerm={setSearchTerm}
            filterStatus={filterStatus}
            setFilterStatus={setFilterStatus}
            showAddTask={showAddTask}
            setShowAddTask={setShowAddTask}
          />

          {showAddTask && (
            <TaskForm
              onSubmit={handleCreateTask}
              onCancel={() => setShowAddTask(false)}
              loading={loading}
            />
          )}

          {error && (
            <div className="bg-red-50 text-red-600 px-4 py-3 rounded-lg mb-4">
              {error}
            </div>
          )}

          <TaskList
            tasks={filteredTasks}
            onUpdate={handleUpdateTask}
            onDelete={handleDeleteTask}
          />
        </div>
      </div>
    </div>
  );
}

export default Dashboard;