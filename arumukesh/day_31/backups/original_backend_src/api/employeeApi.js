import api from "./axios";

export const getEmployees = () => api.get("/employees");
export const createEmployee = (data) => api.post("/employees", data);
export const updateEmployee = (emp_id, data) =>
  api.put(`/employees/${emp_id}`, data);
export const deleteEmployee = (emp_id) => api.delete(`/employees/${emp_id}`);
