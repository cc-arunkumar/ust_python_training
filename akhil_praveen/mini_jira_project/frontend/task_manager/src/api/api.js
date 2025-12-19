import { API_BASE } from "../utils/constants";

class ApiService {
  async request(endpoint, options = {}) {
    const token = localStorage.getItem("token");
    const headers = {
      "Content-Type": "application/json",
      ...(token && { Authorization: `Bearer ${token}` }),
      ...options.headers,
    };

    const response = await fetch(`${API_BASE}${endpoint}`, {
      ...options,
      headers,
    });

    if (response.status === 401) {
      localStorage.removeItem("token");
      localStorage.removeItem("role");
      window.location.reload();
      throw new Error("Unauthorized");
    }

    if (!response.ok) {
      const error = await response.json();
      throw new Error(error.detail || "Request failed");
    }

    // Handle 204 No Content
    if (response.status === 204) {
      return null;
    }

    return response.json();
  }

  // Auth
  login(email, password) {
    return this.request("/auth/login", {
      method: "POST",
      body: JSON.stringify({ email, password }),
    });
  }

  getCurrentUser() {
    return this.request(`/auth/me`);
  }

  // Tasks
  getTasks() {
    return this.request("/tasks/");
  }

  getTask(id) {
    return this.request(`/tasks/${id}`);
  }

  createTask(data) {
    return this.request("/tasks/", {
      method: "POST",
      body: JSON.stringify(data),
    });
  }

  updateTask(id, data) {
    return this.request(`/tasks/${id}`, {
      method: "PUT",
      body: JSON.stringify(data),
    });
  }

  updateTaskStatus(id, status, review = null, extraFields = undefined) {
    const payload = { status };

    // Only add review if it's not null/empty
    if (review && review.trim()) {
      payload.review = review.trim();
    }

    // merge any extra fields (role-specific review fields)
    if (extraFields && typeof extraFields === "object") {
      Object.assign(payload, extraFields);
    }

    return this.request(`/tasks/${id}/status`, {
      method: "PATCH",
      body: JSON.stringify(payload),
    });
  }

  // fetch reviews stored in Mongo for a task
  getTaskReviews(id) {
    return this.request(`/tasks/${id}/reviews`);
  }

  // Employees
  getEmployees() {
    return this.request("/employees/");
  }

  getEmployee(id) {
    return this.request(`/employees/${id}`);
  }

  createEmployee(data) {
    return this.request("/employees/", {
      method: "POST",
      body: JSON.stringify(data),
    });
  }

  updateEmployee(id, data) {
    return this.request(`/employees/${id}`, {
      method: "PUT",
      body: JSON.stringify(data),
    });
  }

  deleteEmployee(id) {
    return this.request(`/employees/${id}`, {
      method: "DELETE",
    });
  }

  // Users (Admin)
  getUsers() {
    return this.request("/users/");
  }

  getUser(id) {
    return this.request(`/users/${id}`);
  }

  createUser(data) {
    return this.request("/users/", {
      method: "POST",
      body: JSON.stringify(data),
    });
  }

  updateUser(id, data) {
    return this.request(`/users/${id}`, {
      method: "PUT",
      body: JSON.stringify(data),
    });
  }

  deleteUser(id) {
    return this.request(`/users/${id}`, {
      method: "DELETE",
    });
  }
}

const api = new ApiService();
export default api;
