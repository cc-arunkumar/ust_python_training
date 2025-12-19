import React, { useState, useEffect } from "react";
import Login from "./components/Login";
import Header from "./components/Header";
import TaskBoard from "./components/TaskBoard";
import EmployeeManagement from "./components/EmployeeManagement";
import api from "./api/api";

function App() {
  const [isAuthenticated, setIsAuthenticated] = useState(false);
  const [role, setRole] = useState("");
  const [currentEmpId, setCurrentEmpId] = useState(null);
  const [tasks, setTasks] = useState([]);
  const [employees, setEmployees] = useState([]);
  const [activeTab, setActiveTab] = useState("tasks");
  const [loading, setLoading] = useState(true);
  const [openTaskId, setOpenTaskId] = useState(null);

  useEffect(() => {
    const token = localStorage.getItem("token");
    const storedRole = localStorage.getItem("role");
    if (token && storedRole) {
      setIsAuthenticated(true);
      const active = storedRole.includes(",")
        ? storedRole
            .split(",")
            .map((r) => r.trim())
            .filter(Boolean)[0]
        : storedRole;
      setRole(active);
      const empIdRaw = localStorage.getItem("emp_id");
      if (empIdRaw) setCurrentEmpId(Number(empIdRaw));
    } else {
      setLoading(false);
    }
  }, []);

  useEffect(() => {
    if (isAuthenticated) {
      loadData();
    }
  }, [isAuthenticated]);

  // WebSocket for realtime updates
  useEffect(() => {
    if (!isAuthenticated) return undefined;

    const protocol = window.location.protocol === "https:" ? "wss" : "ws";
    const host = window.location.hostname || "localhost";
    const port = 8000;
    const url = `${protocol}://${host}:${port}/ws/updates`;
    let ws;
    try {
      ws = new WebSocket(url);
    } catch (e) {
      console.warn("WebSocket connection failed:", e);
      return undefined;
    }

    ws.onopen = () => console.log("Realtime: connected to", url);
    ws.onclose = () => console.log("Realtime: disconnected");
    ws.onerror = (e) => console.warn("Realtime: websocket error", e);
    ws.onmessage = (ev) => {
      try {
        const msg = JSON.parse(ev.data);
        const interesting = [
          "task_created",
          "task_updated",
          "task_status_updated",
          "employee_created",
          "employee_updated",
          "employee_deleted",
        ];
        if (interesting.includes(msg.type)) {
          setTimeout(() => loadData().catch((e) => console.error(e)), 200);
        }
      } catch (err) {
        // ignore parse errors
      }
    };

    return () => {
      try {
        ws.close();
      } catch (e) {}
    };
  }, [isAuthenticated]);

  const loadData = async () => {
    setLoading(true);
    try {
      const [tasksData, employeesData] = await Promise.all([
        api.getTasks(),
        api.getEmployees(),
      ]);

      console.log("Loaded tasks:", tasksData);

      const normalized = (tasksData || []).map((t) => ({
        ...t,
        priority: t.priority === "CRITICAL" ? "HIGH" : t.priority,
      }));
      setTasks(normalized);
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
    const empIdRaw = localStorage.getItem("emp_id");
    if (empIdRaw) setCurrentEmpId(Number(empIdRaw));
  };

  const handleLogout = () => {
    localStorage.removeItem("token");
    localStorage.removeItem("role");
    localStorage.removeItem("roles");
    localStorage.removeItem("emp_id");
    setIsAuthenticated(false);
    setRole("");
    setCurrentEmpId(null);
    setActiveTab("tasks");
  };

  const handleRoleChange = async (newRole) => {
    setRole(newRole);
    try {
      await loadData();
    } catch (err) {
      console.error("Failed to reload after role change", err);
    }
  };

  const handleUpdateStatus = async (taskId, status, review) => {
    try {
      console.log("App.handleUpdateStatus:", {
        taskId,
        status,
        review,
        userRole: role,
        currentEmpId,
      });

      // Find the task to check if current user is the reviewer
      const task = tasks.find((t) => t.task_id === taskId);
      const isReviewer =
        task &&
        currentEmpId != null &&
        Number(currentEmpId) === Number(task.reviewer);

      const username = localStorage.getItem("username") || null;
      const nowTs = new Date().toISOString();
      const roleUpper = (role || "").toUpperCase();
      const isManagerRole =
        roleUpper.includes("MANAGER") || roleUpper.includes("ADMIN");

      // Prepare extra fields for role-specific remarks
      const extra = {};
      const clientRemarksToInject = [];

      if (review && review.trim()) {
        // Determine if this is a reviewer remark or developer remark
        // Manager/Admin OR designated reviewer = reviewer remarks
        // Otherwise = developer remarks
        const isReviewerRemark = isManagerRole || isReviewer;

        if (isReviewerRemark) {
          // Store as reviewer remarks
          extra.reviewer_review = review.trim();
          if (username) extra.reviewer_by = username;
          extra.reviewer_ts = nowTs;

          // Optimistic UI update
          clientRemarksToInject.push({
            from: "reviewer",
            text: review.trim(),
            by: username,
            byEmpId: currentEmpId,
            ts: nowTs,
          });

          console.log("Storing as REVIEWER remarks:", extra);
        } else {
          // Store as developer remarks
          extra.developer_review = review.trim();
          if (username) extra.developer_by = username;
          extra.developer_ts = nowTs;

          // Optimistic UI update
          clientRemarksToInject.push({
            from: "developer",
            text: review.trim(),
            by: username,
            byEmpId: currentEmpId,
            ts: nowTs,
          });

          console.log("Storing as DEVELOPER remarks:", extra);
        }
      }

      // Optimistic UI: add client remarks immediately
      if (clientRemarksToInject.length) {
        setTasks((prev) =>
          prev.map((t) =>
            t.task_id === taskId
              ? {
                  ...t,
                  _clientRemarks: [
                    ...(t._clientRemarks || []),
                    ...clientRemarksToInject,
                  ],
                }
              : t
          )
        );
      }

      // Call API with the review field (for backend to store in reviews collection)
      // AND the extra fields (for role-specific storage)
      // include current active role so backend can store it with the review
      if (role) extra.role = role;
      // Avoid sending the top-level `review` when we already set role-specific fields
      // so the backend does not mistake a developer remark for a reviewer remark.
      const topLevelReview =
        Object.keys(extra).length &&
        (extra.reviewer_review || extra.developer_review)
          ? null
          : review && review.trim()
          ? review.trim()
          : null;

      await api.updateTaskStatus(
        taskId,
        status,
        topLevelReview,
        Object.keys(extra).length ? extra : undefined
      );

      console.log("API call completed, reloading data...");

      // Reload data from server
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
      <div className="min-h-screen flex items-center justify-center bg-gray-50">
        <div className="text-xl text-gray-600">Loading...</div>
      </div>
    );
  }

  const canManageEmployees = role.includes("ADMIN") || role.includes("MANAGER");
  const canCreateTasks = role.includes("ADMIN") || role.includes("MANAGER");
  const openTaskDetail = (taskId) => {
    setActiveTab("tasks");
    // ensure tasks view is visible, then instruct TaskBoard to open the detail
    setOpenTaskId(taskId);
    // clear after a short delay so subsequent opens work
    setTimeout(() => setOpenTaskId(null), 5000);
  };

  return (
    <div className="min-h-screen bg-gray-50">
      <Header
        role={role}
        tasks={tasks}
        currentEmpId={currentEmpId}
        onOpenTask={openTaskDetail}
        activeTab={activeTab}
        onTabChange={setActiveTab}
        onLogout={handleLogout}
        canManageEmployees={canManageEmployees}
        onRoleChange={handleRoleChange}
        onRefresh={loadData}
      />

      <main className="container mx-auto bg-gray-200">
        {activeTab === "tasks" ? (
          <TaskBoard
            tasks={tasks}
            employees={employees}
            onRefresh={loadData}
            canCreateTasks={canCreateTasks}
            userRole={role}
            currentEmpId={currentEmpId}
            onUpdateStatus={handleUpdateStatus}
            onSaveTask={handleSaveTask}
            openTaskId={openTaskId}
          />
        ) : (
          <EmployeeManagement
            employees={employees}
            onRefresh={loadData}
            role={role}
            currentEmpId={currentEmpId}
          />
        )}
      </main>
    </div>
  );
}

export default App;
