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
  
  getTasks: async (token, role, empId) => {
    let endpoint = '/tasks/employee';
    let url = `${API_BASE_URL}${endpoint}`;
    console.log(`role`,role,empId);
    
    if (role === 'admin') {
      endpoint = '/tasks';
      url = `${API_BASE_URL}${endpoint}`;
    } else if (role === 'manager') {
      endpoint = '/tasks/manager';
      url = `${API_BASE_URL}${endpoint}`;
    } else if (role === 'developer') {
      endpoint = '/tasks/employee';
      url = `${API_BASE_URL}${endpoint}?id=${empId}`;
    }
    console.log(`Fetching tasks from ${url} for role ${role}`);
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
  
  getEmployees: async (token, managerId) => {
    const response = await fetch(`${API_BASE_URL}/employees/${managerId}`, {
      headers: { 'Authorization': `Bearer ${token}` }
    });
    if (!response.ok) throw new Error('Failed to fetch employees');
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
  }
};