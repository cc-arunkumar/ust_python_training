import React, { useState, useEffect } from "react";
import Login from "./components/Login";
import Header from "./components/Header";
import TaskBoard from "./components/TaskBoard";
import EmployeeManagement from "./components/EmployeeManagement";
import api from "./api/api";

function App() {
  const [isAuthenticated, setIsAuthenticated] = useState(false);
  const [role, setRole] = useState("");
  const [tasks, setTasks] = useState([]);
  const [employees, setEmployees] = useState([]);
  const [activeTab, setActiveTab] = useState("tasks");
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const token = localStorage.getItem("token");
    const storedRole = localStorage.getItem("role");
    if (token && storedRole) {
      setIsAuthenticated(true);
      setRole(storedRole);
    } else {
      setLoading(false);
    }
  }, []);

  useEffect(() => {
    if (isAuthenticated) {
      loadData();
    }
  }, [isAuthenticated]);

  const loadData = async () => {
    setLoading(true);
    try {
      const [tasksData, employeesData] = await Promise.all([
        api.getTasks(),
        api.getEmployees(),
      ]);

      console.log("Loaded tasks:", tasksData);

      setTasks(tasksData);
      setEmployees(employeesData);
    } catch (err) {
      console.error("Failed to load data:", err);
      const errorMessage = err.message || "Unknown error occurred";
      alert("Failed to load data: " + errorMessage);
    } finally {
      setLoading(false);
    }
  };

  const handleLogin = (userRole) => {
    setIsAuthenticated(true);
    setRole(userRole);
  };

  const handleLogout = () => {
    localStorage.removeItem("token");
    localStorage.removeItem("role");
    setIsAuthenticated(false);
    setRole("");
    setActiveTab("tasks");
  };

  const handleUpdateStatus = async (taskId, status, review) => {
    try {
      console.log("Updating status to:", status);
      await api.updateTaskStatus(taskId, status, review);
      await loadData();
    } catch (err) {
      console.error("Failed to update status:", err);
      const errorMessage = err.message || "Unknown error occurred";
      alert("Failed to update status: " + errorMessage);
    }
  };

  const handleSaveTask = async (editingTask, taskData) => {
    try {
      console.log("Saving task with data:", taskData);

      if (editingTask) {
        await api.updateTask(editingTask.task_id, taskData);
      } else {
        await api.createTask(taskData);
      }
      await loadData();
    } catch (err) {
      console.error("Failed to save task:", err);
      const errorMessage = err.message || "Unknown error occurred";
      alert("Failed to save task: " + errorMessage);
    }
  };

  if (!isAuthenticated) {
    return <Login onLogin={handleLogin} />;
  }

  if (loading) {
    return (
      <div className="min-h-screen flex items-center justify-center">
        <div className="text-xl text-gray-600">Loading...</div>
      </div>
    );
  }

  const canManageEmployees = role.includes("ADMIN");
  const canCreateTasks = role.includes("ADMIN") || role.includes("MANAGER");

  return (
    <div className="min-h-screen bg-gray-50">
      <Header
        role={role}
        activeTab={activeTab}
        onTabChange={setActiveTab}
        onLogout={handleLogout}
        canManageEmployees={canManageEmployees}
      />

      <main className="container mx-auto">
        {activeTab === "tasks" ? (
          <TaskBoard
            tasks={tasks}
            employees={employees}
            onRefresh={loadData}
            canCreateTasks={canCreateTasks}
            userRole={role}
            onUpdateStatus={handleUpdateStatus}
            onSaveTask={handleSaveTask}
          />
        ) : (
          <EmployeeManagement employees={employees} onRefresh={loadData} />
        )}
      </main>
    </div>
  );
}

export default App;
