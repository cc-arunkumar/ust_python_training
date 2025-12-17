import api from "./axios";

export const getEmployeeWithUser = async (emp_id) =>
  (await api.get(`/utils/employee/${emp_id}`)).data;
