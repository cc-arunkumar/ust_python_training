// src/api/taskApi.js
import api from "./axios";

// GET tasks
export const getTasks = () =>
  api.get("/api/v1/tasks");

// GET task by id
export const getTaskById = (id) =>
  api.get(`/api/v1/tasks/${id}`);

// CREATE task
export const createTask = (data) =>
  api.post("/api/v1/tasks", data);

// UPDATE task (non-status)
export const updateTask = (id, data) =>
  api.put(`/api/v1/tasks/${id}`, data);

// UPDATE task status
export const updateTaskStatus = (id, status) =>
  api.patch(`/api/v1/tasks/${id}/status`, { status });

// DELETE task
export const deleteTask = (id) =>
  api.delete(`/api/v1/tasks/${id}`);
