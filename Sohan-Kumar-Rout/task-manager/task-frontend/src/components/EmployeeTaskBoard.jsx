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
    <div className="space-y-8 bg-[#F7F6F3] p-6 rounded-xl text-black font-poppins">
      <h2 className="text-3xl font-semibold text-[#5D6A75] mb-6">My Tasks</h2>

      <table className="w-full text-left border-collapse shadow-lg">
        <thead>
          <tr className="border-b border-[#E3E9EC]">
            <th className="p-4 text-lg text-[#616F77] font-medium">Title</th>
            <th className="p-4 text-lg text-[#616F77] font-medium">Priority</th>
            <th className="p-4 text-lg text-[#616F77] font-medium">Status</th>
            <th className="p-4 text-lg text-[#616F77] font-medium">Actions</th>
          </tr>
        </thead>

        <tbody>
          {tasks.map((task) => (
            <tr
              key={task.task_id}
              className="border-b border-[#E3E9EC] hover:bg-[#F0F5F1] transition-all duration-300"
            >
              <td className="p-4 text-sm text-[#3C4C56]">{task.title}</td>
              <td className="p-4">
                <span
                  className={`px-3 py-1 rounded-full text-xs font-medium ${getPriorityStyle(
                    task.priority
                  )}`}
                >
                  {task.priority}
                </span>
              </td>
              <td className="p-4">
                <span
                  className={`px-3 py-1 rounded-full text-xs font-medium ${getStatusStyle(
                    task.status
                  )}`}
                >
                  {task.status}
                </span>
              </td>

              <td className="p-4 space-x-2">
                {task.status === "TO_DO" && (
                  <button
                    onClick={() =>
                      updateStatus(task.task_id, task.status, "IN_PROGRESS")
                    }
                    className="bg-yellow-600 px-4 py-2 rounded text-white shadow-md hover:bg-yellow-700 transition-all duration-300"
                  >
                    Start (In Progress)
                  </button>
                )}

                {task.status === "IN_PROGRESS" && (
                  <button
                    onClick={() =>
                      updateStatus(task.task_id, task.status, "REVIEW")
                    }
                    className="bg-blue-600 px-4 py-2 rounded text-white shadow-md hover:bg-blue-700 transition-all duration-300"
                  >
                    Send to Review
                  </button>
                )}

                {(task.status === "REVIEW" || task.status === "COMPLETED") && (
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

// Dynamic styling for task priority and status
const getPriorityStyle = (priority) => {
  switch (priority) {
    case "Critical":
      return "bg-[#FF8A80] text-[#B22C1C]"; // Pastel red
    case "High":
      return "bg-[#FFCC80] text-[#F57C00]"; // Pastel orange
    case "Medium":
      return "bg-[#81C784] text-[#388E3C]"; // Pastel green
    case "Low":
      return "bg-[#64B5F6] text-[#1976D2]"; // Pastel blue
    default:
      return "bg-[#B0BEC5] text-[#546E7A]"; // Default gray
  }
};

const getStatusStyle = (status) => {
  switch (status) {
    case "TO_DO":
      return "bg-[#FFF59D] text-[#F57F17]"; // Pastel yellow
    case "IN_PROGRESS":
      return "bg-[#80DEEA] text-[#0097A7]"; // Pastel cyan
    case "REVIEW":
      return "bg-[#B39DDB] text-[#512DA8]"; // Pastel purple
    case "COMPLETED":
      return "bg-[#C8E6C9] text-[#388E3C]"; // Pastel green
    default:
      return "bg-[#E0E0E0] text-[#9E9E9E]"; // Default gray
  }
};

export default EmployeeTaskBoard;
