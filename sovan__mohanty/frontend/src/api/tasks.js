import api from "./axios";

export const listTasks = async () =>
  (await api.get("/tasks")).data;

export const createTask = async ({ title, description, assigned_to, priority }) =>
  (await api.post("/tasks", null, {
    params: { title, description, assigned_to, priority },
  })).data;

export const updateTaskStatus = async (task_id, status) =>
  (await api.put(`/tasks/${task_id}/status`, null, { params: { status } })).data;

// ✅ New: update task priority (MANAGER/ADMIN only)
export const updateTaskPriority = async (task_id, priority) =>
  (await api.put(`/tasks/${task_id}/priority`, null, { params: { priority } })).data;
