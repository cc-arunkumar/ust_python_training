import { useEffect, useState } from "react";
import { getTasks } from "../api/task.api";
import TaskCard from "../components/TaskCard";
import { useAuth } from "../context/AuthContext";

const STATUSES = [
  { key: "TO_DO", label: "TO DO" },
  { key: "IN_PROGRESS", label: "IN PROGRESS" },
  { key: "REVIEW", label: "REVIEW" },
  { key: "DONE", label: "COMPLETED" },
];

export default function Board() {
  const { activeRole } = useAuth();
  const [tasks, setTasks] = useState([]);
  const [grouped, setGrouped] = useState({});

  // Fetch tasks
  const fetchTasks = async () => {
    const data = await getTasks();
    setTasks(data);
  };

  useEffect(() => {
    fetchTasks();
  }, [activeRole]);

  // Group tasks by status
  useEffect(() => {
    const map = {
      TO_DO: [],
      IN_PROGRESS: [],
      REVIEW: [],
      DONE: [],
    };

    tasks.forEach((task) => {
      map[task.status]?.push(task);
    });

    setGrouped(map);
  }, [tasks]);

  return (
    <div className="h-full px-6 py-4">
      {/* BOARD GRID */}
      <div className="grid grid-cols-4 gap-4 h-full">

        {STATUSES.map((col) => (
          <div
            key={col.key}
            className="flex flex-col bg-gray-100 rounded-lg"
          >
            {/* COLUMN HEADER */}
            <div className="px-3 py-2 border-b bg-gray-100 rounded-t-lg">
              <h2 className="text-sm font-semibold text-gray-700">
                {col.label}
              </h2>
            </div>

            {/* COLUMN BODY (SCROLLABLE) */}
            <div className="flex-1 overflow-y-auto p-3 space-y-3">
              {grouped[col.key]?.length === 0 && (
                <p className="text-sm text-gray-400 text-center mt-4">
                  No tasks
                </p>
              )}

              {grouped[col.key]?.map((task) => (
                <TaskCard
                  key={task.t_id}
                  task={task}
                  role={activeRole}
                  refresh={fetchTasks}
                />
              ))}
            </div>
          </div>
        ))}

      </div>
    </div>
  );
}
