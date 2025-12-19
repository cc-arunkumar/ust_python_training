import api from './api';

export const getAttachments = async () => {
  const res = await api.get('/attachments');
  return res.data;
};

export const createAttachment = async (data) => {
  return await api.post('/attachments', data);
};

export const uploadAttachment = async (formData) => {
  // formData is a FormData instance with fields: task_id, uploaded_by, file
  // Let the browser set the Content-Type including boundary
  return await api.post('/attachments/upload', formData);
};

export const deleteAttachment = async (id) => {
  return await api.delete(`/attachments/${id}`);
};
