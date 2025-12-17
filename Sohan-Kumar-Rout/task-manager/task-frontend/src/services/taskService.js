import api from "./api";

export const getTasks = async () => {
  return await api.get("/tasks");
};

export const createTask = async (data) => {
  return await api.post("/tasks", data);
};

export const updateTask = async (id, data) => {
  return await api.put(`/tasks/${id}`, data);
};

export const deleteTask = async (id) => {
  return await api.delete(`/tasks/${id}`);
};
