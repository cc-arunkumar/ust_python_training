import React, { useEffect, useState } from "react";
import { api, setAuthToken, getStoredToken } from "./api";
import Login from "./components/Login";
import TaskList from "./components/TaskList";
import TaskForm from "./components/TaskForm";
import "./App.css";

export default function App() {
  const [token, setToken] = useState(getStoredToken());
  const [tasks, setTasks] = useState([]);
  const [loading, setLoading] = useState(false);
  const [toast, setToast] = useState(null);

  useEffect(() => {
    if (token) {
      setAuthToken(token);
      fetchTasks();
    }
  }, [token]);

  const showToast = (type, msg) => {
    setToast({ type, msg });
    setTimeout(() => setToast(null), 2000);
  };

  const fetchTasks = async () => {
    try {
      setLoading(true);
      const { data } = await api.get("/tasks");
      setTasks(data);
    } catch (e) {
      showToast("error", "Failed to load tasks");
    } finally {
      setLoading(false);
    }
  };

  const handleLogin = async (username, password) => {
    try {
      const { data } = await api.post("/login", { username, password });
      setToken(data.access_token);
      setAuthToken(data.access_token);
      showToast("success", "Logged in");
    } catch (e) {
      showToast("error", "Invalid credentials");
    }
  };

  const handleCreate = async (title, description) => {
    try {
      const { data } = await api.post("/tasks", { title, description });
      setTasks((prev) => [data, ...prev]);
      showToast("success", "Task created");
    } catch {
      showToast("error", "Create failed");
    }
  };

  const handleUpdate = async (taskId, updates) => {
    try {
      const { data } = await api.put(`/tasks/${taskId}`, updates);
      setTasks((prev) => prev.map((t) => (t.id === taskId ? data : t)));
      showToast("success", "Task updated");
    } catch {
      showToast("error", "Update failed");
    }
  };

  const handleDelete = async (taskId) => {
    try {
      await api.delete(`/tasks/${taskId}`);
      setTasks((prev) => prev.filter((t) => t.id !== taskId));
      showToast("success", "Task deleted");
    } catch {
      showToast("error", "Delete failed");
    }
  };

  const logout = () => {
    setAuthToken(null);
    setToken(null);
    setTasks([]);
    showToast("success", "Logged out");
  };

  return (
    <div className="app-shell">
      <div className="glass-card">
        <header className="header">
          <h1 className="brand">UST Task Manager</h1>
          {!!token && (
            <button className="btn ghost" onClick={logout}>
              Logout
            </button>
          )}
        </header>

        {!token ? (
          <Login onLogin={handleLogin} />
        ) : (
          <>
            <TaskForm onCreate={handleCreate} loading={loading} />
            <TaskList
              tasks={tasks}
              onUpdate={handleUpdate}
              onDelete={handleDelete}
              refresh={fetchTasks}
            />
          </>
        )}
      </div>

      {toast && (
        <div className={`toast ${toast.type}`}>
          <span>{toast.msg}</span>
        </div>
      )}
    </div>
  );
}
