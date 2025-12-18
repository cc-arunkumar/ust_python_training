import React, { useState, useEffect } from "react";
import { Plus, Search, Filter } from "lucide-react";
import { useAuth } from "../../contexts/AuthContext";
import { useNavigate } from "react-router-dom";
import { api } from "../../services/api";
import Header from "../layout/Header";
import TaskBoard from "./TaskBoard";
import CreateTaskModal from "../modals/CreateTaskModal";

const Dashboard = () => {
  const { user, token } = useAuth();
  const navigate = useNavigate();

  const [tasks, setTasks] = useState([]);
  const [loading, setLoading] = useState(true);
  const [showCreateModal, setShowCreateModal] = useState(false);
  const [searchTerm, setSearchTerm] = useState("");
  const [filterPriority, setFilterPriority] = useState("All");
  const [userRoles, setUserRoles] = useState([]);
  const [userName, setUserName] = useState("User");

  const [currentView, setCurrentView] = useState(null); // 'admin' | 'manager' | 'developer'

  // For task creation helpers
  const [managerEmployees, setManagerEmployees] = useState([]); // developers under a manager
  const [managers, setManagers] = useState([]); // managers list for admin reviewer

  // Callback to receive user name from Header
  const handleUserNameFetched = (name) => {
    setUserName(name);
  };

  // Fetch user roles once
  useEffect(() => {
    const fetchUserRoles = async () => {
      try {
        const userData = await api.getUserById(token, user.emp_id);

        if (userData && Array.isArray(userData.role)) {
          setUserRoles(userData.role);
          setCurrentView(userData.role[0] || "developer");
        } else {
          setUserRoles(["developer"]);
          setCurrentView("developer");
        }
      } catch (err) {
        console.error("Failed to fetch roles:", err);
        setUserRoles(["developer"]);
        setCurrentView("developer");
      }
    };

    fetchUserRoles();
  }, [token, user.emp_id]);

  // Load tasks and helper lists when currentView changes
  useEffect(() => {
    if (currentView) {
      loadTasks();
      loadHelperLists();
    }
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [currentView]);

  const loadTasks = async () => {
    try {
      setLoading(true);
      const data = await api.getTasks(token, currentView, user.emp_id);
      setTasks(Array.isArray(data) ? data : []);
    } catch (error) {
      console.error("Error loading tasks:", error);
      setTasks([]);
    } finally {
      setLoading(false);
    }
  };

  const loadHelperLists = async () => {
    // Manager view: load developers under this manager
    if (currentView === "manager") {
      try {
        const data = await api.getEmployees(token, user.emp_id);
        setManagerEmployees(Array.isArray(data) ? data : []);
      } catch (err) {
        console.error("Error loading employees for manager:", err);
        setManagerEmployees([]);
      }
    } else {
      setManagerEmployees([]);
    }

    // Admin view: load managers list for reviewer dropdown
    if (currentView === "admin") {
      try {
        const mgrs = await api.getManagers(token);
        setManagers(Array.isArray(mgrs) ? mgrs : []);
      } catch (err) {
        console.error("Error loading managers for admin:", err);
        setManagers([]);
      }
    } else {
      setManagers([]);
    }
  };

  // status change receives full task
  const handleStatusChange = async (task, newStatus) => {
    try {
      // Manager: must assign before moving To Do → In Progress
      if (
        currentView === "manager" &&
        task.status === "To Do" &&
        newStatus === "In Progress" &&
        !task.assigned_to
      ) {
        alert(
          "Please assign this task to a developer before moving it to In Progress."
        );
        return;
      }

      await api.updateTaskStatus(token, task._id, newStatus);
      loadTasks();
    } catch (error) {
      console.error("Error updating task:", error);
      alert("Failed to update task status");
    }
  };

  const handleAddRemark = async (taskId, remark) => {
    try {
      await api.addRemark(token, user.emp_id, taskId, remark);
      loadTasks();
    } catch (error) {
      console.error("Error adding remark:", error);
    }
  };

  // NEW: assign handler for TaskCard
  const handleAssign = async (taskId, empId) => {
    try {
      // assuming you have an updateTask API that accepts partial updates
      await api.updateTask(token, taskId, {
        assigned_to: empId,
        assigned_by: user.emp_id,
        assigned_at: new Date().toISOString(),
        updated_by: user.emp_id,
      });
      loadTasks();
    } catch (error) {
      console.error("Error assigning task:", error);
      alert("Failed to assign task");
    }
  };

  const filteredTasks = tasks.filter((task) => {
    const matchesSearch =
      task.title.toLowerCase().includes(searchTerm.toLowerCase()) ||
      task.description.toLowerCase().includes(searchTerm.toLowerCase());
    const matchesPriority =
      filterPriority === "All" || task.priority === filterPriority;
    return matchesSearch && matchesPriority;
  });

  if (loading || !currentView) {
    return (
      <div className="min-h-screen bg-gradient-to-br from-blue-50 via-purple-50 to-pink-50 flex items-center justify-center">
        <div className="text-center">
          <div className="relative">
            <div className="animate-spin rounded-full h-16 w-16 border-4 border-gray-200 mx-auto mb-4"></div>
            <div className="animate-spin rounded-full h-16 w-16 border-4 border-blue-600 border-t-transparent absolute top-0 left-1/2 transform -translate-x-1/2"></div>
          </div>
          <p className="text-gray-700 font-semibold text-lg">
            Loading your workspace...
          </p>
          <p className="text-gray-500 text-sm mt-2">Just a moment</p>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 via-purple-50 to-pink-50">
      <Header
        currentView={currentView}
        userRoles={userRoles}
        onChangeView={setCurrentView}
        onNavigate={navigate}
        onUserNameFetched={handleUserNameFetched}
      />

      <main className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        {/* Welcome Section */}
        <div className="mb-8">
          <h2 className="text-3xl font-bold bg-gradient-to-r from-blue-600 via-purple-600 to-pink-600 bg-clip-text text-transparent mb-2">
            Welcome back, {userName}!
          </h2>
          <p className="text-gray-600">
            You have{" "}
            <span className="font-semibold text-purple-600">
              {filteredTasks.length}
            </span>{" "}
            tasks to manage
          </p>
        </div>

        {/* Controls */}
        <div className="mb-8 bg-gradient-to-br from-white via-blue-50/30 to-purple-50/30 rounded-3xl shadow-2xl p-8 border-2 border-white backdrop-blur-sm relative overflow-hidden">
          {/* Decorative background elements */}
          <div className="absolute top-0 right-0 w-64 h-64 bg-gradient-to-br from-blue-400/10 to-purple-400/10 rounded-full blur-3xl"></div>
          <div className="absolute bottom-0 left-0 w-64 h-64 bg-gradient-to-tr from-pink-400/10 to-blue-400/10 rounded-full blur-3xl"></div>

          <div className="relative z-10 flex flex-col sm:flex-row gap-4 items-start sm:items-center justify-between">
            <div className="flex flex-col sm:flex-row gap-4 flex-1 w-full sm:w-auto">
              {/* Search Input */}
              <div className="relative flex-1 max-w-md group">
                <div className="absolute inset-0 bg-gradient-to-r from-blue-500 to-purple-500 rounded-2xl opacity-0 group-focus-within:opacity-100 blur transition-opacity duration-300"></div>
                <div className="relative">
                  <Search
                    className="absolute left-4 top-1/2 transform -translate-y-1/2 text-gray-400 group-focus-within:text-blue-600 transition-all duration-300 group-focus-within:scale-110"
                    size={20}
                  />
                  <input
                    type="text"
                    placeholder="Search tasks..."
                    value={searchTerm}
                    onChange={(e) => setSearchTerm(e.target.value)}
                    className="w-full pl-12 pr-4 py-4 border-2 border-gray-200 rounded-2xl focus:ring-4 focus:ring-blue-500/20 focus:border-blue-500 transition-all outline-none bg-white shadow-lg hover:shadow-xl font-medium text-gray-700 placeholder:text-gray-400"
                  />
                </div>
              </div>

              {/* Priority Filter */}
              <div className="relative group min-w-[200px]">
                <div className="absolute inset-0 bg-gradient-to-r from-purple-500 to-pink-500 rounded-2xl opacity-0 group-focus-within:opacity-100 blur transition-opacity duration-300"></div>
                <div className="relative">
                  <Filter
                    className="absolute left-4 top-1/2 transform -translate-y-1/2 text-gray-400 group-focus-within:text-purple-600 transition-all duration-300 pointer-events-none group-focus-within:scale-110"
                    size={20}
                  />
                  <select
                    value={filterPriority}
                    onChange={(e) => setFilterPriority(e.target.value)}
                    className="w-full pl-12 pr-12 py-4 border-2 border-gray-200 rounded-2xl focus:ring-4 focus:ring-purple-500/20 focus:border-purple-500 bg-white transition-all outline-none appearance-none cursor-pointer font-semibold text-gray-700 shadow-lg hover:shadow-xl"
                  >
                    <option value="All">All Priorities</option>
                    <option value="Low">🟢 Low Priority</option>
                    <option value="Medium">🟡 Medium Priority</option>
                    <option value="High">🔴 High Priority</option>
                  </select>
                  <div className="absolute right-4 top-1/2 transform -translate-y-1/2 pointer-events-none">
                    <svg
                      className="w-5 h-5 text-gray-400 group-focus-within:text-purple-600 transition-colors"
                      fill="none"
                      stroke="currentColor"
                      viewBox="0 0 24 24"
                    >
                      <path
                        strokeLinecap="round"
                        strokeLinejoin="round"
                        strokeWidth={2.5}
                        d="M19 9l-7 7-7-7"
                      />
                    </svg>
                  </div>
                </div>
              </div>
            </div>

            {/* Only non-developer (admin/manager) can create tasks */}
            {currentView !== "developer" && (
              <button
                onClick={() => setShowCreateModal(true)}
                className="flex items-center gap-2 px-8 py-4 bg-gradient-to-r from-blue-600 via-purple-600 to-pink-600 text-white rounded-2xl hover:shadow-2xl hover:shadow-purple-500/50 transform hover:scale-105 transition-all font-bold relative overflow-hidden group shadow-xl"
              >
                <div className="absolute inset-0 bg-gradient-to-r from-pink-600 via-purple-600 to-blue-600 opacity-0 group-hover:opacity-100 transition-opacity duration-300"></div>
                <div className="absolute inset-0 bg-white opacity-0 group-hover:opacity-20 animate-pulse"></div>
                <Plus
                  size={22}
                  className="relative z-10 group-hover:rotate-90 transition-transform duration-300"
                />
                <span className="relative z-10">Create Task</span>
              </button>
            )}
          </div>
        </div>

        <TaskBoard
          tasks={filteredTasks}
          onStatusChange={handleStatusChange}
          onAddRemark={handleAddRemark}
          onAssign={handleAssign}
          userRole={currentView}
          employees={managerEmployees}
          token={token} // ✅ ADD THIS LINE
        />
      </main>

      {showCreateModal && (
        <CreateTaskModal
          token={token}
          empId={user.emp_id}
          currentRole={currentView}
          employees={managerEmployees} // for manager assigning to developers
          managers={managers} // for admin selecting reviewer (manager)
          onClose={() => setShowCreateModal(false)}
          onSuccess={() => {
            setShowCreateModal(false);
            loadTasks();
          }}
        />
      )}
    </div>
  );
};

export default Dashboard;
