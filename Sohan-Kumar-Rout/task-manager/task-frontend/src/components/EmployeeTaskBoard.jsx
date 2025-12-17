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
                {task.status === "TO_DO" && (
                  <button
                    onClick={() =>
                      updateStatus(task.task_id, task.status, "IN_PROGRESS")
                    }
                    className="bg-yellow-600 px-3 py-1 rounded"
                  >
                    Start (In Progress)
                  </button>
                )}

                {task.status === "IN_PROGRESS" && (
                  <button
                    onClick={() =>
                      updateStatus(task.task_id, task.status, "REVIEW")
                    }
                    className="bg-blue-600 px-3 py-1 rounded"
                  >
                    Send to Review
                  </button>
                )}

                {(task.status === "REVIEW" ||
                  task.status === "COMPLETED") && (
                  <span className="text-gray-400 text-sm">
                    Waiting for manager review
                  </span>
                )}
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default EmployeeTaskBoard;
