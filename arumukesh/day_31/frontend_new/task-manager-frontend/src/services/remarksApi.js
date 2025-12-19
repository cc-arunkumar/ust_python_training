import api from "./api";

export const remarksApi = {
  getRemarks: async (taskId) => {
    const response = await api.get(`/api/v1/tasks/${taskId}/remarks`);
    return response.data;
  },

  postRemark: async (taskId, message) => {
    const response = await api.post(`/api/v1/tasks/${taskId}/remarks`, {
      message,
    });
    return response.data;
  },
};

export default remarksApi;
