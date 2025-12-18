// App.js
import { BrowserRouter as Router, Routes, Route, Navigate } from "react-router-dom";
import Sidebar from "./components/Sidebar";
import Topbar from "./components/Topbar";
import Dashboard from "./pages/Dashboard";
import Tasks from "./pages/Tasks";
import Users from "./pages/Users";
import Login from "./pages/Login";
import { Toaster } from "react-hot-toast";

// Protected wrapper with role check
function Protected({ children, allowedRoles }) {
  const token = localStorage.getItem("token");
  if (!token) return <Navigate to="/login" replace />;

  let payload;
  try {
    payload = JSON.parse(atob(token.split(".")[1]));
  } catch (e) {
    console.error("Invalid token", e);
    return <Navigate to="/login" replace />;
  }

  const userRole = payload.role;

  if (allowedRoles && !allowedRoles.includes(userRole)) {
    // redirect employees away from restricted routes
    return <Navigate to="/" replace />;
  }

  return children;
}

// Layout that only shows after login
function AppLayout({ children }) {
  return (
    <div className="flex h-screen">
      <Sidebar />
      <div className="flex-1 flex flex-col bg-gray-50 dark:bg-gray-900">
        <Topbar />
        <div className="flex-1 overflow-y-auto">{children}</div>
      </div>
    </div>
  );
}

export default function App() {
  return (
    <Router>
      <Routes>
        {/* Login route without sidebar/topbar */}
        <Route path="/login" element={<Login />} />

        {/* Protected routes with layout */}
        <Route
          path="/"
          element={
            <Protected>
              <AppLayout>
                <Dashboard />
              </AppLayout>
            </Protected>
          }
        />
        <Route
          path="/tasks"
          element={
            <Protected>
              <AppLayout>
                <Tasks />
              </AppLayout>
            </Protected>
          }
        />
        <Route
          path="/users"
          element={
            <Protected allowedRoles={["ADMIN", "MANAGER"]}>
              <AppLayout>
                <Users />
              </AppLayout>
            </Protected>
          }
        />
      </Routes>

      {/* Toast notifications available globally */}
      <Toaster position="top-right" />
    </Router>
  );
}
