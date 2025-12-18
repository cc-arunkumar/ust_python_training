import React, { useEffect, useState } from "react";
import { LogOut, LayoutDashboard } from "lucide-react";
import { NavLink, useNavigate } from "react-router-dom";
import "./Navigation.css";

const Navigation = ({ onLogout, ...props }) => {
  const navigate = useNavigate();
  const [user, setUser] = useState(null);
  const [role, setRole] = useState("");

  useEffect(() => {
    const u = JSON.parse(localStorage.getItem("taskflow_user") || "null");
    setUser(u);
    const r =
      localStorage.getItem("taskflow_role") || u?.roles?.[0] || "Employee";
    setRole(r);
  }, []);

  useEffect(() => {
    function onStorageChange() {
      const u = JSON.parse(localStorage.getItem("taskflow_user") || "null");
      setUser(u);
    }
    window.addEventListener("storage", onStorageChange);
    return () => window.removeEventListener("storage", onStorageChange);
  }, []);

  // changed: delegate logout to parent if provided
  function logout() {
    if (typeof onLogout === "function") {
      onLogout();
      return;
    }
    // fallback if parent handler not provided
    localStorage.removeItem("taskflow_user");
    localStorage.removeItem("taskflow_role");
    navigate("/");
  }

  function handleRoleChange(next) {
    setRole(next);
    localStorage.setItem("taskflow_role", next);
    window.dispatchEvent(
      new CustomEvent("taskflow:roleChange", { detail: next })
    );
  }

  const initials = (user?.name || "User")
    .split(" ")
    .map((n) => n[0])
    .slice(0, 2)
    .join("");

  return (
    <header
      className="tf-nav"
      role="navigation"
      aria-label="TaskFlow Navigation"
    >
      <div className="tf-nav-left">
        <div className="tf-brand" onClick={() => navigate("/home")} aria-hidden>
          <LayoutDashboard size={20} style={{ marginRight: 8 }} />
          TaskFlow
        </div>
        <nav className="tf-links" aria-label="Main links">
          <NavLink
            to="/home"
            className={({ isActive }) => (isActive ? "active" : "")}
          >
            Dashboard
          </NavLink>
          <NavLink
            to="/employees"
            className={({ isActive }) => (isActive ? "active" : "")}
          >
            Employees
          </NavLink>
        </nav>
      </div>

      <div className="tf-nav-right">
        <div className="tf-role-wrap">
          <label className="tf-role-label">Your Role</label>
          <select
            aria-label="Select role"
            className="tf-role-select"
            value={role}
            onChange={(e) => handleRoleChange(e.target.value)}
          >
            {(user?.roles || ["Employee"]).map((r) => (
              <option key={r} value={r}>
                {r}
              </option>
            ))}
          </select>
        </div>

        <div
          className="tf-user"
          title={`${user?.name || ""} • ${user?.id || ""}`}
        >
          <div className="tf-avatar">{initials}</div>
          <div className="tf-user-info">
            <div className="tf-user-name">{user?.name || "User Name"}</div>
            <div className="tf-user-id">{user?.id || "EMP000"}</div>
          </div>
        </div>

        <button className="tf-logout" onClick={logout} aria-label="Logout">
          <LogOut size={16} style={{ marginRight: 6 }} />
          Logout
        </button>
      </div>
    </header>
  );
};

export default Navigation;
