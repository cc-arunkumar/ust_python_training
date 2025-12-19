import api from "./api";

export interface Notification {
  id: string;
  type: string;
  task_id?: number;
  to_eid?: number;
  from_eid?: number;
  message?: string;
  read?: boolean;
  created_at?: string;
}

const listNotifications = async (unread = false) => {
  const res = await api.get<Notification[]>(`/notifications/list`, {
    params: { unread },
  });
  return res.data;
};

const markRead = async (id: string) => {
  const res = await api.put<Notification>(`/notifications/${id}/read`);
  return res.data;
};

const markAllRead = async () => {
  const res = await api.put(`/notifications/mark_all_read`);
  return res.data;
};

export default { listNotifications, markRead, markAllRead };
