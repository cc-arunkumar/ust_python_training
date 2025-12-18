import React, { createContext, useState, useEffect, useContext } from "react";
import { api } from "../services/api";

const AuthContext = createContext(undefined);

export const useAuth = () => {
  const context = useContext(AuthContext);
  if (context === undefined) {
    // Avoid throwing to prevent the whole app from crashing if a component
    // accidentally calls useAuth outside of the provider (helps dev/debug).
    // Log a warning and return a safe fallback.
    // NOTE: Ideally the app should be wrapped with <AuthProvider /> — this
    // fallback only prevents an uncaught runtime error.
    // eslint-disable-next-line no-console
    console.warn(
      "useAuth() called outside of AuthProvider — returning fallback auth object."
    );
    return {
      user: null,
      token: null,
      loading: true,
      login: async () => {},
      logout: () => {},
      isAuthenticated: false,
    };
  }
  return context;
};

export const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null);
  const [token, setToken] = useState(localStorage.getItem("token"));
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const storedUser = localStorage.getItem("user");
    if (storedUser && token) {
      setUser(JSON.parse(storedUser));
    }
    setLoading(false);
  }, [token]);

  const login = async (emp_id, password) => {
    const data = await api.login(emp_id, password);
    localStorage.setItem("token", data.token);

    // TODO: Get actual roles from API response
    // For now using all roles for testing
    const userData = {
      emp_id,
      roles: ["admin", "manager", "developer"],
    };

    localStorage.setItem("user", JSON.stringify(userData));
    setToken(data.token);
    setUser(userData);
  };

  const logout = () => {
    localStorage.removeItem("token");
    localStorage.removeItem("user");
    setToken(null);
    setUser(null);
  };

  const value = {
    user,
    token,
    loading,
    login,
    logout,
    isAuthenticated: !!user && !!token,
  };

  return <AuthContext.Provider value={value}>{children}</AuthContext.Provider>;
};
