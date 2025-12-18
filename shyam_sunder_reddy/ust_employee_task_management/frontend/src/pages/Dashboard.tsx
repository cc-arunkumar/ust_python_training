import { useEffect, useState } from "react";
import { useAuth } from "../context/AuthContext";
import { taskAPI, employeeAPI } from "../services/api";
import {
  CheckSquare,
  Users,
  Clock,
  AlertCircle,
  TrendingUp,
} from "lucide-react";
import { useNavigate } from "react-router-dom";
import type { Task } from "../types";

const Dashboard = () => {
  const { activeRole } = useAuth();
  const navigate = useNavigate();
  const [stats, setStats] = useState({
    totalTasks: 0,
    completedTasks: 0,
    inProgressTasks: 0,
    reviewTasks: 0,
    pendingTasks: 0,
    totalEmployees: 0,
  });
  const [recentTasks, setRecentTasks] = useState<Task[]>([]);
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    const fetchData = async () => {
      if (!activeRole) {
        console.warn("⚠️ No active role selected, cannot fetch data");
        setIsLoading(false);
        return;
      }

      try {
        const role = activeRole as string;
        console.log("📊 Fetching dashboard data with role:", role);

        const [tasks, employees] = await Promise.all([
          taskAPI.getAll(role).catch((err) => {
            console.error("❌ Error fetching tasks:", err);
            return [];
          }),
          employeeAPI.getAll(role).catch((err) => {
            console.error("❌ Error fetching employees:", err);
            return [];
          }),
        ]);

        console.log("📦 Received data:", {
          tasks: tasks.length,
          employees: employees.length,
        });

        const completed = tasks.filter((t) => t.status === "DONE").length;
        const inProgress = tasks.filter(
          (t) => t.status === "IN_PROGRESS"
        ).length;
        const review = tasks.filter((t) => t.status === "REVIEW").length;
        const pending = tasks.filter((t) => t.status === "TO_DO").length;

        setStats({
          totalTasks: tasks.length,
          completedTasks: completed,
          inProgressTasks: inProgress,
          reviewTasks: review,
          pendingTasks: pending,
          totalEmployees: employees.length,
        });

        setRecentTasks(tasks.slice(0, 5));
      } catch (error) {
        console.error("❌ Error fetching dashboard data:", error);
      } finally {
        setIsLoading(false);
      }
    };

    fetchData();
  }, [activeRole]);

  const statCards = [
    {
      title: "Total Tasks",
      value: stats.totalTasks,
      icon: CheckSquare,
      color: "text-blue-300", // Lighter color for the icon
      bgColor: "bg-blue-50", // Same as the card background
    },
    {
      title: "Completed",
      value: stats.completedTasks,
      icon: CheckSquare,
      color: "text-green-300", // Lighter color for the icon
      bgColor: "bg-green-50", // Same as the card background
    },
    {
      title: "In Progress",
      value: stats.inProgressTasks,
      icon: Clock,
      color: "text-yellow-300", // Lighter color for the icon
      bgColor: "bg-yellow-50", // Same as the card background
    },
    {
      title: "In Review",
      value: stats.reviewTasks,
      icon: TrendingUp,
      color: "text-indigo-300", // Lighter color for the icon
      bgColor: "bg-indigo-50", // Same as the card background
    },
    {
      title: "Pending",
      value: stats.pendingTasks,
      icon: AlertCircle,
      color: "text-orange-300", // Lighter color for the icon
      bgColor: "bg-orange-50", // Same as the card background
    },
    {
      title: "Employees",
      value: stats.totalEmployees,
      icon: Users,
      color: "text-purple-300", // Lighter color for the icon
      bgColor: "bg-purple-50", // Same as the card background
    },
  ];

  const getStatusColor = (status?: string) => {
    switch (status) {
      case "DONE":
        return "bg-green-100 text-green-800";
      case "IN_PROGRESS":
        return "bg-yellow-100 text-yellow-800";
      case "REVIEW":
        return "bg-indigo-100 text-indigo-800";
      case "TO_DO":
        return "bg-orange-100 text-orange-800";
      default:
        return "bg-gray-100 text-gray-800";
    }
  };

  const getPriorityColor = (priority: string) => {
    switch (priority.toLowerCase()) {
      case "high":
        return "bg-red-100 text-red-800";
      case "medium":
        return "bg-yellow-100 text-yellow-800";
      case "low":
        return "bg-green-100 text-green-800";
      default:
        return "bg-gray-100 text-gray-800";
    }
  };

  if (isLoading) {
    return (
      <div className="flex items-center justify-center h-64">
        <div className="animate-spin rounded-full h-12 w-12 border-t-2 border-b-2 border-primary-500"></div>
      </div>
    );
  }

  return (
    <div className="space-y-6 animate-fade-in">
      <div>
        <h1 className="text-3xl font-bold text-gray-800 mb-2">Dashboard</h1>
        <p className="text-gray-600">
          Welcome back! Here's an overview of your tasks and team.
        </p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-5 gap-4">
        {statCards.map((stat, index) => {
          const Icon = stat.icon;
          return (
            <div
              key={stat.title}
              className="card animate-slide-up"
              style={{ animationDelay: `${index * 0.1}s` }}
            >
              <div className="flex items-center justify-between">
                <div>
                  <p className="text-sm text-gray-600 mb-1">{stat.title}</p>
                  <p className="text-2xl font-bold text-gray-800">
                    {stat.value}
                  </p>
                </div>
                <div className={`${stat.bgColor} p-3 rounded-lg`}>
                  <Icon className={stat.color} size={24} />
                </div>
              </div>
            </div>
          );
        })}
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        <div className="card">
          <div className="flex items-center justify-between mb-4">
            <h2 className="text-xl font-semibold text-gray-800">
              Recent Tasks
            </h2>
            <button
              onClick={() => navigate("/tasks")}
              className="text-primary-600 hover:text-primary-700 text-sm font-medium"
            >
              View All
            </button>
          </div>
          <div className="space-y-3">
            {recentTasks.length === 0 ? (
              <p className="text-gray-500 text-center py-8">No tasks found</p>
            ) : (
              recentTasks.map((task) => (
                <div
                  key={task.t_id}
                  onClick={() => navigate(`/tasks/${task.t_id}`)}
                  className="p-4 border border-gray-200 rounded-lg hover:border-primary-300 hover:shadow-md transition-all duration-200 cursor-pointer"
                >
                  <div className="flex items-start justify-between mb-2">
                    <h3 className="font-medium text-gray-800">{task.title}</h3>
                    <span
                      className={`px-2 py-1 rounded text-xs font-medium ${getPriorityColor(
                        task.priority
                      )}`}
                    >
                      {task.priority}
                    </span>
                  </div>
                  <p className="text-sm text-gray-600 mb-2 line-clamp-2">
                    {task.description}
                  </p>
                  <div className="flex items-center gap-2">
                    <span
                      className={`px-2 py-1 rounded text-xs font-medium ${getStatusColor(
                        task.status
                      )}`}
                    >
                      {task.status || "TO_DO"}
                    </span>
                    {task.assigned_to && (
                      <span className="text-xs text-gray-500">
                        Assigned to: {task.assigned_to}
                      </span>
                    )}
                  </div>
                </div>
              ))
            )}
          </div>
        </div>

        <div className="card">
          <div className="flex items-center gap-2 mb-4">
            <TrendingUp className="text-primary-600" size={24} />
            <h2 className="text-xl font-semibold text-gray-800">Quick Stats</h2>
          </div>
          <div className="space-y-4">
            <div className="flex items-center justify-between p-3 bg-blue-50 rounded-lg">
              <span className="text-gray-700">Completion Rate</span>
              <span className="font-bold text-blue-600">
                {stats.totalTasks > 0
                  ? Math.round((stats.completedTasks / stats.totalTasks) * 100)
                  : 0}
                %
              </span>
            </div>
            <div className="flex items-center justify-between p-3 bg-green-50 rounded-lg">
              <span className="text-gray-700">Active Tasks</span>
              <span className="font-bold text-green-600">
                {stats.inProgressTasks}
              </span>
            </div>
            <div className="flex items-center justify-between p-3 bg-orange-50 rounded-lg">
              <span className="text-gray-700">Pending Tasks</span>
              <span className="font-bold text-orange-600">
                {stats.pendingTasks}
              </span>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Dashboard;
