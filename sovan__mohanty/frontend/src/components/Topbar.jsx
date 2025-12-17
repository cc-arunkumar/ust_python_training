import { useEffect, useState } from "react";
import { getUser } from "../api/users";

export default function Topbar() {
  const [user, setUser] = useState(null);

  useEffect(() => {
    const token = localStorage.getItem("token");
    if (!token) return;
    const payload = JSON.parse(atob(token.split(".")[1]));
    getUser(payload.user_id).then(setUser).catch(() => setUser(null));
  }, []);

  const onLogout = () => {
    localStorage.removeItem("token");
    window.location.href = "/login";
  };

  const roleBadge = (role) => {
    switch (role) {
      case "ADMIN":
        return "bg-red-100 text-red-600 dark:bg-red-900 dark:text-red-300";
      case "MANAGER":
        return "bg-purple-100 text-purple-600 dark:bg-purple-900 dark:text-purple-300";
      case "EMPLOYEE":
        return "bg-green-100 text-green-600 dark:bg-green-900 dark:text-green-300";
      default:
        return "bg-gray-100 text-gray-600 dark:bg-gray-700 dark:text-gray-300";
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
    <div className="h-16 bg-white dark:bg-gray-900 shadow flex items-center justify-between px-6">
      <div className="text-lg font-semibold text-gray-800 dark:text-gray-200">
        Jira Lite
      </div>
      <div className="flex items-center space-x-4">
        {user && (
          <div className="flex items-center space-x-2">
            {/* Circular avatar */}
            <div className="w-10 h-10 rounded-full overflow-hidden border-2 border-gray-300 dark:border-gray-600">
              <img
                src={roleAvatar(user.role)}
                alt={`${user.role} avatar`}
                className="w-full h-full object-cover"
              />
            </div>
            {/* Role badge */}
            <span
              className={`px-2 py-1 rounded text-xs font-medium ${roleBadge(
                user.role
              )}`}
            >
              {user.role}
            </span>
          </div>
        )}

        <button
          onClick={onLogout}
          className="text-sm text-blue-600 dark:text-blue-400 hover:underline"
        >
          Logout
        </button>
      </div>
    </div>
  );
}
