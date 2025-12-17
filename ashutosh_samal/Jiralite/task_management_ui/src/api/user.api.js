import API from "./axios";

/* ================= USERS API ================= */

export const getUsers = async () => {
  const res = await API.get("/users/");
  return res.data;
};

export const getUserById = async (e_id) => {
  const res = await API.get(`/users/${e_id}`);
  return res.data;
};

export const createUser = async (data) => {
  const res = await API.post("/users/", data);
  return res.data;
};

export const updateUser = async (e_id, data) => {
  const res = await API.put(`/users/${e_id}`, data);
  return res.data;
};

export const deleteUser = async (e_id) => {
  await API.delete(`/users/${e_id}`);
};
