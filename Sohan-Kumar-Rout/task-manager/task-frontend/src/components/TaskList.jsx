import React, { useEffect, useState } from "react";
import { getTasks, deleteTask } from "../services/taskService";

const TaskList = () => {
  const [tasks, setTasks] = useState([]);
  const role = localStorage.getItem("role");

  const loadTasks = async () => {
    const res = await getTasks();
    setTasks(res.data);
  };

  useEffect(() => {
    loadTasks();
  }, []);

  const handleDelete = async (id) => {
    if (!window.confirm("Delete this task")) return;
    await deleteTask(id);
    loadTasks();
  };

  return (
    <div className="bg-gray-800 p-6 rounded-xl text-white w-full">
      <h2 className="text-2xl font-bold mb-4 text-blue-400">Tasks</h2>

      <table className="w-full text-left border-collapse">
        <thead>
          <tr className="border-b border-gray-600 text-gray-300">
            <th className="p-3">Title</th>
            <th className="p-3">Assigned To</th>
            <th className="p-3">Priority</th>
            <th className="p-3">Status</th>
            {role !== "Employee" && <th className="p-3">Actions</th>}
          </tr>
        </thead>

        <tbody>
          {tasks.map((task) => (
            <tr key={task.task_id} className="border-b border-gray-700">
              <td className="p-3">{task.title}</td>
              <td className="p-3">{task.assigned_to}</td>
              <td className="p-3">{task.priority}</td>
              <td className="p-3">{task.status}</td>

              {role !== "Employee" && (
                <td className="p-3 space-x-2">
                  <button
                    onClick={() =>
                      (window.location.href = `/admin/tasks/create?id=${task.task_id}`)
                    }
                    className="bg-blue-600 px-3 py-1 rounded hover:bg-blue-700"
                  >
                    Edit
                  </button>

                  <button
                    onClick={() => handleDelete(task.task_id)}
                    className="bg-red-600 px-3 py-1 rounded hover:bg-red-700"
                  >
                    Delete
                  </button>
                </td>
              )}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default TaskList;
