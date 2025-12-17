import { api } from "./api";

export const taskService = {
  getAllTasks: async () => {
    return api.get("/tasks");
  },

  getTaskById: async (taskId) => {
    return api.get(`/tasks/${taskId}`);
  },

  createTask: async (taskData) => {
    return api.post("/tasks", taskData);
  },

  updateTask: async (taskId, taskData) => {
    return api.put(`/tasks/${taskId}`, taskData);
  },

  updateTaskStatus: async (taskId, status) => {
    return api.patch(`/tasks/${taskId}`, { status });
  },

  deleteTask: async (taskId) => {
    return api.delete(`/tasks/${taskId}`);
  },

  getTasksByManager: async (managerId) => {
    return api.get(`/tasks/manager/${managerId}`);
  },

  addRemark: async (taskId, remark) => {
    return api.patch(`/tasks/remark/${taskId}`, remark);
  },
};
