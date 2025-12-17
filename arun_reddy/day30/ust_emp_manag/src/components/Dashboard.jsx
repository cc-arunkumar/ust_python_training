import React, { useState, useEffect } from "react";
import Sidebar from "./Sidebar";
import SummaryCards from "./SummaryCards";
import KanbanBoard from "./Kanbanboard";
import CreateTaskModal from "./tasks/CreateTaskModal";
import { taskService } from "../services/taskService";
import { employeeService } from "../services/employeeService";
import { getNextStatus } from "../utils/helpers";
import { USER_ROLES } from "../utils/constants";

const Dashboard = ({ user, onLogout }) => {
  const [tasks, setTasks] = useState([]);
  const [employees, setEmployees] = useState([]);
  const [isCreateModalOpen, setIsCreateModalOpen] = useState(false);
  const [isSidebarOpen, setIsSidebarOpen] = useState(true);
  const [loading, setLoading] = useState(true);

  const canCreateTask =
    user.role === USER_ROLES.ADMIN || user.role === USER_ROLES.MANAGER;

  useEffect(() => {
    loadData();
  }, []);

  const loadData = async () => {
    try {
      setLoading(true);
      const tasksData = await taskService.getAllTasks();
      setTasks(tasksData);

      if (canCreateTask) {
        try {
          const employeesData = await employeeService.getByManager(user.emp_id);
          setEmployees(employeesData);
        } catch (e) {
          console.warn("Could not load employees:", e);
        }
      }
    } catch (error) {
      console.error("Error loading data:", error);
    } finally {
      setLoading(false);
    }
  };

  const handleCreateTask = async (taskData) => {
    try {
      await taskService.createTask(taskData);
      setIsCreateModalOpen(false);
      loadData();
    } catch (error) {
      console.error("Error creating task:", error);
      alert("Failed to create task");
    }
  };

  const handleStatusChange = async (task) => {
    const nextStatus = getNextStatus(task.status);

    if (nextStatus) {
      try {
        await taskService.updateTaskStatus(task._id, nextStatus);
        loadData();
      } catch (error) {
        console.error("Error updating task:", error);
      }
    }
  };

  const getTasksByStatus = (status) => {
    return tasks.filter((task) => task.status === status);
  };

  const taskCounts = {
    "to-do": getTasksByStatus("to-do").length,
    "in-progress": getTasksByStatus("in-progress").length,
    review: getTasksByStatus("review").length,
    completed: getTasksByStatus("completed").length,
  };

  return (
    <div className="min-h-screen bg-gray-50 flex">
      <Sidebar
        user={user}
        isOpen={isSidebarOpen}
        onToggle={() => setIsSidebarOpen(!isSidebarOpen)}
        onCreateTask={() => setIsCreateModalOpen(true)}
        onLogout={onLogout}
      />

      <div className="flex-1 overflow-auto">
        <div className="p-8">
          {/* Header */}
          <div className="mb-8">
            <h1 className="text-3xl font-bold text-gray-900 mb-2">
              Welcome back, {user.name}! 👋
            </h1>
            <p className="text-gray-600">
              Here's what's happening with your tasks today.
            </p>
          </div>

          <SummaryCards taskCounts={taskCounts} />

          <KanbanBoard
            tasks={tasks}
            onStatusChange={handleStatusChange}
            loading={loading}
          />
        </div>
      </div>

      <CreateTaskModal
        isOpen={isCreateModalOpen}
        onClose={() => setIsCreateModalOpen(false)}
        onCreateTask={handleCreateTask}
        user={user}
        employees={employees}
      />
    </div>
  );
};

export default Dashboard;
