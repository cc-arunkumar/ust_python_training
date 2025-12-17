import { api } from "./api";
import { API_BASE_URL } from "../utils/constants";

export const authService = {
  login: async (empId, password) => {
    const response = await fetch(`${API_BASE_URL}/auth/login`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        emp_id: parseInt(empId),
        password,
      }),
    });

    if (!response.ok) {
      const error = await response.json();
      throw new Error(error.detail || "Login failed");
    }

    return response.json();
  },

  logout: () => {
    sessionStorage.clear();
  },

  getStoredToken: () => {
    return sessionStorage.getItem("access_token");
  },

  setToken: (token) => {
    sessionStorage.setItem("access_token", token);
  },
};
