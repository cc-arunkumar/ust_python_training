import React, { useState } from "react";
import { LayoutDashboard } from "lucide-react";
import { apiService } from "../services/api";
import { useNavigate } from "react-router-dom";
import "./LoginPage.css";

const LoginPage = ({ onLogin }) => {
  const [empId, setEmpId] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const navigate = useNavigate();

  const submit = async (e) => {
    e.preventDefault();
    setError("");
    const id = empId.trim();

    if (!id || !password) {
      setError("Please enter Employee ID and Password");
      return;
    }

    function parseJwt(token) {
      try {
        const payload = token.split(".")[1];
        const json = atob(payload.replace(/-/g, "+").replace(/_/g, "/"));
        return JSON.parse(decodeURIComponent(escape(json)));
      } catch {
        return null;
      }
    }

    try {
      if (!apiService?.login) throw new Error("apiService.login not available");

      const res = await apiService.login(id, password);
      const token = res?.access_token || res?.token;
      if (!token) {
        setError("Login failed: no token returned");
        return;
      }

      // persist token
      apiService.setToken(token, true);

      // fetch employee/user info (declare empData in outer scope)
      let empData = null;
      try {
        empData = await apiService.getEmployeeWithUser(id, token);
        console.log("getEmployeeWithUser response:", empData);
      } catch (err) {
        console.warn("Failed to fetch employee/user:", err);
        empData = null;
      }

      // build normalized user object
      const userObj = {
        id: empData?.emp_id || empData?.employee?.id || empData?.user?.id || id,
        name:
          empData?.name ||
          empData?.user?.name ||
          empData?.employee?.name ||
          "User",
        roles:
          empData?.user?.roles ||
          empData?.roles ||
          (empData?.role
            ? Array.isArray(empData.role)
              ? empData.role
              : [empData.role]
            : null) ||
          [],
      };

      // if roles still empty, try decoding JWT
      if (!userObj.roles || userObj.roles.length === 0) {
        const jwt = parseJwt(token);
        const jwtRoles =
          jwt?.roles ||
          (jwt?.role
            ? Array.isArray(jwt.role)
              ? jwt.role
              : [jwt.role]
            : null);
        if (jwtRoles) userObj.roles = jwtRoles;
      }
      if (!userObj.roles || userObj.roles.length === 0)
        userObj.roles = ["Employee"];

      const finalRole = String(userObj.roles[0] || "Employee");

      // persist user and role
      localStorage.setItem("taskflow_user", JSON.stringify(userObj));
      localStorage.setItem("taskflow_role", finalRole);
      console.log("Saved taskflow_user:", userObj);
      console.log("Saved taskflow_role:", finalRole);

      // inform parent and navigate
      if (typeof onLogin === "function") {
        try {
          onLogin(token, { user: userObj }, true);
        } catch (err) {
          console.warn("onLogin handler error:", err);
        }
      }

      navigate("/home", { replace: true });
      setTimeout(() => {
        if (window.location.pathname !== "/home")
          window.location.assign("/home");
      }, 300);
    } catch (err) {
      console.error("Login error:", err);
      setError(err?.message || "Login failed");
    }
  };

  return (
    <div className="tf-login-root">
      <div className="tf-login-card" role="form" aria-label="Login form">
        <div className="tf-icon" aria-hidden>
          <LayoutDashboard size={28} />
        </div>
        <h1 className="tf-title">Welcome back</h1>
        <p className="tf-sub">Sign in to continue</p>

        <form onSubmit={submit} className="tf-form" noValidate>
          <label className="tf-label">
            Employee ID
            <input
              className="tf-input"
              value={empId}
              onChange={(e) => {
                setEmpId(e.target.value);
                setError("");
              }}
              placeholder="e.g. EMP001"
              aria-label="Employee ID"
              required
            />
          </label>

          <label className="tf-label">
            Password
            <input
              className="tf-input"
              value={password}
              onChange={(e) => {
                setPassword(e.target.value);
                setError("");
              }}
              type="password"
              placeholder="Password"
              aria-label="Password"
              required
            />
          </label>

          {error && (
            <div className="tf-error" role="alert">
              {error}
            </div>
          )}

          <button className="tf-btn" type="submit" aria-label="Sign in">
            Sign In
          </button>
        </form>
      </div>
    </div>
  );
};

export default LoginPage;
