import React, { createContext, useContext, useState, useCallback } from "react";
import { User, Employee, Role, AuthContextType } from "@/types";
import api from "@/services/api"; // axios instance

const AuthContext = createContext<AuthContextType | undefined>(undefined);

export const AuthProvider: React.FC<{ children: React.ReactNode }> = ({
  children,
}) => {
  const [user, setUser] = useState<(User & { employee: Employee }) | null>(
    () => {
      const saved = localStorage.getItem("currentUser");
      return saved ? JSON.parse(saved) : null;
    }
  );
  const login = useCallback(
    async (e_id: string, password: string): Promise<boolean> => {
      try {
        const emp_id = parseInt(e_id, 10); // convert string to number
        if (isNaN(emp_id)) return false;

        const res = await api.post("/api/auth/login", {
          username: emp_id, // backend expects numeric emp_id
          password,
        });

        const { access_token, user } = res.data;
        localStorage.setItem("token", access_token);
        localStorage.setItem("currentUser", JSON.stringify(user));

        setUser(user);
        return true;
      } catch {
        return false;
      }
    },
    []
  );

  const logout = useCallback(() => {
    setUser(null);
    localStorage.removeItem("currentUser");
    localStorage.removeItem("token");
  }, []);

  // 🔁 ROLE FLAGS (developer ➜ employee)
  const isAdmin = user?.role.includes("admin") ?? false;
  const isManager = user?.role.includes("manager") ?? false;
  const isEmployee = user?.role.includes("employee") ?? false;

  // 🧠 Highest role resolution
  const highestRole: Role = isAdmin
    ? "admin"
    : isManager
    ? "manager"
    : "employee";

  return (
    <AuthContext.Provider
      value={{
        user,
        login,
        loading: false,
        logout,
        isAdmin,
        isManager,
        isEmployee,
        highestRole,
      }}
    >
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = (): AuthContextType => {
  const context = useContext(AuthContext);
  if (context === undefined) {
    throw new Error("useAuth must be used within an AuthProvider");
  }
  return context;
};
