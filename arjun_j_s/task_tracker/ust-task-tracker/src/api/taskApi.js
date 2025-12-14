const API_BASE = 'http://localhost:8000';

export const login = async (username, password) => {
  const response = await fetch(`${API_BASE}/login`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ username, password })
  });
  
  if (!response.ok) {
    throw new Error('Invalid username or password');
  }
  
  return await response.json();
};

export const getTasks = async (token) => {
  const response = await fetch(`${API_BASE}/task`, {
    headers: { 'Authorization': `Bearer ${token}` }
  });
  
  if (!response.ok) {
    throw new Error('Failed to fetch tasks');
  }
  
  return await response.json();
};

export const createTask = async (token, task) => {
  const response = await fetch(`${API_BASE}/task`, {
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${token}`,
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(task)
  });
  
  if (!response.ok) {
    throw new Error('Failed to create task');
  }
  
  return await response.json();
};

export const updateTask = async (token, taskId, updates) => {
  const response = await fetch(`${API_BASE}/task/${taskId}`, {
    method: 'PUT',
    headers: {
      'Authorization': `Bearer ${token}`,
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(updates)
  });
  
  if (!response.ok) {
    throw new Error('Failed to update task');
  }
  
  return await response.json();
};

export const deleteTask = async (token, taskId) => {
  const response = await fetch(`${API_BASE}/task/${taskId}`, {
    method: 'DELETE',
    headers: { 'Authorization': `Bearer ${token}` }
  });
  
  if (!response.ok) {
    throw new Error('Failed to delete task');
  }
  
  return await response.json();
};