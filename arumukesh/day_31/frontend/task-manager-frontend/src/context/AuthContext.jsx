import React, { createContext, useContext, useEffect, useState } from "react";
import api from "../api/axios";
import { loginUser as apiLogin } from "../api/authApi";

/* eslint-disable react-refresh/only-export-components */
const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null);

  useEffect(() => {
    const token = localStorage.getItem("token");
    if (token) {
      api.defaults.headers.common["Authorization"] = `Bearer ${token}`;
      try {
        const payload = JSON.parse(atob(token.split(".")[1]));
        // avoid synchronous setState inside effect per lint rule
        setTimeout(() => setUser(payload), 0);
      } catch (e) {
        console.warn("Invalid token in storage", e);
        localStorage.removeItem("token");
      }
    }
  }, []);

  const login = async (user_id, password) => {
    const data = await apiLogin(user_id, password);
    if (data?.access_token) {
      localStorage.setItem("token", data.access_token);
      api.defaults.headers.common[
        "Authorization"
      ] = `Bearer ${data.access_token}`;
      try {
        setUser(JSON.parse(atob(data.access_token.split(".")[1])));
      } catch (e) {
        console.warn(e);
        setUser(null);
      }
    }
    return data;
  };

  const logout = () => {
    localStorage.removeItem("token");
    delete api.defaults.headers.common["Authorization"];
    setUser(null);
  };

  return (
    <AuthContext.Provider value={{ user, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => useContext(AuthContext);
