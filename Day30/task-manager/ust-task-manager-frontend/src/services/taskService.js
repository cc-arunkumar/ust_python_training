import api from "./api";

export const taskService = {
  getAll: async () => {
    // Request a larger limit to avoid missing tasks due to pagination (default backend limit is 10)
    const response = await api.get("/api/tasks", {
      params: { page: 1, limit: 1000 },
    });
    // Handle both paginated ({tasks: [], total: ...}) and flat array formats
    return response.data.tasks ? response.data.tasks : response.data;
  },
  getMy: async () => {
    const response = await api.get("/api/tasks/my");
    return response.data; // { created: [], assigned: [], reviewer: [] }
  },
  create: async (data) => {
    return await api.post("/api/tasks", data);
  },
  uploadFile: async (taskId, file) => {
    const form = new FormData();
    form.append("file", file);
    // Let the browser set the Content-Type (including boundary) for multipart/form-data
    return await api.post(`/api/tasks/${taskId}/files`, form);
  },
  update: async (id, data) => {
    return await api.put(`/api/tasks/${id}`, data);
  },
  updateStatus: async (id, status, priority) => {
    return await api.patch(`/api/tasks/${id}/status`, { status, priority });
  },
  delete: async (id) => {
    return await api.delete(`/api/tasks/${id}`);
  },
};
