import { useEffect, useState } from "react";
import api from "../api/axios";
import TaskBoard from "../components/TaskBoard";
import ActivityLog from "../components/Activitylog";
import { toast, ToastContainer } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";

export default function TasksPage({ search }) {
  const [tasks, setTasks] = useState([]);
  const [logs, setLogs] = useState([]);

  useEffect(() => {
    api.get("/tasks").then((res) => setTasks(res.data));
  }, []);

  const handleDragEnd = async (result) => {
    if (!result.destination) return;
    const taskId = result.draggableId;
    const newStatus = result.destination.droppableId;

    try {
      await api.patch(`/tasks/${taskId}/status`, { status: newStatus });
      setTasks(
        tasks.map((t) =>
          t.taskid === Number(taskId) ? { ...t, status: newStatus } : t
        )
      );
      const message = `Task ${taskId} moved to ${newStatus}`;
      setLogs([message, ...logs]);
      toast.info(message);
    } catch (err) {
      toast.error("Failed to update task status");
    }
  };

  const filteredTasks = tasks.filter(
    (t) =>
      t.title.toLowerCase().includes(search.toLowerCase()) ||
      t.description.toLowerCase().includes(search.toLowerCase())
  );

  return (
    <div className="container">
      <h2>Project Board</h2>
      <TaskBoard tasks={filteredTasks} onDragEnd={handleDragEnd} />
      <ActivityLog logs={logs} />
      <ToastContainer position="bottom-right" />
    </div>
  );
}
