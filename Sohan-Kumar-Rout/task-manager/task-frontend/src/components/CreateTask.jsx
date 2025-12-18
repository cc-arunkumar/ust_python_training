import React, { useEffect, useState } from "react";
import { createTask, updateTask, getTasks } from "../services/taskService";
import { getEmployees } from "../services/employeeService";
import { toast } from "react-toastify";

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
    status: "TO_DO",
  });

  const loadEmployees = async () => {
    try {
      const res = await getEmployees();
      setEmployees(res);
    } catch (err) {
      toast.error("Failed to load employees!");
    }
  };

  const loadTask = async () => {
    if (!editId) return;
    try {
      const tasks = await getTasks();
      const task = tasks.find((t) => String(t.task_id) === String(editId));
      if (task) setForm(task);
    } catch (err) {
      toast.error("Failed to load task!");
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
        toast.success("Task updated successfully!");
      } else {
        await createTask(form);
        toast.success("Task created successfully!");
      }
      const role = localStorage.getItem("role");
      if (role === "Admin") window.location.href = "/admin/tasks";
      else window.location.href = "/manager/tasks";
    } catch (err) {
      toast.error("Failed to save task!");
    }
  };

  return (
    <div className="bg-gray-200 p-6 rounded-xl text-black w-full">
      <h2 className="text-2xl font-bold mb-4 text-blue-600">
        {editId ? "Edit Task" : "Create Task"}
      </h2>

      <form onSubmit={handleSubmit} className="space-y-4">
        <input
          className="w-full p-3 bg-white rounded border shadow-sm"
          placeholder="Title"
          value={form.title}
          onChange={(e) => setForm({ ...form, title: e.target.value })}
          required
        />

        <textarea
          className="w-full p-3 bg-white rounded border shadow-sm"
          placeholder="Description"
          value={form.description}
          onChange={(e) => setForm({ ...form, description: e.target.value })}
          required
        />

        <select
          className="w-full p-3 bg-white rounded border shadow-sm"
          value={form.assigned_to}
          onChange={(e) => setForm({ ...form, assigned_to: e.target.value })}
          required
        >
          <option value="">Assign To</option>
          {employees.map((emp) => (
            <option key={emp.id} value={emp.id}>
              {emp.name}
            </option>
          ))}
        </select>

        <select
          className="w-full p-3 bg-white rounded border shadow-sm"
          value={form.priority}
          onChange={(e) => setForm({ ...form, priority: e.target.value })}
        >
          <option>Low</option>
          <option>Medium</option>
          <option>High</option>
          <option>Critical</option>
        </select>

        <select
          className="w-full p-3 bg-white rounded border shadow-sm"
          value={form.status}
          onChange={(e) => setForm({ ...form, status: e.target.value })}
        >
          <option value="TO_DO">To Do</option>
          <option value="IN_PROGRESS">In Progress</option>
          <option value="REVIEW">Review</option>
          <option value="COMPLETED">Completed</option>
        </select>

        <button
          type="submit"
          className="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600 shadow-md"
        >
          {editId ? "Update" : "Create"}
        </button>
      </form>
    </div>
  );
};

export default CreateTask;
