import React from "react";
import { useAuth } from "../context/AuthContext";
import { useNavigate } from "react-router-dom";

export default function Navbar() {
  const { user, logout } = useAuth();
  const nav = useNavigate();

  const doLogout = () => {
    logout();
    nav("/login");
  };

  return (
    <header className="flex items-center justify-between p-4 bg-white border-b">
      <div className="flex items-center gap-3">
        <div className="w-9 h-9 bg-[var(--accent)] rounded-md flex items-center justify-center text-white font-bold">
          TF
        </div>
        <h1 className="text-lg font-semibold">TaskFlow</h1>
      </div>
      <div className="flex items-center gap-4">
        <input
          className="px-3 py-2 border rounded-md"
          placeholder="Search tasks, users..."
        />
        <div className="flex items-center gap-3">
          {user && (
            <div className="text-sm text-gray-700">
              {user.emp_id || user.user_id || user.sub}
            </div>
          )}
          <button
            onClick={doLogout}
            className="px-3 py-2 bg-red-500 text-white rounded-md"
          >
            Logout
          </button>
        </div>
      </div>
    </header>
  );
}
