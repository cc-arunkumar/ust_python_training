import { Navigate, Outlet } from "react-router-dom";
import { useAuth } from "../../context/AuthContext";

const ProtectedRoute = () => {
  const { user, loading } = useAuth();

  if (loading) {
    return (
      <div className="h-screen flex items-center justify-center text-blue-600 font-bold">
        Checking Authentication...
      </div>
    );
  }

  // If not logged in, kick back to login
  if (!user) {
    return <Navigate to="/login" replace />;
  }

  // 👇 Render the child routes (The Layout, Dashboard, etc.)
  return <Outlet />;
};

export default ProtectedRoute;
