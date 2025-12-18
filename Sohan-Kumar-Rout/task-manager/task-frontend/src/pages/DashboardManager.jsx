import React, { useEffect, useMemo, useState } from "react";
import { getTasks, createTask, updateTask } from "../services/taskService";
import { getEmployees } from "../services/employeeService";

/* -------------------- Dynamic Tailwind Helpers -------------------- */
const statusStyles = {
  TO_DO: "bg-yellow-200 text-yellow-800", // Dark pastel yellow
  IN_PROGRESS: "bg-blue-200 text-blue-800", // Dark pastel blue
  REVIEWED: "bg-purple-200 text-purple-800", // Dark pastel purple
  COMPLETED: "bg-green-200 text-green-800", // Dark pastel green
};

const priorityStyles = {
  Low: "bg-gray-300 text-gray-700", // Dark pastel gray
  Medium: "bg-blue-300 text-blue-800", // Dark pastel blue
  High: "bg-orange-300 text-orange-800", // Dark pastel orange
  Critical: "bg-red-300 text-red-800", // Dark pastel red
};

const MetricCard = ({ title, value, color }) => (
  <div
    className={`p-5 rounded-xl border shadow-md transition-all duration-300
    hover:scale-[1.02] hover:shadow-lg ${color}`}
  >
    <p className="text-sm opacity-70">{title}</p>
    <h3 className="text-3xl font-bold mt-1">{value}</h3>
  </div>
);

/* -------------------- Dashboard -------------------- */
const DashboardManager = () => {
  const managerId = localStorage.getItem("emp_id");
  const userName = localStorage.getItem("user_name") || "Manager";

  const [tasks, setTasks] = useState([]);
  const [employees, setEmployees] = useState([]);
  const [loading, setLoading] = useState(true);
  const [err, setErr] = useState("");
  const [selectedTask, setSelectedTask] = useState(null);
  const [remark, setRemark] = useState("");

  const [activeTab, setActiveTab] = useState("Active");
  const [priorityFilter, setPriorityFilter] = useState("");

  const [form, setForm] = useState({
    title: "",
    description: "",
    assigned_to: "",
    assigned_by: managerId,
    priority: "Medium",
    status: "TO_DO",
  });

  /* -------------------- Load Data -------------------- */
  useEffect(() => {
    const load = async () => {
      try {
        setLoading(true);
        const tRes = await getTasks();
        setTasks(tRes?.data || []);

        const eRes = await getEmployees();
        setEmployees(
          (eRes || []).filter(
            (e) => String(e.manager_id) === String(managerId)
          )
        );
      } catch {
        setErr("Failed to load dashboard data.");
      } finally {
        setLoading(false);
      }
    };
    load();
  }, [managerId]);

  /* -------------------- Derived Data -------------------- */
  const progress = useMemo(() => {
    if (!tasks.length) return 0;
    return Math.round(
      (tasks.filter((t) => t.status === "COMPLETED").length / tasks.length) * 100
    );
  }, [tasks]);

  /* -------------------- Filters -------------------- */
  const tabStatusMap = {
    Active: "IN_PROGRESS",
    Pending: "TO_DO",
    Reviewed: "REVIEWED",
    Completed: "COMPLETED",
  };

  const filteredTasks = useMemo(() => {
    let data = tasks.filter(
      (t) => t.status === tabStatusMap[activeTab]
    );

    if (priorityFilter) {
      data = data.filter((t) => t.priority === priorityFilter);
    }

    return data;
  }, [tasks, activeTab, priorityFilter]);

  /* -------------------- Create Task -------------------- */
  const handleCreate = async (e) => {
    e.preventDefault();
    setErr("");

    if (!form.title || !form.assigned_to) {
      setErr("Title and employee are required.");
      return;
    }

    try {
      await createTask(form);
      setForm({ ...form, title: "", description: "" });

      const tRes = await getTasks();
      setTasks(tRes?.data || []);
    } catch {
      setErr("Failed to create task.");
    }
  };

  /* -------------------- Update Remark -------------------- */
  const handleRemarkUpdate = async (taskId) => {
    if (!remark) {
      setErr("Please provide a remark.");
      return;
    }

    try {
      // Update task with remark
      const updatedTask = { ...selectedTask, remark };
      await updateTask(taskId, updatedTask);
      setRemark("");
      setSelectedTask(null);
      const tRes = await getTasks();
      setTasks(tRes?.data || []);
      setErr(""); // Clear error if successful
    } catch {
      setErr("Failed to update task remark.");
    }
  };

  /* -------------------- UI -------------------- */
  return (
    <div className="space-y-8">
      {/* Header */}
      <div>
        <h1 className="text-3xl font-bold">Good Morning, {userName}</h1>
        <p className="text-sm opacity-70">Here’s your overview for today</p>
      </div>

      {/* Metrics */}
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
        <MetricCard title="Employees" value={employees.length} color="bg-indigo-200" />
        <MetricCard title="Tasks" value={tasks.length} color="bg-blue-200" />
        <MetricCard title="Completed" value={tasks.filter((t) => t.status === "COMPLETED").length} color="bg-green-200" />
        <MetricCard title="Progress" value={`${progress}%`} color="bg-purple-200" />
      </div>

      {/* Filters */}
      <div className="flex flex-wrap gap-4">
        {Object.keys(tabStatusMap).map((tab) => (
          <button
            key={tab}
            onClick={() => setActiveTab(tab)}
            className={`px-4 py-1.5 rounded-full text-sm transition duration-300 ease-in-out ${
              activeTab === tab
                ? "bg-blue-600 text-white"
                : "bg-gray-200 hover:bg-gray-300"
            }`}
          >
            {tab}
          </button>
        ))}

        <select
          value={priorityFilter}
          onChange={(e) => setPriorityFilter(e.target.value)}
          className="px-3 py-1.5 rounded-lg border bg-white shadow-sm"
        >
          <option value="">Sort by Priority</option>
          <option value="Critical">Critical</option>
          <option value="High">High</option>
          <option value="Medium">Medium</option>
          <option value="Low">Low</option>
        </select>
      </div>

      {/* MAIN GRID */}
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
        {/* LEFT SIDE (TASKS) */}
        <div className="lg:col-span-2 space-y-6">
          {/* Task List */}
          <div className="space-y-4">
            {filteredTasks.map((task) => (
              <div
                key={task.task_id}
                className="p-4 rounded-xl bg-white border shadow-md hover:shadow-lg transition duration-300 transform hover:scale-105 animate-vibration"
                onMouseEnter={() => setSelectedTask(task)} // Hover effect to show task details
                onMouseLeave={() => setSelectedTask(null)} // Remove task details when mouse leaves
              >
                <div className="flex justify-between">
                  <div>
                    <h3 className="font-semibold">{task.title}</h3>
                    <p className="text-sm opacity-70">{task.description}</p>
                  </div>
                  <span className={`px-2 py-1 text-xs rounded-full ${statusStyles[task.status]}`}>
                    {task.status}
                  </span>
                </div>

                <div className="mt-2">
                  <span className={`px-2 py-1 text-xs rounded-full ${priorityStyles[task.priority]}`}>
                    {task.priority}
                  </span>
                </div>

                {/* Hovered details */}
                {selectedTask?.task_id === task.task_id && (
                  <div className="mt-4 border-t pt-2">
                    <div>
                      <p className="text-sm">Assigned to: {task.assigned_to}</p>
                      <textarea
                        className="w-full mt-2 p-2 border rounded"
                        placeholder="Add remarks for the employee"
                        value={remark}
                        onChange={(e) => setRemark(e.target.value)}
                      />
                    </div>
                    <button
                      className="mt-2 bg-blue-600 text-white p-2 rounded"
                      onClick={() => handleRemarkUpdate(task.task_id)}
                    >
                      Add Remark
                    </button>
                  </div>
                )}
              </div>
            ))}
          </div>
        </div>

        {/* RIGHT SIDE (CREATE TASK + EMPLOYEES) */}
        <div className="space-y-6">
          {/* Create Task */}
          <div className="p-5 rounded-xl bg-white border shadow-md">
            <h2 className="font-bold mb-3">Create Task</h2>

            {err && <p className="text-sm text-red-500 mb-2">{err}</p>}

            <form onSubmit={handleCreate} className="space-y-3">
              <input
                placeholder="Title"
                className="w-full p-2 rounded border dark:border-gray-700 bg-transparent"
                value={form.title}
                onChange={(e) => setForm({ ...form, title: e.target.value })}
              />

              <textarea
                placeholder="Description"
                rows={3}
                className="w-full p-2 rounded border dark:border-gray-700 bg-transparent"
                value={form.description}
                onChange={(e) => setForm({ ...form, description: e.target.value })}
              />

              <select
                className="w-full p-2 rounded border dark:border-gray-700 bg-transparent"
                value={form.assigned_to}
                onChange={(e) => setForm({ ...form, assigned_to: e.target.value })}
              >
                <option value="">Assign To</option>
                {employees.map((e) => (
                  <option key={e.id} value={e.id}>
                    {e.name}
                  </option>
                ))}
              </select>

              <select
                className="w-full p-2 rounded border dark:border-gray-700 bg-transparent"
                value={form.priority}
                onChange={(e) => setForm({ ...form, priority: e.target.value })}
              >
                <option>Low</option>
                <option>Medium</option>
                <option>High</option>
                <option>Critical</option>
              </select>

              <button
                className="w-full py-2 rounded-lg text-white
                bg-gradient-to-r from-blue-600 to-indigo-600
                hover:from-blue-700 hover:to-indigo-700 transition"
              >
                Create Task
              </button>
            </form>
          </div>

          {/* Employees Under Manager */}
          <div className="p-5 rounded-xl bg-white border shadow-md">
            <h2 className="font-bold mb-3">Employees Under Me</h2>
            <ul className="space-y-2">
              {employees.map((emp) => (
                <li
                  key={emp.id}
                  className="flex justify-between p-3 rounded-lg
                  bg-gray-50 dark:bg-gray-900 hover:bg-gray-100 dark:hover:bg-gray-800 transition"
                >
                  <div>
                    <p className="font-medium">{emp.name}</p>
                    <p className="text-xs opacity-60">{emp.role || "Employee"}</p>
                  </div>
                  <span className="text-xs px-2 py-1 rounded-full bg-green-200 text-green-700">
                    Active
                  </span>
                </li>
              ))}
            </ul>
          </div>
        </div>
      </div>

      {loading && <p className="opacity-60">Loading...</p>}
    </div>
  );
};

export default DashboardManager;
