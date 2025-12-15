import axios from "axios";

const API_BASE = "http://127.0.0.1:8000"; // FastAPI default host/port

export const api = axios.create({
  baseURL: API_BASE,
});

export const setAuthToken = (token) => {
  if (token) {
    api.defaults.headers.common["Authorization"] = `Bearer ${token}`;
    localStorage.setItem("token", token);
  } else {
    delete api.defaults.headers.common["Authorization"];
    localStorage.removeItem("token");
  }
};

export const getStoredToken = () => localStorage.getItem("token");
