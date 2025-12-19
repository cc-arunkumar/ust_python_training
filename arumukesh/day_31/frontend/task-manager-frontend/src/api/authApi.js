import api from "./axios";

export const loginUser = async (user_id, password) => {
  // Backend expects { emp_id: int, password }
  const payload = { emp_id: Number(user_id), password };
  const response = await api.post("/login", payload);
  // store token if present
  if (response?.data?.access_token)
    localStorage.setItem("token", response.data.access_token);
  return response.data;
};
