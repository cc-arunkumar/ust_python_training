import React, { useEffect, useMemo, useState } from "react";
import {
  PieChart,
  Pie,
  Cell,
  Tooltip,
  ResponsiveContainer,
  BarChart,
  Bar,
  XAxis,
  YAxis,
  CartesianGrid,
  Legend,
} from "recharts";

import { getTasks } from "../services/taskService";
import { getEmployees } from "../services/employeeService";

/* -------------------- Colors -------------------- */
const STATUS_COLORS = {
  TO_DO: "#F6C177",
  IN_PROGRESS: "#7DA9E3",
  REVIEWED: "#C3AED6",
  COMPLETED: "#8ED1B2",
};

/* -------------------- Metric Card -------------------- */
const MetricCard = ({ title, value, color }) => (
  <div
    className={`p-5 rounded-xl shadow-md transition hover:scale-[1.03] ${color}`}
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
  const [activeTab, setActiveTab] = useState("TO_DO");
  const [loading, setLoading] = useState(true);

  /* -------------------- Load Data -------------------- */
  useEffect(() => {
    const loadData = async () => {
      setLoading(true);
      const tRes = await getTasks();
      const eRes = await getEmployees();

      setTasks(tRes?.data || []);
      setEmployees(
        (eRes || []).filter(
          (e) => String(e.manager_id) === String(managerId)
        )
      );
      setLoading(false);
    };

    loadData();
  }, [managerId]);

  /* -------------------- Derived Data -------------------- */

  const filteredTasks = useMemo(
    () => tasks.filter((t) => t.status === activeTab),
    [tasks, activeTab]
  );

  const taskStatusData = useMemo(() => {
    const map = { TO_DO: 0, IN_PROGRESS: 0, REVIEWED: 0, COMPLETED: 0 };
    tasks.forEach((t) => map[t.status]++);
    return Object.keys(map).map((k) => ({ name: k, value: map[k] }));
  }, [tasks]);

  const completedByEmployee = useMemo(() => {
    const map = {};
    employees.forEach((e) => {
      map[e.id] = { name: e.name, completed: 0 };
    });
    tasks.forEach((t) => {
      if (t.status === "COMPLETED" && map[t.assigned_to]) {
        map[t.assigned_to].completed++;
      }
    });
    return Object.values(map);
  }, [tasks, employees]);

  /* -------------------- UI -------------------- */
  return (
    <div className="space-y-10">
      {/* Header */}
      <div>
        <h1 className="text-3xl font-bold text-[#2A4D69]">
          Welcome back, {userName}
        </h1>
        <p className="text-sm opacity-70">
          Overview of your team & tasks
        </p>
      </div>

      {/* Metrics */}
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
        <MetricCard title="Employees" value={employees.length} color="bg-indigo-200" />
        <MetricCard title="Total Tasks" value={tasks.length} color="bg-blue-200" />
        <MetricCard
          title="Completed"
          value={tasks.filter((t) => t.status === "COMPLETED").length}
          color="bg-green-200"
        />
        <MetricCard
          title="In Progress"
          value={tasks.filter((t) => t.status === "IN_PROGRESS").length}
          color="bg-yellow-200"
        />
      </div>

      {/* Tabs */}
      <div className="flex gap-3 flex-wrap">
        {["TO_DO", "IN_PROGRESS", "REVIEWED", "COMPLETED"].map((tab) => (
          <button
            key={tab}
            onClick={() => setActiveTab(tab)}
            className={`px-4 py-1.5 rounded-full text-sm transition ${
              activeTab === tab
                ? "bg-blue-600 text-white"
                : "bg-gray-200 hover:bg-gray-300"
            }`}
          >
            {tab.replace("_", " ")}
          </button>
        ))}
      </div>

      {/* Main Content */}
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
        {/* Tasks */}
        <div className="lg:col-span-2 space-y-4">
          {filteredTasks.map((task) => (
            <div
              key={task.task_id}
              className="p-4 bg-white rounded-xl shadow hover:shadow-lg transition"
            >
              <div className="flex justify-between">
                <div>
                  <h3 className="font-semibold">{task.title}</h3>
                  <p className="text-sm opacity-70">{task.description}</p>
                </div>
                <span
                  className="px-3 py-1 text-xs rounded-full"
                  style={{
                    backgroundColor: STATUS_COLORS[task.status],
                  }}
                >
                  {task.status}
                </span>
              </div>
            </div>
          ))}
        </div>

        {/* Employees */}
        <div className="bg-white rounded-xl shadow p-5">
          <h2 className="font-bold mb-4">Employees Under Me</h2>
          <ul className="space-y-2">
            {employees.map((e) => (
              <li
                key={e.id}
                className="flex justify-between items-center p-3 rounded-lg bg-gray-50"
              >
                <div>
                  <p className="font-medium">{e.name}</p>
                  <p className="text-xs opacity-60">{e.role || "Employee"}</p>
                </div>
                <span className="text-xs px-2 py-1 rounded-full bg-green-200 text-green-700">
                  Active
                </span>
              </li>
            ))}
          </ul>
        </div>
      </div>

      {/* -------------------- GRAPHS -------------------- */}
      <div className="space-y-6">
        <h2 className="text-2xl font-bold text-[#2A4D69]">
          Task Analytics
        </h2>

        <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
          {/* Pie */}
          <div className="bg-white p-5 rounded-xl shadow">
            <h3 className="font-semibold mb-4">Tasks by Status</h3>
            <ResponsiveContainer width="100%" height={300}>
              <PieChart>
                <Pie data={taskStatusData} dataKey="value" label>
                  {taskStatusData.map((d) => (
                    <Cell key={d.name} fill={STATUS_COLORS[d.name]} />
                  ))}
                </Pie>
                <Tooltip />
              </PieChart>
            </ResponsiveContainer>
          </div>

          {/* Bar */}
          <div className="bg-white p-5 rounded-xl shadow">
            <h3 className="font-semibold mb-4">
              Completed Tasks per Employee
            </h3>
            <ResponsiveContainer width="100%" height={300}>
              <BarChart data={completedByEmployee}>
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="name" />
                <YAxis allowDecimals={false} />
                <Tooltip />
                <Legend />
                <Bar dataKey="completed" fill="#8ED1B2" radius={[6, 6, 0, 0]} />
              </BarChart>
            </ResponsiveContainer>
          </div>
        </div>
      </div>

      {loading && <p className="opacity-60">Loading...</p>}
    </div>
  );
};

export default DashboardManager;
