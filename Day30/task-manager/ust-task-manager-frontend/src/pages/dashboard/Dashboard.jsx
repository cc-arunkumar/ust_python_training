import { useEffect, useState } from "react";
import api from "../../services/api";
import { useAuth } from "../../context/AuthContext";
import {
  Briefcase,
  CheckCircle2,
  Clock,
  TrendingUp,
  Users,
  UserCog,
} from "lucide-react";
import {
  PieChart,
  Pie,
  Cell,
  Tooltip,
  Legend,
  ResponsiveContainer,
  BarChart,
  Bar,
  XAxis,
  YAxis,
  CartesianGrid,
} from "recharts";

const COLORS = ["#10B981", "#3B82F6", "#F59E0B", "#EF4444"];
// Explicit mapping for pie slices by label to ensure correct colors and ordering
const STATUS_COLOR_MAP = {
  "To Do": "#9CA3AF", // gray
  "In Progress": "#3B82F6", // blue
  Review: "#F59E0B", // amber
  Completed: "#10B981", // green
};

function Dashboard() {
  const { user } = useAuth();
  const [loading, setLoading] = useState(true);
  const [stats, setStats] = useState({
    totalTasks: 0,
    completed: 0,
    inProgress: 0,
    pending: 0,
    review: 0,
    employees: 0,
    users: 0,
  });
  const [workloadData, setWorkloadData] = useState([]);

  useEffect(() => {
    if (user) loadDashboard();
  }, [user]);

  const loadDashboard = async () => {
    try {
      const tasksRes = await api.get("/api/tasks");
      const tasks = tasksRes.data.tasks || tasksRes.data || [];

      const completed = tasks.filter((t) => t.status === "COMPLETED").length;
      const inProgress = tasks.filter((t) => t.status === "IN_PROGRESS").length;
      const review = tasks.filter((t) => t.status === "REVIEW").length;
      const pending = tasks.filter((t) => t.status === "TO_DO").length;

      // Build workload data: count tasks per assignee
      const byAssignee = {};
      tasks.forEach((t) => {
        const name = t.assigned_to ? String(t.assigned_to) : "Unassigned";
        byAssignee[name] = (byAssignee[name] || 0) + 1;
      });
      // Convert to array and sort desc, then keep top 8 for clarity
      const workloadArr = Object.keys(byAssignee).map((k) => ({
        name: k,
        value: byAssignee[k],
      }));
      workloadArr.sort((a, b) => b.value - a.value);
      const topWorkload = workloadArr.slice(0, 8);

      let empCount = 0;
      let userCount = 0;

      if (user.role === "admin") {
        try {
          const empRes = await api.get("/api/employees");
          const userRes = await api.get("/api/users");
          empCount = empRes.data.length || 0;
          userCount = userRes.data.length || 0;
        } catch (e) {
          console.warn("Admin stats fetch failed", e);
        }
      }

      setStats({
        totalTasks: tasks.length,
        completed,
        inProgress,
        pending,
        review,
        employees: empCount,
        users: userCount,
      });

      setWorkloadData(topWorkload);
    } catch (err) {
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  const chartData = [
    { name: "To Do", value: stats.pending },
    { name: "In Progress", value: stats.inProgress },
    { name: "Review", value: stats.review },
    { name: "Completed", value: stats.completed },
  ];

  if (loading) return <div className="p-10 text-center">Loading...</div>;

  return (
    // 1. CONTAINER: Centered and constrained width
    <div className="max-w-6xl mx-auto p-6 space-y-6">
      {/* Header */}
      <div className="flex justify-between items-center mb-2">
        <h1 className="text-2xl font-bold text-gray-800">Dashboard</h1>
        <span className="bg-blue-100 text-blue-800 text-xs px-3 py-1 rounded-full uppercase font-bold tracking-wide">
          {user.role} View
        </span>
      </div>

      {/* 2. STATS GRID: 3 columns on desktop, 1 on mobile */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
        <StatCard
          title="Total Tasks"
          value={stats.totalTasks}
          icon={<Briefcase size={20} />}
          color="bg-blue-500"
        />
        <StatCard
          title="Completed"
          value={stats.completed}
          icon={<CheckCircle2 size={20} />}
          color="bg-green-500"
        />
        <StatCard
          title="Pending"
          value={stats.pending}
          icon={<Clock size={20} />}
          color="bg-yellow-500"
        />

        {user.role === "admin" && (
          <>
            <StatCard
              title="Employees"
              value={stats.employees}
              icon={<Users size={20} />}
              color="bg-purple-500"
            />
            <StatCard
              title="System Users"
              value={stats.users}
              icon={<UserCog size={20} />}
              color="bg-pink-500"
            />
            <StatCard
              title="Active Now"
              value="-"
              icon={<TrendingUp size={20} />}
              color="bg-indigo-500"
            />
          </>
        )}
      </div>

      {/* 3. CHARTS GRID: Side by Side */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6 mt-6">
        {/* Pie Chart Container */}
        <div className="bg-white p-5 rounded-lg shadow border border-gray-100 h-80">
          <h3 className="text-sm font-bold text-gray-600 mb-4 uppercase tracking-wider">
            Status Distribution
          </h3>
          <ResponsiveContainer width="100%" height="85%">
            <PieChart>
              <Pie
                data={chartData}
                cx="50%"
                cy="50%"
                innerRadius={60}
                outerRadius={80}
                paddingAngle={5}
                dataKey="value"
              >
                {chartData.map((entry, index) => (
                  <Cell
                    key={`cell-${index}`}
                    fill={
                      STATUS_COLOR_MAP[entry.name] ||
                      COLORS[index % COLORS.length]
                    }
                  />
                ))}
              </Pie>
              <Tooltip />
              <Legend verticalAlign="bottom" height={36} />
            </PieChart>
          </ResponsiveContainer>
        </div>

        {/* Bar Chart Container */}
        <div className="bg-white p-5 rounded-lg shadow border border-gray-100 h-80">
          <h3 className="text-sm font-bold text-gray-600 mb-4 uppercase tracking-wider">
            Workload
          </h3>
          <ResponsiveContainer width="100%" height="85%">
            <BarChart
              data={workloadData}
              margin={{ top: 10, right: 30, left: 10, bottom: 60 }}
            >
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis
                dataKey="name"
                type="category"
                tick={{ fontSize: 12 }}
                interval={0}
                angle={-35}
                textAnchor="end"
              />
              <YAxis type="number" />
              <Tooltip />
              <Bar dataKey="value" barSize={24} radius={[4, 4, 0, 0]}>
                {workloadData.map((entry, index) => (
                  <Cell
                    key={`cell-${index}`}
                    fill={COLORS[index % COLORS.length]}
                  />
                ))}
              </Bar>
            </BarChart>
          </ResponsiveContainer>
        </div>
      </div>
    </div>
  );
}

// Compact Stat Card
const StatCard = ({ title, value, icon, color }) => (
  <div className="bg-white p-4 rounded-lg shadow-sm border border-gray-100 flex items-center justify-between">
    <div>
      <p className="text-gray-500 text-xs font-semibold uppercase">{title}</p>
      <h3 className="text-2xl font-bold text-gray-800">{value}</h3>
    </div>
    <div className={`p-2 rounded-md ${color} text-white`}>{icon}</div>
  </div>
);

export default Dashboard;
