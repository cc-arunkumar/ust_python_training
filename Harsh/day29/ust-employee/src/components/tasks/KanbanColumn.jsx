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
  return (
    <div className="flex-1 min-w-[280px] bg-gray-100 rounded-lg p-3">
      <h3 className="text-xs font-semibold text-gray-600 uppercase">
        {status}
      </h3>

      <Droppable droppableId={status}>
        {(provided) => (
          <div
            ref={provided.innerRef}
            {...provided.droppableProps}
            className="space-y-3 mt-3 min-h-[100px]"
          >
            {tasks.map((task, index) => {
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
        )}
      </Droppable>
    </div>
  );
};

export default KanbanColumn;
