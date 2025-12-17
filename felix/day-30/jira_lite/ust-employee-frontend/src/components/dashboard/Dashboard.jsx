import React, { useState, useEffect } from 'react';
import { Plus, Search } from 'lucide-react';
import { useAuth } from '../../contexts/AuthContext';
import { useNavigate } from 'react-router-dom';
import { api } from '../../services/api';
import Header from '../layout/Header';
import TaskBoard from './TaskBoard';
import CreateTaskModal from '../modals/CreateTaskModal';

const Dashboard = () => {
  const { user, token } = useAuth();
  const navigate = useNavigate();
  const [tasks, setTasks] = useState([]);
  const [loading, setLoading] = useState(true);
  const [showCreateModal, setShowCreateModal] = useState(false);
  const [searchTerm, setSearchTerm] = useState('');
  const [filterPriority, setFilterPriority] = useState('All');
  const [userRoles, setUserRoles] = useState([]);

  // 🔹 Track which view is active - initialize with null, will be set after roles are fetched
  const [currentView, setCurrentView] = useState(null);

  // 🔹 Fetch user roles on mount
  useEffect(() => {
    const fetchUserRoles = async () => {
      try {
        const userData = await api.getUserById(token, user.emp_id);
        
        if (userData && Array.isArray(userData.role)) {
          setUserRoles(userData.role);
          // Set default view to first role
          setCurrentView(userData.role[0] || 'developer');
        } else {
          setUserRoles(['developer']);
          setCurrentView('developer');
        }
      } catch (err) {
        console.error('Failed to fetch roles:', err);
        setUserRoles(['developer']);
        setCurrentView('developer');
      }
    };

    fetchUserRoles();
  }, [token, user.emp_id]);

  const canCreateTasks = ['admin', 'manager'].includes(currentView);
  
  console.log('User Roles:', userRoles);
  console.log('Current View:', currentView);

  useEffect(() => {
    // Only load tasks after currentView is set
    if (currentView) {
      loadTasks();
    }
  }, [currentView]);

  const loadTasks = async () => {
    try {
      setLoading(true);
      const data = await api.getTasks(token, currentView, user.emp_id);
      setTasks(Array.isArray(data) ? data : []);
    } catch (error) {
      console.error('Error loading tasks:', error);
      setTasks([]);
    } finally {
      setLoading(false);
    }
  };

  const handleStatusChange = async (taskId, newStatus) => {
    try {
      await api.updateTaskStatus(token, taskId, newStatus);
      loadTasks();
    } catch (error) {
      console.error('Error updating task:', error);
    }
  };

  const handleAddRemark = async (taskId, remark) => {
    try {
      await api.addRemark(token, user.emp_id, taskId, remark);
      loadTasks();
    } catch (error) {
      console.error('Error adding remark:', error);
    }
  };

  const filteredTasks = tasks.filter(task => {
    const matchesSearch =
      task.title.toLowerCase().includes(searchTerm.toLowerCase()) ||
      task.description.toLowerCase().includes(searchTerm.toLowerCase());
    const matchesPriority = filterPriority === 'All' || task.priority === filterPriority;
    return matchesSearch && matchesPriority;
  });

  // Show loading until currentView is set
  if (loading || !currentView) {
    return (
      <div className="min-h-screen bg-gray-50 flex items-center justify-center">
        <div className="text-center">
          <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-600 mx-auto mb-4"></div>
          <p className="text-gray-600">Loading...</p>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-gray-50 to-gray-100">
      {/* 🔹 Pass handler and navigation to Header */}
      <Header onChangeView={setCurrentView} onNavigate={navigate} />

      <main className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        {/* Controls */}
        <div className="mb-6 flex flex-col sm:flex-row gap-4 items-start sm:items-center justify-between">
          <div className="flex flex-col sm:flex-row gap-3 flex-1 w-full sm:w-auto">
            <div className="relative flex-1 max-w-md">
              <Search
                className="absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-400"
                size={18}
              />
              <input
                type="text"
                placeholder="Search tasks..."
                value={searchTerm}
                onChange={(e) => setSearchTerm(e.target.value)}
                className="w-full pl-10 pr-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
              />
            </div>

            <select
              value={filterPriority}
              onChange={(e) => setFilterPriority(e.target.value)}
              className="px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent bg-white"
            >
              <option value="All">All Priorities</option>
              <option value="Low">Low</option>
              <option value="Medium">Medium</option>
              <option value="High">High</option>
            </select>
          </div>

          {currentView !== "developer" && (
            <button
              onClick={() => setShowCreateModal(true)}
              className="flex items-center gap-2 px-6 py-2 bg-gradient-to-r from-blue-600 to-purple-600 text-white rounded-lg hover:shadow-lg transform hover:-translate-y-0.5 transition-all font-semibold"
            >
              <Plus size={20} />
              Create Task
            </button>
          )}
        </div>

        <TaskBoard
          tasks={filteredTasks}
          onStatusChange={handleStatusChange}
          onAddRemark={handleAddRemark}
          userRole={currentView} // 🔹 pass currentView as userRole
        />
      </main>

      {showCreateModal && (
        <CreateTaskModal
          token={token}
          empId={user.emp_id}
          onClose={() => setShowCreateModal(false)}
          onSuccess={() => {
            setShowCreateModal(false);
            loadTasks();
          }}
        />
      )}
    </div>
  );
};

export default Dashboard;