import React, { useEffect, useState } from "react";
import { getTasks, deleteTask } from "../services/taskService";
import { toast, ToastContainer } from "react-toastify"; // Import toast and ToastContainer
import 'react-toastify/dist/ReactToastify.css'; // Import Toastify styles
import 'animate.css';

const TaskList = () => {
  const [tasks, setTasks] = useState([]);
  const role = localStorage.getItem("role");

  const loadTasks = async () => {
    try {
      const res = await getTasks();
      setTasks(res.data);
    } catch (err) {
      toast.error("Failed to load tasks.");
    }
  };

  useEffect(() => {
    loadTasks();
  }, []);

  const handleDelete = async (id) => {
    if (!window.confirm("Are you sure you want to delete this task?")) return;

    try {
      await deleteTask(id);
      loadTasks(); // Reload the tasks after deletion
      toast.success("Task deleted successfully!"); // Show success notification
    } catch (err) {
      toast.error("Failed to delete task. Please try again."); // Show error notification
    }
  };

  return (
    <div className="bg-gradient-to-r from-green-50 via-blue-50 to-purple-50 p-8 rounded-lg shadow-xl text-gray-800 w-full min-h-screen animate__animated animate__fadeIn">
      <h2 className="text-3xl font-bold mb-6 text-center text-indigo-600 animate__animated animate__zoomIn">
        Tasks
      </h2>

      <div className="overflow-x-auto shadow-lg rounded-lg">
        <table className="w-full text-left border-separate table-auto">
          <thead>
            <tr className="bg-gray-200 text-gray-800">
              <th className="p-4">Title</th>
              <th className="p-4">Assigned To</th>
              <th className="p-4">Priority</th>
              <th className="p-4">Status</th>
              {role !== "Employee" && <th className="p-4">Actions</th>}
            </tr>
          </thead>

          <tbody>
            {tasks.map((task) => (
              <tr
                key={task.task_id}
                className="border-b border-gray-300 hover:bg-gray-100 transform transition duration-200"
              >
                <td className="p-4">{task.title}</td>
                <td className="p-4">{task.assigned_to}</td>
                <td className="p-4">{task.priority}</td>
                <td className="p-4">{task.status}</td>

                {role !== "Employee" && (
                  <td className="p-4 space-x-4 flex items-center justify-center">
                    <button
                      onClick={() =>
                        (window.location.href = `/admin/tasks/create?id=${task.task_id}`)
                      }
                      className="bg-gradient-to-r from-indigo-400 to-indigo-600 text-white px-4 py-2 rounded-lg hover:bg-indigo-700 transition duration-300"
                    >
                      Edit
                    </button>

                    <button
                      onClick={() => handleDelete(task.task_id)}
                      className="bg-gradient-to-r from-red-400 to-red-600 text-white px-4 py-2 rounded-lg hover:bg-red-700 transition duration-300"
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

      {/* Toast Container for showing notifications */}
      <ToastContainer position="top-right" autoClose={3000} hideProgressBar newestOnTop closeOnClick rtl={false} pauseOnFocusLoss draggable pauseOnHover />
    </div>
  );
};

export default TaskList;
