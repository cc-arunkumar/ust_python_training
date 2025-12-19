import api from "./axios";

// Task endpoints live under /api/v1 on the backend
export const getTasks = () => api.get("/api/v1/tasks");
export const getTaskById = (id) => api.get(`/api/v1/tasks/${id}`);
export const createTask = (data) => api.post("/api/v1/tasks", data);
export const updateTask = (id, data) => api.put(`/api/v1/tasks/${id}`, data);
export const updateTaskStatus = (id, status) =>
  // Backend expects both t_id and status in the request body
  api.patch(`/api/v1/tasks/${id}/status`, { t_id: id, status });
export const deleteTask = (id) => api.delete(`/api/v1/tasks/${id}`);
