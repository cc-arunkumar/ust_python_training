import api from './api';

const baseRoot = api.defaults.baseURL.replace('/api', '');

export const getAttachmentsForTask = async (taskId) => {
  const res = await api.get(`/attachments/task/${taskId}`);
  return res.data;
};

export const uploadAttachment = async (taskId, file) => {
  const form = new FormData();
  // send only the file in the multipart body; taskId is part of the path
  form.append('file', file);
  // POST to /attachments/upload/{taskId}
  const res = await api.post(`/attachments/upload/${encodeURIComponent(String(taskId))}`, form, {
    headers: { 'Content-Type': 'multipart/form-data' },
  });
  return res.data;
};

export const deleteAttachment = async (id) => {
  const res = await api.delete(`/attachments/${id}`);
  return res.data;
};

export const getDownloadUrl = (filePath) => {
  if (!filePath) return null;
  // filePath usually looks like "/uploads/123_file.pdf"
  return `${baseRoot}${filePath}`;
};

export default {
  getAttachmentsForTask,
  uploadAttachment,
  deleteAttachment,
  getDownloadUrl,
};
