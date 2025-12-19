import { useMemo } from "react";
import {
  PieChart,
  Pie,
  Cell,
  BarChart,
  Bar,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  ResponsiveContainer,
  Legend,
} from 'recharts';

// Simple Card wrappers (no external UI lib needed)
const Card = ({ className, children }) => (
  <div className={`bg-white rounded-lg shadow border ${className || ''}`}>
    {children}
  </div>
);
const CardHeader = ({ children }) => (
  <div className="px-6 py-4 border-b border-gray-200">{children}</div>
);
const CardTitle = ({ children }) => <h3 className="text-lg font-semibold">{children}</h3>;
const CardContent = ({ children }) => <div className="p-6">{children}</div>;

const PerformancePieChart = ({ tasksByStatus, title = "Task Status Distribution" }) => {
  const getStatusColor = (status) => {
    switch (status) {
      case 'TO_DO': return '#3B82F6';
      case 'IN_PROGRESS': return '#F59E0B';
      case 'REVIEW': return '#8B5CF6';
      case 'DONE': return '#10B981';
      default: return '#6B7280';
    }
  };

  const data = useMemo(() => 
    Object.entries(tasksByStatus).map(([status, tasks]) => ({
      name: status.replace('_', ' '),
      value: tasks.length,
      fill: getStatusColor(status),
    }))
  , [tasksByStatus]);

  const totalTasks = data.reduce((sum, entry) => sum + entry.value, 0);

  return (
    <Card className="w-full">
      <CardHeader>
        <CardTitle>{title}</CardTitle>
        <p className="text-sm text-gray-500 mt-1">Total: {totalTasks} tasks</p>
      </CardHeader>
      <CardContent>
        <ResponsiveContainer width="100%" height={300}>
          <PieChart>
            <Pie
              data={data}
              cx="50%"
              cy="50%"
              outerRadius={80}
              innerRadius={40}
              dataKey="value"
              label={({ name, percent }) => `${name} ${(percent * 100).toFixed(0)}%`}
            >
              {data.map((entry, index) => (
                <Cell key={`cell-${index}`} fill={entry.fill} />
              ))}
            </Pie>
            <Tooltip formatter={(value) => [`${value} tasks`]} />
            <Legend />
          </PieChart>
        </ResponsiveContainer>
      </CardContent>
    </Card>
  );
};

const EmployeePerformanceBarChart = ({ tasks, title = "Employee Performance by Completion" }) => {
  const employeeData = useMemo(() => {
    const grouped = {};
    tasks.forEach(task => {
      const empId = task.assigned_to;
      if (!grouped[empId]) grouped[empId] = { completed: 0, total: 0, name: empId };
      grouped[empId].total += 1;
      if (task.status === 'DONE') grouped[empId].completed += 1;
    });

    return Object.values(grouped).map(emp => ({
      name: emp.name,
      completed: emp.completed,
      total: emp.total,
      rate: ((emp.completed / emp.total) * 100).toFixed(1),
      fill: emp.rate > 70 ? '#10B981' : emp.rate > 40 ? '#F59E0B' : '#EF4444',
    }));
  }, [tasks]);

  return (
    <Card className="w-full">
      <CardHeader>
        <CardTitle>{title}</CardTitle>
        <p className="text-sm text-gray-500 mt-1">Completion Rate %</p>
      </CardHeader>
      <CardContent>
        <ResponsiveContainer width="100%" height={300}>
          <BarChart data={employeeData} margin={{ top: 20, right: 30, left: 20, bottom: 5 }}>
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="name" angle={-45} textAnchor="end" height={70} />
            <YAxis />
            <Tooltip formatter={(value, name) => [value, name]} />
            <Legend />
            <Bar dataKey="completed" fill="#8884d8" radius={[4, 4, 0, 0]} />
            <Bar dataKey="rate" fill="#82ca9d" radius={[4, 4, 0, 0]} stackId="a" /> {/* Added stackId for better visualization */}
          </BarChart>
        </ResponsiveContainer>
      </CardContent>
    </Card>
  );
};

export { PerformancePieChart, EmployeePerformanceBarChart };