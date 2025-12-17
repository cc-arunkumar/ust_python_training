import api from "./axios";

export const login = (data) => api.post("/auth/login", data);

export const switchRole = (role) =>
  api.post(`/auth/switch-role?active_role=${role}`);
