import React from "react";
import { toast } from "sonner";
import { Task, Priority } from "@/types";
import { useEmployees } from "@/contexts/EmployeesContext";
import { Calendar, User, Flag, MessageSquare, Paperclip } from "lucide-react";
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
  const resolveId = (val?: string | number) => {
    if (val == null) return undefined;
    const s = String(val);
    const digits = s.replace(/\D/g, "");
    return digits || undefined;
  };
  const assigneeId = task.assigned_to
    ? resolveId(task.assigned_to)
    : (resolveId((task as any).assigned_to_id) as string | undefined);

  // additional fallback: task.assigned_to might be an object with emp_id/e_id
  let assignee = assigneeId ? getEmployeeById(assigneeId) : null;
  if (!assignee) {
    const at = (task as any).assigned_to;
    if (at && typeof at === "object") {
      const candidateId = resolveId(at.emp_id || at.e_id || at.id);
      if (candidateId) assignee = getEmployeeById(candidateId);
      if (!assignee && at.name) {
        // create a lightweight employee object so we can render the name
        assignee = {
          e_id: at.e_id || String(at.emp_id || ""),
          name: at.name,
        } as any;
      }
    }
  }
  const priority = priorityConfig[task.priority];

  return (
    <div
      className={`relative pt-4 task-card ${
        isDragging ? "task-card-dragging" : ""
      } animate-card-enter`}
      // keep the card clickable for opening details; we handle attach button separately
      onClick={() => {
        // show a lightweight in-app notification when a task card is opened
        try {
          toast(`${task.t_id} — ${task.title} • ${task.status}`);
        } catch (e) {
          // ignore
        }
        if (onClick) onClick();
      }}
    >
      {/* id (left) and priority (right next to id) on same top row; title below */}
      <div className="flex items-center justify-between gap-2 mb-2">
        <div className="flex items-center gap-2">
          <span className="text-[10px] font-mono text-muted-foreground bg-muted px-1 py-0.5 rounded">
            {task.t_id}
          </span>
          <span
            className={`flex items-center gap-1 text-[10px] font-medium ${priority.class}`}
          >
            <Flag className="h-3 w-3" />
            {priority.label}
          </span>
        </div>
      </div>

      <div className="mb-2">
        <h4 className="font-medium text-foreground text-sm leading-tight line-clamp-2">
          {task.title}
        </h4>
      </div>

      <p className="text-xs text-muted-foreground mb-3 line-clamp-2">
        {task.description}
      </p>

      <div className="flex items-center justify-between pt-3 border-t border-border">
        <div className="flex items-center gap-3">
          {assignee && (
            <div className="flex items-center gap-1.5 text-xs text-muted-foreground">
              <User className="h-3 w-3" />
              <span className="truncate max-w-[120px]">
                {String(assignee.name)}
              </span>
            </div>
          )}
          <div className="flex items-center gap-1.5 text-xs text-muted-foreground">
            <Calendar className="h-3 w-3" />
            <span>{format(new Date(task.expected_closure), "MMM d")}</span>
          </div>
        </div>
        <div className="flex items-center gap-2">
          <button
            onClick={(e) => {
              // stop card onClick from firing when clicking the attachment button
              e.stopPropagation();
              // open modal handled below via custom event
              const ev = new CustomEvent("task:open-attach", {
                detail: { task },
              });
              window.dispatchEvent(ev);
            }}
            title="Attach file / Add remark"
            className="p-1 rounded hover:bg-muted/60"
          >
            <Paperclip className="h-4 w-4" />
          </button>
        </div>
      </div>
    </div>
  );
};

export default TaskCard;
