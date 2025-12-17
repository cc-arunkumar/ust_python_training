import { useEffect, useState } from "react";
import { getUser } from "../api/users";
import { health } from "../api/utils";
import { Line, Bar } from "react-chartjs-2";
import {
  Chart as ChartJS,
  LineElement,
  PointElement,
  CategoryScale,
  LinearScale,
  Tooltip,
  Legend,
  Filler,
  BarElement,
} from "chart.js";

ChartJS.register(
  LineElement,
  PointElement,
  CategoryScale,
  LinearScale,
  Tooltip,
  Legend,
  Filler,
  BarElement
);

export default function Dashboard() {
  const [user, setUser] = useState(null);
  const [healthInfo, setHealthInfo] = useState(null);

  useEffect(() => {
    const token = localStorage.getItem("token");
    if (!token) return;

    const payload = JSON.parse(atob(token.split(".")[1]));
    const userId = payload.user_id;

    getUser(userId).then(setUser).catch(() => setUser(null));
    health().then(setHealthInfo).catch(() => setHealthInfo(null));
  }, []);

  // Line chart: task trends
  const taskTrendData = {
    labels: ["Week 1", "Week 2", "Week 3", "Week 4"],
    datasets: [
      {
        label: "TO_DO",
        data: [5, 4, 6, 3],
        borderColor: "#3b82f6",
        backgroundColor: "rgba(147, 197, 253, 0.4)",
        fill: true,
        tension: 0.4,
      },
      {
        label: "IN_PROGRESS",
        data: [2, 5, 3, 4],
        borderColor: "#facc15",
        backgroundColor: "rgba(253, 230, 138, 0.4)",
        fill: true,
        tension: 0.4,
      },
      {
        label: "REVIEW",
        data: [1, 2, 3, 2],
        borderColor: "#a855f7",
        backgroundColor: "rgba(216, 180, 252, 0.4)",
        fill: true,
        tension: 0.4,
      },
      {
        label: "DONE",
        data: [3, 6, 8, 10],
        borderColor: "#22c55e",
        backgroundColor: "rgba(134, 239, 172, 0.4)",
        fill: true,
        tension: 0.4,
      },
    ],
  };

  // Bar chart: task distribution by priority
const taskPriorityData = {
  labels: ["HIGH", "MEDIUM", "LOW"],
  datasets: [
    {
      label: "Tasks by Priority",
      data: [7, 12, 5],
      backgroundColor: [
        "rgba(239, 68, 68, 0.7)",   // red with opacity
        "rgba(250, 204, 21, 0.7)",  // yellow with opacity
        "rgba(34, 197, 94, 0.7)",   // green with opacity
      ],
      borderColor: ["#ef4444", "#facc15", "#22c55e"],
      borderWidth: 1,
      borderRadius: 6,   // rounded bars
      barThickness: 40,  // consistent width
    },
  ],
};

const taskPriorityOptions = {
  responsive: true,
  plugins: {
    legend: {
      display: false, // hide legend since labels are obvious
    },
    tooltip: {
      enabled: true,
      callbacks: {
        label: (context) => `${context.label}: ${context.raw} tasks`,
      },
    },
  },
  scales: {
    x: {
      ticks: {
        color: "#374151", // gray-700
        font: { weight: "bold" },
      },
      grid: { display: false },
    },
    y: {
      beginAtZero: true,
      ticks: {
        stepSize: 2,
        color: "#374151",
      },
      grid: { color: "rgba(209, 213, 219, 0.3)" }, // subtle grid
    },
  },
};

  return (
    <div className="p-6 space-y-6 text-gray-800 dark:text-gray-200">
      <h1 className="text-2xl font-bold">Dashboard</h1>
      {user && (
        <>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
            {/* Welcome card */}
            <div className="bg-white dark:bg-gray-800 p-4 rounded-lg shadow border border-gray-200 dark:border-gray-700 transition transform hover:scale-[1.02] hover:bg-pink-50 dark:hover:bg-pink-900/30">
              <p className="text-gray-700 dark:text-gray-200">
                <span className="font-medium">Welcome:</span>{" "}
                {user.employee?.name || `User #${user.user_id}`}
              </p>
              <p className="text-gray-600 dark:text-gray-400">
                <span className="font-medium">Role:</span> {user.role}
              </p>
              <p className="text-gray-600 dark:text-gray-400">
                <span className="font-medium">Status:</span> {user.status}
              </p>
            </div>

            {/* Backend health card */}
            <div className="bg-white dark:bg-gray-800 p-4 rounded-lg shadow border border-gray-200 dark:border-gray-700 transition transform hover:scale-[1.02] hover:bg-blue-50 dark:hover:bg-blue-900/30">
              <p className="text-gray-700 dark:text-gray-200">
                <span className="font-medium">Backend:</span>{" "}
                {healthInfo?.message || "Checking..."}
              </p>
              <p className="text-gray-600 dark:text-gray-400">
                <span className="font-medium">Service:</span>{" "}
                {healthInfo?.status || "unknown"}
              </p>
            </div>

            {/* Quick actions card */}
            <div className="bg-white dark:bg-gray-800 p-4 rounded-lg shadow border border-gray-200 dark:border-gray-700 transition transform hover:scale-[1.02] hover:bg-green-50 dark:hover:bg-green-900/30">
              <p className="text-gray-700 dark:text-gray-200">
                <span className="font-medium">Quick actions:</span>
              </p>
              <ul className="text-sm text-blue-600 dark:text-blue-400 space-y-1 mt-2">
                <li>
                  <a href="/tasks" className="hover:underline">
                    View tasks
                  </a>
                </li>
                {user?.role !== "EMPLOYEE" && (
                  <li>
                    <a href="/users" className="hover:underline">
                      Manage users
                    </a>
                  </li>
                )}
              </ul>
            </div>
          </div>

          {/* Task trend line chart */}
          <div className="bg-white dark:bg-gray-800 p-6 rounded-lg shadow border border-gray-200 dark:border-gray-700">
            <h2 className="text-lg font-semibold mb-4">Task Trends</h2>
            <Line data={taskTrendData} />
          </div>

          {/* Task priority bar chart */}
          <div className="bg-white dark:bg-gray-800 p-6 rounded-lg shadow border border-gray-200 dark:border-gray-700">
            <h2 className="text-lg font-semibold mb-4">Task Priorities</h2>
            <Bar data={taskPriorityData} options={taskPriorityOptions} />
          </div>
        </>
      )}
      {!user && (
        <p className="text-gray-500 dark:text-gray-400">Loading user info...</p>
      )}
    </div>
  );
}
