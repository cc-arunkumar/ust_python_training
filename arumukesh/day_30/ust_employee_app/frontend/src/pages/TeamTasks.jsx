import { useEffect, useState } from "react";
import { getTasks } from "../api/taskApi";

const TeamTasks = () => {
  const [tasks, setTasks] = useState([]);

  useEffect(() => {
    getTasks().then(res => setTasks(res.data));
  }, []);

  return (
    <div className="p-6">
      <h2 className="text-xl font-bold mb-4">Team Tasks</h2>

      <ul className="space-y-3">
        {tasks.map(t => (
          <li key={t.id} className="border p-3 rounded">
            <b>{t.title}</b>
            <p>Status: {t.status}</p>
            <p>Assigned To: {t.assigned_to}</p>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default TeamTasks;
