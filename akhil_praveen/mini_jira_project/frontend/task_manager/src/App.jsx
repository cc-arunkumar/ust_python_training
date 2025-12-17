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
      // if storedRole contains multiple roles (comma separated), pick the first as the active role
      const active = storedRole.includes(",")
        ? storedRole
            .split(",")
            .map((r) => r.trim())
            .filter(Boolean)[0]
        : storedRole;
      setRole(active);
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

  const handleRoleChange = async (newRole) => {
    // update active role and reload data to reflect permissions
    setRole(newRole);
    try {
      await loadData();
    } catch (err) {
      console.error("Failed to reload after role change", err);
    }
  };

  const handleUpdateStatus = async (taskId, status, review) => {
    try {
      console.log("Updating task status:", {
        taskId,
        status,
        review,
        userRole: role,
      });

      // Call the API with the review
      // prepare role-specific fields for remarks and include 'review' so backend stores it
      const extra = {};
      const username =
        localStorage.getItem("username") ||
        localStorage.getItem("user_name") ||
        null;
      const nowTs = new Date().toISOString();
      let clientRemark = null;
      if (review && review.trim()) {
        const isManager =
          (role || "").toUpperCase().includes("MANAGER") ||
          (role || "").toUpperCase().includes("ADMIN");
        if (isManager) {
          extra.reviewer_review = review;
          if (username) extra.reviewer_by = username;
          extra.reviewer_ts = nowTs;
          clientRemark = {
            from: "reviewer",
            text: review,
            by: username || null,
            ts: nowTs,
          };
        } else {
          extra.developer_review = review;
          if (username) extra.developer_by = username;
          extra.developer_ts = nowTs;
          clientRemark = {
            from: "developer",
            text: review,
            by: username || null,
            ts: nowTs,
          };
        }
      }

      // optimistic UI: add client remark to local tasks state so it appears immediately
      if (clientRemark) {
        setTasks((prev) =>
          prev.map((t) =>
            t.task_id === taskId
              ? {
                  ...t,
                  _clientRemarks: [...(t._clientRemarks || []), clientRemark],
                }
              : t
          )
        );
      }

      // include 'review' field so backend inserts into reviews_collection
      await api.updateTaskStatus(
        taskId,
        status,
        review,
        Object.keys(extra).length ? extra : undefined
      );

      // refresh from server then re-inject client remark (server may not include reviews in task payload)
      await loadData();
      if (clientRemark) {
        setTasks((prev) =>
          prev.map((t) =>
            t.task_id === taskId
              ? {
                  ...t,
                  _clientRemarks: [...(t._clientRemarks || []), clientRemark],
                }
              : t
          )
        );
      }
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
      <div className="min-h-screen flex items-center justify-center bg-gray-50">
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
        onRoleChange={handleRoleChange}
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
