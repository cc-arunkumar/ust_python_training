import { createContext, useContext, useEffect, useState } from "react";

const AuthContext = createContext();

export function AuthProvider({ children }) {
  const [user, setUser] = useState(null);
  const [activeRole, setActiveRole] = useState(null);
  const [loading, setLoading] = useState(true);

  // 🔁 Restore session
  useEffect(() => {
    const token = localStorage.getItem("token");
    if (token) {
      setUser({});                 // minimal user
      setActiveRole("DEVELOPER");  // default role
    }
    setLoading(false);
  }, []);

  const login = ({ roles }) => {
    setUser({});
    setActiveRole(roles?.[0] || "DEVELOPER");
  };

  const logout = () => {
    localStorage.clear();
    setUser(null);
    setActiveRole(null);
  };

  const switchRole = (role) => {
    setActiveRole(role);
  };

  return (
    <AuthContext.Provider
      value={{
        user,
        activeRole,
        isAuthenticated: !!localStorage.getItem("token"), // ✅ KEY FIX
        login,
        logout,
        switchRole,
        loading,
      }}
    >
      {children}
    </AuthContext.Provider>
  );
}

export function useAuth() {
  return useContext(AuthContext);
}
