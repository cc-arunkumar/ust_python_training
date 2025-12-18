import { useEffect, useState, useMemo } from "react";
import { getUser } from "../api/users";
import { listTasks } from "../api/tasks";
import { health } from "../api/utils";

export default function Topbar() {
  const [user, setUser] = useState(null);
  const [tasks, setTasks] = useState([]);
  const [healthInfo, setHealthInfo] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const token = localStorage.getItem("token");
    if (!token) {
      setLoading(false);
      return;
    }

    let payload;
    try {
      payload = JSON.parse(atob(token.split(".")[1]));
    } catch (e) {
      console.error("Invalid token", e);
      setLoading(false);
      return;
    }

    const userId = payload.user_id;
    Promise.all([
      getUser(userId).then(setUser).catch(() => setUser(null)),
      health().then(setHealthInfo).catch(() => setHealthInfo(null)),
      listTasks().then(setTasks).catch(() => setTasks([])),
    ]).finally(() => setLoading(false));
  }, []);

  const visibleTasks = useMemo(() => {
    if (!user) return [];
    return user.role === "EMPLOYEE"
      ? tasks.filter((t) => t.assigned_to === user.emp_id)
      : tasks;
  }, [tasks, user]);

  const statusCounts = useMemo(() => {
    return {
      TO_DO: visibleTasks.filter((t) => t.status === "TO_DO").length,
      IN_PROGRESS: visibleTasks.filter((t) => t.status === "IN_PROGRESS").length,
      REVIEW: visibleTasks.filter((t) => t.status === "REVIEW").length,
      DONE: visibleTasks.filter((t) => t.status === "DONE").length,
    };
  }, [visibleTasks]);

  if (loading) {
    return (
      <div className="flex justify-center items-center h-full">
        <p className="text-gray-500 text-lg animate-pulse">Loading dashboard...</p>
      </div>
    );
  }

  const onLogout = () => {
    localStorage.removeItem("token");
    window.location.href = "/login";
  };

  const roleBadge = (role) => {
    switch (role) {
      case "ADMIN":
        return "bg-gradient-to-r from-red-500 to-pink-500 text-white shadow-md";
      case "MANAGER":
        return "bg-gradient-to-r from-purple-500 to-indigo-500 text-white shadow-md";
      case "EMPLOYEE":
        return "bg-gradient-to-r from-green-500 to-emerald-600 text-white shadow-md";
      default:
        return "bg-gradient-to-r from-gray-400 to-gray-600 text-white shadow-md";
    }
  };

  const roleAvatar = (role) => {
    switch (role) {
      case "ADMIN":
        return "https://copilot.microsoft.com/th/id/BCO.4ff84e9e-7416-4bd3-820e-6fa395d61511.png";
      case "MANAGER":
        return "https://copilot.microsoft.com/th/id/BCO.ecc157cf-960b-4b18-bc6c-eac4ef0d3174.png";
      case "EMPLOYEE":
        return "https://copilot.microsoft.com/th/id/BCO.7bb27235-0f53-4931-81a3-c1f1525066dc.png";
      default:
        return "https://via.placeholder.com/40";
    }
  };

  return (
    <div className="h-20 bg-gradient-to-r from-slate-900 via-slate-800 to-slate-900 shadow-lg flex items-center justify-between px-8">
      {/* App title */}
      <div className="text-3xl font-extrabold tracking-wide text-transparent bg-clip-text bg-gradient-to-r from-cyan-400 to-blue-500">
        TaskFlow Dashboard
      </div>

      <div className="flex items-center space-x-8">
        {user && (
          <div className="flex items-center space-x-4">
            {/* Circular avatar */}
            <div className="w-14 h-14 rounded-full overflow-hidden border-2 border-cyan-400 shadow-md">
              <img
                src={roleAvatar(user.role)}
                alt={`${user.role} avatar`}
                className="w-full h-full object-cover"
              />
            </div>
            {/* Role badge */}
            <span
              className={`px-4 py-1.5 rounded-full text-sm font-semibold uppercase tracking-wide ${roleBadge(
                user.role
              )}`}
            >
              {user.role}
            </span>
          </div>
        )}

        {/* Logout button */}
        <button
          onClick={onLogout}
          className="px-4 py-2 rounded-lg bg-gradient-to-r from-blue-500 to-indigo-600 text-white font-medium shadow hover:scale-105 transform transition-all duration-200"
        >
          Logout
        </button>
      </div>
    </div>
  );
}
