import { API_BASE_URL, STORAGE_KEYS } from '../utils/constants';

class ApiService {
  static getHeaders(token = null) {
    const headers = { 'Content-Type': 'application/json' };
    if (token) {
      headers['Authorization'] = `Bearer ${token}`;
    }
    return headers;
  }

  static async request(endpoint, options = {}) {
    const token = localStorage.getItem(STORAGE_KEYS.TOKEN);

    const response = await fetch(`${API_BASE_URL}${endpoint}`, {
      ...options,
      headers: this.getHeaders(token),
    });

    // Do NOT redirect on 401. Just throw
    if (response.status === 401) {
      throw new Error('Invalid credentials'); // <- removed reload
    }

    if (response.status === 204) return null;

    const data = await response.json();

    if (!response.ok) {
      throw new Error(data.detail || 'Request failed');
    }

    return data;
  }

  // Auth APIs
  static async login(email, password) {
    try {
      return await this.request('/auth/login', {
        method: 'POST',
        body: JSON.stringify({ email, password }),
      });
    } catch (err) {
      // Throw same error for LoginPage to catch
      throw new Error('Invalid credentials');
    }
  }

  static async getCurrentUser() {
    return this.request('/auth/me');
  }

  // Employee APIs
  static async getEmployees() {
    return this.request('/employees/');
  }

  static async getEmployee(id) {
    return this.request(`/employees/${id}`);
  }

  static async createEmployee(data) {
    return this.request('/employees/', {
      method: 'POST',
      body: JSON.stringify(data),
    });
  }

  static async updateEmployee(id, data) {
    return this.request(`/employees/${id}`, {
      method: 'PUT',
      body: JSON.stringify(data),
    });
  }

  static async deleteEmployee(id) {
    return this.request(`/employees/${id}`, {
      method: 'DELETE',
    });
  }

  // Task APIs
  static async getTasks() {
    return this.request('/tasks/');
  }

  static async getTask(id) {
    return this.request(`/tasks/${id}`);
  }

  static async createTask(data) {
    return this.request('/tasks/', {
      method: 'POST',
      body: JSON.stringify(data),
    });
  }

  static async updateTask(id, data) {
    return this.request(`/tasks/${id}`, {
      method: 'PUT',
      body: JSON.stringify(data),
    });
  }

  static async updateTaskStatus(id, status, review = null) {
    const payload = { status };
    if (review) payload.review = review;

    return this.request(`/tasks/${id}/status`, {
      method: 'PATCH',
      body: JSON.stringify(payload),
    });
  }

  static async uploadFile(taskId, file) {
    const token = localStorage.getItem(STORAGE_KEYS.TOKEN);
    const formData = new FormData();
    formData.append('file', file);

    const response = await fetch(`${API_BASE_URL}/tasks/${taskId}/upload`, {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${token}`,
      },
      body: formData,
    });

    if (!response.ok) {
      const data = await response.json();
      throw new Error(data.detail || 'Upload failed');
    }

    return response.json();
  }
}

export default ApiService;
