import React, { useEffect, useMemo, useState } from "react";
import { getTasks, createTask } from "../services/taskService";
import { getEmployees } from "../services/employeeService";

const DashboardManager = () => {
  // --- Manager context ---
  const managerId = localStorage.getItem("emp_id");
  const userName = localStorage.getItem("user_name") || "Manager";

  // --- Data state ---
  const [tasks, setTasks] = useState([]);
  const [employees, setEmployees] = useState([]);
  const [loading, setLoading] = useState(true);
  const [err, setErr] = useState("");

  // --- Form state (aligned with your previous CreateTask fields) ---
  const [form, setForm] = useState({
    title: "",
    description: "",
    assigned_to: "",
    assigned_by: managerId || "",
    priority: "Medium",
    status: "TO_DO",
  });

  // --- Load tasks and employees under the manager ---
  useEffect(() => {
    const load = async () => {
      try {
        setLoading(true);

        // Tasks
        const tRes = await getTasks();
        const tData = Array.isArray(tRes?.data) ? tRes.data : tRes || [];
        setTasks(tData);

        // Employees (filter if your API returns all employees)
        const eRes = await getEmployees();
        const eData = Array.isArray(eRes) ? eRes : eRes?.data || [];
        const underMe = eData.filter((e) => {
          // If your API has a manager_id field on employee, filter by it, otherwise skip filter
          return e.manager_id ? String(e.manager_id) === String(managerId) : true;
        });
        setEmployees(underMe);
      } catch (error) {
        console.error("Dashboard load error:", error);
        setErr("Failed to load data. Please try again.");
      } finally {
        setLoading(false);
      }
    };
    load();
  }, [managerId]);

  // --- Derived helpers ---
  const progress = useMemo(() => {
    if (!tasks.length) return 0;
    const completed = tasks.filter((t) => t.status === "COMPLETED").length;
    return Math.round((completed / tasks.length) * 100);
  }, [tasks]);

  const todayStr = new Date().toDateString();
  const yesterdayStr = new Date(Date.now() - 86400000).toDateString();

  const todayTasks = useMemo(
    () => tasks.filter((t) => new Date(t.created_at).toDateString() === todayStr),
    [tasks, todayStr]
  );
  const yesterdayTasks = useMemo(
    () => tasks.filter((t) => new Date(t.created_at).toDateString() === yesterdayStr),
    [tasks, yesterdayStr]
  );

  // --- Create Task handler ---
  const handleCreate = async (e) => {
    e.preventDefault();
    setErr("");

    // Basic validation
    if (!form.title?.trim()) return setErr("Title is required.");
    if (!form.assigned_to) return setErr("Please select an employee.");

    try {
      await createTask(form);
      // Reset title/description but keep assigned_by and defaults
      setForm((prev) => ({
        ...prev,
        title: "",
        description: "",
        status: "TO_DO",
      }));
      // Refresh tasks after creation
      const tRes = await getTasks();
      const tData = Array.isArray(tRes?.data) ? tRes.data : tRes || [];
      setTasks(tData);
    } catch (error) {
      console.error("Create task error:", error);
      setErr(
        error?.response?.data?.message ||
          "Could not create the task. Please check required fields and try again."
      );
    }
  };

  // --- UI ---
  return (
    <div className="w-full">
      {/* Top bar: greeting + quick stats */}
      <div className="flex items-center justify-between mb-6">
        <div>
          <h1 className="text-2xl font-bold">Good Morning, {userName}</h1>
          <p className="text-sm opacity-70">Here’s your overview for today.</p>
        </div>
        <div className="flex gap-3">
          <input
            type="text"
            placeholder="Search tasks..."
            className="px-4 py-2 rounded border bg-white dark:bg-gray-800 dark:border-gray-600"
          />
        </div>
      </div>

      {/* Metric cards */}
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 mb-8">
        <div className="p-4 rounded-lg border dark:border-gray-700 bg-white dark:bg-gray-800">
          <p className="text-sm opacity-70">Active Employees</p>
          <h3 className="text-2xl font-semibold">{employees.length}</h3>
        </div>
        <div className="p-4 rounded-lg border dark:border-gray-700 bg-white dark:bg-gray-800">
          <p className="text-sm opacity-70">Total Tasks</p>
          <h3 className="text-2xl font-semibold">{tasks.length}</h3>
        </div>
        <div className="p-4 rounded-lg border dark:border-gray-700 bg-white dark:bg-gray-800">
          <p className="text-sm opacity-70">Completed</p>
          <h3 className="text-2xl font-semibold">
            {tasks.filter((t) => t.status === "COMPLETED").length}
          </h3>
        </div>
        <div className="p-4 rounded-lg border dark:border-gray-700 bg-white dark:bg-gray-800">
          <p className="text-sm opacity-70">Progress</p>
          <div className="h-2 bg-gray-200 dark:bg-gray-700 rounded mt-2">
            <div
              className="h-2 bg-blue-600 rounded"
              style={{ width: `${progress}%` }}
            />
          </div>
          <p className="text-xs mt-2">{progress}% completed</p>
        </div>
      </div>

      {/* Main content: two columns */}
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        {/* Center: Task lists */}
        <div className="lg:col-span-2">
          <div className="flex gap-2 mb-4">
            {["Active", "Pending", "Reviewed", "Completed"].map((tab) => (
              <button
                key={tab}
                className="px-3 py-1 rounded bg-gray-200 dark:bg-gray-700 text-sm"
              >
                {tab}
              </button>
            ))}
          </div>

          <div className="space-y-6">
            <section>
              <h2 className="text-lg font-semibold mb-2">Yesterday</h2>
              {yesterdayTasks.length === 0 && (
                <p className="text-sm opacity-70">No tasks yesterday.</p>
              )}
              {yesterdayTasks.map((task) => (
                <div
                  key={task.task_id || task.id}
                  className="p-4 rounded bg-gray-100 dark:bg-gray-800 mb-2"
                >
                  <div className="flex justify-between">
                    <h3 className="font-semibold">{task.title}</h3>
                    <span className="text-xs px-2 py-1 rounded bg-gray-200 dark:bg-gray-700">
                      {task.status}
                    </span>
                  </div>
                  {task.description && (
                    <p className="text-sm mt-1 opacity-80">{task.description}</p>
                  )}
                </div>
              ))}
            </section>

            <section>
              <h2 className="text-lg font-semibold mb-2">Today</h2>
              {todayTasks.length === 0 && (
                <p className="text-sm opacity-70">No tasks today yet.</p>
              )}
              {todayTasks.map((task) => (
                <div
                  key={task.task_id || task.id}
                  className="p-4 rounded bg-gray-100 dark:bg-gray-800 mb-2"
                >
                  <div className="flex justify-between">
                    <h3 className="font-semibold">{task.title}</h3>
                    <span className="text-xs px-2 py-1 rounded bg-gray-200 dark:bg-gray-700">
                      {task.status}
                    </span>
                  </div>
                  {task.description && (
                    <p className="text-sm mt-1 opacity-80">{task.description}</p>
                  )}
                </div>
              ))}
            </section>
          </div>
        </div>

        {/* Right: New Task + Employees under me */}
        <div className="lg:col-span-1">
          <div className="p-4 rounded-lg border dark:border-gray-700 bg-white dark:bg-gray-800 mb-6">
            <h2 className="text-lg font-bold mb-3">New Task</h2>

            {err && (
              <div className="mb-3 text-sm text-red-600 dark:text-red-400">
                {err}
              </div>
            )}

            <form onSubmit={handleCreate} className="space-y-3">
              <input
                type="text"
                placeholder="Title"
                value={form.title}
                onChange={(e) => setForm({ ...form, title: e.target.value })}
                className="w-full px-3 py-2 rounded border dark:border-gray-700 bg-white dark:bg-gray-900"
              />

              <textarea
                placeholder="Description"
                value={form.description}
                onChange={(e) => setForm({ ...form, description: e.target.value })}
                className="w-full px-3 py-2 rounded border dark:border-gray-700 bg-white dark:bg-gray-900"
                rows={3}
              />

              <select
                value={form.assigned_to}
                onChange={(e) =>
                  setForm({ ...form, assigned_to: e.target.value })
                }
                className="w-full px-3 py-2 rounded border dark:border-gray-700 bg-white dark:bg-gray-900"
              >
                <option value="">Assign To</option>
                {employees.map((emp) => (
                  <option key={emp.id} value={emp.id}>
                    {emp.name}
                  </option>
                ))}
              </select>

              <select
                value={form.priority}
                onChange={(e) =>
                  setForm({ ...form, priority: e.target.value })
                }
                className="w-full px-3 py-2 rounded border dark:border-gray-700 bg-white dark:bg-gray-900"
              >
                <option>Low</option>
                <option>Medium</option>
                <option>High</option>
                <option>Critical</option>
              </select>

              {/* Hidden but included for backend alignment */}
              <input type="hidden" value={form.assigned_by} readOnly />
              <input type="hidden" value={form.status} readOnly />

              <button
                type="submit"
                className="w-full bg-blue-600 hover:bg-blue-700 text-white py-2 rounded"
                disabled={loading}
              >
                {loading ? "Processing..." : "Create Task"}
              </button>
            </form>
          </div>

          <div className="p-4 rounded-lg border dark:border-gray-700 bg-white dark:bg-gray-800">
            <h2 className="text-lg font-bold mb-3">Employees Under Me</h2>
            {employees.length === 0 && (
              <p className="text-sm opacity-70">No employees found.</p>
            )}
            <ul className="space-y-2">
              {employees.map((emp) => (
                <li
                  key={emp.id}
                  className="flex items-center justify-between px-3 py-2 rounded bg-gray-100 dark:bg-gray-900"
                >
                  <div>
                    <p className="font-medium">{emp.name}</p>
                    {emp.role && (
                      <p className="text-xs opacity-70">{emp.role}</p>
                    )}
                  </div>
                  <span className="text-xs px-2 py-1 rounded bg-gray-200 dark:bg-gray-700">
                    {emp.status || "Active"}
                  </span>
                </li>
              ))}
            </ul>
          </div>
        </div>
      </div>

      {loading && (
        <div className="mt-6 text-sm opacity-70">Loading data...</div>
      )}
    </div>
  );
};

export default DashboardManager;
