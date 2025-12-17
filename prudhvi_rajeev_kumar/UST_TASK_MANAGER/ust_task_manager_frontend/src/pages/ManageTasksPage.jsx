import { useEffect, useState } from "react";
import api from "../api/axios";
import TaskForm from "../components/TaskForm";
import TaskBoard from "../components/TaskBoard";

export default function ManageTasksPage() {
  const [tasks, setTasks] = useState([]);

  useEffect(() => {
    api.get("/tasks").then((res) => setTasks(res.data));
  }, []);

  const createTask = async (taskData) => {
    try {
      const res = await api.post("/tasks", taskData);
      setTasks([res.data, ...tasks]);
    } catch (err) {
      alert(err.response?.data?.detail || "Error creating task");
    }
  };

  return (
    <div className="container">
      <h2>Manage Tasks</h2>
      <TaskForm onSubmit={createTask} />
      <TaskBoard tasks={tasks} />
    </div>
  );
}
