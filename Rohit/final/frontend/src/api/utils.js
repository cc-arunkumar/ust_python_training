import api from "./axios";

export const health = async () =>
  (await api.get("/utils/health")).data;

export const getEmployeeWithUser = async (emp_id) =>
  (await api.get(`/utils/employee/${emp_id}`)).data;
