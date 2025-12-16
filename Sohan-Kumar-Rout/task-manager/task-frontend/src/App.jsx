import React, { useState } from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";

import Login from "./pages/Login";
import ProtectedRoute from "./components/ProtectedRoute";
import Sidebar from "./components/Sidebar";

import EmployeeForm from "./components/EmployeeForm";
import EmployeeList from "./components/EmployeeList";

// Placeholder pages for Manager
const ManagerList = () => <h1 className="text-white text-2xl">Manager List</h1>;
const AddManager = () => <h1 className="text-white text-2xl">Add Manager</h1>;

function App() {
  const [selectedEmployee, setSelectedEmployee] = useState(null);

  return (
    <BrowserRouter>
      <Routes>

        {/* ✅ Login Page */}
        <Route
          path="/login"
          element={<Login onLogin={() => (window.location.href = "/")} />}
        />

        {/* ✅ Dashboard Layout */}
        <Route
          path="/"
          element={
            <ProtectedRoute>
              <div className="flex min-h-screen bg-[#0A1A2F]">
                <Sidebar />

                <div className="flex-1 p-6">
                  <EmployeeForm
                    selectedEmployee={selectedEmployee}
                    onSuccess={() => setSelectedEmployee(null)}
                  />
                  <EmployeeList
                    onEdit={(emp) => setSelectedEmployee(emp)}
                  />
                </div>
              </div>
            </ProtectedRoute>
          }
        />

        <Route
          path="/employees"
          element={
            <ProtectedRoute>
              <div className="flex min-h-screen bg-[#0A1A2F]">
                <Sidebar />
                <div className="flex-1 p-6">
                  <EmployeeList onEdit={(emp) => setSelectedEmployee(emp)} />
                </div>
              </div>
            </ProtectedRoute>
          }
        />

        <Route
          path="/employees/add"
          element={
            <ProtectedRoute>
              <div className="flex min-h-screen bg-[#0A1A2F]">
                <Sidebar />
                <div className="flex-1 p-6">
                  <EmployeeForm />
                </div>
              </div>
            </ProtectedRoute>
          }
        />

        <Route
          path="/managers"
          element={
            <ProtectedRoute>
              <div className="flex min-h-screen bg-[#0A1A2F]">
                <Sidebar />
                <div className="flex-1 p-6">
                  <ManagerList />
                </div>
              </div>
            </ProtectedRoute>
          }
        />

        <Route
          path="/managers/add"
          element={
            <ProtectedRoute>
              <div className="flex min-h-screen bg-[#0A1A2F]">
                <Sidebar />
                <div className="flex-1 p-6">
                  <AddManager />
                </div>
              </div>
            </ProtectedRoute>
          }
        />

      </Routes>
    </BrowserRouter>
  );
}

export default App;