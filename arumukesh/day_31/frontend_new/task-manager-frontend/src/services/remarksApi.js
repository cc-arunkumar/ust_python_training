import api from "./api";

export const remarksApi = {
  getRemarks: async (taskId) => {
    const response = await api.get(`/api/v1/tasks/${taskId}/remarks`);
    return response.data;
  },

  postRemark: async (taskId, message, files) => {
    // send multipart formdata if files provided
    if (files && files.length) {
      const fd = new FormData();
      if (message) fd.append("message", message);
      files.forEach((f) => fd.append("files", f));
      const response = await api.post(`/api/v1/tasks/${taskId}/remarks`, fd);
      return response.data;
    }

    const response = await api.post(`/api/v1/tasks/${taskId}/remarks`, {
      message,
    });
    return response.data;
  },
};

export default remarksApi;
