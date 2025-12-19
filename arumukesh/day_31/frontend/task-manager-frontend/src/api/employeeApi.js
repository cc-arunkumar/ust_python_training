import api from "./axios";

// Employee endpoints are namespaced under /api/v1 on the backend
export const getEmployees = () => api.get("/api/v1/employees");
export const createEmployee = (data) => api.post("/api/v1/employees", data);
export const updateEmployee = (id, data) =>
  api.put(`/api/v1/employees/${id}`, data);
export const deleteEmployee = (id) => api.delete(`/api/v1/employees/${id}`);
