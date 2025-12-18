import React, { useState } from 'react';

const PerformanceBarChart = ({ tasksByStatus }) => {
  const [hovered, setHovered] = useState(null);

  if (!tasksByStatus) return null;

  const data = [
    { key: 'TO_DO', label: 'To Do', value: tasksByStatus.TO_DO?.length || 0, color: 'bg-blue-500' },
    { key: 'IN_PROGRESS', label: 'In Progress', value: tasksByStatus.IN_PROGRESS?.length || 0, color: 'bg-amber-500' },
    { key: 'REVIEW', label: 'Review', value: tasksByStatus.REVIEW?.length || 0, color: 'bg-purple-500' },
    { key: 'DONE', label: 'Done', value: tasksByStatus.DONE?.length || 0, color: 'bg-emerald-500' },
  ];

  const max = Math.max(...data.map(d => d.value), 1);

  return (
    <div className="bg-white rounded-xl shadow border p-6 mb-6">
      <h2 className="text-lg font-bold text-gray-700 mb-6">
        Employee Performance
      </h2>

      <div className="flex items-end justify-between gap-6 relative">
        {data.map(item => (
          <div
            key={item.key}
            className="flex flex-col items-center w-full relative"
            onMouseEnter={() => setHovered(item)}
            onMouseLeave={() => setHovered(null)}
          >
            {/* TOOLTIP */}
            {hovered?.key === item.key && (
              <div className="absolute -top-12 bg-black text-white text-xs px-3 py-1 rounded shadow">
                {item.label} : {item.value} tasks
              </div>
            )}

            {/* VALUE */}
            <span className="text-sm font-semibold mb-2">
              {item.value}
            </span>

            {/* BAR */}
            <div className="w-full bg-gray-200 rounded-lg h-52 flex items-end">
              <div
                className={`${item.color} w-full rounded-lg transition-all duration-300`}
                style={{ height: `${(item.value / max) * 100}%` }}
              />
            </div>

            {/* LABEL */}
            <span className="text-xs mt-2 text-gray-600 text-center">
              {item.label}
            </span>
          </div>
        ))}
      </div>
    </div>
  );
};

export default PerformanceBarChart;
