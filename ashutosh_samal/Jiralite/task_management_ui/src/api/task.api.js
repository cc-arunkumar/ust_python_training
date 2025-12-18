import axios from "axios";

const API = axios.create({
  baseURL: "http://127.0.0.1:8000",
});

API.interceptors.request.use((req) => {
  const token = localStorage.getItem("token");
  if (token) {
    req.headers.Authorization = `Bearer ${token}`;
  }
  return req;
});

// ================= TASK APIs =================

export const getTasks = async () => {
  const res = await API.get("/tasks/");
  return res.data;
};

export const getTaskById = async (id) => {
  const res = await API.get(`/tasks/${id}`);
  return res.data;
};

export const createTask = async (data) => {
  const res = await API.post("/tasks/", data);
  return res.data;
};

export const updateTask = async (id, data) => {
  const res = await API.put(`/tasks/${id}`, data);
  return res.data;
};

export const deleteTask = async (id) => {
  await API.delete(`/tasks/${id}`);
};

export const updateTaskStatus = async (id, payload) => {
  const res = await API.patch(`/tasks/${id}/status`, payload);
  return res.data;
};

export const updateTaskPriority = async (id, priority) => {
  const res = await API.patch(`/tasks/${id}/priority`, null, {
    params: { priority },
  });
  return res.data;
};