import { API_BASE } from '../utils/constants';

class ApiService {
  request(endpoint, options = {}) {
    const token = localStorage.getItem('token');
    const headers = {
      'Content-Type': 'application/json',
      ...(token && { Authorization: `Bearer ${token}` }),
      ...options.headers,
    };

    return fetch(`${API_BASE}${endpoint}`, {
      ...options,
      headers,
    })
      .then(response => {
        if (response.status === 401) {
          localStorage.removeItem('token');
          localStorage.removeItem('role');
          window.location.reload();
          throw new Error('Unauthorized');
        }

        if (!response.ok) {
          return response.json()
            .then(error => {
              console.error('API Error Response:', error);
              
              let errorMessage = 'Request failed';
              
              // Handle FastAPI validation errors (422)
              if (response.status === 422 && error.detail) {
                if (Array.isArray(error.detail)) {
                  errorMessage = error.detail.map(err => 
                    `${err.loc.join('.')}: ${err.msg}`
                  ).join(', ');
                } else {
                  errorMessage = error.detail;
                }
              } else {
                errorMessage = error.detail || error.message || `HTTP ${response.status}: ${response.statusText}`;
              }
              
              throw new Error(errorMessage);
            })
            .catch(e => {
              if (e instanceof Error) throw e;
              throw new Error(`HTTP ${response.status}: ${response.statusText}`);
            });
        }

        // Handle 204 No Content
        if (response.status === 204) {
          return null;
        }

        return response.json();
      })
      .catch(error => {
        if (error instanceof Error) {
          throw error;
        }
        throw new Error(String(error));
      });
  }

  // Auth
  login(email, password) {
    return this.request('/auth/login', {
      method: 'POST',
      body: JSON.stringify({ email, password }),
    });
  }

  // Tasks
  getTasks() {
    return this.request('/tasks/');
  }

  getTask(id) {
    return this.request(`/tasks/${id}`);
  }

  createTask(data) {
    return this.request('/tasks/', {
      method: 'POST',
      body: JSON.stringify(data),
    });
  }

  updateTask(id, data) {
    return this.request(`/tasks/${id}`, {
      method: 'PUT',
      body: JSON.stringify(data),
    });
  }

  updateTaskStatus(id, status, review) {
    return this.request(`/tasks/${id}/status`, {
      method: 'PATCH',
      body: JSON.stringify({ status, review }),
    });
  }

  // Employees
  getEmployees() {
    return this.request('/employees/');
  }

  getEmployee(id) {
    return this.request(`/employees/${id}`);
  }

  createEmployee(data) {
    return this.request('/employees/', {
      method: 'POST',
      body: JSON.stringify(data),
    });
  }

  updateEmployee(id, data) {
    return this.request(`/employees/${id}`, {
      method: 'PUT',
      body: JSON.stringify(data),
    });
  }

  deleteEmployee(id) {
    return this.request(`/employees/${id}`, {
      method: 'DELETE',
    });
  }
}

const api = new ApiService();
export default api;