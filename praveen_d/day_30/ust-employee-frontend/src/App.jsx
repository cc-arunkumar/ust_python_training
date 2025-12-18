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
  const [token, setToken] = useState(localStorage.getItem('token') || '');
  const [tasks, setTasks] = useState([]);
  const [employees, setEmployees] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  // Persist token
  useEffect(() => {
    if (token) {
      localStorage.setItem('token', token);
    } else {
      localStorage.removeItem('token');
    }
  }, [token]);

  // Auto-login if token exists
  useEffect(() => {
    if (token) {
      const payload = decodeToken(token);
      if (payload && payload.emp_id) {
        fetchEmployeeDetails(payload.emp_id, token).then(setUser).catch(() => {
          setToken('');
          setCurrentView('login');
        });
      } else {
        setToken('');
      }
    }
  }, [token]);

  const fetchEmployeeDetails = async (empId, authToken) => {
    try {
      const empData = await api.getEmployee(empId, authToken);
      const payload = decodeToken(authToken);
      return { ...payload, ...empData, name: empData.name || payload.emp_id };
    } catch (err) {
      console.warn('No employee record yet, using token:', err.message);
      const payload = decodeToken(authToken);
      return { ...payload, name: payload.emp_id };
    }
  };

  // Handlers for Login/Role/Logout
  const handleLogin = async (empId, password) => {
    try {
      const response = await api.login(empId, password);
      setToken(response.access_token);
    } catch (err) {
      throw err;
    }
  };

  const handleRoleSelect = (role) => {
    setSelectedRole(role);
    setCurrentView('dashboard');
  };

  const handleLogout = () => {
    setUser(null);
    setSelectedRole(null);
    setToken('');
    setCurrentView('login');
    setTasks([]);
    setEmployees([]);
    setError('');
  };

  // Task Handlers (shared for Employee/Manager/Admin)
 const handleUpdateTasks = (updated) => {
  // If full list passed
  if (Array.isArray(updated)) {
    setTasks(updated);
    return;
  }

  // If single task passed
  setTasks(prev =>
    prev.map(t =>
      t.task_id === updated.task_id ? updated : t
    )
  );
};

  const handleCreateTask = (newTask) => {
    setTasks(prev => [...prev, newTask]);
  };

  // Employee Handlers (for Admin)
  const handleCreateEmployee = (newEmployee) => {
    setEmployees(prev => [...prev, newEmployee]);
  };

  const handleUpdateEmployee = (updatedEmployee) => {
    setEmployees(prev => prev.map(e => e.emp_id === updatedEmployee.emp_id ? updatedEmployee : e));
  };

  const handleDeleteEmployee = (empId) => {
    setEmployees(prev => prev.filter(e => e.emp_id !== empId));
  };

  // Fetch data on login (for dashboards)
useEffect(() => {
  if (token && user) {
    const fetchData = async () => {
      try {
        setLoading(true);

        let tasksData = [];

        if (user.role === 'EMPLOYEE') {
          const allTasks = await api.getTasks(token);

          // 🔍 DEBUG LOGS — ADD HERE
          console.log("ALL TASKS FROM BACKEND:", allTasks);
          console.log("LOGGED IN EMP ID:", user.emp_id);

          tasksData = allTasks.filter(
            t =>
              String(t.assigned_to).trim().toUpperCase() ===
              String(user.emp_id).trim().toUpperCase()
          );
        } else {
          tasksData = await api.getTasks(token);
        }

        setTasks(tasksData);

      } catch (err) {
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
      if (user.role === 'ADMIN' || user.role === 'MANAGER') {
        setCurrentView('roleSelector');
      } else {
        setSelectedRole('EMPLOYEE');
        setCurrentView('dashboard');
      }
    }
  }, [user, token, loading]);

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
  error={error}  // Add this
  onUpdateTasks={handleUpdateTasks}
/>
      )}
      
      {currentView === 'dashboard' && selectedRole === 'MANAGER' && (
        <ManagerDashboard
          user={user}
          tasks={tasks}
          token={token}
          onLogout={handleLogout}
          onSwitchRole={() => setCurrentView('roleSelector')}  // For admin switching
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