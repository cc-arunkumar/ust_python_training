import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import { useAuth } from "./context/AuthContext";
import React from "react";
// Pages
import LoginPage from "./pages/auth/LoginPage";
import Dashboard from "./pages/dashboard/Dashboard"; // Using the Modern Dashboard
import TasksPage from "./pages/tasks/TasksPage";
import TaskDetailsPage from "./pages/tasks/TaskDetailsPage"; // Don't forget this!
import EmployeesPage from "./pages/employees/EmployeesPage";

// Components
import ProtectedRoute from "./components/auth/ProtectedRoute";
import Layout from "./components/layout/Layout";

// Simple 404 Component
const NotFound = () => (
  <div className="flex items-center justify-center h-screen bg-gray-100">
    <h1 className="text-2xl font-bold text-gray-700">404 - Page Not Found</h1>
  </div>
);

const AppRoutes = () => {
  const { user } = useAuth();

  return (
    <BrowserRouter>
      <Routes>
        {/* Public Routes */}
        <Route path="/login" element={<LoginPage />} />

        {/* Protected Routes (Wrapped in Layout) */}
        <Route element={<ProtectedRoute />}>
          <Route element={<Layout />}>
            {/* Dashboard */}
            <Route path="/dashboard" element={<Dashboard />} />

            {/* Tasks */}
            <Route path="/tasks" element={<TasksPage />} />
            <Route path="/tasks/:taskId" element={<TaskDetailsPage />} />

            {/* Admin/Manager Routes */}
            {/* We render these routes, but Sidebar hides links if not allowed. 
        Backend API will ultimately protect data. */}
            <Route path="/employees" element={<EmployeesPage />} />

            {/* Default Redirect */}
            <Route path="/" element={<Navigate to="/dashboard" replace />} />

            <Route path="/employees" element={<EmployeesPage />} />
          </Route>
        </Route>

        {/* Catch-all */}
        <Route path="*" element={<NotFound />} />
      </Routes>
    </BrowserRouter>
  );
};

export default AppRoutes;
