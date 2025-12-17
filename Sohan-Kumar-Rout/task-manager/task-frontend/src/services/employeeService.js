import api from "./api";

export const getEmployees = async () => {
  const res = await api.get("/employees");
  return res.data;
};

export const createEmployee = async (data) => {
  return await api.post("/employees", data);
};

export const updateEmployee = async (id, data) => {
  return await api.put(`/employees/${id}`, data);
};

export const deleteEmployee = async (id) => {
  return await api.delete(`/employees/${id}`);
};
