import React, { useState, useEffect } from 'react';
import Header from '../components/common/Header';
import Sidebar from '../components/common/Sidebar';
import TasksBoard from '../components/tasks/TasksBoard';
import CreateTaskModal from '../components/tasks/CreateTaskModal';
import EmployeesView from '../components/employees/EmployeesView';
import { Plus } from 'lucide-react';
import { taskAPI, employeeAPI } from '../api/apiService';
import { USER_ROLES } from '../utils/constants';
import { hasRole, hasAnyRole } from '../utils/helpers';

const Dashboard = ({ user, onLogout }) => {
  const [activeView, setActiveView] = useState(user.roles[0]);
  const [activeTab, setActiveTab] = useState('tasks');
  const [tasks, setTasks] = useState([]);
  const [employees, setEmployees] = useState([]);
  const [showCreateTaskModal, setShowCreateTaskModal] = useState(false);
  const [sidebarOpen, setSidebarOpen] = useState(false);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  useEffect(() => {
    loadData();
  }, [activeView]);

  const loadData = async () => {
    setLoading(true);
    setError('');
    
    try {
      // Load tasks based on role
      let tasksData = [];
      if (hasRole(user, USER_ROLES.ADMIN)) {
        tasksData = await taskAPI.getAll();
      } else if (hasRole(user, USER_ROLES.MANAGER)) {
        tasksData = await taskAPI.getByManager();
      } else if (hasRole(user, USER_ROLES.DEVELOPER)) {
        tasksData = await taskAPI.getByEmployee(user.emp_id);
      }
      
      setTasks(tasksData);

      // Load employees - managers and admins can see employees
      if (hasAnyRole(user, [USER_ROLES.ADMIN, USER_ROLES.MANAGER])) {
        const employeesData = await employeeAPI.getAll(user.emp_id);
        setEmployees(employeesData);
      }
    } catch (err) {
      console.error('Error loading data:', err);
      setError('Failed to load data. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  const handleStatusChange = async (taskId, newStatus) => {
    try {
      await taskAPI.updateStatus(taskId, newStatus);
      setTasks(tasks.map(t => 
        t._id === taskId ? { ...t, status: newStatus } : t
      ));
    } catch (err) {
      console.error('Error updating task status:', err);
      alert('Failed to update task status');
    }
  };

  const handleCreateTask = async (data) => {
    try {
      const newTask = await taskAPI.create({
        ...data,
        assigned_by: user.emp_id,
        assigned_at: new Date().toISOString(),
        updated_by: user.emp_id,
        updated_at: new Date().toISOString(),
        remarks: []
      });
      
      // Reload tasks to get the complete task data
      loadData();
    } catch (err) {
      console.error('Error creating task:', err);
      throw err;
    }
  };

  const handleCreateEmployee = async (data) => {
    try {
      await employeeAPI.create(data);
      // Reload employees
      const employeesData = await employeeAPI.getAll(user.emp_id);
      setEmployees(employeesData);
    } catch (err) {
      console.error('Error creating employee:', err);
      throw err;
    }
  };

  // Permissions
  const canCreateEmployee = hasRole(user, USER_ROLES.ADMIN);
  const canCreateTask = hasAnyRole(user, [USER_ROLES.ADMIN, USER_ROLES.MANAGER]);
  const canEditTask = hasAnyRole(user, [USER_ROLES.MANAGER, USER_ROLES.DEVELOPER]);

  return (
    <div className="min-h-screen bg-gray-50">
      <Header
        user={user}
        activeView={activeView}
        onViewChange={setActiveView}
        onLogout={onLogout}
        onMenuToggle={() => setSidebarOpen(!sidebarOpen)}
      />

      <div className="flex">
        <Sidebar
          activeTab={activeTab}
          onTabChange={setActiveTab}
          isOpen={sidebarOpen}
          onClose={() => setSidebarOpen(false)}
        />

        <main className="flex-1 p-4 lg:p-6">
          {error && (
            <div className="mb-4 p-4 bg-red-50 border border-red-200 rounded-lg">
              <p className="text-sm text-red-600">{error}</p>
            </div>
          )}

          {loading ? (
            <div className="flex items-center justify-center h-64">
              <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-500"></div>
            </div>
          ) : (
            <>
              {activeTab === 'tasks' && (
                <div>
                  <div className="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-4 mb-6">
                    <div>
                      <h2 className="text-2xl font-bold text-gray-800">Tasks Board</h2>
                      <p className="text-sm text-gray-600 mt-1">
                        Manage and track your tasks
                      </p>
                    </div>
                    {canCreateTask && (
                      <button
                        onClick={() => setShowCreateTaskModal(true)}
                        className="flex items-center gap-2 bg-gradient-to-r from-blue-500 to-purple-600 text-white px-4 py-2 rounded-lg hover:from-blue-600 hover:to-purple-700 transition-all shadow-md"
                      >
                        <Plus className="w-5 h-5" />
                        Create Task
                      </button>
                    )}
                  </div>
                  
                  <TasksBoard
                    tasks={tasks}
                    onStatusChange={handleStatusChange}
                    canEdit={canEditTask}
                  />
                </div>
              )}
              
              {activeTab === 'employees' && (
                <EmployeesView
                  employees={employees}
                  canCreate={canCreateEmployee}
                  onCreate={handleCreateEmployee}
                />
              )}
            </>
          )}
        </main>
      </div>

      {showCreateTaskModal && (
        <CreateTaskModal
          onClose={() => setShowCreateTaskModal(false)}
          onCreate={handleCreateTask}
          employees={employees}
        />
      )}
    </div>
  );
};

export default Dashboard;