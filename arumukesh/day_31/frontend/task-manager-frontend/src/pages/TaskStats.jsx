import React, { useEffect, useState } from "react";
import axios from "axios";
import { useAuth } from "../context/AuthContext";

const TaskStats = () => {
  const { user } = useAuth();
  const [tasks, setTasks] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    const fetchTasks = async () => {
      try {
        const res = await axios.get("/api/v1/tasks");
        setTasks(res.data || []);
      } catch (err) {
        console.error(err);
        setError("Failed to load tasks");
      } finally {
        setLoading(false);
      }
    };
    fetchTasks();
  }, []);

  if (loading)
    return (
      <div className="p-10 text-center text-gray-600">Loading stats...</div>
    );
  if (error)
    return <div className="p-10 text-center text-red-600">{error}</div>;
  if (!user)
    return (
      <div className="p-10 text-center text-gray-600">User not loaded</div>
    );

  const userId = String(user.emp_id);

  // Safe filtering
  const myTasks = tasks.filter((t) => t.assigned_to === userId) || [];
  const myCount = myTasks.length;

  const assignedByMe = tasks.filter((t) => t.assigned_by === userId) || [];
  const assignedCount = assignedByMe.length;

  const reviewTasks = tasks.filter((t) => t.reviewer === userId) || [];
  const reviewCount = reviewTasks.length;

  const StatCard = ({ title, count, color }) => (
    <div className={`bg-white rounded-lg shadow p-6 border-t-4 ${color}`}>
      <h3 className="text-lg font-semibold text-gray-700">{title}</h3>
      <p className="text-4xl font-bold text-gray-900 mt-4">{count}</p>
    </div>
  );

  return (
    <div className="p-8">
      <h2 className="text-3xl font-bold mb-8">Dashboard Overview</h2>
      <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
        <StatCard
          title="Tasks Assigned to Me"
          count={myCount}
          color="border-blue-500"
        />
        <StatCard
          title="Tasks Assigned by Me"
          count={assignedCount}
          color="border-purple-500"
        />
        <StatCard
          title="Tasks Under My Review"
          count={reviewCount}
          color="border-orange-500"
        />
      </div>
    </div>
  );
};

export default TaskStats;
