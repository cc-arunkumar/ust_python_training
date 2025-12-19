import { useEffect, useState } from "react";
import api from "../api/axios";

export default function Tasks() {
  const [tasks, setTasks] = useState([]);

  useEffect(() => {
    api.get("/tasks").then((res) => setTasks(res.data));
  }, []);

  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold mb-4">Tasks</h1>

      <div className="grid gap-4">
        {tasks.map((task) => (
          <div key={task.t_id} className="p-4 bg-white rounded shadow">
            <h2 className="font-semibold">{task.title}</h2>
            <p>{task.description}</p>
            <span className="text-sm text-gray-500">{task.status}</span>
          </div>
        ))}
      </div>
    </div>
  );
}
