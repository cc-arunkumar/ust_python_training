import React, { useEffect, useMemo, useState } from "react";
import {
  getTasks,
  createTask,
  updateTask,
} from "../services/taskService";
import { getEmployees } from "../services/employeeService";

/* -------------------- Styles -------------------- */
const statusStyles = {
  TO_DO: "bg-yellow-200 text-yellow-800",
  IN_PROGRESS: "bg-blue-200 text-blue-800",
  REVIEWED: "bg-purple-200 text-purple-800",
  COMPLETED: "bg-green-200 text-green-800",
};

const priorityStyles = {
  Low: "bg-gray-300 text-gray-700",
  Medium: "bg-blue-300 text-blue-800",
  High: "bg-orange-300 text-orange-800",
  Critical: "bg-red-300 text-red-800",
};

const MetricCard = ({ title, value, color }) => (
  <div
    className={`p-5 rounded-xl border shadow-md transition-all duration-300 hover:scale-[1.02] hover:shadow-lg ${color}`}
  >
    <p className="text-sm opacity-70">{title}</p>
    <h3 className="text-3xl font-bold mt-1">{value}</h3>
  </div>
);

/* -------------------- Typing Header -------------------- */
const TypingHeader = ({ userName }) => {
  const messages = [
    `Good Morning, ${userName}`,
    "Welcome to your dashboard",
  ];
  const [text, setText] = useState("");
  const [msgIndex, setMsgIndex] = useState(0);
  const [charIndex, setCharIndex] = useState(0);
  const [deleting, setDeleting] = useState(false);

  useEffect(() => {
    const current = messages[msgIndex];
    let timer;

    if (!deleting) {
      if (charIndex < current.length) {
        timer = setTimeout(() => {
          setText(current.slice(0, charIndex + 1));
          setCharIndex((c) => c + 1);
        }, 100);
      } else {
        timer = setTimeout(() => setDeleting(true), 800);
      }
    } else {
      if (charIndex > 0) {
        timer = setTimeout(() => {
          setText(current.slice(0, charIndex - 1));
          setCharIndex((c) => c - 1);
        }, 50);
      } else {
        setDeleting(false);
        setMsgIndex((i) => (i + 1) % messages.length);
      }
    }

    return () => clearTimeout(timer);
  }, [charIndex, deleting, msgIndex, messages]);

  return (
    <span>
      {text}
      <span className="ml-1 animate-pulse">|</span>
    </span>
  );
};

/* -------------------- Dashboard -------------------- */
const DashboardManager = () => {
  const managerId = localStorage.getItem("emp_id");
  const userName = localStorage.getItem("user_name") || "Manager";

  const [tasks, setTasks] = useState([]);
  const [employees, setEmployees] = useState([]);
  const [activeTab, setActiveTab] = useState("Active");
  const [priorityFilter, setPriorityFilter] = useState("");
  const [selectedTask, setSelectedTask] = useState(null);
  const [remark, setRemark] = useState("");
  const [loading, setLoading] = useState(true);
  const [err, setErr] = useState("");

  const tabStatusMap = {
    Active: "IN_PROGRESS",
    Pending: "TO_DO",
    Reviewed: "REVIEWED",
    Completed: "COMPLETED",
  };

  /* -------------------- Load Data -------------------- */
  useEffect(() => {
    const load = async () => {
      try {
        setLoading(true);
        const tRes = await getTasks();
        const eRes = await getEmployees();
        setTasks(tRes?.data || []);
        setEmployees(
          (eRes || []).filter(
            (e) => String(e.manager_id) === String(managerId)
          )
        );
      } catch {
        setErr("Failed to load dashboard data");
      } finally {
        setLoading(false);
      }
    };
    load();
  }, [managerId]);

  /* -------------------- Derived -------------------- */
  const progress = useMemo(() => {
    if (!tasks.length) return 0;
    return Math.round(
      (tasks.filter((t) => t.status === "COMPLETED").length /
        tasks.length) *
        100
    );
  }, [tasks]);

  const filteredTasks = useMemo(() => {
    let data = tasks.filter(
      (t) => t.status === tabStatusMap[activeTab]
    );
    if (priorityFilter) {
      data = data.filter((t) => t.priority === priorityFilter);
    }
    return data;
  }, [tasks, activeTab, priorityFilter]);

  /* -------------------- Remarks -------------------- */
  const handleRemarkUpdate = async (taskId) => {
    if (!remark) return;
    const role = localStorage.getItem("role") || "Manager";
    const payload = {
      remarks: JSON.stringify({
        sender: role,
        text: remark,
        ts: new Date().toISOString(),
      }),
      updated_by: role === "Manager" ? null : managerId,
    };
    await updateTask(taskId, payload);
    const tRes = await getTasks();
    setTasks(tRes?.data || []);
    setRemark("");
    setSelectedTask(null);
  };

  /* -------------------- UI -------------------- */
  return (
    <div className="space-y-8">
      <h1 className="text-3xl font-bold">
        <TypingHeader userName={userName} />
      </h1>

      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
        <MetricCard
          title="Employees"
          value={employees.length}
          color="bg-indigo-200"
        />
        <MetricCard
          title="Tasks"
          value={tasks.length}
          color="bg-blue-200"
        />
        <MetricCard
          title="Completed"
          value={
            tasks.filter((t) => t.status === "COMPLETED").length
          }
          color="bg-green-200"
        />
        <MetricCard
          title="Progress"
          value={`${progress}%`}
          color="bg-purple-200"
        />
      </div>

      <div className="flex gap-3 flex-wrap">
        {Object.keys(tabStatusMap).map((tab) => (
          <button
            key={tab}
            onClick={() => setActiveTab(tab)}
            className={`px-4 py-1.5 rounded-full ${
              activeTab === tab
                ? "bg-blue-600 text-white"
                : "bg-gray-200"
            }`}
          >
            {tab}
          </button>
        ))}
        <select
          value={priorityFilter}
          onChange={(e) => setPriorityFilter(e.target.value)}
          className="px-3 py-1.5 rounded-lg border"
        >
          <option value="">All Priorities</option>
          <option value="Critical">Critical</option>
          <option value="High">High</option>
          <option value="Medium">Medium</option>
          <option value="Low">Low</option>
        </select>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
        <div className="lg:col-span-2 space-y-4">
          {filteredTasks.map((task) => (
            <div
              key={task.task_id}
              className="p-4 bg-white border rounded-xl shadow cursor-pointer"
              onClick={() =>
                setSelectedTask(
                  selectedTask?.task_id === task.task_id
                    ? null
                    : task
                )
              }
            >
              <div className="flex justify-between">
                <div>
                  <h3 className="font-semibold">{task.title}</h3>
                  <p className="text-sm opacity-70">
                    {task.description}
                  </p>
                </div>
                <span
                  className={`px-2 py-1 text-xs rounded-full ${statusStyles[task.status]}`}
                >
                  {task.status}
                </span>
              </div>

              <div className="mt-2">
                <span
                  className={`px-2 py-1 text-xs rounded-full ${priorityStyles[task.priority]}`}
                >
                  {task.priority}
                </span>
              </div>

              {selectedTask?.task_id === task.task_id && (
                <div className="mt-3 border-t pt-3">
                  <textarea
                    className="w-full p-2 border rounded"
                    value={remark}
                    onChange={(e) => setRemark(e.target.value)}
                    placeholder="Add remark"
                  />
                  <button
                    className="mt-2 bg-blue-600 text-white px-4 py-1.5 rounded"
                    onClick={() =>
                      handleRemarkUpdate(task.task_id)
                    }
                  >
                    Add Remark
                  </button>
                </div>
              )}
            </div>
          ))}
        </div>

        <div className="bg-white border rounded-xl shadow p-5">
          <h2 className="font-bold mb-4">Employees Under Me</h2>
          <ul className="space-y-2">
            {employees.map((e) => (
              <li
                key={e.id}
                className="flex justify-between p-3 bg-gray-50 rounded"
              >
                <div>
                  <p className="font-medium">{e.name}</p>
                  <p className="text-xs opacity-60">
                    {e.role || "Employee"}
                  </p>
                </div>
                <span className="text-xs px-2 py-1 rounded-full bg-green-200 text-green-700">
                  Active
                </span>
              </li>
            ))}
          </ul>
        </div>
      </div>

      {loading && <p>Loading...</p>}
      {err && <p className="text-red-600">{err}</p>}
    </div>
  );
};

export default DashboardManager;
