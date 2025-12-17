import { BrowserRouter, Routes, Route } from "react-router-dom";
import { AuthProvider } from "./auth/AuthContext";
import ProtectedRoute from "./auth/ProtectedRoute";
import Sidebar from "./components/Sidebar";
import Topbar from "./components/Topbar";
import LoginPage from "./pages/LoginPage";
import Dashboard from "./pages/Dashboard";
import TasksPage from "./pages/TasksPage";
import ManageTasksPage from "./pages/ManageTasksPage";
import AdminPage from "./pages/AdminPage";
import { useState } from "react";

export default function App() {
  const [search, setSearch] = useState("");

  return (
    <AuthProvider>
      <BrowserRouter>
        <Sidebar />
        {/* Topbar is now global */}
        <Topbar search={search} setSearch={setSearch} />
        <Routes>
          <Route path="/" element={<LoginPage />} />
          <Route
            path="/dashboard"
            element={
              <ProtectedRoute>
                <Dashboard />
              </ProtectedRoute>
            }
          />
          <Route
            path="/tasks"
            element={
              <ProtectedRoute allowRoles={["employee", "manager", "admin"]}>
                <TasksPage search={search} />
              </ProtectedRoute>
            }
          />
          <Route
            path="/manage"
            element={
              <ProtectedRoute allowRoles={["manager", "admin"]}>
                <ManageTasksPage />
              </ProtectedRoute>
            }
          />
          <Route
            path="/admin"
            element={
              <ProtectedRoute allowRoles={["admin"]}>
                <AdminPage />
              </ProtectedRoute>
            }
          />
        </Routes>
      </BrowserRouter>
    </AuthProvider>
  );
}
