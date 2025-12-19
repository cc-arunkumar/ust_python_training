// src/pages/MyTasks.jsx
import React, { useEffect, useState } from "react";
import axios from "axios";
import { useAuth } from "../context/AuthContext";

const MyTasks = () => {
  const [tasks, setTasks] = useState([]);
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(true);
  const { user } = useAuth();

  // Safe role access (in case role is missing or null)
  const role = user?.role ? user.role.toLowerCase() : "";

  useEffect(() => {
    const fetchTasks = async () => {
      if (!user) return;
      try {
        setLoading(true);
        const response = await axios.get("/api/v1/tasks");

        let myTasks = response.data;

        // Client-side filtering based on role
        if (role === "developer") {
          // Developers see only tasks assigned to them
          myTasks = response.data.filter(
            (task) => String(task.assigned_to) === String(user.emp_id)
          );
        }

        setTasks(myTasks);
      } catch (err) {
        console.error(err);
        setError("Failed to fetch tasks");
      } finally {
        setLoading(false);
      }
    };

    fetchTasks();
  }, [user, role]);

  return (
    <div>
      <h2 className="text-xl font-bold mb-4">My Tasks</h2>
      {loading && <p>Loading tasks...</p>}
      {error && <p className="text-red-500">{error}</p>}

      {!loading && tasks.length === 0 && !error && (
        <p>No tasks assigned to you.</p>
      )}

      {tasks.length > 0 && (
        <table className="w-full border-collapse border border-gray-300">
          <thead className="bg-gray-200">
            <tr>
              <th className="border border-gray-300 px-4 py-2">ID</th>
              <th className="border border-gray-300 px-4 py-2">Title</th>
              <th className="border border-gray-300 px-4 py-2">Status</th>
              <th className="border border-gray-300 px-4 py-2">Priority</th>
            </tr>
          </thead>
          <tbody>
            {tasks.map((task) => (
              <tr key={task.t_id} className="hover:bg-gray-50">
                <td className="border border-gray-300 px-4 py-2">
                  {task.t_id}
                </td>
                <td className="border border-gray-300 px-4 py-2">
                  {task.title}
                </td>
                <td className="border border-gray-300 px-4 py-2">
                  {task.status}
                </td>
                <td className="border border-gray-300 px-4 py-2">
                  {task.priority}
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
};

export default MyTasks;
