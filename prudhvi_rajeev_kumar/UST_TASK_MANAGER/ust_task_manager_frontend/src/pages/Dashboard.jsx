import { useEffect, useState, useContext } from "react";
import { useNavigate } from "react-router-dom";
import api from "../api/axios";
import { AuthContext } from "../auth/AuthContext";

export default function Dashboard() {
  const { user } = useContext(AuthContext);
  const [stats, setStats] = useState({ todo: 0, inprogress: 0, review: 0, done: 0 });
  const [recentActivity, setRecentActivity] = useState([]);
  const navigate = useNavigate();

  useEffect(() => {
    api.get("/tasks").then((res) => {
      const tasks = res.data;
      const counts = { todo: 0, inprogress: 0, review: 0, done: 0 };
      tasks.forEach((t) => {
        if (counts[t.status] !== undefined) counts[t.status]++;
      });
      setStats(counts);
    });

    api.get("/activity").then((res) => {
      setRecentActivity(res.data);
    }).catch(() => {
      setRecentActivity([
        "Rajeev moved Task #12 to Done",
        "Manager created Task #15",
        "Admin added new user"
      ]);
    });
  }, []);

  return (
    <div className="container">
      <h2>Dashboard</h2>
      <p>Welcome, <strong>{user?.sub}</strong> — Role: <strong>{user?.role}</strong></p>

      {/* Stats Cards */}
      <div className="stats-grid">
        <div className="stat-card todo"><h3>To Do</h3><p>{stats.todo} tasks</p></div>
        <div className="stat-card inprogress"><h3>In Progress</h3><p>{stats.inprogress} tasks</p></div>
        <div className="stat-card review"><h3>Review</h3><p>{stats.review} tasks</p></div>
        <div className="stat-card done"><h3>Done</h3><p>{stats.done} tasks</p></div>
      </div>

      {/* Role-specific sections */}
      {user?.role === "employee" && (
        <div className="card">
          <h3>Your Tasks</h3>
          <button className="btn" onClick={() => navigate("/tasks")}>View My Tasks</button>
        </div>
      )}
      {user?.role === "manager" && (
        <div className="card">
          <h3>Manager Tools</h3>
          <button className="btn" onClick={() => navigate("/manage")}>Assign New Task</button>
          <button className="btn" onClick={() => navigate("/tasks")}>Review Tasks</button>
        </div>
      )}
      {user?.role === "admin" && (
        <div className="card">
          <h3>Admin Controls</h3>
          <button className="btn" onClick={() => navigate("/admin")}>Create User</button>
          <button className="btn" onClick={() => navigate("/reports")}>System Reports</button>
          <button className="btn" onClick={() => navigate("/admin")}>Manage Roles</button>
        </div>
      )}

      {/* Recent Activity */}
      <div className="card">
        <h3>Recent Activity</h3>
        <ul>
          {recentActivity.map((item, i) => <li key={i}>{item}</li>)}
        </ul>
      </div>
    </div>
  );
}
