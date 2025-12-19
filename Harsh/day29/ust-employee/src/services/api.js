import { API_BASE_URL, STORAGE_KEYS } from "../utils/constants";

class ApiService {
  static getHeaders(token = null) {
    const headers = { "Content-Type": "application/json" };
    if (token) {
      headers["Authorization"] = `Bearer ${token}`;
    }
    return headers;
  }

  static async request(endpoint, options = {}) {
    const token = localStorage.getItem(STORAGE_KEYS.TOKEN);

    const response = await fetch(`${API_BASE_URL}${endpoint}`, {
      ...options,
      headers: this.getHeaders(token),
    });

    if (response.status === 401) {
      throw new Error("Invalid credentials"); // <- no reload
    }

    if (response.status === 204) return null;

    let data;
    try {
      data = await response.json();
    } catch {
      throw new Error("Invalid response from server");
    }

    if (!response.ok) {
      throw new Error(data.detail || "Request failed");
    }

    // Normalize legacy task statuses
    if (Array.isArray(data)) {
      return data.map((item) => this._normalizeTaskStatus(item));
    } else if (data && data.status) {
      return this._normalizeTaskStatus(data);
    }

    return data;
  }

  // Normalize IN_PROGRESS -> ON_PROCESS
  static _normalizeTaskStatus(task) {
    if (!task) return task;
    if (task.status === "IN_PROGRESS") task.status = "ON_PROCESS";
    if (task.status === "IN_REVIEW") task.status = "REVIEW";
    return task;
  }

  // Auth APIs
  static async login(email, password) {
    try {
      return await this.request("/auth/login", {
        method: "POST",
        body: JSON.stringify({ email, password }),
      });
    } catch (err) {
      throw new Error("Invalid credentials");
    }
  }

  static async getCurrentUser() {
    return this.request("/auth/me");
  }

  // Employee APIs
  static async getEmployees() {
    return this.request("/employees/");
  }

  static async getEmployee(id) {
    return this.request(`/employees/${id}`);
  }

  static async createEmployee(data) {
    return this.request("/employees/", {
      method: "POST",
      body: JSON.stringify(data),
    });
  }

  static async updateEmployee(id, data) {
    return this.request(`/employees/${id}`, {
      method: "PUT",
      body: JSON.stringify(data),
    });
  }

  static async deleteEmployee(id) {
    return this.request(`/employees/${id}`, { method: "DELETE" });
  }

  // Task APIs
  static async getTasks() {
    return this.request("/tasks/");
  }

  static async getTask(id) {
    return this.request(`/tasks/${id}`);
  }

  static async createTask(data) {
    // Ensure frontend sends correct status
    if (data.status === "IN_PROGRESS") data.status = "ON_PROCESS";
    if (data.status === "IN_REVIEW") data.status = "REVIEW";

    return this.request("/tasks/", {
      method: "POST",
      body: JSON.stringify(data),
    });
  }

  static async updateTask(id, data) {
    if (data.status === "IN_PROGRESS") data.status = "ON_PROCESS";
    if (data.status === "IN_REVIEW") data.status = "REVIEW";

    return this.request(`/tasks/${id}`, {
      method: "PUT",
      body: JSON.stringify(data),
    });
  }

  static async updateTaskStatus(id, status, review = null) {
    if (status === "IN_PROGRESS") status = "ON_PROCESS";
    if (status === "IN_REVIEW") status = "REVIEW";

    const payload = { status };
    if (review) payload.review = review;

    return this.request(`/tasks/${id}/status`, {
      method: "PATCH",
      body: JSON.stringify(payload),
    });
  }

  static async uploadFile(taskId, file) {
    const token = localStorage.getItem(STORAGE_KEYS.TOKEN);
    const formData = new FormData();
    formData.append("file", file);

    const response = await fetch(`${API_BASE_URL}/tasks/${taskId}/upload`, {
      method: "POST",
      headers: {
        Authorization: `Bearer ${token}`,
      },
      body: formData,
    });

    if (!response.ok) {
      const data = await response.json();
      throw new Error(data.detail || "Upload failed");
    }

    return response.json();
  }

  // Remarks APIs (text + optional file upload stored in GridFS)
  static async createRemark(taskId, text = null, file = null) {
    const token = localStorage.getItem(STORAGE_KEYS.TOKEN);
    const formData = new FormData();
    if (text) formData.append("text", text);
    if (file) formData.append("file", file);

    const response = await fetch(`${API_BASE_URL}/tasks/${taskId}/remarks`, {
      method: "POST",
      headers: {
        Authorization: `Bearer ${token}`,
      },
      body: formData,
    });

    if (!response.ok) {
      let data = { detail: "Create remark failed" };
      try {
        data = await response.json();
      } catch (e) {}
      throw new Error(data.detail || "Create remark failed");
    }

    return response.json();
  }

  static async listRemarks(taskId) {
    return this.request(`/tasks/${taskId}/remarks`);
  }

  static getRemarkAttachmentUrl(fileId) {
    return `${API_BASE_URL}/tasks/remarks/attachments/${fileId}`;
  }

  // Fetch attachments and filter by task id as a frontend fallback
  static async getAttachmentsForTask(taskId) {
    // Call the backend endpoint that lists attachments for a task
    try {
      return await this.request(`/tasks/${taskId}/attachments`);
    } catch (err) {
      // if backend doesn't support that route, return empty array
      return [];
    }
  }

  // Delete Task
  static async deleteTask(id) {
    return this.request(`/tasks/${id}`, { method: "DELETE" });
  }

  // User APIs
  static async getUsers() {
    return this.request(`/users/`);
  }

  static async getUser(id) {
    return this.request(`/users/${id}`);
  }

  static async createUser(data) {
    return this.request(`/users/`, {
      method: "POST",
      body: JSON.stringify(data),
    });
  }

  static async updateUser(id, data) {
    return this.request(`/users/${id}`, {
      method: "PUT",
      body: JSON.stringify(data),
    });
  }

  static async deleteUser(id) {
    return this.request(`/users/${id}`, { method: "DELETE" });
  }
}

export default ApiService;
