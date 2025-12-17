import React from "react";
import { Folder, Clock, AlertCircle, CheckCircle } from "lucide-react";

const SummaryCards = ({ taskCounts }) => {
  const stats = [
    {
      label: "To Do",
      count: taskCounts["to-do"],
      color: "from-gray-500 to-gray-600",
      icon: Folder,
    },
    {
      label: "In Progress",
      count: taskCounts["in-progress"],
      color: "from-blue-500 to-blue-600",
      icon: Clock,
    },
    {
      label: "Review",
      count: taskCounts["review"],
      color: "from-yellow-500 to-yellow-600",
      icon: AlertCircle,
    },
    {
      label: "Completed",
      count: taskCounts["completed"],
      color: "from-green-500 to-green-600",
      icon: CheckCircle,
    },
  ];

  return (
    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">
      {stats.map((stat, index) => (
        <div
          key={index}
          className="bg-white rounded-xl shadow-md p-6 border border-gray-200"
        >
          <div className="flex items-center justify-between mb-4">
            <div className={`p-3 bg-gradient-to-br ${stat.color} rounded-lg`}>
              <stat.icon className="w-6 h-6 text-white" />
            </div>
            <span className="text-3xl font-bold text-gray-900">
              {stat.count}
            </span>
          </div>
          <h3 className="text-sm font-semibold text-gray-600">{stat.label}</h3>
        </div>
      ))}
    </div>
  );
};

export default SummaryCards;
