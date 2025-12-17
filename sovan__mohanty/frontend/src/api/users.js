import api from "./axios";

export const loginByUser = async (user_id, password) =>
  (await api.post("/users/login/by-user", null, { params: { user_id, password } })).data;

export const getUser = async (user_id) =>
  (await api.get(`/users/${user_id}`)).data;

export const listUsers = async () =>
  (await api.get("/users")).data;

export const updateUserStatus = async (user_id, status) =>
  (await api.patch(`/users/${user_id}/status`, null, { params: { status } })).data;
