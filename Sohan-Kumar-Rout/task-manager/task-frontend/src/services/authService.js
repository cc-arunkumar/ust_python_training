import api from "./api";

export const loginUser = async (emp_id, password) => {
  const res = await api.post("/login", { emp_id, password });
  return res.data;
};
