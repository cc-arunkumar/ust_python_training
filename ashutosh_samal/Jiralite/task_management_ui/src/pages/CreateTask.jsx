import { useState } from "react";
import { createTask } from "../api/task.api";
import { useAuth } from "../context/AuthContext";
import { useNavigate } from "react-router-dom";

export default function CreateTask() {
  const { activeRole } = useAuth();
  const navigate = useNavigate();

  // 🔐 Only Admin / Manager
  if (activeRole !== "ADMIN" && activeRole !== "MANAGER") {
    return <div className="p-6">Unauthorized</div>;
  }

  const [form, setForm] = useState({
    title: "",
    description: "",
    assigned_to: "",
    priority: "MEDIUM",
    expected_closure: "",
  });

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    await createTask({
      ...form,
      assigned_to: Number(form.assigned_to),
    });

    navigate("/dashboard");
  };

  return (
    <div className="h-screen flex flex-col">
      <div className="p-6 max-w-xl mx-auto w-full">
        <h2 className="text-xl font-semibold mb-4">
          Create Task
        </h2>

        <form
          onSubmit={handleSubmit}
          className="space-y-4 bg-white p-6 rounded shadow"
        >
          <input
            name="title"
            placeholder="Title"
            className="w-full border p-2 rounded"
            onChange={handleChange}
            required
          />

          <textarea
            name="description"
            placeholder="Description"
            className="w-full border p-2 rounded"
            onChange={handleChange}
            required
          />

          <input
            name="assigned_to"
            type="number"
            placeholder="Assign to (Employee ID)"
            className="w-full border p-2 rounded"
            onChange={handleChange}
            required
          />

          <select
            name="priority"
            className="w-full border p-2 rounded"
            onChange={handleChange}
          >
            <option value="LOW">LOW</option>
            <option value="MEDIUM">MEDIUM</option>
            <option value="HIGH">HIGH</option>
          </select>

          <input
            name="expected_closure"
            type="datetime-local"
            className="w-full border p-2 rounded"
            onChange={handleChange}
          />

          <button
            type="submit"
            className="bg-blue-600 text-white px-4 py-2 rounded"
          >
            Create Task
          </button>
        </form>
      </div>
    </div>
  );
}
