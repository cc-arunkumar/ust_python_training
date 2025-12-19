// src/auth/AuthContext.jsx
import { createContext, useContext, useState } from "react";

const AuthContext = createContext(null);

export const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(() => {
    try {
      return JSON.parse(localStorage.getItem("user"));
    } catch {
      return null;
    }
  });

  const login = (data) => {
    if (!data?.user) {
      console.error("Login response missing user data", data);
      return;
    }

    // ✅ USE `roles` (plural) — EXACT match with backend
    const normalizedUser = {
      emp_id: data.user.emp_id,
      roles: Array.isArray(data.user.roles)
        ? data.user.roles
        : [],
    };

    localStorage.setItem("token", data.access_token);
    localStorage.setItem("user", JSON.stringify(normalizedUser));
    setUser(normalizedUser);
  };

  const logout = () => {
    localStorage.removeItem("token");
    localStorage.removeItem("user");
    setUser(null);
  };

  return (
    <AuthContext.Provider value={{ user, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => {
  const ctx = useContext(AuthContext);
  if (!ctx) {
    throw new Error("useAuth must be used within AuthProvider");
  }
  return ctx;
};
