// src/services/authService.js
import api from "./api.js";

export const authService = {
  login: async (empId, password) => {
    const params = new URLSearchParams();
    params.append("username", empId);
    params.append("password", password);

    try {
      const response = await api.post(
        "/api/auth/login",
        params,
        {
          headers: {
            "Content-Type": "application/x-www-form-urlencoded",
          },
        }
      );

      // Backend returns { access_token, token_type }
      const token = response.data.access_token;

      if (!token) {
        throw new Error("No token received from server");
      }

      // ✅ RETURN TOKEN STRING ONLY
      return token;
    } catch (error) {
      console.error(
        "Login failed:",
        error.response?.data || error.message
      );
      throw error;
    }
  },
};

export default authService;
