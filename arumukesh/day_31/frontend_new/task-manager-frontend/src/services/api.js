import axios from "axios";
import { toast } from "react-toastify";

const api = axios.create({
  baseURL: import.meta.env.VITE_API_BASE_URL || "http://localhost:8000",
  headers: {
    "Content-Type": "application/json",
  },
});

// Request interceptor
api.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem("token");
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

// Response interceptor
api.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response) {
      const { status, data } = error.response;

      if (status === 401) {
        // Unauthorized - token expired or invalid
        localStorage.removeItem("token");
        window.location.href = "/login";
        toast.error("Session expired. Please login again.");
      } else if (status === 403) {
        toast.error("You do not have permission to perform this action.");
      } else if (status === 404) {
        toast.error("Resource not found.");
      } else if (status >= 500) {
        toast.error("Server error. Please try again later.");
      } else {
        toast.error(data.detail || "An error occurred.");
      }
    } else if (error.request) {
      // If this was a network-level failure (no response) we show a toast
      // except for endpoints that manage their own optimistic-retry flows
      // (remarks are handled in-component to avoid noisy global toasts).
      const url = error.config?.url || "";
      if (!url.includes("/remarks")) {
        toast.error("Network error. Please check your connection.");
      }
    } else {
      toast.error("An unexpected error occurred.");
    }

    return Promise.reject(error);
  }
);

export default api;
