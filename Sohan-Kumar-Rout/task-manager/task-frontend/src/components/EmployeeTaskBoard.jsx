import React, { useEffect, useState } from "react";
import { getTasks, updateTask } from "../services/taskService";

const EmployeeTaskBoard = () => {
  const [tasks, setTasks] = useState([]);

  const loadTasks = async () => {
    const res = await getTasks();
    setTasks(res.data);
  };

  useEffect(() => {
    loadTasks();
  }, []);

  const updateStatus = async (task_id, status) => {
    await updateTask(task_id, { status });
    loadTasks();
  };

  return (
    <div className="bg-gray-800 p-6 rounded-xl">
      <h2 className="text-2xl font-bold mb-4 text-blue-400">My Tasks</h2>

      <table className="w-full text-left">
        <thead>
          <tr className="border-b border-gray-600">
            <th className="p-3">Title</th>
            <th className="p-3">Priority</th>
            <th className="p-3">Status</th>
            <th className="p-3">Actions</th>
          </tr>
        </thead>

        <tbody>
          {tasks.map((task) => (
            <tr key={task.task_id} className="border-b border-gray-700">
              <td className="p-3">{task.title}</td>
              <td className="p-3">{task.priority}</td>
              <td className="p-3">{task.status}</td>

              <td className="p-3 space-x-2">
                <button
                  onClick={() => updateStatus(task.task_id, "In Progress")}
                  className="bg-yellow-600 px-3 py-1 rounded"
                >
                  In Progress
                </button>

                <button
                  onClick={() => updateStatus(task.task_id, "Completed")}
                  className="bg-green-600 px-3 py-1 rounded"
                >
                  Completed
                </button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default EmployeeTaskBoard;
