import React, { useEffect, useState } from "react";
import { getTasks, deleteTask } from "../services/taskService";
import { useNavigate } from "react-router-dom";

const TaskList = ({ onEdit }) => {
  const [tasks, setTasks] = useState([]);
  const navigate = useNavigate();

  useEffect(() => {
    loadTasks();
  }, []);

  const loadTasks = async () => {
    const res = await getTasks();
    setTasks(res.data);
  };

  const handleDelete = async (id) => {
    if (!window.confirm("Delete this task")) return;
    await deleteTask(id);
    loadTasks();
  };

  return (
    <div className="bg-[#1F2635] p-6 rounded-xl shadow-lg text-white w-full">
      <h2 className="text-2xl font-bold mb-4 text-blue-400">All Tasks</h2>

      <table className="w-full text-left border-collapse">
        <thead>
          <tr className="border-b border-gray-600 text-gray-300">
            <th className="p-3">ID</th>
            <th className="p-3">Title</th>
            <th className="p-3">Assigned To</th>
            <th className="p-3">Priority</th>
            <th className="p-3">Status</th>
            <th className="p-3">Actions</th>
          </tr>
        </thead>

        <tbody>
          {tasks.map((task) => (
            <tr key={task.task_id} className="border-b border-gray-700">
              <td className="p-3">{task.task_id}</td>
              <td className="p-3">{task.title}</td>
              <td className="p-3">{task.assignedTo}</td>
              <td className="p-3">{task.priority}</td>
              <td className="p-3">{task.status}</td>
              <td className="p-3 space-x-2">
                <button
                  onClick={() => {
                    onEdit(task);
                    navigate("/tasks/create");
                  }}
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
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default TaskList;
