import React, { useState } from "react";
import { CheckCircle2, Circle, Clock, Eye, Sparkles } from "lucide-react";
import { STATUS_COLORS } from "../../utils/constants";
import TaskCard from "./TaskCard";

const PRIORITY_ORDER = { High: 1, Medium: 2, Low: 3 };

const TaskBoard = ({
  tasks,
  onStatusChange,
  onAddRemark,
  onAssign,
  onOpenPanel,
  userRole,
  employees,
  token, // ✅ ADD TOKEN PROP
  currentUserId,
}) => {
  const canEditTasks = ["admin", "manager", "developer"].includes(userRole);
  const [draggedTask, setDraggedTask] = useState(null);

  const tasksByStatus = {
    "To Do": tasks.filter((t) => t.status === "To Do"),
    "In Progress": tasks.filter((t) => t.status === "In Progress"),
    Review: tasks.filter((t) => t.status === "Review"),
    Done: tasks.filter((t) => t.status === "Done"),
  };

  const statusConfig = {
    "To Do": {
      icon: <Circle size={22} />,
      gradient: "from-gray-500 to-gray-600",
      bgGradient: "from-gray-50 to-gray-100",
      borderColor: "border-gray-200",
      iconBg: "bg-gray-100",
      textColor: "text-gray-700",
    },
    "In Progress": {
      icon: <Clock size={22} />,
      gradient: "from-blue-500 to-cyan-500",
      bgGradient: "from-blue-50 to-cyan-50",
      borderColor: "border-blue-200",
      iconBg: "bg-blue-100",
      textColor: "text-blue-700",
    },
    Review: {
      icon: <Eye size={22} />,
      gradient: "from-purple-500 to-pink-500",
      bgGradient: "from-purple-50 to-pink-50",
      borderColor: "border-purple-200",
      iconBg: "bg-purple-100",
      textColor: "text-purple-700",
    },
    Done: {
      icon: <CheckCircle2 size={22} />,
      gradient: "from-green-500 to-emerald-500",
      bgGradient: "from-green-50 to-emerald-50",
      borderColor: "border-green-200",
      iconBg: "bg-green-100",
      textColor: "text-green-700",
    },
  };

  const handleDragStart = (e, task) => {
    if (!canEditTasks) return;
    setDraggedTask(task);
    e.dataTransfer.effectAllowed = "move";
  };

  const isValidTransition = (currentStatus, newStatus, role, task) => {
    if (currentStatus === "Done") return false;
    if (currentStatus === newStatus) return false;

    // Prevent moving unassigned "To Do" tasks to any other status
    if (currentStatus === "To Do" && !task.assigned_to) {
      return false;
    }

    if (role === "developer") {
      return currentStatus === "In Progress" && newStatus === "Review";
    }

    if (role === "manager") {
      if (currentStatus === "To Do" && newStatus === "In Progress") return true;
      if (currentStatus === "Review" && newStatus === "Done") return true;
      if (currentStatus === "Review" && newStatus === "In Progress")
        return true;
      return false;
    }

    if (role === "admin") {
      return currentStatus === "To Do" && newStatus === "In Progress";
    }

    return false;
  };

  const handleDragOver = (e, status) => {
    if (!canEditTasks || !draggedTask) {
      e.preventDefault();
      return;
    }

    if (isValidTransition(draggedTask.status, status, userRole, draggedTask)) {
      e.preventDefault();
      e.dataTransfer.dropEffect = "move";
    } else {
      e.dataTransfer.dropEffect = "none";
    }
  };

  const handleDrop = (e, newStatus) => {
    e.preventDefault();
    if (!canEditTasks || !draggedTask) return;

    if (
      isValidTransition(draggedTask.status, newStatus, userRole, draggedTask)
    ) {
      onStatusChange(draggedTask, newStatus);
    }
    setDraggedTask(null);
  };

  const handleDragEnd = () => {
    setDraggedTask(null);
  };

  return (
    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
      {Object.entries(tasksByStatus).map(([status, statusTasks]) => {
        const config = statusConfig[status];
        const isValidDropZone =
          draggedTask &&
          isValidTransition(draggedTask.status, status, userRole, draggedTask);

        // sort by priority: High → Medium → Low
        const sortedTasks = [...statusTasks].sort(
          (a, b) =>
            (PRIORITY_ORDER[a.priority] || 99) -
            (PRIORITY_ORDER[b.priority] || 99)
        );

        return (
          <div
            key={status}
            className={`rounded-3xl border-2 ${
              config.borderColor
            } bg-gradient-to-br ${
              config.bgGradient
            } p-6 flex flex-col transition-all duration-300 shadow-lg hover:shadow-2xl relative overflow-hidden ${
              isValidDropZone
                ? "ring-4 ring-green-400 ring-opacity-50 scale-105 shadow-2xl shadow-green-500/30"
                : ""
            } ${
              draggedTask && !isValidDropZone && draggedTask.status !== status
                ? "opacity-40 scale-95"
                : ""
            }`}
            onDragOver={(e) => handleDragOver(e, status)}
            onDrop={(e) => handleDrop(e, status)}
          >
            {/* Decorative background element */}
            <div
              className={`absolute top-0 right-0 w-32 h-32 bg-gradient-to-br ${config.gradient} opacity-10 rounded-full blur-3xl`}
            ></div>

            {/* Valid drop zone indicator */}
            {isValidDropZone && (
              <div className="absolute inset-0 border-4 border-dashed border-green-400 rounded-3xl pointer-events-none animate-pulse">
                <div className="absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2">
                  <Sparkles className="text-green-500" size={48} />
                </div>
              </div>
            )}

            {/* Header */}
            <div className="flex items-center justify-between mb-6 relative z-10">
              <div className="flex items-center gap-3">
                <div
                  className={`w-12 h-12 rounded-2xl bg-gradient-to-br ${config.gradient} flex items-center justify-center shadow-lg text-white transform hover:scale-110 transition-transform duration-200`}
                >
                  {config.icon}
                </div>
                <div>
                  <h2 className={`font-bold text-lg ${config.textColor}`}>
                    {status}
                  </h2>
                  <p className="text-xs text-gray-500 font-medium">
                    {sortedTasks.length}{" "}
                    {sortedTasks.length === 1 ? "task" : "tasks"}
                  </p>
                </div>
              </div>
              <div
                className={`px-4 py-2 rounded-xl bg-white shadow-md border-2 ${config.borderColor}`}
              >
                <span
                  className={`text-lg font-bold bg-gradient-to-r ${config.gradient} bg-clip-text text-transparent`}
                >
                  {sortedTasks.length}
                </span>
              </div>
            </div>

            {/* Task list */}
            <div className="space-y-4 flex-1 relative z-10 min-h-[200px] custom-scrollbar">
              {sortedTasks.length === 0 ? (
                <div className="absolute inset-0 flex items-center justify-center">
                  <div className="text-center py-8">
                    <div
                      className={`w-20 h-20 mx-auto mb-4 rounded-2xl ${config.iconBg} flex items-center justify-center`}
                    >
                      <Circle
                        size={40}
                        className={`${config.textColor} opacity-30`}
                      />
                    </div>
                    <p className="text-sm font-medium text-gray-400">
                      No tasks yet
                    </p>
                    <p className="text-xs text-gray-300 mt-1">
                      Drag tasks here
                    </p>
                  </div>
                </div>
              ) : (
                sortedTasks.map((task, index) => (
                  <div
                    key={task._id}
                    draggable={canEditTasks}
                    onDragStart={(e) => handleDragStart(e, task)}
                    onDragEnd={handleDragEnd}
                    className={`transform transition-all duration-200 ${
                      canEditTasks ? "cursor-move hover:scale-105" : ""
                    } ${
                      draggedTask?._id === task._id ? "opacity-30 scale-95" : ""
                    }`}
                    style={{
                      animationDelay: `${index * 0.1}s`,
                      animation: "slideIn 0.3s ease-out forwards",
                    }}
                  >
                    <TaskCard
                      task={task}
                      token={token} // ✅ PASS TOKEN TO TASKCARD
                      onStatusChange={(newStatus) =>
                        onStatusChange(task, newStatus)
                      }
                      onAddRemark={onAddRemark}
                      canEdit={canEditTasks}
                      onAssign={onAssign}
                      employees={employees}
                      currentUserId={currentUserId}
                      onOpenPanel={onOpenPanel}
                    />
                  </div>
                ))
              )}
            </div>
          </div>
        );
      })}
    </div>
  );
};

export default TaskBoard;
