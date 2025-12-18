import React, { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import { apiService } from "../services/api";
import "./Home.css";

export default function Home() {
  const navigate = useNavigate();
  const [user, setUser] = useState(null);
  const [role, setRole] = useState("Employee");
  const [tasks, setTasks] = useState([]);
  const [loadingTasks, setLoadingTasks] = useState(false);
  const [taskError, setTaskError] = useState(null);

  useEffect(() => {
    const stored = localStorage.getItem("taskflow_user");
    if (!stored) {
      navigate("/");
      return;
    }
    const u = JSON.parse(stored);
    setUser(u);
    setRole(
      localStorage.getItem("taskflow_role") || u?.roles?.[0] || "Employee"
    );
  }, [navigate]);

  useEffect(() => {
    function onRoleEvent(e) {
      setRole(e.detail);
    }
    window.addEventListener("taskflow:roleChange", onRoleEvent);
    return () => window.removeEventListener("taskflow:roleChange", onRoleEvent);
  }, []);

  useEffect(() => {
    // load tasks from backend and compute stats dynamically
    let mounted = true;
    async function loadTasks() {
      setLoadingTasks(true);
      setTaskError(null);
      try {
        const token = apiService.getToken();
        const data = await apiService.getTasks(token);
        if (!mounted) return;
        setTasks(Array.isArray(data) ? data : data?.tasks || []);
      } catch (err) {
        console.error("Failed to load tasks:", err);
        if (mounted) setTaskError(err.message || "Failed to load tasks");
      } finally {
        if (mounted) setLoadingTasks(false);
      }
    }
    loadTasks();
    return () => {
      mounted = false;
    };
  }, []);

  if (!user) return null;

  const stats = {
    total: tasks.length,
    inProgress: tasks.filter((t) =>
      (t.status || "").toLowerCase().includes("progress")
    ).length,
    review: tasks.filter((t) =>
      (t.status || "").toLowerCase().includes("review")
    ).length,
    done: tasks.filter((t) => (t.status || "").toLowerCase().includes("done"))
      .length,
  };

  return (
    <div className="tf-home-root">
      <main className="tf-main">
        <section className="tf-hero">
          <h2>Welcome back, {user.name}</h2>
          <p className="tf-hero-sub">
            Here’s what’s happening with your projects today.
          </p>
        </section>

        <section className="tf-stats" aria-label="Task summary">
          <div className="tf-stat-card">
            <div className="tf-stat-value">
              {loadingTasks ? "…" : stats.total}
            </div>
            <div className="tf-stat-label">Total Tasks</div>
          </div>
          <div className="tf-stat-card">
            <div className="tf-stat-value">{stats.inProgress}</div>
            <div className="tf-stat-label">In Progress</div>
          </div>
          <div className="tf-stat-card">
            <div className="tf-stat-value">{stats.review}</div>
            <div className="tf-stat-label">Review</div>
          </div>
          <div className="tf-stat-card">
            <div className="tf-stat-value">{stats.done}</div>
            <div className="tf-stat-label">Done</div>
          </div>
        </section>

        {taskError && (
          <div className="tf-error">Error loading tasks: {taskError}</div>
        )}

        <section className="tf-board" aria-label="Task board">
          {tasks.slice(0, 10).map((t) => (
            <article key={t.id || t.task_id} className="tf-task">
              <div className="tf-task-title">{t.title || t.name}</div>
              <div className="tf-task-meta">
                <span className="tf-assignee">
                  {t.assignee || t.owner || "-"}
                </span>
                <span className="tf-due">{t.due_date || t.due || ""}</span>
                <span
                  className={`tf-badge tf-priority-${(
                    t.priority || "low"
                  ).toLowerCase()}`}
                >
                  {t.priority || "N/A"}
                </span>
              </div>
            </article>
          ))}
          {tasks.length === 0 && !loadingTasks && (
            <div className="tf-no-results">No tasks found.</div>
          )}
        </section>
      </main>
    </div>
  );
}
