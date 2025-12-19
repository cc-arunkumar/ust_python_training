import React, { useState, useEffect } from 'react';
import { api, decodeToken } from './services/api';
import LoginPage from './components/pages/LoginPage';
import RoleSelector from './components/pages/RoleSelector';
import EmployeeDashboard from './components/pages/EmployeeDashboard';
import ManagerDashboard from './components/pages/ManagerDashboard';
import AdminDashboard from './components/pages/AdminDashboard';

const App = () => {
  const [currentView, setCurrentView] = useState('login');
  const [user, setUser] = useState(null);
  const [selectedRole, setSelectedRole] = useState(null);
  const [token, setToken] = useState(null);
  const [tasks, setTasks] = useState([]);
  const [employees, setEmployees] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  // Load token on mount
  useEffect(() => {
    const savedToken = localStorage.getItem('token');
    console.log('[DEBUG] Initial token load:', savedToken ? 'Token found' : 'No token');
    
    if (savedToken && savedToken !== 'null' && savedToken !== 'undefined') {
      // Verify it's a valid JWT format
      if (savedToken.startsWith('eyJ')) {
        setToken(savedToken);
      } else {
        console.warn('[DEBUG] Invalid token format, clearing');
        localStorage.removeItem('token');
      }
    }
    setLoading(false);
  }, []);

  // Persist token changes
  useEffect(() => {
    if (token) {
      console.log('[DEBUG] Saving token to localStorage');
      localStorage.setItem('token', token);
    } else {
      console.log('[DEBUG] Removing token from localStorage');
      localStorage.removeItem('token');
    }
  }, [token]);

  // Auto-login if token exists
  useEffect(() => {
    if (token && !user) {
      console.log('[DEBUG] Auto-login: Decoding token');
      const payload = decodeToken(token);
      
      if (payload && payload.emp_id) {
        console.log('[DEBUG] Token payload:', payload);
        fetchEmployeeDetails(payload.emp_id, token)
          .then(userData => {
            console.log('[DEBUG] User data loaded:', userData);
            setUser(userData);
          })
          .catch((err) => {
            console.error('[DEBUG] Failed to fetch employee details:', err);
            // Don't clear token just because employee details failed
            // Use token data as fallback
            const fallbackUser = {
              ...payload,
              name: payload.emp_id
            };
            console.log('[DEBUG] Using fallback user data:', fallbackUser);
            setUser(fallbackUser);
          });
      } else {
        console.error('[DEBUG] Invalid token payload, logging out');
        handleLogout();
      }
    }
  }, [token]);

  const fetchEmployeeDetails = async (empId, authToken) => {
    try {
      console.log('[DEBUG] Fetching employee details for:', empId);
      const empData = await api.getEmployee(empId, authToken);
      const payload = decodeToken(authToken);
      return { 
        ...payload, 
        ...empData, 
        name: empData.name || payload.emp_id 
      };
    } catch (err) {
      console.warn('[DEBUG] Employee fetch failed:', err.message);
      // Return token data as fallback
      const payload = decodeToken(authToken);
      return { 
        ...payload, 
        name: payload.emp_id 
      };
    }
  };

  // Handlers for Login/Role/Logout
  const handleLogin = async (empId, password) => {
    try {
      console.log('[DEBUG] Logging in:', empId);
      const response = await api.login(empId, password);
      
      if (!response.access_token) {
        throw new Error('No access token received');
      }
      
      console.log('[DEBUG] Login successful, token received');
      setToken(response.access_token);
      setError('');
    } catch (err) {
      console.error('[DEBUG] Login failed:', err);
      throw err;
    }
  };

  const handleRoleSelect = (role) => {
    console.log('[DEBUG] Role selected:', role);
    setSelectedRole(role);
    setCurrentView('dashboard');
  };

  const handleLogout = () => {
    console.log('[DEBUG] Logging out');
    setUser(null);
    setSelectedRole(null);
    setToken(null);
    setCurrentView('login');
    setTasks([]);
    setEmployees([]);
    setError('');
  };

  // Task Handlers
  const handleUpdateTasks = (updated) => {
    // If full list passed
    if (Array.isArray(updated)) {
      console.log('[DEBUG] Updating all tasks:', updated.length);
      setTasks(updated);
      return;
    }

    // If single task passed
    console.log('[DEBUG] Updating single task:', updated.task_id);
    setTasks(prev =>
      prev.map(t =>
        t.task_id === updated.task_id ? updated : t
      )
    );
  };

  const handleCreateTask = (newTask) => {
    console.log('[DEBUG] Creating task:', newTask.task_id);
    setTasks(prev => [...prev, newTask]);
  };

  // Employee Handlers
  const handleCreateEmployee = (newEmployee) => {
    console.log('[DEBUG] Creating employee:', newEmployee.emp_id);
    setEmployees(prev => [...prev, newEmployee]);
  };

  const handleUpdateEmployee = (updatedEmployee) => {
    console.log('[DEBUG] Updating employee:', updatedEmployee.emp_id);
    setEmployees(prev => prev.map(e => e.emp_id === updatedEmployee.emp_id ? updatedEmployee : e));
  };

  const handleDeleteEmployee = (empId) => {
    console.log('[DEBUG] Deleting employee:', empId);
    setEmployees(prev => prev.filter(e => e.emp_id !== empId));
  };

  // Fetch data on login
  useEffect(() => {
    if (token && user) {
      const fetchData = async () => {
        try {
          setLoading(true);
          console.log('[DEBUG] Fetching tasks for user:', user.emp_id, 'role:', user.role);

          let tasksData = [];

          if (user.role === 'EMPLOYEE') {
            const allTasks = await api.getTasks(token);
            console.log('[DEBUG] All tasks from backend:', allTasks.length);
            console.log('[DEBUG] Filtering for emp_id:', user.emp_id);

            tasksData = allTasks.filter(
              t =>
                String(t.assigned_to).trim().toUpperCase() ===
                String(user.emp_id).trim().toUpperCase()
            );
            console.log('[DEBUG] Filtered tasks:', tasksData.length);
          } else {
            tasksData = await api.getTasks(token);
            console.log('[DEBUG] All tasks loaded:', tasksData.length);
          }

          setTasks(tasksData);
          setError('');

        } catch (err) {
          console.error('[DEBUG] Failed to fetch tasks:', err);
          setError(err.message);
        } finally {
          setLoading(false);
        }
      };

      fetchData();
    }
  }, [token, user]);

  // Determine dashboard based on role
  useEffect(() => {
    if (user && token && !loading) {
      console.log('[DEBUG] Determining view for role:', user.role);
      
      if (user.role === 'ADMIN' || user.role === 'MANAGER') {
        setCurrentView('roleSelector');
      } else {
        setSelectedRole('EMPLOYEE');
        setCurrentView('dashboard');
      }
    }
  }, [user, token, loading]);

  // Show loading screen during initial token check
  if (loading) {
    return (
      <div className="min-h-screen flex items-center justify-center bg-gray-100">
        <div className="text-center">
          <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-600 mx-auto mb-4"></div>
          <p className="text-gray-600">Loading...</p>
        </div>
      </div>
    );
  }

  // Main Render
  return (
    <div>
      {currentView === 'login' && (
        <LoginPage onLogin={handleLogin} loading={loading} error={error} />
      )}
      {currentView === 'roleSelector' && (
        <RoleSelector user={user} onRoleSelect={handleRoleSelect} />
      )}
      {currentView === 'dashboard' && selectedRole === 'EMPLOYEE' && user?.role === 'EMPLOYEE' && (
        <EmployeeDashboard
          user={user}
          tasks={tasks}
          token={token}
          onLogout={handleLogout}
          onError={setError}
          error={error}
          onUpdateTasks={handleUpdateTasks}
        />
      )}
      
      {currentView === 'dashboard' && selectedRole === 'MANAGER' && (
        <ManagerDashboard
          user={user}
          tasks={tasks}
          token={token}
          onLogout={handleLogout}
          onSwitchRole={() => setCurrentView('roleSelector')}
          onError={setError}
          onUpdateTasks={handleUpdateTasks}
          onCreateTask={handleCreateTask}
        />
      )}
      {currentView === 'dashboard' && selectedRole === 'ADMIN' && (
        <AdminDashboard
          user={user}
          employees={employees}
          tasks={tasks}
          token={token}
          onLogout={handleLogout}
          onSwitchRole={() => setCurrentView('roleSelector')}
          onError={setError}
          onCreateEmployee={handleCreateEmployee}
          onUpdateEmployee={handleUpdateEmployee}
          onDeleteEmployee={handleDeleteEmployee}
          onUpdateTasks={handleUpdateTasks}
          onCreateTask={handleCreateTask}
        />
      )}
    </div>
  );
};

export default App;