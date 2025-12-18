import React, { useState, useEffect } from "react";
import { Routes, Route } from "react-router-dom";
import LoginPage from "./pages/LoginPage";
import DashboardPage from "./pages/DashboardPage";
import EmployeesPage from "./pages/EmployeesPage";
import Home from "./pages/Home";
import Navigation from "./components/Navigation";
import { ToastProvider } from "./components/Toast";
import { apiService } from "./services/api";
import "./index.css";
import "./App.css";

const App = () => {
  const [currentPage, setCurrentPage] = useState("login");
  const [authToken, setAuthToken] = useState(null);
  const [currentUser, setCurrentUser] = useState(null);
  // use the same key other components expect
  const [selectedRole, setSelectedRole] = useState(
    () => localStorage.getItem("taskflow_role") || null
  );

  useEffect(() => {
    // hydrate token from storage if present
    const t = apiService.getToken();
    if (t) setAuthToken(t);
  }, []);

  const handleLogin = (token, userData, remember = true) => {
    // store token according to remember
    apiService.setToken(token, remember);
    setAuthToken(token);

    // normalize user object (support both shapes: { user: {...} } or direct user)
    const normalized = userData?.user || userData || {};
    setCurrentUser(normalized);

    // prefer roles array, fallback to single role string
    const role =
      normalized?.roles?.[0] ||
      (Array.isArray(normalized?.role) ? normalized.role[0] : null) ||
      normalized?.role ||
      null;

    setSelectedRole(role);
    if (role) localStorage.setItem("taskflow_role", role);

    // persist normalized user so Navigation/Home can read it
    try {
      localStorage.setItem("taskflow_user", JSON.stringify(normalized));
    } catch (e) {
      /* ignore storage errors */
    }

    setCurrentPage("dashboard");
  };

  const handleLogout = () => {
    apiService.clearToken();
    setAuthToken(null);
    setCurrentUser(null);
    setSelectedRole(null);
    localStorage.removeItem("taskflow_role");
    localStorage.removeItem("taskflow_user");
    setCurrentPage("login");
  };

  if (currentPage === "login") {
    return (
      <ToastProvider>
        <LoginPage
          onLogin={(token, userData) => handleLogin(token, userData)}
        />
      </ToastProvider>
    );
  }

  return (
    <ToastProvider>
      <div className="min-h-screen bg-gray-50">
        {/* Render Navigation only when not on login page */}
        {currentPage !== "login" && (
          <Navigation
            currentPage={currentPage}
            setCurrentPage={setCurrentPage}
            currentUser={currentUser}
            selectedRole={selectedRole}
            onLogout={handleLogout}
            onRoleChange={(r) => {
              setSelectedRole(r);
              if (r) localStorage.setItem("taskflow_role", r);
            }}
          />
        )}

        <Routes>
          <Route
            path="/"
            element={
              <DashboardPage
                currentUser={currentUser}
                selectedRole={selectedRole}
                authToken={authToken}
              />
            }
          />
          <Route
            path="/employees"
            element={
              <EmployeesPage
                authToken={authToken}
                selectedRole={selectedRole}
              />
            }
          />
          <Route path="/home" element={<Home />} />
          {/* other routes can be added */}
        </Routes>
      </div>
    </ToastProvider>
  );
};

export default App;
