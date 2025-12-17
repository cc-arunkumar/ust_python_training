import api from "./axios";

export const uploadFile = async (file) => {
  const formData = new FormData();
  formData.append("file", file);
  const res = await api.post("/utils/upload", formData, {
    headers: { "Content-Type": "multipart/form-data" },
  });
  return res.data;
};
