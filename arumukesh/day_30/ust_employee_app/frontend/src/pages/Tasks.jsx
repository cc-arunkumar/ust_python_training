import { useEffect, useState } from "react";
import { getTasks } from "../api/taskApi";
import TaskCard from "../components/TaskCard";

export default function Tasks() {
  const [tasks, setTasks] = useState([]);

  useEffect(() => {
    getTasks().then(res => setTasks(res.data));
  }, []);

  return (
    <div className="p-6 grid gap-4">
      {tasks.map(task => (
        <TaskCard key={task.t_id} task={task} />
      ))}
    </div>
  );
}
