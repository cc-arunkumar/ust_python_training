import React, { useState, useMemo } from "react";
import { DragDropContext, DropResult } from "@hello-pangea/dnd";
import { Task, TaskStatus, Role } from "@/types";
import { Input } from "@/components/ui/input";
import { Search } from "lucide-react";
import { useTasks } from "@/contexts/TaskContext";
import { useAuth } from "@/contexts/AuthContext";
import KanbanColumn from "./KanbanColumn";
import TaskDetailModal from "./TaskDetailModal";
import CreateTaskModal from "./CreateTaskModal";
import FileAttachmentModal from "./FileAttachmentModal";
import { useEffect } from "react";
import { toast } from "sonner";

interface TaskBoardProps {
  viewMode: Role;
}

const TaskBoard: React.FC<TaskBoardProps> = ({ viewMode }) => {
  const { tasks, updateTaskStatus, reviewDecision, updatingTasks } = useTasks();
  const { user, isAdmin, isManager } = useAuth();
  const [selectedTask, setSelectedTask] = useState<Task | null>(null);
  const [searchTerm, setSearchTerm] = useState("");
  const [showCreateModal, setShowCreateModal] = useState(false);
  ``;
  const [attachmentTask, setAttachmentTask] = useState<Task | null>(null);
  const statusColors: Record<TaskStatus, { bg: string; text: string }> = {
    TO_DO: { bg: "bg-black-700", text: "text-blue-100" },
    IN_PROGRESS: { bg: "bg-orange-700", text: "text-orange-100" },
    REVIEW: { bg: "bg-indigo-700", text: "text-indigo-100" },
    DONE: { bg: "bg-green-700", text: "text-green-100" },
  };
  useEffect(() => {
    const handler = (e: Event) => {
      const ev = e as CustomEvent;
      const t = ev?.detail?.task as Task | undefined;
      if (t) setAttachmentTask(t);
    };
    window.addEventListener("task:open-attach", handler as EventListener);
    return () =>
      window.removeEventListener("task:open-attach", handler as EventListener);
  }, []);

  const filteredTasks = useMemo(() => {
    const base = (() => {
      if (viewMode === "admin") {
        return tasks;
      }
      if (viewMode === "manager") {
        // Manager sees tasks they created, assigned, or are reviewer of.
        // Additionally, managers should be able to view all open (TO_DO) tasks.
        return tasks.filter(
          (t) =>
            t.status === "TO_DO" ||
            t.created_by === user?.e_id ||
            t.assigned_by === user?.e_id ||
            t.reviewer === user?.e_id
        );
      }
      // Employee (developer) sees only their assigned tasks. Unassigned TO_DO tasks
      // should not be visible to other employees.
      return tasks.filter((t) => t.assigned_to === user?.e_id);
    })();

    const term = String(searchTerm || "")
      .trim()
      .toLowerCase();
    if (!term) return base;

    return base.filter((t) => {
      return (
        (t.title || "").toLowerCase().includes(term) ||
        (t.description || "").toLowerCase().includes(term) ||
        String(t.t_id || "")
          .toLowerCase()
          .includes(term)
      );
    });
  }, [tasks, viewMode, user?.e_id, searchTerm]);

  const tasksByStatus = useMemo(() => {
    const grouped: Record<TaskStatus, Task[]> = {
      TO_DO: [],
      IN_PROGRESS: [],
      REVIEW: [],
      DONE: [],
    };
    filteredTasks.forEach((task) => {
      grouped[task.status ?? "TO_DO"].push(task);
    });

    return grouped;
  }, [filteredTasks]);

  const canMoveTask = (
    task: Task,
    from: TaskStatus,
    to: TaskStatus
  ): boolean => {
    const r = (viewMode || "").toLowerCase();

    // Admins cannot move tasks at all
    if (r === "admin") return false;

    // Manager: only REVIEW -> IN_PROGRESS or REVIEW -> DONE
    if (r === "manager") {
      return from === "REVIEW" && (to === "IN_PROGRESS" || to === "DONE");
    }

    // Employee: TO_DO -> IN_PROGRESS, IN_PROGRESS -> REVIEW
    if (r === "employee") {
      if (from === "TO_DO" && to === "IN_PROGRESS") return true;
      if (from === "IN_PROGRESS" && to === "REVIEW") return true;
      return false;
    }

    return false;
  };

  const handleDragEnd = (result: DropResult) => {
    if (!result.destination) return;

    const { draggableId, source, destination } = result;
    const fromStatus = source.droppableId as TaskStatus;
    const toStatus = destination.droppableId as TaskStatus;

    if (fromStatus === toStatus) return;

    const task = tasks.find((t) => t.t_id === draggableId);
    if (!task) return;

    // Completed tasks are not movable
    if (task.status === "DONE") {
      toast.error("Cannot move a completed task");
      return;
    }

    if (!canMoveTask(task, fromStatus, toStatus)) {
      toast.error("You do not have permission to make this status change");
      return;
    }

    // Check if remark is required (REVIEW -> IN_PROGRESS)
    if (fromStatus === "REVIEW" && toStatus === "IN_PROGRESS") {
      setSelectedTask(task);
      toast.info(
        "Please add a remark explaining why the task is being sent back"
      );
      return;
    }

    // If moving REVIEW -> DONE (approve) as manager/reviewer, call reviewDecision
    if (fromStatus === "REVIEW" && toStatus === "DONE") {
      try {
        reviewDecision(draggableId, "APPROVE", undefined, user?.e_id || "");
        return;
      } catch (e) {
        // fallback to generic update
      }
    }

    updateTaskStatus(draggableId, toStatus, user?.e_id || "");
  };

  const canCreateTask = viewMode === "admin" || viewMode === "manager";

  return (
    <div className="p-6">
      <div className="mb-6">
        <div className="flex items-start justify-between gap-4">
          <div>
            <h2 className="text-2xl font-bold text-foreground">Task Board</h2>
            <p className="text-muted-foreground text-sm">
              {viewMode === "admin" &&
                "Viewing all tasks across the organization"}
              {viewMode === "manager" &&
                "Viewing tasks you manage, review, and open (TO_DO) tasks"}
              {viewMode === "employee" && "Viewing your assigned tasks"}
            </p>
          </div>
          <div className="relative flex-1 max-w-sm">
            {/* Icon */}
            <div className="absolute left-3 top-1/3 -translate-y-1/2 flex items-center pointer-events-none">
              <Search className="h-4 w-4 text-muted-foreground" />
            </div>

            {/* Input */}
            <Input
              placeholder="Search tasks..."
              value={searchTerm}
              onChange={(e) => setSearchTerm(e.target.value)}
              className="pl-10"
            />

            {/* Task count */}
            <div className="text-sm text-muted-foreground mt-1 text-right">
              {filteredTasks.length} task{filteredTasks.length !== 1 ? "s" : ""}
            </div>
          </div>
        </div>
      </div>

      <DragDropContext onDragEnd={handleDragEnd}>
        <div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-4 gap-4">
          <KanbanColumn
            status="TO_DO"
            tasks={tasksByStatus.TO_DO}
            onTaskClick={setSelectedTask}
            canAdd={canCreateTask}
            viewMode={viewMode}
            onAdd={() => setShowCreateModal(true)}
            updatingTasks={updatingTasks}
            color={statusColors.TO_DO}
          />
          <KanbanColumn
            status="IN_PROGRESS"
            tasks={tasksByStatus.IN_PROGRESS}
            onTaskClick={setSelectedTask}
            viewMode={viewMode}
            updatingTasks={updatingTasks}
            color={statusColors.IN_PROGRESS}
          />
          <KanbanColumn
            status="REVIEW"
            tasks={tasksByStatus.REVIEW}
            onTaskClick={setSelectedTask}
            viewMode={viewMode}
            updatingTasks={updatingTasks}
            color={statusColors.REVIEW}
          />
          <KanbanColumn
            status="DONE"
            tasks={tasksByStatus.DONE}
            onTaskClick={setSelectedTask}
            viewMode={viewMode}
            updatingTasks={updatingTasks}
            color={statusColors.DONE}
          />
        </div>
      </DragDropContext>

      {selectedTask && (
        <TaskDetailModal
          task={selectedTask}
          onClose={() => setSelectedTask(null)}
          viewMode={viewMode}
        />
      )}

      {showCreateModal && (
        <CreateTaskModal onClose={() => setShowCreateModal(false)} />
      )}

      {attachmentTask && (
        <FileAttachmentModal
          task={attachmentTask}
          onClose={() => setAttachmentTask(null)}
        />
      )}
    </div>
  );
};

export default TaskBoard;
