import React from "react";
import { Droppable } from "@hello-pangea/dnd";
import TaskCard from "./TaskCard";

const KanbanColumn = ({
  status,
  tasks,
  employees = [],
  onTaskView,
  onTaskEdit,
  onTaskDelete,
}) => {
  const taskCount = Array.isArray(tasks) ? tasks.length : 0;

  // Map status to a subtle background color for visual separation
  const statusBgMap = {
    TODO: "bg-purple-50",
    ON_PROCESS: "bg-yellow-50",
    REVIEW: "bg-indigo-50",
    DONE: "bg-emerald-50",
  };

  const bgClass = statusBgMap[status] || "bg-gray-100";

  return (
    <Droppable droppableId={status}>
      {(provided, snapshot) => (
        <div
          className={`flex-1 min-w-[280px] rounded-lg p-3 ${bgClass} transition-all duration-300 ease-out ${
            snapshot.isDraggingOver
              ? "ring-2 ring-blue-200 bg-opacity-90"
              : "shadow-sm hover:shadow-md"
          }`}
        >
          <div className="flex items-start justify-between">
            <h3 className="text-xs font-semibold text-gray-600 uppercase">
              {status}
            </h3>
            <div className="text-xs text-slate-600 bg-white/80 px-2 py-0.5 rounded-full shadow-sm">
              {taskCount} {taskCount === 1 ? "task" : "tasks"}
            </div>
          </div>

          <div
            ref={provided.innerRef}
            {...provided.droppableProps}
            className="space-y-3 mt-3 min-h-[100px] transition-colors duration-200"
          >
            {Array.isArray(tasks) &&
              tasks.map((task, index) => {
                const assigned = employees.find(
                  (e) => Number(e.emp_id) === Number(task.assigned_to)
                );
                return (
                  <TaskCard
                    key={task.task_id}
                    task={task}
                    index={index}
                    assignedEmployee={assigned}
                    onView={onTaskView}
                    onEdit={onTaskEdit}
                    onDelete={onTaskDelete}
                  />
                );
              })}
            {provided.placeholder}
          </div>
        </div>
      )}
    </Droppable>
  );
};

export default KanbanColumn;
