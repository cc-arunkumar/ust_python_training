import api from "./axios";

export const loginUser = async (user_id, password) => {
  const response = await api.post("/login", { user_id, password });
  return response.data;
};
