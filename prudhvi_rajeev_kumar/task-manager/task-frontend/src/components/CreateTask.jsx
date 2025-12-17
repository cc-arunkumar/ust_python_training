import React, { useEffect, useState } from "react";
import { createTask, updateTask, getTasks } from "../services/taskService";
import { getEmployees } from "../services/employeeService";
import { toast, ToastContainer } from "react-toastify"; // Import toast and ToastContainer
import 'react-toastify/dist/ReactToastify.css'; // Import Toastify styles
import 'animate.css';

const CreateTask = () => {
  const params = new URLSearchParams(window.location.search);
  const editId = params.get("id");

  const [employees, setEmployees] = useState([]);
  const [form, setForm] = useState({
    title: "",
    description: "",
    assigned_to: "",
    assigned_by: localStorage.getItem("emp_id"),
    priority: "Medium",
  });

  const loadEmployees = async () => {
    try {
      const res = await getEmployees();
      setEmployees(res);
    } catch (err) {
      toast.error("Failed to load employees.");
    }
  };

  const loadTask = async () => {
    if (!editId) return;
    try {
      const res = await getTasks();
      const task = res.data.find((t) => t.task_id == editId);
      if (task) setForm(task);
    } catch (err) {
      toast.error("Failed to load task.");
    }
  };

  useEffect(() => {
    loadEmployees();
    loadTask();
  }, []);

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      if (editId) {
        await updateTask(editId, form);
        toast.success("Task updated successfully!"); // Success notification for update
      } else {
        await createTask(form);
        toast.success("Task created successfully!"); // Success notification for creation
      }

      const role = localStorage.getItem("role");
      if (role === "Admin") window.location.href = "/admin/tasks";
      else window.location.href = "/manager/tasks";
    } catch (err) {
      toast.error("Failed to save task. Please try again."); // Error notification
    }
  };

  return (
    <div className="bg-gradient-to-r from-blue-800 to-purple-700 p-8 rounded-lg shadow-xl text-white w-full min-h-screen animate__animated animate__fadeIn">
      <h2 className="text-3xl font-bold mb-6 text-center text-blue-200">
        {editId ? "Edit Task" : "Create Task"}
      </h2>

      <form onSubmit={handleSubmit} className="space-y-6 max-w-xl mx-auto">
        <input
          className="w-full p-4 bg-gray-700 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 transition-all duration-300"
          placeholder="Title"
          value={form.title}
          onChange={(e) => setForm({ ...form, title: e.target.value })}
        />

        <textarea
          className="w-full p-4 bg-gray-700 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 transition-all duration-300"
          placeholder="Description"
          value={form.description}
          onChange={(e) => setForm({ ...form, description: e.target.value })}
        />

        <select
          className="w-full p-4 bg-gray-700 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 transition-all duration-300"
          value={form.assigned_to}
          onChange={(e) => setForm({ ...form, assigned_to: e.target.value })}
        >
          <option value="">Assign To</option>
          {employees.map((emp) => (
            <option key={emp.id} value={emp.id}>
              {emp.name}
            </option>
          ))}
        </select>

        <select
          className="w-full p-4 bg-gray-700 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 transition-all duration-300"
          value={form.priority}
          onChange={(e) => setForm({ ...form, priority: e.target.value })}
        >
          <option>Low</option>
          <option>Medium</option>
          <option>High</option>
          <option>Critical</option>
        </select>

        <button
          className="w-full bg-blue-600 px-4 py-3 rounded-lg hover:bg-blue-700 transition-all duration-300"
        >
          {editId ? "Update Task" : "Create Task"}
        </button>
      </form>

      {/* Toast Container for showing notifications */}
      <ToastContainer position="top-right" autoClose={3000} hideProgressBar newestOnTop closeOnClick rtl={false} pauseOnFocusLoss draggable pauseOnHover />
    </div>
  );
};

export default CreateTask;
