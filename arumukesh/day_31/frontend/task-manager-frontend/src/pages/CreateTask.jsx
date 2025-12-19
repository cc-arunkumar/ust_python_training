// src/pages/CreateTask.jsx
import React, { useState, useEffect } from "react";
import axios from "axios";
import { useAuth } from "../context/AuthContext";

const CreateTask = () => {
  const { user } = useAuth();
  const [employees, setEmployees] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const [success, setSuccess] = useState("");

  const [formData, setFormData] = useState({
    title: "",
    description: "",
    assigned_to: "",
    priority: "medium",
    status: "pending",
    reviewer: "",
    expected_closure: "",
    remarks: "",
  });

  useEffect(() => {
    // Fetch all employees for dropdowns
    const fetchEmployees = async () => {
      try {
        const res = await axios.get("/api/v1/employees");
        setEmployees(res.data);
      } catch (err) {
        console.error(err);
        setError("Failed to load employees");
      }
    };
    fetchEmployees();
  }, []);

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError("");
    setSuccess("");
    setLoading(true);

    try {
      // Build payload exactly matching TaskCreate model
      const payload = {
        title: formData.title.trim(),
        description: formData.description.trim(),
        created_by: String(user.emp_id), // ← Convert to string
        assigned_to: formData.assigned_to, // already string from dropdown
        assigned_by: String(user.emp_id), // ← Convert to string
        priority: formData.priority.toLowerCase(),
        status: formData.status.toLowerCase(),
        reviewer: formData.reviewer,
        expected_closure: new Date(formData.expected_closure).toISOString(),
        remarks: formData.remarks.trim() || null,
      };

      await axios.post("/api/v1/tasks", payload);

      setSuccess("Task created successfully!");
      // Reset form
      setFormData({
        title: "",
        description: "",
        assigned_to: "",
        priority: "medium",
        status: "pending",
        reviewer: "",
        expected_closure: "",
        remarks: "",
      });
    } catch (err) {
      if (err.response?.status === 422) {
        const details = err.response.data.detail;
        if (Array.isArray(details)) {
          const messages = details.map((d) => `${d.loc.join(" → ")}: ${d.msg}`);
          setError("Validation errors: " + messages.join("; "));
        } else {
          setError("Invalid data submitted");
        }
      } else if (err.response?.status === 400) {
        setError(err.response.data.detail || "Reviewer must be a manager");
      } else if (err.response?.status === 403) {
        setError("You are not authorized to create tasks");
      } else {
        setError("Failed to create task");
      }
    } finally {
      setLoading(false);
    }
  };

  if (!user) {
    return <div className="p-6">Loading user...</div>;
  }

  // Filter managers (mgr_id is None/null) for reviewer
  const managers = employees.filter(
    (emp) => emp.mgr_id === null || emp.mgr_id === ""
  );
  // const managers = employees.filter(emp => !emp.mgr_id);
  return (
    <div className="max-w-4xl mx-auto p-6 bg-white rounded-lg shadow">
      <h2 className="text-2xl font-bold mb-6">Create New Task</h2>

      {error && (
        <div className="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded mb-6">
          {error}
        </div>
      )}
      {success && (
        <div className="bg-green-100 border border-green-400 text-green-700 px-4 py-3 rounded mb-6">
          {success}
        </div>
      )}

      <form onSubmit={handleSubmit} className="space-y-6">
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">
              Title *
            </label>
            <input
              type="text"
              name="title"
              value={formData.title}
              onChange={handleChange}
              required
              maxLength={100}
              className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
            />
          </div>

          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">
              Priority *
            </label>
            <select
              name="priority"
              value={formData.priority}
              onChange={handleChange}
              className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
            >
              <option value="high">High</option>
              <option value="medium">Medium</option>
              <option value="low">Low</option>
            </select>
          </div>
        </div>

        <div>
          <label className="block text-sm font-medium text-gray-700 mb-1">
            Description *
          </label>
          <textarea
            name="description"
            value={formData.description}
            onChange={handleChange}
            required
            rows={4}
            maxLength={200}
            className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
          />
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">
              Assign To *
            </label>
            <select
              name="assigned_to"
              value={formData.assigned_to}
              onChange={handleChange}
              required
              className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
            >
              <option value="">Select Assignee</option>
              {employees.map((emp) => (
                <option key={emp.emp_id} value={emp.emp_id}>
                  {emp.name} ({emp.emp_id}) - {emp.designation}
                </option>
              ))}
            </select>
          </div>

          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">
              Reviewer * (Must be Manager)
            </label>
            <select
              name="reviewer"
              value={formData.reviewer}
              onChange={handleChange}
              required
              className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
            >
              <option value="">Select Reviewer</option>
              {employees.map((emp) => (
                <option key={emp.emp_id} value={emp.emp_id}>
                  {emp.name} ({emp.emp_id}) - {emp.designation}
                </option>
              ))}
            </select>
            {managers.length === 0 && (
              <p className="text-xs text-orange-600 mt-1">
                No managers found. Create a manager employee first.
              </p>
            )}
          </div>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">
              Status *
            </label>
            <select
              name="status"
              value={formData.status}
              onChange={handleChange}
              className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
            >
              <option value="pending">Pending</option>
              <option value="in_progress">In Progress</option>
              <option value="on_hold">On Hold</option>
              <option value="completed">Completed</option>
              <option value="cancelled">Cancelled</option>
            </select>
          </div>

          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">
              Expected Closure Date *
            </label>
            <input
              type="date"
              name="expected_closure"
              value={formData.expected_closure}
              onChange={handleChange}
              required
              className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
            />
          </div>
        </div>

        <div>
          <label className="block text-sm font-medium text-gray-700 mb-1">
            Remarks (Optional)
          </label>
          <textarea
            name="remarks"
            value={formData.remarks}
            onChange={handleChange}
            rows={3}
            maxLength={500}
            className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
          />
        </div>

        <div className="flex gap-4">
          <button
            type="submit"
            disabled={loading}
            className="bg-blue-600 text-white px-6 py-3 rounded-md hover:bg-blue-700 disabled:opacity-50 disabled:cursor-not-allowed"
          >
            {loading ? "Creating..." : "Create Task"}
          </button>
        </div>
      </form>
    </div>
  );
};

export default CreateTask;
