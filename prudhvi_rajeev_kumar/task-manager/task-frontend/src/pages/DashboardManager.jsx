import React, { useEffect, useMemo, useState } from "react";
import { getTasks, createTask } from "../services/taskService";
import { getEmployees } from "../services/employeeService";
import { toast, ToastContainer } from "react-toastify"; // Import toast and ToastContainer
import "react-toastify/dist/ReactToastify.css"; // Import Toastify styles

const DashboardManager = () => {
  const managerId = localStorage.getItem("emp_id");
  const userName = localStorage.getItem("user_name") || "Manager";

  const [tasks, setTasks] = useState([]);
  const [employees, setEmployees] = useState([]);
  const [loading, setLoading] = useState(true);
  const [err, setErr] = useState("");
  const [searchQuery, setSearchQuery] = useState("");
  const [selectedTab, setSelectedTab] = useState("Active");

  const [form, setForm] = useState({
    title: "",
    description: "",
    assigned_to: "",
    assigned_by: managerId || "",
    priority: "Medium",
    status: "TO_DO",
  });

  useEffect(() => {
    const load = async () => {
      try {
        setLoading(true);
        const tRes = await getTasks();
        const tData = Array.isArray(tRes?.data) ? tRes.data : [];
        setTasks(tData);

        const eRes = await getEmployees();
        const eData = Array.isArray(eRes) ? eRes : eRes?.data || [];
        const underMe = eData.filter((e) => String(e.manager_id) === String(managerId));
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

  const progress = useMemo(() => {
    if (!tasks.length) return 0;
    const completed = tasks.filter((t) => t.status === "COMPLETED").length;
    return Math.round((completed / tasks.length) * 100);
  }, [tasks]);

  const todayStr = new Date().toDateString();
  const yesterdayStr = new Date(Date.now() - 86400000).toDateString();

  const todayTasks = useMemo(() => tasks.filter((t) => new Date(t.created_at).toDateString() === todayStr), [tasks, todayStr]);
  const yesterdayTasks = useMemo(() => tasks.filter((t) => new Date(t.created_at).toDateString() === yesterdayStr), [tasks, yesterdayStr]);

  const handleCreate = async (e) => {
    e.preventDefault();
    setErr("");

    if (!form.title?.trim()) return setErr("Title is required.");
    if (!form.assigned_to) return setErr("Please select an employee.");

    try {
      await createTask(form);
      setForm((prev) => ({ ...prev, title: "", description: "", status: "TO_DO" }));
      const tRes = await getTasks();
      const tData = Array.isArray(tRes?.data) ? tRes.data : [];
      setTasks(tData);
      
      // Success Toast notification
      toast.success("Task created successfully!");
    } catch (error) {
      setErr("Could not create the task. Please check required fields and try again.");
      
      // Error Toast notification
      toast.error("Error creating task. Please try again.");
    }
  };

  const filteredTasks = useMemo(() => {
    return tasks.filter((task) =>
      task.title.toLowerCase().includes(searchQuery.toLowerCase()) ||
      task.description?.toLowerCase().includes(searchQuery.toLowerCase())
    );
  }, [tasks, searchQuery]);

  const tabFilteredTasks = useMemo(() => {
    return filteredTasks.filter((task) => {
      if (selectedTab === "Active") return task.status !== "COMPLETED";
      if (selectedTab === "Completed") return task.status === "COMPLETED";
      if (selectedTab === "Pending") return task.status === "TO_DO";
      if (selectedTab === "Reviewed") return task.status === "REVIEWED";
      return true;
    });
  }, [filteredTasks, selectedTab]);

  return (
    <div className="w-full bg-gray-50 dark:bg-gray-900 p-6">
      {/* Header */}
      <div className="flex items-center justify-between mb-6">
        <div>
          <h1 className="text-3xl font-bold text-gray-800 dark:text-white">Good Morning, {userName}</h1>
          <p className="text-lg text-gray-600 dark:text-gray-400">Here's your overview for today.</p>
        </div>
        <div className="flex gap-4">
          <input
            type="text"
            placeholder="Search tasks..."
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
            className="px-4 py-2 rounded-lg border border-gray-300 bg-white dark:bg-gray-800 dark:border-gray-700 text-black dark:text-white"
          />
        </div>
      </div>

      {/* Stats Cards */}
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">
        <div className="p-4 bg-white dark:bg-gray-700 rounded-lg shadow-md">
          <p className="text-sm text-gray-600 dark:text-gray-300">Active Employees</p>
          <h3 className="text-2xl font-semibold">{employees.length}</h3>
        </div>
        <div className="p-4 bg-white dark:bg-gray-700 rounded-lg shadow-md">
          <p className="text-sm text-gray-600 dark:text-gray-300">Total Tasks</p>
          <h3 className="text-2xl font-semibold">{tasks.length}</h3>
        </div>
        <div className="p-4 bg-white dark:bg-gray-700 rounded-lg shadow-md">
          <p className="text-sm text-gray-600 dark:text-gray-300">Completed</p>
          <h3 className="text-2xl font-semibold">{tasks.filter((t) => t.status === "COMPLETED").length}</h3>
        </div>
        <div className="p-4 bg-white dark:bg-gray-700 rounded-lg shadow-md">
          <p className="text-sm text-gray-600 dark:text-gray-300">Progress</p>
          <div className="h-2 bg-gray-200 dark:bg-gray-700 rounded mt-2">
            <div className="h-2 bg-blue-600 dark:bg-blue-400 rounded" style={{ width: `${progress}%` }} />
          </div>
          <p className="text-xs mt-2">{progress}% completed</p>
        </div>
      </div>

      {/* Task Management */}
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        {/* Task Lists */}
        <div className="lg:col-span-2">
          <div className="flex gap-2 mb-4">
            {["Active", "Pending", "Reviewed", "Completed"].map((tab) => (
              <button
                key={tab}
                onClick={() => setSelectedTab(tab)}
                className={`px-6 py-2 rounded-lg ${selectedTab === tab ? "bg-blue-700" : "bg-blue-600"} hover:bg-blue-700 transition duration-300`}
              >
                {tab}
              </button>
            ))}
          </div>

          <div className="space-y-6">
            <section>
              <h2 className="text-lg font-semibold mb-2">Yesterday</h2>
              {yesterdayTasks.length === 0 && <p className="text-sm text-gray-600 dark:text-gray-400">No tasks yesterday.</p>}
              {yesterdayTasks.map((task) => (
                <div key={task.task_id} className="p-4 bg-white dark:bg-gray-800 rounded-lg mb-3 shadow-md">
                  <div className="flex justify-between">
                    <h3 className="font-semibold text-gray-800 dark:text-white">{task.title}</h3>
                    <span className="text-xs px-2 py-1 rounded bg-gray-200 dark:bg-gray-600">{task.status}</span>
                  </div>
                  {task.description && <p className="text-sm text-gray-600 dark:text-gray-300 mt-1">{task.description}</p>}
                </div>
              ))}
            </section>

            <section>
              <h2 className="text-lg font-semibold mb-2">Today</h2>
              {tabFilteredTasks.length === 0 && <p className="text-sm text-gray-600 dark:text-gray-400">No tasks today yet.</p>}
              {tabFilteredTasks.map((task) => (
                <div key={task.task_id} className="p-4 bg-white dark:bg-gray-800 rounded-lg mb-3 shadow-md">
                  <div className="flex justify-between">
                    <h3 className="font-semibold text-gray-800 dark:text-white">{task.title}</h3>
                    <span className="text-xs px-2 py-1 rounded bg-gray-200 dark:bg-gray-600">{task.status}</span>
                  </div>
                  {task.description && <p className="text-sm text-gray-600 dark:text-gray-300 mt-1">{task.description}</p>}
                </div>
              ))}
            </section>
          </div>
        </div>

        {/* Sidebar: New Task Form */}
        <div className="lg:col-span-1">
          <div className="p-4 bg-white dark:bg-gray-700 rounded-lg shadow-md mb-6">
            <h2 className="text-lg font-bold mb-3">New Task</h2>

            {err && <div className="mb-3 text-sm text-red-600 dark:text-red-400">{err}</div>}

            <form onSubmit={handleCreate} className="space-y-4">
              <input
                type="text"
                placeholder="Task Title"
                value={form.title}
                onChange={(e) => setForm({ ...form, title: e.target.value })}
                className="w-full px-4 py-2 rounded-lg border bg-white dark:bg-gray-900 dark:border-gray-600 text-black dark:text-white"
              />

              <textarea
                placeholder="Description"
                value={form.description}
                onChange={(e) => setForm({ ...form, description: e.target.value })}
                className="w-full px-4 py-2 rounded-lg border bg-white dark:bg-gray-900 dark:border-gray-600 text-black dark:text-white"
                rows={3}
              />

              <select
                value={form.assigned_to}
                onChange={(e) => setForm({ ...form, assigned_to: e.target.value })}
                className="w-full px-4 py-2 rounded-lg border bg-white dark:bg-gray-900 dark:border-gray-600 text-black dark:text-white"
              >
                <option value="">Assign To</option>
                {employees.map((emp) => (
                  <option key={emp.id} value={emp.id}>{emp.name}</option>
                ))}
              </select>

              <select
                value={form.priority}
                onChange={(e) => setForm({ ...form, priority: e.target.value })}
                className="w-full px-4 py-2 rounded-lg border bg-white dark:bg-gray-900 dark:border-gray-600 text-black dark:text-white"
              >
                <option>Low</option>
                <option>Medium</option>
                <option>High</option>
                <option>Critical</option>
              </select>

              <button type="submit" className="w-full bg-blue-600 hover:bg-blue-700 text-white py-2 rounded-lg">
                {loading ? "Processing..." : "Create Task"}
              </button>
            </form>
          </div>
        </div>
      </div>

      {/* Toast Container for showing notifications */}
      <ToastContainer position="top-right" autoClose={3000} hideProgressBar newestOnTop closeOnClick rtl={false} pauseOnFocusLoss draggable pauseOnHover />

      {loading && <div className="mt-6 text-sm text-gray-500">Loading data...</div>}
    </div>
  );
};

export default DashboardManager;
