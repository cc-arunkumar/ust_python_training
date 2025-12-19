import React, { useEffect } from "react";
import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import { ToastContainer } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";

import Login from "./pages/Login";

// Admin components
import SidebarAdmin from "./components/SidebarAdmin";
import EmployeeList from "./components/EmployeeList";
import EmployeeForm from "./components/EmployeeForm";
import TaskList from "./components/TaskList";
import CreateTask from "./components/CreateTask";
import KanbanBoard from "./components/KanbanBoard";

// Manager components
import SidebarManager from "./components/SidebarManager";
import DashboardManager from "./pages/DashboardManager";

// Employee components
import SidebarEmployee from "./components/SidebarEmployee";
import EmployeeTaskBoard from "./components/EmployeeTaskBoard";

const Layout = ({ sidebar, children }) => (
  <div className="flex">
    {sidebar}
    <div className="flex-1 p-6 bg-white text-black transition-all duration-300">
      {children}
    </div>
  </div>
);

function App() {
  // Force light theme globally (no toggle)
  useEffect(() => {
    document.documentElement.className = "light";
  }, []);

  return (
    <BrowserRouter>
      <Routes>
        {/* Login route */}
        <Route path="/login" element={<Login />} />

        {/* --- Admin Routes --- */}
        <Route
          path="/admin/employees"
          element={
            <Layout sidebar={<SidebarAdmin />}>
              <EmployeeList />
            </Layout>
          }
        />
        <Route
          path="/admin/employees/create"
          element={
            <Layout sidebar={<SidebarAdmin />}>
              <EmployeeForm />
            </Layout>
          }
        />
        <Route
          path="/admin/tasks"
          element={
            <Layout sidebar={<SidebarAdmin />}>
              <TaskList />
            </Layout>
          }
        />
        <Route
          path="/admin/tasks/create"
          element={
            <Layout sidebar={<SidebarAdmin />}>
              <CreateTask />
            </Layout>
          }
        />
        <Route
          path="/admin/kanban"
          element={
            <Layout sidebar={<SidebarAdmin />}>
              <KanbanBoard />
            </Layout>
          }
        />
        {/* Redirect /admin to /admin/employees to avoid 404 error */}
        <Route path="/admin" element={<Navigate to="/admin/employees" replace />} />

        {/* --- Manager Routes --- */}
        <Route
          path="/manager/dashboard"
          element={
            <Layout sidebar={<SidebarManager />}>
              <DashboardManager />
            </Layout>
          }
        />
        <Route
          path="/manager/tasks"
          element={
            <Layout sidebar={<SidebarManager />}>
              <TaskList />
            </Layout>
          }
        />
        <Route
          path="/manager/tasks/create"
          element={
            <Layout sidebar={<SidebarManager />}>
              <CreateTask />
            </Layout>
          }
        />
        <Route
          path="/manager/kanban"
          element={
            <Layout sidebar={<SidebarManager />}>
              <KanbanBoard />
            </Layout>
          }
        />

        {/* --- Employee Routes --- */}
        <Route
          path="/employee/tasks"
          element={
            <Layout sidebar={<SidebarEmployee />}>
              <EmployeeTaskBoard />
            </Layout>
          }
        />
        <Route
          path="/employee/kanban"
          element={
            <Layout sidebar={<SidebarEmployee />}>
              <KanbanBoard />
            </Layout>
          }
        />

        {/* Default route (if no other route matched) */}
        <Route path="/" element={<Navigate to="/login" />} />
      </Routes>

      {/* Global Toasts */}
      <ToastContainer
        position="top-right"
        autoClose={3000}
        hideProgressBar={false}
        newestOnTop={false}
        closeOnClick
        pauseOnHover
        draggable
        theme="light"
      />
    </BrowserRouter>
  );
}

export default App;
