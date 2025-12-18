import React from "react";
import { Droppable, Draggable } from "@hello-pangea/dnd";
import { Task, TaskStatus } from "@/types";
import TaskCard from "./TaskCard";
import { Plus } from "lucide-react";

interface KanbanColumnProps {
  status: TaskStatus;
  tasks: Task[];
  onTaskClick: (task: Task) => void;
  canAdd?: boolean;
  onAdd?: () => void;
}

const statusConfig: Record<
  TaskStatus,
  { title: string; columnClass: string; countClass: string }
> = {
  TO_DO: {
    title: "To Do",
    columnClass: "kanban-column-todo",
    countClass: "status-todo",
  },
  IN_PROGRESS: {
    title: "In Progress",
    columnClass: "kanban-column-inprogress",
    countClass: "status-inprogress",
  },
  REVIEW: {
    title: "Review",
    columnClass: "kanban-column-review",
    countClass: "status-review",
  },
  DONE: {
    title: "Done",
    columnClass: "kanban-column-done",
    countClass: "status-done",
  },
};

const KanbanColumn: React.FC<KanbanColumnProps> = ({
  status,
  tasks,
  onTaskClick,
  canAdd,
  onAdd,
}) => {
  const config = statusConfig[status];

  return (
    <div className={`kanban-column ${config.columnClass}`}>
      <div className="flex items-center justify-between mb-4">
        <div className="flex items-center gap-2">
          <h3 className="font-semibold text-foreground">{config.title}</h3>
          <span className={`status-badge ${config.countClass}`}>
            {tasks.length}
          </span>
        </div>
        {canAdd && (
          <button
            onClick={onAdd}
            className="p-1.5 rounded-lg hover:bg-background/50 text-muted-foreground hover:text-foreground transition-colors"
          >
            <Plus className="h-4 w-4" />
          </button>
        )}
      </div>

      <Droppable droppableId={status}>
        {(provided, snapshot) => (
          <div
            ref={provided.innerRef}
            {...provided.droppableProps}
            className={`flex-1 space-y-3 min-h-[200px] rounded-lg p-2 transition-colors ${
              snapshot.isDraggingOver
                ? "bg-primary/5 ring-2 ring-primary/20"
                : ""
            }`}
          >
            {tasks.map((task, index) => (
              <Draggable
                key={task.t_id}
                draggableId={task.t_id}
                index={index}
                isDragDisabled={task.status === "DONE"}
              >
                {(provided, snapshot) => (
                  <div
                    ref={provided.innerRef}
                    {...provided.draggableProps}
                    {...provided.dragHandleProps}
                  >
                    <TaskCard
                      task={task}
                      isDragging={snapshot.isDragging}
                      onClick={() => onTaskClick(task)}
                    />
                  </div>
                )}
              </Draggable>
            ))}
            {provided.placeholder}
            {tasks.length === 0 && !snapshot.isDraggingOver && (
              <div className="flex items-center justify-center h-32 text-muted-foreground text-sm">
                No tasks
              </div>
            )}
          </div>
        )}
      </Droppable>
    </div>
  );
};

export default KanbanColumn;
