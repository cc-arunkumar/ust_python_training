import React, {
  createContext,
  useContext,
  useState,
  useEffect,
  ReactNode,
} from "react";
import { authAPI, normalizeRoleForApi } from "../services/api";
import type { User, LoginCredentials } from "../types";

interface AuthContextType {
  user: User | null;
  token: string | null;
  login: (credentials: LoginCredentials) => Promise<void>;
  logout: () => void;
  isLoading: boolean;
  isAuthenticated: boolean;
  activeRole: string | null;
  setActiveRole: (role: string) => void;
}

const AuthContext = createContext<AuthContextType | undefined>(undefined);

export const AuthProvider: React.FC<{ children: ReactNode }> = ({
  children,
}) => {
  const [user, setUser] = useState<User | null>(null);
  const [token, setToken] = useState<string | null>(
    localStorage.getItem("token")
  );
  const [isLoading, setIsLoading] = useState(true);
  const [activeRole, setActiveRoleState] = useState<string | null>(
    localStorage.getItem("activeRole")
  );

  useEffect(() => {
    const initAuth = async () => {
      const storedToken = localStorage.getItem("token");
      if (storedToken) {
        try {
          const userData = await authAPI.getMe();
          setUser(userData);
          setToken(storedToken);
          // initialize activeRole from storage or default to first role
          const storedRole = localStorage.getItem("activeRole");
          if (storedRole) {
            setActiveRoleState(storedRole);
          } else if (userData?.role) {
            const defaultRole = normalizeRoleForApi(userData.role) || null;
            if (defaultRole) {
              setActiveRoleState(defaultRole);
              localStorage.setItem("activeRole", defaultRole);
            }
          }
        } catch (error) {
          localStorage.removeItem("token");
          setToken(null);
        }
      }
      setIsLoading(false);
    };
    initAuth();
  }, []);

  const login = async (credentials: LoginCredentials) => {
    try {
      const response = await authAPI.login(credentials);
      // Temporary debug logs to help trace sign-in issues
      // eslint-disable-next-line no-console
      console.log("authAPI.login response:", response);
      localStorage.setItem("token", response.access_token);
      setToken(response.access_token);
      if (response.user) {
        setUser(response.user);
        // set default active role on login (normalize stored value)
        const defaultRole = normalizeRoleForApi(response.user.role) || null;
        setActiveRoleState(defaultRole);
        if (defaultRole) localStorage.setItem("activeRole", defaultRole);
      } else {
        throw new Error("User data not received from server");
      }
    } catch (err) {
      // eslint-disable-next-line no-console
      console.error("authAPI.login error:", err);
      throw err;
    }
  };

  const logout = () => {
    localStorage.removeItem("token");
    localStorage.removeItem("activeRole");
    setToken(null);
    setUser(null);
  };

  return (
    <AuthContext.Provider
      value={{
        user,
        token,
        login,
        logout,
        isLoading,
        isAuthenticated: !!token && !!user,
        activeRole,
        setActiveRole: (role: string) => {
          setActiveRoleState(role);
          localStorage.setItem("activeRole", role);
        },
      }}
    >
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => {
  const context = useContext(AuthContext);
  if (context === undefined) {
    throw new Error("useAuth must be used within an AuthProvider");
  }
  return context;
};
