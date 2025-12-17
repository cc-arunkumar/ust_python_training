import { useEffect, useState } from "react";
import { useParams, useNavigate } from "react-router-dom";
import { getTaskById, updateTask } from "../api/task.api";
import { useAuth } from "../context/AuthContext";

export default function EditTask() {
  const { id } = useParams();
  const navigate = useNavigate();
  const { activeRole } = useAuth();

  // 🔐 Only ADMIN / MANAGER
  if (activeRole === "DEVELOPER") {
    return (
      <div className="p-6 text-red-600">
        Unauthorized
      </div>
    );
  }

  const [form, setForm] = useState({
    title: "",
    description: "",
    assigned_to: "",
    priority: "MEDIUM",
    expected_closure: "",
  });

  const [loading, setLoading] = useState(true);

  // 🔹 Load task
  useEffect(() => {
    const loadTask = async () => {
      try {
        const data = await getTaskById(id);

        setForm({
          title: data.title,
          description: data.description,
          assigned_to: data.assigned_to,
          priority: data.priority,
          expected_closure: data.expected_closure
            ? data.expected_closure.slice(0, 16)
            : "",
        });
      } finally {
        setLoading(false);
      }
    };

    loadTask();
  }, [id]);

  const handleChange = (e) => {
    setForm({
      ...form,
      [e.target.name]: e.target.value,
    });
  };

  const submit = async (e) => {
    e.preventDefault();

    await updateTask(id, {
      ...form,
      assigned_to: Number(form.assigned_to),
    });

    // ✅ Go back to dashboard
    navigate("/dashboard");
  };

  if (loading) return <div className="p-6">Loading…</div>;

  return (
    <div className="p-6 max-w-xl mx-auto">
      <h2 className="text-xl font-semibold mb-4">
        Edit Task
      </h2>

      <form
        onSubmit={submit}
        className="space-y-4 bg-white p-6 rounded shadow"
      >
        <input
          name="title"
          value={form.title}
          onChange={handleChange}
          className="w-full border p-2 rounded"
          placeholder="Title"
          required
        />

        <textarea
          name="description"
          value={form.description}
          onChange={handleChange}
          className="w-full border p-2 rounded"
          placeholder="Description"
          required
        />

        <input
          name="assigned_to"
          type="number"
          value={form.assigned_to}
          onChange={handleChange}
          className="w-full border p-2 rounded"
          placeholder="Assign to (Employee ID)"
          required
        />

        <select
          name="priority"
          value={form.priority}
          onChange={handleChange}
          className="w-full border p-2 rounded"
        >
          <option value="LOW">LOW</option>
          <option value="MEDIUM">MEDIUM</option>
          <option value="HIGH">HIGH</option>
        </select>

        <input
          name="expected_closure"
          type="datetime-local"
          value={form.expected_closure}
          onChange={handleChange}
          className="w-full border p-2 rounded"
        />

        <button
          type="submit"
          className="bg-blue-600 text-white px-4 py-2 rounded"
        >
          Update Task
        </button>
      </form>
    </div>
  );
}
