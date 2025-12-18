import React from "react";
import { Task, Priority } from "@/types";
import { useEmployees } from "@/contexts/EmployeesContext";
import { Calendar, User, Flag, MessageSquare } from "lucide-react";
import { format } from "date-fns";

interface TaskCardProps {
  task: Task;
  isDragging?: boolean;
  onClick?: () => void;
}

const priorityConfig: Record<Priority, { class: string; label: string }> = {
  high: { class: "priority-high", label: "High" },
  medium: { class: "priority-medium", label: "Medium" },
  low: { class: "priority-low", label: "Low" },
};

const TaskCard: React.FC<TaskCardProps> = ({ task, isDragging, onClick }) => {
  const { getEmployeeById } = useEmployees();
  const assignee = task.assigned_to ? getEmployeeById(task.assigned_to) : null;
  const priority = priorityConfig[task.priority];

  return (
    <div
      className={`task-card ${
        isDragging ? "task-card-dragging" : ""
      } animate-card-enter`}
      onClick={onClick}
    >
      <div className="flex items-start justify-between gap-2 mb-3">
        <h4 className="font-medium text-foreground text-sm leading-tight line-clamp-2">
          {task.title}
        </h4>
        <span
          className={`flex items-center gap-1 text-xs font-medium ${priority.class}`}
        >
          <Flag className="h-3 w-3" />
          {priority.label}
        </span>
      </div>

      <p className="text-xs text-muted-foreground mb-3 line-clamp-2">
        {task.description}
      </p>

      <div className="flex items-center justify-between pt-3 border-t border-border">
        <div className="flex items-center gap-3">
          {assignee && (
            <div className="flex items-center gap-1.5 text-xs text-muted-foreground">
              <User className="h-3 w-3" />
              <span className="truncate max-w-[80px]">
                {assignee.name.split(" ")[0]}
              </span>
            </div>
          )}
          <div className="flex items-center gap-1.5 text-xs text-muted-foreground">
            <Calendar className="h-3 w-3" />
            <span>{format(new Date(task.expected_closure), "MMM d")}</span>
          </div>
        </div>
        <span className="text-[10px] font-mono text-muted-foreground bg-muted px-1.5 py-0.5 rounded">
          {task.t_id}
        </span>
      </div>
    </div>
  );
};

export default TaskCard;
