import React, { useEffect, useMemo, useState } from "react";
import { getTasks, createTask, updateTask } from "../services/taskService";
import { getEmployees } from "../services/employeeService";

/* -------------------- Dynamic Tailwind Helpers -------------------- */
const statusStyles = {
  TO_DO: "bg-yellow-200 text-yellow-800", // Pastel Yellow
  IN_PROGRESS: "bg-blue-200 text-blue-800", // Pastel Blue
  REVIEWED: "bg-purple-200 text-purple-800", // Pastel Purple
  COMPLETED: "bg-green-200 text-green-800", // Pastel Green
};

const priorityStyles = {
  Low: "bg-gray-300 text-gray-800", // Pastel Gray
  Medium: "bg-blue-300 text-blue-800", // Pastel Blue
  High: "bg-orange-300 text-orange-800", // Pastel Orange
  Critical: "bg-red-300 text-red-800", // Pastel Red
};

const MetricCard = ({ title, value, color }) => (
  <div
    className={`p-5 rounded-xl border shadow-lg transition-all duration-300 ease-in-out
    hover:scale-105 hover:shadow-2xl ${color}`}
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
        setEmployees((eRes || []).filter((e) => String(e.manager_id) === String(managerId)));
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

  // Small set of realistic-looking sample tasks to show when real data is empty
  const sampleTasks = [
    {
      task_id: 1001,
      title: "Implement OAuth login flow",
      description: "Add OAuth2 login with Google and Microsoft to support SSO for enterprise users.",
      priority: "High",
      status: "IN_PROGRESS",
      assigned_to: 201,
      remarks: "Manager: Please make sure to include logout and token refresh handling.",
      created_at: "2025-12-10T09:12:00Z",
      updated_at: "2025-12-15T14:30:00Z",
      expected_closure: "2025-12-22",
    },
    {
      task_id: 1002,
      title: "Prepare Q1 roadmap slides",
      description: "Collate feature updates and timelines for the Q1 stakeholder presentation.",
      priority: "Medium",
      status: "TO_DO",
      assigned_to: 202,
      remarks: "",
      created_at: "2025-12-12T11:00:00Z",
      updated_at: "2025-12-12T11:00:00Z",
      expected_closure: "2025-12-20",
    },
    {
      task_id: 1003,
      title: "Load testing for API",
      description: "Run k6 scenarios and address performance bottlenecks under 5k RPS.",
      priority: "Critical",
      status: "REVIEWED",
      assigned_to: 203,
      remarks: "Manager: Please attach the k6 report.",
      created_at: "2025-12-01T08:00:00Z",
      updated_at: "2025-12-14T16:45:00Z",
      expected_closure: "2025-12-18",
    },
    {
      task_id: 1004,
      title: "Refactor notifications service",
      description: "Split email and in-app notifications and add retry logic.",
      priority: "Low",
      status: "COMPLETED",
      assigned_to: 204,
      remarks: "Completed and verified by QA.",
      created_at: "2025-11-20T10:20:00Z",
      updated_at: "2025-12-01T12:00:00Z",
      expected_closure: "2025-12-01",
    },
  ];

  const filteredTasks = useMemo(() => {
    let data = tasks.filter((t) => t.status === tabStatusMap[activeTab]);
    if (priorityFilter) {
      data = data.filter((t) => t.priority === priorityFilter);
    }
    // if there is no real data for this tab, fall back to the sample dataset
    if (!data || data.length === 0) {
      data = sampleTasks.filter((t) => t.status === tabStatusMap[activeTab]);
      if (priorityFilter) data = data.filter((t) => t.priority === priorityFilter);
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
      // Prepare task data with updated remarks
      const updatedTask = { remarks: remark };
      await updateTask(taskId, updatedTask); // Update the task with new remark

      setRemark(""); // Clear the remark input
      setSelectedTask(null); // Clear the selected task
      setErr(""); // Clear error if successful

      // Fetch the updated tasks
      const tRes = await getTasks();
      setTasks(tRes?.data || []);
    } catch {
      setErr("Failed to update task remark.");
    }
  };

  /* -------------------- UI -------------------- */
  return (
    <div className="space-y-8 bg-gradient-to-r from-purple-100 via-indigo-100 to-pink-100 p-8 min-h-screen">
      {/* Header */}
      <div>
        <h1 className="text-3xl font-bold text-indigo-800">Good Morning, {userName}</h1>
        <p className="text-sm opacity-70">Here’s your overview for today</p>
      </div>

      {/* Metrics */}
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
        <MetricCard title="Employees" value={employees.length} color="bg-indigo-50" />
        <MetricCard title="Tasks" value={tasks.length} color="bg-blue-50" />
        <MetricCard title="Completed" value={tasks.filter((t) => t.status === "COMPLETED").length} color="bg-green-50" />
        <MetricCard title="Progress" value={`${progress}%`} color="bg-purple-50" />
      </div>

      {/* Filters */}
      <div className="flex flex-wrap gap-4 mt-4">
        {Object.keys(tabStatusMap).map((tab) => (
          <button
            key={tab}
            onClick={() => setActiveTab(tab)}
            className={`px-4 py-1.5 rounded-full text-sm transition-all duration-300 ease-in-out
              ${activeTab === tab
                ? "bg-indigo-500 text-white scale-105"
                : "bg-indigo-200 hover:bg-indigo-300"} 
            `}
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
                className="p-4 rounded-xl bg-white border shadow-md hover:shadow-lg transition duration-300 transform hover:scale-105 cursor-pointer flex gap-4"
                onClick={() => setSelectedTask(task)}
              >
                <div className="w-12 h-12 rounded-full bg-indigo-100 flex items-center justify-center text-indigo-700 font-bold">{String(task.title || 'T').charAt(0)}</div>
                <div className="flex-1">
                  <div className="flex justify-between items-start">
                    <div>
                      <h3 className="font-semibold text-lg">{task.title}</h3>
                      <p className="text-sm text-gray-600 mt-1 line-clamp-2">{task.description}</p>
                    </div>
                    <div className="text-right">
                      <div className={`px-2 py-1 text-xs rounded-full ${statusStyles[task.status]}`}>{task.status}</div>
                      <div className="text-xs text-gray-500 mt-1">Due: {task.expected_closure || '—'}</div>
                    </div>
                  </div>

                  <div className="mt-3 flex items-center justify-between">
                    <div className="flex items-center gap-2">
                      <span className={`px-2 py-1 text-xs rounded-full ${priorityStyles[task.priority]}`}>{task.priority}</span>
                      <div className="text-xs text-gray-500">Assignee: <strong className="ml-1 text-gray-700">{task.assigned_to}</strong></div>
                    </div>
                    <div className="text-sm text-gray-500">Updated: {task.updated_at ? new Date(task.updated_at).toLocaleDateString() : ''}</div>
                  </div>
                </div>
              </div>
            ))}
          </div>
        </div>

        {/* RIGHT SIDE (TASK DETAIL & REMARKS) */}
        {selectedTask && (
          <div
            className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50"
            onClick={() => setSelectedTask(null)} // Close the modal on background click
          >
            <div
              className="relative p-6 bg-white rounded-lg shadow-lg transition-all duration-300 transform scale-100 hover:scale-105"
              onClick={(e) => e.stopPropagation()} // Prevent click event from propagating to the background
            >
              <h3 className="text-lg font-bold">{selectedTask.title}</h3>
              <p className="text-sm opacity-70">{selectedTask.description}</p>
              <p className="mt-2 text-sm">Assigned To: {selectedTask.assigned_to}</p>
              <p className="mt-2 text-sm">Priority: {selectedTask.priority}</p>
              <p className="mt-2 text-sm">Status: {selectedTask.status}</p>
              <p className="mt-2 text-sm">Remarks: {selectedTask.remarks}</p>

              <textarea
                className="w-full mt-4 p-2 border rounded"
                value={remark}
                onChange={(e) => setRemark(e.target.value)}
                placeholder="Add remark..."
              />
              <button
                className="mt-4 bg-indigo-500 text-white p-2 rounded"
                onClick={() => handleRemarkUpdate(selectedTask.task_id)}
              >
                Update Remark
              </button>
            </div>
          </div>
        )}
      </div>

      {/* Charts: Status line chart (7 days) + Priority count bar chart */}
      <div className="bg-white p-6 rounded-lg shadow-md">
        <h3 className="text-lg font-semibold mb-4">Task analytics</h3>

        {/* prepare chart data client-side */}
        {/* compute last 7 days labels and counts per status */}
        <Charts tasks={tasks.length ? tasks : sampleTasks} />
      </div>

      {loading && <p className="opacity-60">Loading...</p>}
    </div>
  );
};

export default DashboardManager;

/* -------------------- Charts Component (inline, dependency-free SVG) -------------------- */
function Charts({ tasks }) {
  // Ensure we have tasks array
  const data = Array.isArray(tasks) ? tasks : [];

  // helper: normalize status keys used across app
  const normalizeStatus = (s) => {
    if (!s) return 'TO_DO';
    if (s === 'REVIEWED') return 'REVIEW';
    return s;
  };

  // last 7 days labels (dates at midnight)
  const days = Array.from({ length: 7 }).map((_, i) => {
    const d = new Date();
    d.setHours(0,0,0,0);
    d.setDate(d.getDate() - (6 - i));
    return d;
  });

  const dayLabels = days.map(d => `${d.getMonth()+1}/${d.getDate()}`);

  // statuses to plot (consistent order)
  const statuses = ['TO_DO', 'IN_PROGRESS', 'REVIEW', 'COMPLETED'];
  const statusColors = {
    TO_DO: '#5E6C84',
    IN_PROGRESS: '#FFAB00',
    REVIEW: '#2684FF',
    COMPLETED: '#36B37E'
  };

  // build snapshot counts per day per status (approximation)
  // Since we don't have full history of status transitions, approximate by assuming
  // the task's current status began at its `updated_at` (or `created_at` if no update)
  // and persisted thereafter. For each day in the window, we count the task in its
  // current status if the status-start-date is on-or-before that day.
  const countsByStatus = {};
  statuses.forEach(s => countsByStatus[s] = Array(days.length).fill(0));

  data.forEach(task => {
    const status = normalizeStatus(task.status);
    const startStr = task.updated_at || task.created_at || new Date().toISOString();
    const start = new Date(startStr);
    start.setHours(0,0,0,0);

    // for each day, if the task's status-start is <= day, include it in that day's snapshot
    days.forEach((d, idx) => {
      if (start.getTime() <= d.getTime()) {
        if (!countsByStatus[status]) countsByStatus[status] = Array(days.length).fill(0);
        countsByStatus[status][idx] += 1;
      }
    });
  });

  // compute priority counts for bar chart
  const priorities = ['Low','Medium','High','Critical'];
  const priorityCounts = priorities.reduce((acc,p) => { acc[p]=0; return acc; }, {});
  data.forEach(t => {
    const p = t.priority || 'Low';
    const key = Object.keys(priorityCounts).find(k => k.toLowerCase() === String(p).toLowerCase()) || 'Low';
    priorityCounts[key] = (priorityCounts[key] || 0) + 1;
  });

  // Small chart rendering helpers
  // PieChart (donut) for snapshot distribution (latest day)
  const PieChart = ({ width=420, height=260 }) => {
    const cx = width / 2 - 20;
    const cy = height / 2 - 10;
    const outerR = Math.min(width, height) * 0.28;
    const innerR = outerR * 0.56; // donut thickness

    const lastIdx = days.length - 1;
    const values = statuses.map(s => (countsByStatus[s] && countsByStatus[s][lastIdx]) || 0);
    const total = values.reduce((a,b) => a + b, 0) || 1;

    // polar helpers
    const polar = (angle, r) => {
      const rad = (angle - 90) * Math.PI / 180; // start at top
      return { x: cx + r * Math.cos(rad), y: cy + r * Math.sin(rad) };
    };

    let angleStart = 0;

    return (
      <svg width="100%" viewBox={`0 0 ${width} ${height}`} preserveAspectRatio="xMidYMid meet">
        <defs>
          <filter id="softShadow" x="-20%" y="-20%" width="140%" height="140%">
            <feDropShadow dx="0" dy="2" stdDeviation="6" floodOpacity="0.12"/>
          </filter>
        </defs>

        <title>Task status distribution (approximate snapshot)</title>

        {/* slices (donut segments) */}
        {values.map((v, i) => {
          const share = v / total;
          const angle = share * 360;
          const start = angleStart;
          const end = angleStart + angle;
          const p1 = polar(start, outerR);
          const p2 = polar(end, outerR);
          const p3 = polar(end, innerR);
          const p4 = polar(start, innerR);
          const large = angle > 180 ? 1 : 0;

          // donut path: outer arc, line to inner arc end, inner arc back, close
          const d = `M ${p1.x} ${p1.y} A ${outerR} ${outerR} 0 ${large} 1 ${p2.x} ${p2.y} L ${p3.x} ${p3.y} A ${innerR} ${innerR} 0 ${large} 0 ${p4.x} ${p4.y} Z`;
          const midAngle = start + angle / 2;
          const labelPos = polar(midAngle, (outerR + innerR) / 2);

          angleStart += angle;
          return (
            <g key={statuses[i]} filter="url(#softShadow)">
              <path d={d} fill={statusColors[statuses[i]]} stroke="#fff" strokeWidth={1} />
              {share > 0.03 && (
                <text x={labelPos.x} y={labelPos.y} fontSize={11} textAnchor="middle" fill="#06202A" fontWeight={600}>{`${Math.round(share*100)}%`}</text>
              )}
              <title>{`${statuses[i].replace('_',' ')}: ${v} (${Math.round(share*100)}%)`}</title>
            </g>
          );
        })}

        {/* center label */}
        <circle cx={cx} cy={cy} r={innerR - 6} fill="#ffffff" />
        <text x={cx} y={cy-6} fontSize={12} fontWeight={700} textAnchor="middle" fill="#0f172a">{total}</text>
        <text x={cx} y={cy+12} fontSize={11} textAnchor="middle" fill="#94A3B8">tasks</text>

        {/* legend to the right with nicer layout */}
        {statuses.map((s, i) => {
          const lx = width - 150;
          const ly = 30 + i*28;
          const v = values[i];
          return (
            <g key={s}>
              <rect x={lx} y={ly-10} width={14} height={12} rx={4} fill={statusColors[s]} />
              <text x={lx+20} y={ly} fontSize={12} fill="#334155">{s.replace('_',' ')} <tspan className="text-gray-500">({v})</tspan></text>
            </g>
          );
        })}
      </svg>
    );
  };

  const BarChart = ({ width=420, height=260 }) => {
    const padding = 36;
    const innerW = width - padding*2;
    const innerH = height - padding*2;
    const categories = Object.keys(priorityCounts);
    const maxVal = Math.max(1, ...Object.values(priorityCounts));
    const barW = innerW / categories.length * 0.5;

    const colors = { Low:'#36B37E', Medium:'#FFAB00', High:'#FF7A7A', Critical:'#AE0E0E' };

    // y ticks
    const ticks = 4;

    return (
      <svg width="100%" viewBox={`0 0 ${width} ${height}`} preserveAspectRatio="xMidYMid meet">
        <defs>
          <linearGradient id="gLow" x1="0" x2="0" y1="0" y2="1"><stop offset="0%" stopColor="#4ADE80" stopOpacity="1"/><stop offset="100%" stopColor="#16A34A" stopOpacity="0.9"/></linearGradient>
          <linearGradient id="gMed" x1="0" x2="0" y1="0" y2="1"><stop offset="0%" stopColor="#FFD27A" stopOpacity="1"/><stop offset="100%" stopColor="#FFAB00" stopOpacity="0.9"/></linearGradient>
          <linearGradient id="gHigh" x1="0" x2="0" y1="0" y2="1"><stop offset="0%" stopColor="#FF9B9B" stopOpacity="1"/><stop offset="100%" stopColor="#FF7A7A" stopOpacity="0.9"/></linearGradient>
          <linearGradient id="gCrit" x1="0" x2="0" y1="0" y2="1"><stop offset="0%" stopColor="#F87171" stopOpacity="1"/><stop offset="100%" stopColor="#AE0E0E" stopOpacity="0.95"/></linearGradient>
        </defs>

        {/* y grid and labels */}
        {Array.from({length: ticks+1}).map((_,i)=>{
          const val = Math.round((maxVal / ticks) * i);
          const y = padding + innerH - (innerH * (i / ticks));
          return (
            <g key={i}>
              <line x1={padding} x2={width-padding} y1={y} y2={y} stroke="#F1F5F9" />
              <text x={padding-8} y={y+4} fontSize={11} fill="#94A3B8" textAnchor="end">{val}</text>
            </g>
          );
        })}

        {/* bars */}
        {categories.map((cat, i) => {
          const x = padding + (i * (innerW / categories.length)) + ((innerW / categories.length - barW)/2);
          const h = (priorityCounts[cat] / Math.max(1, maxVal)) * innerH;
          const y = padding + (innerH - h);
          const gid = cat === 'Low' ? 'gLow' : cat === 'Medium' ? 'gMed' : cat === 'High' ? 'gHigh' : 'gCrit';
          return (
            <g key={cat}>
              <rect x={x} y={y} width={barW} height={h} rx={8} fill={`url(#${gid})`}>
                <title>{`${cat}: ${priorityCounts[cat]}`}</title>
              </rect>
              <text x={x + barW/2} y={y - 8} fontSize={12} fill="#0f172a" textAnchor="middle" fontWeight={700}>{priorityCounts[cat]}</text>
              <text x={x + barW/2} y={height - 10} fontSize={12} fill="#334155" textAnchor="middle">{cat}</text>
            </g>
          );
        })}
      </svg>
    );
  };

  return (
    <div className="flex flex-col lg:flex-row gap-6">
      <div className="flex-1 bg-white p-3 rounded shadow-sm">
        <h4 className="text-sm font-medium text-gray-700 mb-2">Task status distribution (snapshot)</h4>
        <div className="w-full overflow-hidden">
          <PieChart />
        </div>
      </div>

      <div className="w-[420px] bg-white p-3 rounded shadow-sm">
        <h4 className="text-sm font-medium text-gray-700 mb-2">Priority counts</h4>
        <div className="w-full overflow-hidden">
          <BarChart />
        </div>
      </div>
    </div>
  );
}
