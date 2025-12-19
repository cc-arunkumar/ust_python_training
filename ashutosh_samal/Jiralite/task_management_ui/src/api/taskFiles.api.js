import axios from "./axios"; // your existing axios instance

export const uploadTaskFile = (taskId, file) => {
  const formData = new FormData();
  formData.append("file", file);

  return axios.post(`/tasks/${taskId}/files`, formData, {
    headers: { "Content-Type": "multipart/form-data" },
  });
};

export const getTaskFiles = (taskId) => {
  return axios.get(`/tasks/${taskId}/files`);
};

export const downloadTaskFile = (taskId, fileId) => {
  return axios.get(`/tasks/${taskId}/files/${fileId}`, {
    responseType: "blob",
  });
};
