import { useEffect, useState, useMemo } from "react";
import { getUser } from "../api/users";
import { health } from "../api/utils";
import { listTasks } from "../api/tasks";

export default function Dashboard() {
  const [user, setUser] = useState(null);
  const [healthInfo, setHealthInfo] = useState(null);
  const [tasks, setTasks] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const token = localStorage.getItem("token");
    if (!token) {
      setLoading(false);
      return;
    }

    let payload;
    try {
      payload = JSON.parse(atob(token.split(".")[1]));
    } catch (e) {
      console.error("Invalid token", e);
      setLoading(false);
      return;
    }

    const userId = payload.user_id;

    Promise.all([
      getUser(userId)
        .then(setUser)
        .catch(() => setUser(null)),
      health()
        .then(setHealthInfo)
        .catch(() => setHealthInfo(null)),
      listTasks()
        .then(setTasks)
        .catch(() => setTasks([])),
    ]).finally(() => setLoading(false));
  }, []);

  const visibleTasks = useMemo(() => {
    if (!user) return [];
    return user.role === "EMPLOYEE"
      ? tasks.filter((t) => t.assigned_to === user.emp_id)
      : tasks;
  }, [tasks, user]);
  console.log(visibleTasks);
  const statusCounts = useMemo(() => {
    return {
      TO_DO: visibleTasks.filter((t) => t.status === "TO_DO").length,
      IN_PROGRESS: visibleTasks.filter((t) => t.status === "IN_PROGRESS")
        .length,
      REVIEW: visibleTasks.filter((t) => t.status === "REVIEW").length,
      DONE: visibleTasks.filter((t) => t.status === "DONE").length,
    };
  }, [visibleTasks]);

  if (loading) {
    return (
      <div className="flex justify-center items-center h-full">
        <p className="text-gray-500 text-lg animate-pulse">
          Loading dashboard...
        </p>
      </div>
    );
  }

  return (
    <div className="p-6 space-y-6 text-gray-800 dark:text-gray-200">
      <h1 className="text-3xl font-extrabold tracking-wide text-transparent bg-clip-text bg-gradient-to-r from-cyan-400 to-blue-500">
        Dashboard
      </h1>
      <p className="text-gray-500">
        Here's what's happening with your tasks today
      </p>

      {user && (
        <>
          {/* Task summary boxes */}
          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6 mt-6">
            {/* Big card spanning all 3 columns */}
            <div className="lg:col-span-3 bg-gradient-to-r from-cyan-500 to-blue-600 rounded-xl shadow-lg p-8 text-center transform hover:scale-105 transition duration-300">
              <h3 className="text-2xl font-semibold text-white">Overview</h3>
              <p className="text-5xl font-extrabold text-white">
                {visibleTasks.length} Tasks
              </p>
              <p className="mt-2 text-gray-200">
                Summary of all tasks assigned
              </p>
            </div>

            {/* Smaller cards */}
            <div className="bg-gradient-to-r from-yellow-400 to-orange-500 rounded-xl shadow-lg p-6 text-center transform hover:scale-105 transition duration-300">
              <h3 className="text-lg font-semibold text-white">To Do</h3>
              <p className="text-4xl font-extrabold text-white">
                {statusCounts.TO_DO}
              </p>
            </div>

            <div className="bg-gradient-to-r from-purple-500 to-pink-600 rounded-xl shadow-lg p-6 text-center transform hover:scale-105 transition duration-300">
              <h3 className="text-lg font-semibold text-white">In Progress</h3>
              <p className="text-4xl font-extrabold text-white">
                {statusCounts.IN_PROGRESS}
              </p>
            </div>

            <div className="bg-gradient-to-r from-pink-500 to-rose-600 rounded-xl shadow-lg p-6 text-center transform hover:scale-105 transition duration-300">
              <h3 className="text-lg font-semibold text-white">Review</h3>
              <p className="text-4xl font-extrabold text-white">
                {statusCounts.REVIEW}
              </p>
            </div>

            <div className="bg-gradient-to-r from-green-500 to-emerald-600 rounded-xl shadow-lg p-6 text-center transform hover:scale-105 transition duration-300">
              <h3 className="text-lg font-semibold text-white">Done</h3>
              <p className="text-4xl font-extrabold text-white">
                {statusCounts.DONE}
              </p>
            </div>
          </div>
        </>
      )}

      {!user && (
        <p className="text-gray-500 dark:text-gray-400">Loading user info...</p>
      )}
    </div>
  );
}
