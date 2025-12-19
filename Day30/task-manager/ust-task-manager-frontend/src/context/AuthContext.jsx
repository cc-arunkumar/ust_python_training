//

import { createContext, useContext, useEffect, useState } from "react";
import { jwtDecode } from "jwt-decode";

const AuthContext = createContext(null);

export const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const token = localStorage.getItem("token");
    if (token) {
      try {
        const decoded = jwtDecode(token);
        setUser({
          emp_id: decoded.emp_id || decoded.sub,
          role: decoded.role,
        });
      } catch (err) {
        console.error("Invalid token", err);
        localStorage.removeItem("token");
      }
    } else {
      console.log("No token found in localStorage");
    }
    setLoading(false); // <--- CRITICAL: Must happen even if no token
  }, []);

  const login = (token) => {
    localStorage.setItem("token", token);
    try {
      const decoded = jwtDecode(token);
      setUser({
        emp_id: decoded.emp_id || decoded.sub,
        role: decoded.role,
      });
    } catch (err) {
      console.error("Login decode error", err);
    }
  };

  const logout = () => {
    localStorage.removeItem("token");
    setUser(null);
    window.location.href = "/login";
  };

  return (
    <AuthContext.Provider value={{ user, login, logout, loading }}>
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => useContext(AuthContext);
