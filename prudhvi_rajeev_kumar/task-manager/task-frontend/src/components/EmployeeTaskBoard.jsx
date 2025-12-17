import React, { useEffect, useState } from "react";
import { getTasks, updateTask } from "../services/taskService";
import { FaArrowRight, FaCheckCircle, FaTimesCircle } from "react-icons/fa"; // Adding icons for actions

const EmployeeTaskBoard = () => {
  const [tasks, setTasks] = useState([]);

  const loadTasks = async () => {
    const res = await getTasks();
    setTasks(res.data);
  };

  useEffect(() => {
    loadTasks();
  }, []);

  const updateStatus = async (task_id, currentStatus, newStatus) => {
    // Enforce employee rules on frontend too
    const allowed =
      (currentStatus === "TO_DO" && newStatus === "IN_PROGRESS") ||
      (currentStatus === "IN_PROGRESS" && newStatus === "REVIEW");

    if (!allowed) {
      alert(
        `As an employee you can only move TO_DO -> IN_PROGRESS or IN_PROGRESS -> REVIEW`
      );
      return;
    }

    await updateTask(task_id, { status: newStatus });
    loadTasks();
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-indigo-600 to-blue-500 p-8">
      <h2 className="text-3xl font-bold mb-6 text-white">My Tasks</h2>

      <div className="overflow-x-auto bg-white dark:bg-gray-800 rounded-lg shadow-xl p-4">
        <table className="w-full text-left text-gray-800 dark:text-gray-300">
          <thead>
            <tr className="bg-gray-200 dark:bg-gray-700 text-gray-900 dark:text-white">
              <th className="p-4">Title</th>
              <th className="p-4">Priority</th>
              <th className="p-4">Status</th>
              <th className="p-4">Actions</th>
            </tr>
          </thead>

          <tbody>
            {tasks.map((task) => (
              <tr
                key={task.task_id}
                className="border-b border-gray-300 hover:bg-gray-50 dark:hover:bg-gray-700 transition-all"
              >
                <td className="p-4">{task.title}</td>
                <td className="p-4">
                  <span
                    className={`font-semibold ${
                      task.priority === "High"
                        ? "text-red-500"
                        : task.priority === "Medium"
                        ? "text-yellow-500"
                        : "text-green-500"
                    }`}
                  >
                    {task.priority}
                  </span>
                </td>
                <td className="p-4">{task.status}</td>

                <td className="p-4 space-x-4">
                  {task.status === "TO_DO" && (
                    <button
                      onClick={() =>
                        updateStatus(task.task_id, task.status, "IN_PROGRESS")
                      }
                      className="bg-yellow-600 hover:bg-yellow-700 text-white px-4 py-2 rounded-full flex items-center justify-center transition-all duration-300"
                    >
                      <FaArrowRight className="mr-2" /> Start
                    </button>
                  )}

                  {task.status === "IN_PROGRESS" && (
                    <button
                      onClick={() =>
                        updateStatus(task.task_id, task.status, "REVIEW")
                      }
                      className="bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded-full flex items-center justify-center transition-all duration-300"
                    >
                      <FaCheckCircle className="mr-2" /> Send to Review
                    </button>
                  )}

                  {(task.status === "REVIEW" || task.status === "COMPLETED") && (
                    <span className="text-gray-500 dark:text-gray-400 text-sm flex items-center">
                      <FaTimesCircle className="mr-2" />
                      Waiting for manager review
                    </span>
                  )}
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default EmployeeTaskBoard;
