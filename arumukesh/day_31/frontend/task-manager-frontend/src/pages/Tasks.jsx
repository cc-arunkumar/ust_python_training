import React, { useEffect, useState } from "react";
import { getTasks } from "../api/taskApi";

export default function Tasks() {
  const [tasks, setTasks] = useState([]);
  useEffect(() => {
    (async () => {
      try {
        const res = await getTasks();
        setTasks(res.data);
      } catch (e) {
        console.error(e);
      }
    })();
  }, []);

  return (
    <div>
      <h2 className="text-xl font-semibold mb-4">Tasks</h2>
      <div className="grid gap-3">
        {tasks.map((t) => (
          <div key={t.t_id} className="p-3 bg-white rounded shadow">
            <div className="font-semibold">{t.title}</div>
            <div className="text-sm text-gray-600">{t.description}</div>
            <div className="text-xs text-gray-500">{t.status}</div>
          </div>
        ))}
      </div>
    </div>
  );
}
