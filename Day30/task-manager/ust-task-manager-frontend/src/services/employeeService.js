import api from "./api";

export const employeeService = {
  getAll: async () => {
    const response = await api.get("/api/employees");
    return response.data;
  },
  create: async (data) => {
    return await api.post("/api/employees", data);
  },
  update: async (id, data) => {
    return await api.put(`/api/employees/${id}`, data);
  },
  delete: async (id) => {
    return await api.delete(`/api/employees/${id}`);
  },
};
