import { useParams } from "react-router-dom";
import { useEffect, useState } from "react";
import { getTaskById } from "../api/taskApi";

export default function TaskDetails() {
  const { id } = useParams();
  const [task, setTask] = useState(null);

  useEffect(() => {
    getTaskById(id).then(res => setTask(res.data));
  }, [id]);

  if (!task) return null;

  return (
    <div className="p-6">
      <h1 className="text-xl font-bold">{task.title}</h1>
      <p>{task.description}</p>
      <p>Status: {task.status}</p>
    </div>
  );
}
