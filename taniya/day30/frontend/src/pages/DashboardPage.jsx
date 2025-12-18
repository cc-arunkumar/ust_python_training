import { useState, useEffect } from "react";
import { Plus, CheckCircle, Clock, AlertCircle, ListTodo } from "lucide-react";
import { apiService } from "../services/api";
import TaskCard from "../components/TaskCard";
import StatsCard from "../components/StatsCard";

const DashboardPage = ({ currentUser, selectedRole, authToken }) => {
  const [tasks, setTasks] = useState([]);
  const [showCreateTask, setShowCreateTask] = useState(false);
  const [taskForm, setTaskForm] = useState({
    title: "",
    description: "",
    assigned_to: "",
    priority: "MEDIUM",
  });

  useEffect(() => {
    loadTasks();
  }, []);

  const loadTasks = async () => {
    try {
      const data = await apiService.getTasks(authToken);
      // If the current selected role is EMPLOYEE, filter tasks to assigned only
      if (selectedRole === "EMPLOYEE" && currentUser?.emp_id) {
        setTasks(
          data.filter(
            (t) => Number(t.assigned_to) === Number(currentUser.emp_id)
          )
        );
      } else {
        setTasks(data);
      }
    } catch (error) {
      console.error("Error loading tasks:", error);
    }
  };

  const handleCreateTask = async () => {
    if (!taskForm.title || !taskForm.description || !taskForm.assigned_to) {
      return;
    }

    try {
      await apiService.createTask(taskForm, authToken);
      setShowCreateTask(false);
      setTaskForm({
        title: "",
        description: "",
        assigned_to: "",
        priority: "MEDIUM",
      });
      loadTasks();
    } catch (error) {
      console.error("Error creating task:", error);
    }
  };

  const handleTaskStatusUpdated = (updatedTask) => {
    // Replace updated task in state
    setTasks((prev) =>
      prev.map((t) => (t.id === updatedTask.id ? updatedTask : t))
    );
  };

  const taskStats = {
    total: tasks.length,
    inProgress: tasks.filter((t) => t.status === "IN_PROGRESS").length,
    review: tasks.filter((t) => t.status === "REVIEW").length,
    done: tasks.filter((t) => t.status === "DONE").length,
  };

  const tasksByStatus = {
    TO_DO: tasks.filter((t) => t.status === "TO_DO"),
    IN_PROGRESS: tasks.filter((t) => t.status === "IN_PROGRESS"),
    REVIEW: tasks.filter((t) => t.status === "REVIEW"),
    DONE: tasks.filter((t) => t.status === "DONE"),
  };

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
      <div className="mb-8">
        <h1 className="text-3xl font-bold text-gray-900">
          Welcome back, {currentUser?.employee?.name || "User"}
        </h1>
        <p className="text-gray-600 mt-1">
          Your Role:{" "}
          <span className="font-semibold text-blue-600">{selectedRole}</span>
        </p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-4 gap-6 mb-8">
        <StatsCard
          title="Total Tasks"
          value={taskStats.total}
          icon={ListTodo}
          color="bg-blue-500"
          borderColor="border-blue-500"
        />
        <StatsCard
          title="In Progress"
          value={taskStats.inProgress}
          icon={Clock}
          color="bg-yellow-500"
          borderColor="border-yellow-500"
        />
        <StatsCard
          title="Review"
          value={taskStats.review}
          icon={AlertCircle}
          color="bg-purple-500"
          borderColor="border-purple-500"
        />
        <StatsCard
          title="Done"
          value={taskStats.done}
          icon={CheckCircle}
          color="bg-green-500"
          borderColor="border-green-500"
        />
      </div>

      {(selectedRole === "MANAGER" || selectedRole === "ADMIN") && (
        <div className="mb-6">
          <button
            onClick={() => setShowCreateTask(!showCreateTask)}
            className="px-6 py-3 bg-gradient-to-r from-blue-600 to-purple-600 text-white rounded-lg font-medium hover:from-blue-700 hover:to-purple-700 transition-all shadow-lg hover:shadow-xl inline-flex items-center space-x-2"
          >
            <Plus className="w-5 h-5" />
            <span>Create New Task</span>
          </button>
        </div>
      )}

      {showCreateTask && (
        <div className="bg-white rounded-xl shadow-sm p-6 mb-8 border border-gray-200">
          <h3 className="text-lg font-semibold mb-4">Create New Task</h3>
          <div className="space-y-4">
            <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
              <input
                type="text"
                placeholder="Task Title"
                value={taskForm.title}
                onChange={(e) =>
                  setTaskForm({ ...taskForm, title: e.target.value })
                }
                className="px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500"
              />
              <input
                type="number"
                placeholder="Assign to Employee ID"
                value={taskForm.assigned_to}
                onChange={(e) =>
                  setTaskForm({ ...taskForm, assigned_to: e.target.value })
                }
                className="px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500"
              />
            </div>
            <textarea
              placeholder="Task Description"
              value={taskForm.description}
              onChange={(e) =>
                setTaskForm({ ...taskForm, description: e.target.value })
              }
              className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500"
              rows="3"
            />
            <select
              value={taskForm.priority}
              onChange={(e) =>
                setTaskForm({ ...taskForm, priority: e.target.value })
              }
              className="px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 w-full md:w-auto"
            >
              <option value="HIGH">High Priority</option>
              <option value="MEDIUM">Medium Priority</option>
              <option value="LOW">Low Priority</option>
            </select>
            <div className="flex space-x-3">
              <button
                onClick={handleCreateTask}
                className="px-6 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition-all"
              >
                Create Task
              </button>
              <button
                onClick={() => setShowCreateTask(false)}
                className="px-6 py-2 bg-gray-200 text-gray-700 rounded-lg hover:bg-gray-300 transition-all"
              >
                Cancel
              </button>
            </div>
          </div>
        </div>
      )}

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
        {Object.entries(tasksByStatus).map(([status, statusTasks]) => (
          <div
            key={status}
            className="bg-gray-50 rounded-xl p-4 border border-gray-200"
          >
            <h3 className="font-semibold text-gray-900 mb-4 flex items-center justify-between">
              <span>{status.replace("_", " ")}</span>
              <span className="bg-gray-200 text-gray-700 text-xs px-2 py-1 rounded-full">
                {statusTasks.length}
              </span>
            </h3>
            <div className="space-y-3">
              {statusTasks.map((task) => (
                <TaskCard
                  key={task.id}
                  task={task}
                  selectedRole={selectedRole}
                  currentUser={currentUser}
                  authToken={authToken}
                  onStatusChange={handleTaskStatusUpdated}
                />
              ))}
              {statusTasks.length === 0 && (
                <div className="text-center text-gray-400 py-8 text-sm">
                  No tasks
                </div>
              )}
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default DashboardPage;
