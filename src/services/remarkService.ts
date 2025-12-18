import api from "./api";

export interface Remark {
  _id: string;
  task_id: number;
  user_id: number;
  comment: string;
  created_at: string;
  updated_at?: string;
}

export interface RemarkCreateRequest {
  task_id: number;
  comment: string;
}

export const remarkService = {
  // Get remarks for a task
  getRemarksByTask: async (
    task_id: number,
    role?: string
  ): Promise<Remark[]> => {
    // Backend route: GET /api/Remark/getbytask?task_id=<id>&role=<Role>
    const url = `/api/Remark/getbytask?task_id=${task_id}${
      role ? `&role=${encodeURIComponent(role)}` : ""
    }`;
    const response = await api.get(url);
    return response.data || [];
  },

  // Create new remark
  // createRemark requires e_id in header on the backend and accepts optional file upload
  createRemark: async (
    remark: RemarkCreateRequest,
    role: string,
    file?: File | null
  ): Promise<Remark> => {
    // Backend expects a multipart/form-data POST to /api/Remark/create with fields:
    // task_id, comment, role and optional file
    const form = new FormData();
    form.append("task_id", String(remark.task_id));
    form.append("comment", remark.comment);
    form.append("role", role);
    if (file) form.append("file", file);
    const response = await api.post(`/api/Remark/create`, form, {
      headers: { "Content-Type": "multipart/form-data" },
    });
    return response.data;
  },

  // Update remark
  // update uses PUT /api/remarks/{remark_id} with x_user_id and x_role headers
  updateRemark: async (
    remark_id: string,
    comment: string,
    role: string,
    file?: File | null
  ): Promise<Remark> => {
    const form = new FormData();
    form.append("remark_id", remark_id);
    if (comment) form.append("comment", comment);
    if (role) form.append("role", role);
    if (file) form.append("file", file);
    const response = await api.put(`/api/Remark/update`, form, {
      headers: { "Content-Type": "multipart/form-data" },
    });
    return response.data;
  },

  // Delete remark
  deleteRemark: async (remark_id: string, role: string): Promise<void> => {
    // Backend expects /api/Remark/delete?id=<remark_id>&role=<Role>
    await api.delete(
      `/api/Remark/delete?id=${encodeURIComponent(
        remark_id
      )}&role=${encodeURIComponent(role)}`
    );
  },
};
