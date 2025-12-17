import { API_BASE_URL } from '../utils/constants';

export const api = {
  login: async (emp_id, password) => {
    const response = await fetch(`${API_BASE_URL}/login`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ emp_id, password })
    });
    if (!response.ok) throw new Error('Login failed');
    return response.json();
  },
  
  getTasks: async (token, role) => {
    const url = `${API_BASE_URL}/tasks?role=${role}`;
    const response = await fetch(url, {
      headers: { 'Authorization': `Bearer ${token}` }
    });
    if (!response.ok) throw new Error('Failed to fetch tasks');
    return response.json();
  },
  
  getTaskById: async (token, taskId) => {
    const response = await fetch(`${API_BASE_URL}/tasks/${taskId}`, {
      headers: { 'Authorization': `Bearer ${token}` }
    });
    if (!response.ok) throw new Error('Failed to fetch task');
    return response.json();
  },

  getUserById: async (token, empId) => {
    const response = await fetch(`${API_BASE_URL}/users/${empId}`, {
      headers: { 'Authorization': `Bearer ${token}` }
    });
    if (!response.ok) throw new Error('Failed to fetch user');
    return response.json();
  },
  
  createTask: async (token, taskData) => {
    const response = await fetch(`${API_BASE_URL}/create_tasks`, {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${token}`,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(taskData)
    });
    if (!response.ok) throw new Error('Failed to create task');
    return response.json();
  },
  
  updateTask: async (token, taskId, taskData) => {
    const response = await fetch(`${API_BASE_URL}/update_one_tasks/${taskId}`, {
      method: 'PUT',
      headers: {
        'Authorization': `Bearer ${token}`,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(taskData)
    });
    if (!response.ok) throw new Error('Failed to update task');
    return response.json();
  },
  
  updateTaskStatus: async (token, taskId, status) => {
    const response = await fetch(`${API_BASE_URL}/tasks/${taskId}/status`, {
      method: 'PATCH',
      headers: {
        'Authorization': `Bearer ${token}`,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ status })
    });
    if (!response.ok) throw new Error('Failed to update task status');
    return response.json();
  },
  
  addRemark: async (token, empId, taskId, remark) => {
    const response = await fetch(`${API_BASE_URL}/tasks/${empId}/${taskId}/remarks`, {
      method: 'PATCH',
      headers: {
        'Authorization': `Bearer ${token}`,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ remarks: remark })
    });
    if (!response.ok) throw new Error('Failed to add remark');
    return response.json();
  },
  
  // Employee Management APIs
  getEmployees: async (token, managerId) => {
    const response = await fetch(`${API_BASE_URL}/employees/${managerId}`, {
      headers: { 'Authorization': `Bearer ${token}` }
    });
    if (!response.ok) throw new Error('Failed to fetch employees');
    return response.json();
  },

  getEmployeesForAdmin: async (token) => {
    const response = await fetch(`${API_BASE_URL}/employees/admin`, {
      headers: { 'Authorization': `Bearer ${token}` }
    });
    if (!response.ok) throw new Error('Failed to fetch employees for admin');
    return response.json();
  },
  
  createEmployee: async (token, employeeData) => {
    const response = await fetch(`${API_BASE_URL}/employees`, {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${token}`,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(employeeData)
    });
    if (!response.ok) throw new Error('Failed to create employee');
    return response.json();
  },
  
  updateEmployee: async (token, managerId, empId, employeeData) => {
    console.log('Updating employee with data:', employeeData);
    const response = await fetch(`${API_BASE_URL}/employees/${managerId}/${empId}`, {
      method: 'PUT',
      headers: {
        'Authorization': `Bearer ${token}`,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(employeeData)
    });
    if (!response.ok) throw new Error('Failed to update employee');
    return response.json();
  },
  
  deleteEmployee: async (token, managerId, empId) => {
    const response = await fetch(`${API_BASE_URL}/employees/${managerId}/${empId}`, {
      method: 'DELETE',
      headers: { 'Authorization': `Bearer ${token}` }
    });
    if (!response.ok) throw new Error('Failed to delete employee');
    return response.json();
  },

  // User Management APIs
  createUser: async (token, userData) => {
    const response = await fetch(`${API_BASE_URL}/users`, {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${token}`,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(userData)
    });
    if (!response.ok) throw new Error('Failed to create user');
    return response.json();
  },

  updateUserRole: async (token, empId, role) => {
    const response = await fetch(`${API_BASE_URL}/users/${empId}/role`, {
      method: 'PUT',
      headers: {
        'Authorization': `Bearer ${token}`,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ role })
    });
    if (!response.ok) throw new Error('Failed to update user role');
    return response.json();
  }
};