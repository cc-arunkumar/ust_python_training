import React, { useEffect, useState } from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";

import Login from "./pages/Login";
import DashboardManager from "./pages/DashboardManager";   // ✅ Manager Dashboard
import KanbanBoard from "./components/KanbanBoard";

import SidebarAdmin from "./components/SidebarAdmin";
import SidebarManager from "./components/SidebarManager";
import SidebarEmployee from "./components/SidebarEmployee";

import EmployeeList from "./components/EmployeeList";
import EmployeeForm from "./components/EmployeeForm";
import TaskList from "./components/TaskList";
import CreateTask from "./components/CreateTask";
import EmployeeTaskBoard from "./components/EmployeeTaskBoard";

import { FaMoon, FaSun } from "react-icons/fa";

// ---------------- THEME TOGGLE BUTTON ----------------
const ThemeToggle = ({ theme, toggleTheme }) => (
  <button
    onClick={toggleTheme}
    className="fixed top-4 right-4 p-3 rounded-full shadow-lg 
               bg-gray-200 dark:bg-gray-800 text-gray-900 dark:text-white 
               transition-all duration-300 hover:scale-110 z-50"
  >
    {theme === "light" ? <FaMoon size={18} /> : <FaSun size={18} />}
  </button>
);

// ---------------- LAYOUT WRAPPER ----------------
const Layout = ({ sidebar, children }) => (
  <div className="flex">
    {sidebar}
    <div className="flex-1 p-6 
      bg-white text-black 
      dark:bg-gray-900 dark:text-white 
      transition-all duration-300">
      {children}
    </div>
  </div>
);

function App() {
  const [theme, setTheme] = useState("light");

  useEffect(() => {
    const savedTheme = localStorage.getItem("theme") || "light";
    setTheme(savedTheme);
    document.documentElement.className = savedTheme;
  }, []);

  const toggleTheme = () => {
    const newTheme = theme === "light" ? "dark" : "light";
    setTheme(newTheme);
    document.documentElement.className = newTheme;
    localStorage.setItem("theme", newTheme);
  };

  return (
    <BrowserRouter>
      <ThemeToggle theme={theme} toggleTheme={toggleTheme} />

      <Routes>
        {/* LOGIN */}
        <Route path="/login" element={<Login />} />

        {/* ---------------- ADMIN ROUTES ---------------- */}
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

        {/* ---------------- MANAGER ROUTES ---------------- */}
        <Route
          path="/manager/dashboard"
          element={
            <Layout sidebar={<SidebarManager />}>
              <DashboardManager />   {/* ✅ Manager Dashboard */}
            </Layout>
          }
        />
        <Route
          path="/manager/employees"
          element={
            <Layout sidebar={<SidebarManager />}>
              <EmployeeList />
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

        {/* ---------------- EMPLOYEE ROUTES ---------------- */}
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

        {/* DEFAULT ROUTE */}
        <Route path="/" element={<Login />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
