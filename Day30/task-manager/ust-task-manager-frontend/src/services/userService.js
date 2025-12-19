import api from "./api";

export const userService = {
  getAll: async () => {
    const response = await api.get("/api/users");
    return response.data;
  },
  create: async (data) => {
    return await api.post("/api/users", data);
  },
  updatePassword: async (empId, password) => {
    return await api.put(`/api/users/${empId}/password`, { password });
  },
  delete: async (empId) => {
    return await api.delete(`/api/users/${empId}`);
  }
};