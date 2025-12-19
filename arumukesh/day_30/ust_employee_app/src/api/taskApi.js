import api from "./axios";

export const getTasks = () => api.get("/tasks");
export const getTaskById = (id) => api.get(`/tasks/${id}`);
export const createTask = (data) => api.post("/tasks", data);
export const updateTask = (id, data) => api.put(`/tasks/${id}`, data);
export const updateTaskStatus = (id, status) =>
  api.patch(`/tasks/${id}/status`, { status });
export const deleteTask = (id) => api.delete(`/tasks/${id}`);
