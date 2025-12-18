// services/api.ts
import axios from "axios";

const api = axios.create({
  baseURL: "http://localhost:8000", // your backend URL
});

api.interceptors.request.use((config) => {
  const token = localStorage.getItem("token"); // or your auth store
  if (token && config.headers) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

export default api;
