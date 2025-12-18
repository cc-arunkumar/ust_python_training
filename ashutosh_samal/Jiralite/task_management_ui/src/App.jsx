import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import { useAuth } from "./context/AuthContext";

import Login from "./pages/Login";
import Dashboard from "./pages/Dashboard";
import CreateTask from "./pages/CreateTask";
import EditTask from "./pages/EditTask";
import Employees from "./pages/Employees";
import EmployeeForm from "./pages/EmployeeForm";
import Users from "./pages/Users";
import UserForm from "./pages/UserForm";

export default function App() {
  const { isAuthenticated, loading } = useAuth();

  // ⏳ Wait until auth state is restored
  if (loading) return null;

  return (
    <BrowserRouter>
      <Routes>
        {/* 🔓 PUBLIC */}
        <Route path="/" element={<Login />} />

        {/* 🔐 PROTECTED */}
        {isAuthenticated ? (
          <>
            {/* DASHBOARD */}
            <Route path="/dashboard" element={<Dashboard />} />

            {/* TASKS */}
            <Route path="/tasks/create" element={<CreateTask />} />
            <Route path="/tasks/:id/edit" element={<EditTask />} />

            {/* EMPLOYEES */}
            <Route path="/admin/employees" element={<Employees />} />
            <Route path="/admin/employees/create" element={<EmployeeForm />} />
            <Route
              path="/admin/employees/:id/edit"
              element={<EmployeeForm />}
            />

            {/* USERS */}
            <Route path="/admin/users" element={<Users />} />
            <Route path="/admin/users/create" element={<UserForm />} />
            <Route path="/admin/users/:id/edit" element={<UserForm />} />

            {/* FALLBACK */}
            <Route path="*" element={<Navigate to="/dashboard" />} />
          </>
        ) : (
          <Route path="*" element={<Navigate to="/" />} />
        )}
      </Routes>
    </BrowserRouter>
  );
}

