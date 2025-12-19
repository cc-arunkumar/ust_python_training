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
    expected_closure: "",
    status: "TO_DO",
  });

  const loadEmployees = async () => {
    try {
      const res = await getEmployees();
      const data = Array.isArray(res) ? res : (res?.data || []);
      setEmployees(data);
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
    <div className="bg-gradient-to-r from-green-50 via-blue-50 to-purple-50 p-8 rounded-lg shadow-xl text-gray-800 w-full min-h-screen animate__animated animate__fadeIn">
      <div className="max-w-3xl mx-auto">
        <h2 className="text-3xl font-bold mb-4 text-indigo-600">{editId ? "Edit Task" : "Create Task"}</h2>

        <form onSubmit={handleSubmit} className="space-y-6 bg-white p-6 rounded-lg shadow">
          <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
            <input
              className="w-full p-3 bg-gray-100 rounded-lg focus:outline-none focus:ring-2 focus:ring-indigo-300"
              placeholder="Title"
              value={form.title}
              onChange={(e) => setForm({ ...form, title: e.target.value })}
            />

            <select
              className="w-full p-3 bg-gray-100 rounded-lg"
              value={form.priority}
              onChange={(e) => setForm({ ...form, priority: e.target.value })}
            >
              <option>Low</option>
              <option>Medium</option>
              <option>High</option>
              <option>Critical</option>
            </select>
          </div>

          <textarea
            className="w-full p-3 bg-gray-100 rounded-lg h-36"
            placeholder="Description"
            value={form.description}
            onChange={(e) => setForm({ ...form, description: e.target.value })}
          />

          <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
            <select
              className="md:col-span-2 p-3 bg-gray-100 rounded-lg"
              value={form.assigned_to}
              onChange={(e) => setForm({ ...form, assigned_to: e.target.value })}
            >
              <option value="">Assign To</option>
              {employees.map((emp) => (
                <option key={emp.id} value={emp.id}>
                  {emp.name} — {emp.designation}
                </option>
              ))}
            </select>

            <input
              type="date"
              className="p-3 bg-gray-100 rounded-lg"
              value={form.expected_closure || ''}
              onChange={(e) => setForm({ ...form, expected_closure: e.target.value })}
            />
          </div>

          <div className="flex items-center justify-between gap-4">
            <select
              className="p-3 bg-gray-100 rounded-lg w-1/3"
              value={form.status}
              onChange={(e) => setForm({ ...form, status: e.target.value })}
            >
              <option value="TO_DO">TO_DO</option>
              <option value="IN_PROGRESS">IN_PROGRESS</option>
              <option value="REVIEWED">REVIEWED</option>
              <option value="COMPLETED">COMPLETED</option>
            </select>

            <div className="flex gap-2 ml-auto">
              <button
                type="button"
                onClick={() => {
                  const role = localStorage.getItem("role");
                  if (role === "Admin") window.location.href = "/admin/tasks";
                  else window.location.href = "/manager/tasks";
                }}
                className="px-4 py-2 rounded border"
              >
                Cancel
              </button>

              <button
                type="submit"
                className="px-6 py-2 rounded bg-gradient-to-r from-indigo-500 to-purple-500 text-white"
              >
                {editId ? "Update Task" : "Create Task"}
              </button>
            </div>
          </div>
        </form>

        {/* Toast Container for showing notifications */}
        <ToastContainer position="top-right" autoClose={3000} hideProgressBar newestOnTop closeOnClick rtl={false} pauseOnFocusLoss draggable pauseOnHover />
      </div>
    </div>
  );
};

export default CreateTask;
