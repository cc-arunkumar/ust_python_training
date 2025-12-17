import React from "react";
import TaskCard from "./tasks/TaskCard";

const KanbanBoard = ({ tasks, onStatusChange, loading }) => {
  const statuses = ["to-do", "in-progress", "review", "completed"];

  const getTasksByStatus = (status) => {
    return tasks.filter((task) => task.status === status);
  };

  if (loading) {
    return (
      <div className="flex items-center justify-center h-64">
        <div className="text-gray-500">Loading tasks...</div>
      </div>
    );
  }

  return (
    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
      {statuses.map((status) => (
        <div key={status} className="bg-gray-100 rounded-xl p-4">
          <div className="flex items-center justify-between mb-4">
            <h2 className="text-lg font-bold text-gray-900 capitalize">
              {status.replace("-", " ")}
            </h2>
            <span className="px-3 py-1 bg-white rounded-full text-sm font-semibold text-gray-700">
              {getTasksByStatus(status).length}
            </span>
          </div>
          <div className="space-y-3">
            {getTasksByStatus(status).map((task) => (
              <TaskCard
                key={task._id}
                task={task}
                onStatusChange={onStatusChange}
              />
            ))}
            {getTasksByStatus(status).length === 0 && (
              <div className="text-center py-8 text-gray-400 text-sm">
                No tasks
              </div>
            )}
          </div>
        </div>
      ))}
    </div>
  );
};

export default KanbanBoard;
