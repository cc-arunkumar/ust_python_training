import axios from "axios";

const API = "http://localhost:8000/api";

export const getTasks = () =>
  axios.get(`${API}/tasks`);

export const getTaskById = (id) =>
  axios.get(`${API}/tasks/${id}`);

export const createTask = (task) =>
  axios.post(`${API}/tasks`, task);

export const updateTask = (id, task) =>
  axios.put(`${API}/tasks/${id}`, task);

export const deleteTask = (id) =>
  axios.delete(`${API}/tasks/${id}`);
