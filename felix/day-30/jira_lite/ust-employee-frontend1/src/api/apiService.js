import { API_BASE_URL } from '../utils/constants';
import { getToken } from '../utils/helpers';

// Base API call function
const apiCall = async (endpoint, options = {}) => {
  const token = getToken();
  
  const defaultHeaders = {
    'Content-Type': 'application/json',
  };

  if (token) {
    defaultHeaders['Authorization'] = `Bearer ${token}`;
  }

  const config = {
    ...options,
    headers: {
      ...defaultHeaders,
      ...options.headers,
    },
  };

  try {
    const response = await fetch(`${API_BASE_URL}${endpoint}`, config);
    
    if (!response.ok) {
      const error = await response.json();
      throw new Error(error.detail || 'Something went wrong');
    }

    return await response.json();
  } catch (error) {
    console.error('API Error:', error);
    throw error;
  }
};

// Authentication APIs
export const authAPI = {
  login: async (empId, password) => {
    return apiCall('/login', {
      method: 'POST',
      body: JSON.stringify({
        emp_id: parseInt(empId),
        password: password
      })
    });
  }
};

// Employee APIs
export const employeeAPI = {
  getAll: async (managerId) => {
    return apiCall(`/employees/${managerId}`);
  },

  getOne: async (managerId, empId) => {
    return apiCall(`/employees/${managerId}/${empId}`);
  },

  create: async (employeeData) => {
    return apiCall('/employees', {
      method: 'POST',
      body: JSON.stringify(employeeData)
    });
  },

  update: async (managerId, empId, employeeData) => {
    return apiCall(`/employees/${managerId}/${empId}`, {
      method: 'PUT',
      body: JSON.stringify(employeeData)
    });
  },

  delete: async (managerId, empId) => {
    return apiCall(`/employees/${managerId}/${empId}`, {
      method: 'DELETE'
    });
  }
};

// Task APIs
export const taskAPI = {
  getAll: async () => {
    return apiCall('/tasks');
  },

  getById: async (taskId) => {
    return apiCall(`/tasks/${taskId}`);
  },

  getByEmployee: async (empId) => {
    return apiCall(`/tasks/employee?id=${empId}`);
  },

  getByManager: async () => {
    return apiCall('/tasks/manager');
  },

  create: async (taskData) => {
    return apiCall('/create_tasks', {
      method: 'PUT',
      body: JSON.stringify(taskData)
    });
  },

  update: async (taskId, taskData) => {
    return apiCall(`/update_one_tasks/${taskId}`, {
      method: 'PUT',
      body: JSON.stringify(taskData)
    });
  },

  updateStatus: async (taskId, status) => {
    return apiCall(`/tasks/${taskId}/status`, {
      method: 'PATCH',
      body: JSON.stringify({ status })
    });
  },

  updateRemarks: async (empId, taskId, remarks) => {
    return apiCall(`/tasks/${empId}/${taskId}/remarks`, {
      method: 'PATCH',
      body: JSON.stringify({ remarks })
    });
  }
};

export default {
  auth: authAPI,
  employee: employeeAPI,
  task: taskAPI
};