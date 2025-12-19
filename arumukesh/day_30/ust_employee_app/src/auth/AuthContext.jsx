import { createContext, useContext, useState } from "react";
import api from "../api/axios";

const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null);

  const login = async (user_id, password) => {
    const res = await api.post("/login", { user_id, password });
    localStorage.setItem("token", res.data.access_token);
    setUser(parseJwt(res.data.access_token));
  };

  const logout = () => {
    localStorage.removeItem("token");
    setUser(null);
  };

  return (
    <AuthContext.Provider value={{ user, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => useContext(AuthContext);

function parseJwt(token) {
  return JSON.parse(atob(token.split(".")[1]));
}
