import axios from 'axios';

// Create axios instance
const api = axios.create({
  baseURL: import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000', 
  headers: {
    "Content-Type": "application/json"
  }
});

// Attach JWT token to every request
api.interceptors.request.use((config) => {
  const token = localStorage.getItem("token");
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

// ================= AUTH =================

export const login = async (username, password) => {
  try {
    const response = await api.post('/login', { username, password });
    
    // Store token in localStorage
    localStorage.setItem('token', response.data.access_token);
    
    return response.data;
  } catch (error) {
    if (error.response?.status === 401) {
      throw new Error('Invalid username or password');
    }
    throw new Error(error.response?.data?.detail || 'Login failed');
  }
};

export const logout = () => {
  localStorage.removeItem('token');
};

export const isAuthenticated = () => {
  return !!localStorage.getItem('token');
};

// ================= TASKS =================

export const getTasks = async () => {
  try {
    const response = await api.get('/task');
    return response.data;
  } catch (error) {
    if (error.response?.status === 401) {
      localStorage.removeItem('token');
      throw new Error('Session expired. Please login again.');
    }
    throw new Error(error.response?.data?.detail || 'Failed to fetch tasks');
  }
};

export const getTaskById = async (taskId) => {
  try {
    const response = await api.get(`/task/${taskId}`);
    return response.data;
  } catch (error) {
    if (error.response?.status === 404) {
      throw new Error('Task not found');
    }
    if (error.response?.status === 401) {
      localStorage.removeItem('token');
      throw new Error('Session expired. Please login again.');
    }
    throw new Error(error.response?.data?.detail || 'Failed to fetch task');
  }
};

export const createTask = async (task) => {
  try {
    const response = await api.post('/task', {
      title: task.title,
      description: task.description,
      completed: task.completed ?? false
    });
    return response.data;
  } catch (error) {
    if (error.response?.status === 401) {
      localStorage.removeItem('token');
      throw new Error('Session expired. Please login again.');
    }
    throw new Error(error.response?.data?.detail || 'Failed to create task');
  }
};

export const updateTask = async (taskId, updates) => {
  try {
    const response = await api.put(`/task/${taskId}`, {
      title: updates.title,
      description: updates.description,
      completed: updates.completed
    });
    return response.data;
  } catch (error) {
    if (error.response?.status === 404) {
      throw new Error('Task not found');
    }
    if (error.response?.status === 401) {
      localStorage.removeItem('token');
      throw new Error('Session expired. Please login again.');
    }
    throw new Error(error.response?.data?.detail || 'Failed to update task');
  }
};

export const deleteTask = async (taskId) => {
  try {
    const response = await api.delete(`/task/${taskId}`);
    return response.data;
  } catch (error) {
    if (error.response?.status === 404) {
      throw new Error('Task not found');
    }
    if (error.response?.status === 401) {
      localStorage.removeItem('token');
      throw new Error('Session expired. Please login again.');
    }
    throw new Error(error.response?.data?.detail || 'Failed to delete task');
  }
};

export default api;