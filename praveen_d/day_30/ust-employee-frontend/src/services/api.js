const API_BASE_URL = "http://127.0.0.1:8000";  // Or use import.meta.env.VITE_API_URL

// JWT Decode Utility
export const decodeToken = (token) => {
  try {
    const base64Url = token.split('.')[1];
    const base64 = base64Url.replace(/-/g, '+').replace(/_/g, '/');
    const jsonPayload = decodeURIComponent(atob(base64).split('').map((c) => {
      return '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2);
    }).join(''));
    return JSON.parse(jsonPayload);
  } catch (error) {
    console.error('Failed to decode token:', error);
    return null;
  }
};

// API Service
export const api = {
  login: async (emp_id, password) => {
  const url = `${API_BASE_URL}/auth/login?emp_id=${encodeURIComponent(emp_id)}&password=${encodeURIComponent(password)}`;

  const response = await fetch(url, {
    method: 'POST',
  });

  if (!response.ok) {
    const errorData = await response.json().catch(() => ({}));
    throw new Error(errorData.detail || 'Login failed');
  }

  return response.json();
},

  getTasks: async (token) => {
    const response = await fetch(`${API_BASE_URL}/tasks/`, {
      headers: { 'Authorization': `Bearer ${token}` },
    });
    if (!response.ok) {
      const errorData = await response.json().catch(() => ({}));
      throw new Error(errorData.detail || 'Failed to fetch tasks');
    }
    return response.json();
  },

  updateTaskStatus: async (taskId, status, remarks = '', token) => {
    const response = await fetch(`${API_BASE_URL}/tasks/${taskId}`, {
      method: 'PATCH',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${token}`,
      },
      body: JSON.stringify({ status_: status, remarks }),
    });
    if (!response.ok) {
      const errorData = await response.json().catch(() => ({}));
      throw new Error(errorData.detail || 'Failed to update task');
    }
    return response.json();
  },

  getEmployees: async (token) => {
    const response = await fetch(`${API_BASE_URL}/employees/`, {
      headers: { 'Authorization': `Bearer ${token}` },
    });
    if (!response.ok) {
      const errorData = await response.json().catch(() => ({}));
      throw new Error(errorData.detail || 'Failed to fetch employees');
    }
    return response.json();
  },

  createEmployee: async (employeeData, token) => {
    const response = await fetch(`${API_BASE_URL}/employees/`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${token}`,
      },
      body: JSON.stringify(employeeData),
    });
    if (!response.ok) {
      const errorData = await response.json().catch(() => ({}));
      throw new Error(errorData.detail || 'Failed to create employee');
    }
    return response.json();
  },

  updateEmployee: async (empId, employeeData, token) => {
    const response = await fetch(`${API_BASE_URL}/employees/${empId}`, {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${token}`,
      },
      body: JSON.stringify(employeeData),
    });
    if (!response.ok) {
      const errorData = await response.json().catch(() => ({}));
      throw new Error(errorData.detail || 'Failed to update employee');
    }
    return response.json();
  },

  deleteEmployee: async (empId, token) => {
    const response = await fetch(`${API_BASE_URL}/employees/${empId}`, {
      method: 'DELETE',
      headers: { 'Authorization': `Bearer ${token}` },
    });
    if (!response.ok) {
      const errorData = await response.json().catch(() => ({}));
      throw new Error(errorData.detail || 'Failed to delete employee');
    }
    return response.json();
  },

  createTask: async (taskData, token) => {
    const response = await fetch(`${API_BASE_URL}/tasks/`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${token}`,
      },
      body: JSON.stringify(taskData),
    });
    if (!response.ok) {
      const errorData = await response.json().catch(() => ({}));
      throw new Error(errorData.detail || 'Failed to create task');
    }
    return response.json();
  },

  getEmployee: async (empId, token) => {
    const response = await fetch(`${API_BASE_URL}/employees/${empId}`, {
      headers: { 'Authorization': `Bearer ${token}` },
    });
    if (!response.ok) {
      const errorData = await response.json().catch(() => ({}));
      throw new Error(errorData.detail || 'Employee not found');
    }
    return response.json();
  },
};