import axios from "axios";

// Base URL points to backend root. Most API wrappers include the /api/v1 prefix
// except authentication which is exposed at `/login` on the root path.
const api = axios.create({ baseURL: "http://localhost:8000" });

api.interceptors.request.use((config) => {
  const token = localStorage.getItem("token");
  if (token) config.headers.Authorization = `Bearer ${token}`;
  return config;
});

export default api;
