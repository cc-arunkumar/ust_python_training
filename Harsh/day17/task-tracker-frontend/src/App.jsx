import { useContext, useEffect, useState } from "react";
import { AuthContext } from "./context/AuthContext";
import Login from "./components/Login";
import TaskForm from "./components/TaskForm";
import TaskItem from "./components/TaskItem";
import API from "./api";
import "./index.css";

export default function App() {
  const { user, logout } = useContext(AuthContext);
  const [tasks, setTasks] = useState([]);

  // Fetch tasks from backend
  const fetchTasks = async () => {
    try {
      const response = await API.get("/tasks");
      setTasks(response.data);
    } catch (error) {
      console.error("Failed to fetch tasks:", error);
    }
  };

  // Load tasks on mount
  useEffect(() => {
    if (user) {
      fetchTasks();
    }
  }, [user]);

  return (
    <div className="app-container">
      {user ? (
        <>
          {/* Top-right logout button */}
          <div className="logout-container">
            <button className="btn-secondary" onClick={logout}>
              Logout
            </button>
          </div>

          {/* Left side: TaskForm */}
          <div className="taskform-container">
            <TaskForm refreshTasks={fetchTasks} />
          </div>

          {/* Right side: All tasks in one container */}
          <div className="tasks-container">
            <h2 className="tasklist-title">My Tasks</h2>
            {tasks.length === 0 ? (
              <p>No tasks yet. Add one using the form!</p>
            ) : (
              tasks.map((task) => (
                <TaskItem key={task.id} task={task} refreshTasks={fetchTasks} />
              ))
            )}
          </div>
        </>
      ) : (
        <Login />
      )}
    </div>
  );
}
