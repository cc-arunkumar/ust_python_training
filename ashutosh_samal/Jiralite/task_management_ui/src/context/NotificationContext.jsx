import { createContext, useContext, useEffect, useState } from "react";
import { getTasks, updateTask } from "../api/task.api";

const NotificationContext = createContext();

export function NotificationProvider({ children }) {
  const [notifications, setNotifications] = useState([]);

  const loadNotifications = async () => {
    const tasks = await getTasks();

    const all = tasks
      .filter((t) => t.notification)
      .map((t) => ({
        taskId: t.t_id,
        ...t.notification,
      }))
      .sort((a, b) => new Date(b.ts) - new Date(a.ts));

    setNotifications(all);
  };

  const markAsRead = async (taskId) => {
    await updateTask(taskId, {
      notification: { read: true },
    });
    loadNotifications();
  };

  useEffect(() => {
    loadNotifications();
  }, []);

  return (
    <NotificationContext.Provider
      value={{
        notifications,
        unreadCount: notifications.filter((n) => !n.read).length,
        reload: loadNotifications,
        markAsRead,
      }}
    >
      {children}
    </NotificationContext.Provider>
  );
}

export function useNotifications() {
  return useContext(NotificationContext);
}
