import React, { useState } from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";

import Login from "./pages/Login";
import ProtectedRoute from "./components/ProtectedRoute";
import Sidebar from "./components/Sidebar";

import EmployeeForm from "./components/EmployeeForm";
import EmployeeList from "./components/EmployeeList";

import CreateTask from "./components/CreateTask";
import TaskList from "./components/TaskList";

function App() {
  const [selectedEmployee, setSelectedEmployee] = useState(null);
  const [selectedTask, setSelectedTask] = useState(null);

  const withLayout = (content) => (
    <ProtectedRoute>
      <div className="flex min-h-screen bg-[#0A1A2F]">
        <Sidebar />
        <div className="flex-1 p-6">{content}</div>
      </div>
    </ProtectedRoute>
  );

  return (
    <BrowserRouter>
      <Routes>

        {/* LOGIN */}
        <Route
          path="/login"
          element={<Login onLogin={() => (window.location.href = "/")} />}
        />

        {/* HOME — FORM + LIST */}
        <Route
          path="/"
          element={withLayout(
            <>
              <EmployeeForm
                selectedEmployee={selectedEmployee}
                onSuccess={() => setSelectedEmployee(null)}
              />
              <EmployeeList onEdit={(emp) => setSelectedEmployee(emp)} />
            </>
          )}
        />

        {/* EMPLOYEES — ONLY LIST */}
        <Route
          path="/employees"
          element={withLayout(
            <EmployeeList onEdit={(emp) => setSelectedEmployee(emp)} />
          )}
        />

        {/* EMPLOYEES/ADD — FORM + LIST */}
        <Route
          path="/employees/add"
          element={withLayout(
            <>
              <EmployeeForm
                selectedEmployee={selectedEmployee}
                onSuccess={() => setSelectedEmployee(null)}
              />
              <EmployeeList onEdit={(emp) => setSelectedEmployee(emp)} />
            </>
          )}
        />

        {/* TASK LIST */}
        <Route
          path="/tasks"
          element={withLayout(
            <TaskList onEdit={(task) => setSelectedTask(task)} />
          )}
        />

        {/* CREATE / UPDATE TASK */}
        <Route
          path="/tasks/create"
          element={withLayout(
            <CreateTask
              selectedTask={selectedTask}
              onSuccess={() => setSelectedTask(null)}
            />
          )}
        />

      </Routes>
    </BrowserRouter>
  );
}

export default App;
