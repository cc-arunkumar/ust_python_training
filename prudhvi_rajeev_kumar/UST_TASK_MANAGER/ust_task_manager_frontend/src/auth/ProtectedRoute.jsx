import { useContext } from "react";
import { Navigate } from "react-router-dom";
import { AuthContext } from "./AuthContext";

export default function ProtectedRoute({ children, allowRoles }) {
  const { user } = useContext(AuthContext);
  if (!user) return <Navigate to="/" replace />;
  if (allowRoles && !allowRoles.includes(user.role)) {
    return <Navigate to="/dashboard" replace />;
  }
  return children;
}
