import { BrowserRouter as Router, Routes, Route, Navigate } from "react-router-dom";
import Sidebar from "./components/Sidebar";
import Topbar from "./components/Topbar";
import Dashboard from "./pages/Dashboard";
import Tasks from "./pages/Tasks";
import Users from "./pages/Users";
import Login from "./pages/Login";
import { Toaster } from "react-hot-toast";

function Protected({ children }) {
  const token = localStorage.getItem("token");
  if (!token) return <Navigate to="/login" replace />;
  return children;
}

export default function App() {
  return (
    <Router>
      <div className="flex h-screen">
        <Sidebar />
        {/* main content area now supports dark mode */}
        <div className="flex-1 flex flex-col bg-gray-50 dark:bg-gray-900">
          <Topbar />
          <div className="flex-1 overflow-y-auto">
            <Routes>
              <Route
                path="/"
                element={
                  <Protected>
                    <Dashboard />
                  </Protected>
                }
              />
              <Route
                path="/tasks"
                element={
                  <Protected>
                    <Tasks />
                  </Protected>
                }
              />
              <Route
                path="/users"
                element={
                  <Protected>
                    <Users />
                  </Protected>
                }
              />
              <Route path="/login" element={<Login />} />
            </Routes>
          </div>
        </div>
      </div>
      {/* Toast notifications available globally */}
      <Toaster position="top-right" />
    </Router>
  );
}
