import React, { useState, useEffect } from "react";
import LoginPage from "./components/auth/LoginPage";
import Dashboard from "./components/dashboard/Dashboard";
import { authService } from "./services/authService";
import { parseJWT } from "./utils/helpers";

const App = () => {
  console.log("App component rendered");
  const [user, setUser] = useState(null);

  useEffect(() => {
    console.log("useEffect running");
    const token = authService.getStoredToken();
    console.log("Token from storage:", token ? "exists" : "none");

    if (token) {
      try {
        const payload = parseJWT(token);
        console.log("Parsed payload:", payload);
        if (payload) {
          setUser({
            access_token: token,
            role: payload.role || "developer",
            name: payload.name || "User",
            emp_id: parseInt(payload.sub),
          });
        }
      } catch (e) {
        console.error("Error restoring session:", e);
      }
    }
  }, []);

  const handleLogin = (userObj) => {
    console.log("Login successful:", userObj);
    setUser(userObj);
  };

  const handleLogout = () => {
    console.log("Logging out");
    authService.logout();
    setUser(null);
  };

  console.log("Current user state:", user);

  return (
    <div className="min-h-screen">
      {!user ? (
        <LoginPage onLogin={handleLogin} />
      ) : (
        <Dashboard user={user} onLogout={handleLogout} />
      )}
    </div>
  );
};

export default App;
