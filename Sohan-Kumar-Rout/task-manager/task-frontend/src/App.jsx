import React from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";

import Login from "./pages/Login";
import KanbanBoard from "./components/KanbanBoard";

import SidebarAdmin from "./components/SidebarAdmin";
import SidebarManager from "./components/SidebarManager";
import SidebarEmployee from "./components/SidebarEmployee";

import EmployeeList from "./components/EmployeeList";
import EmployeeForm from "./components/EmployeeForm";
import TaskList from "./components/TaskList";
import CreateTask from "./components/CreateTask";
import EmployeeTaskBoard from "./components/EmployeeTaskBoard";

const Layout = ({ sidebar, children }) => (
  <div className="flex">
    {sidebar}
    <div className="flex-1 p-6 bg-gray-900 text-white">{children}</div>
  </div>
);

function App() {
  return (
    <BrowserRouter>
      <Routes>
        {/* LOGIN */}
        <Route path="/login" element={<Login />} />

        {/* ---------------- ADMIN ROUTES ---------------- */}

        {/* Admin → Employee List */}
        <Route
          path="/admin/employees"
          element={
            <Layout sidebar={<SidebarAdmin />}>
              <EmployeeList />
            </Layout>
          }
        />

        {/* Admin → Create Employee */}
        <Route
          path="/admin/employees/create"
          element={
            <Layout sidebar={<SidebarAdmin />}>
              <EmployeeForm />
            </Layout>
          }
        />

        {/* Admin → Task List */}
        <Route
          path="/admin/tasks"
          element={
            <Layout sidebar={<SidebarAdmin />}>
              <TaskList />
            </Layout>
          }
        />

        {/* Admin → Create Task */}
        <Route
          path="/admin/tasks/create"
          element={
            <Layout sidebar={<SidebarAdmin />}>
              <CreateTask />
            </Layout>
          }
        />

        {/* Admin → Kanban Board */}
        <Route
          path="/admin/kanban"
          element={
            <Layout sidebar={<SidebarAdmin />}>
              <KanbanBoard />
            </Layout>
          }
        />

        {/* ---------------- MANAGER ROUTES ---------------- */}

        {/* Manager → Employees Under Him */}
        <Route
          path="/manager/employees"
          element={
            <Layout sidebar={<SidebarManager />}>
              <EmployeeList />
            </Layout>
          }
        />

        {/* Manager → Task List */}
        <Route
          path="/manager/tasks"
          element={
            <Layout sidebar={<SidebarManager />}>
              <TaskList />
            </Layout>
          }
        />

        {/* Manager → Create Task */}
        <Route
          path="/manager/tasks/create"
          element={
            <Layout sidebar={<SidebarManager />}>
              <CreateTask />
            </Layout>
          }
        />

        {/* Manager → Kanban Board */}
        <Route
          path="/manager/kanban"
          element={
            <Layout sidebar={<SidebarManager />}>
              <KanbanBoard />
            </Layout>
          }
        />

        {/* ---------------- EMPLOYEE ROUTES ---------------- */}

        {/* Employee → My Tasks */}
        <Route
          path="/employee/tasks"
          element={
            <Layout sidebar={<SidebarEmployee />}>
              <EmployeeTaskBoard />
            </Layout>
          }
        />

        {/* Employee → Kanban Board */}
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
