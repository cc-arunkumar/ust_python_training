import React, { useState, useMemo } from "react";
import { DragDropContext, DropResult } from "@hello-pangea/dnd";
import { Task, TaskStatus, Role } from "@/types";
import { useTasks } from "@/contexts/TaskContext";
import { useAuth } from "@/contexts/AuthContext";
import KanbanColumn from "./KanbanColumn";
import TaskDetailModal from "./TaskDetailModal";
import CreateTaskModal from "./CreateTaskModal";
import { toast } from "sonner";

interface TaskBoardProps {
  viewMode: Role;
}

const TaskBoard: React.FC<TaskBoardProps> = ({ viewMode }) => {
  const { tasks, updateTaskStatus } = useTasks();
  const { user, isAdmin, isManager } = useAuth();
  const [selectedTask, setSelectedTask] = useState<Task | null>(null);
  const [showCreateModal, setShowCreateModal] = useState(false);

  const filteredTasks = useMemo(() => {
    if (viewMode === "admin") {
      return tasks;
    }
    if (viewMode === "manager") {
      // Manager sees tasks they created, assigned, or are reviewer of
      return tasks.filter(
        (t) =>
          t.created_by === user?.e_id ||
          t.assigned_by === user?.e_id ||
          t.reviewer === user?.e_id
      );
    }
    // Developer sees only their assigned tasks
    return tasks.filter((t) => t.assigned_to === user?.e_id);
  }, [tasks, viewMode, user?.e_id]);

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
    const isDev = viewMode === "employee";
    const isMgr = viewMode === "manager";
    const isReviewer = task.reviewer === user?.e_id;

    // Developer can only move from IN_PROGRESS to REVIEW
    if (isDev && !isMgr) {
      return from === "IN_PROGRESS" && to === "REVIEW";
    }

    // Admin can't review (move from REVIEW to DONE)
    if (viewMode === "admin" && from === "REVIEW" && to === "DONE") {
      return false;
    }

    // Only reviewer can move from REVIEW to DONE or back to IN_PROGRESS
    if (from === "REVIEW") {
      return isReviewer;
    }

    return true;
  };

  const handleDragEnd = (result: DropResult) => {
    if (!result.destination) return;

    const { draggableId, source, destination } = result;
    const fromStatus = source.droppableId as TaskStatus;
    const toStatus = destination.droppableId as TaskStatus;

    if (fromStatus === toStatus) return;

    const task = tasks.find((t) => t.t_id === draggableId);
    if (!task) return;

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

    updateTaskStatus(draggableId, toStatus, user?.e_id || "");
  };

  const canCreateTask = viewMode === "admin" || viewMode === "manager";

  return (
    <div className="p-6">
      <div className="mb-6">
        <h2 className="text-2xl font-bold text-foreground">Task Board</h2>
        <p className="text-muted-foreground text-sm">
          {viewMode === "admin" && "Viewing all tasks across the organization"}
          {viewMode === "manager" && "Viewing tasks you manage or review"}
          {viewMode === "employee" && "Viewing your assigned tasks"}
        </p>
      </div>

      <DragDropContext onDragEnd={handleDragEnd}>
        <div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-4 gap-4">
          <KanbanColumn
            status="TO_DO"
            tasks={tasksByStatus.TO_DO}
            onTaskClick={setSelectedTask}
            canAdd={canCreateTask}
            onAdd={() => setShowCreateModal(true)}
          />
          <KanbanColumn
            status="IN_PROGRESS"
            tasks={tasksByStatus.IN_PROGRESS}
            onTaskClick={setSelectedTask}
          />
          <KanbanColumn
            status="REVIEW"
            tasks={tasksByStatus.REVIEW}
            onTaskClick={setSelectedTask}
          />
          <KanbanColumn
            status="DONE"
            tasks={tasksByStatus.DONE}
            onTaskClick={setSelectedTask}
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
    </div>
  );
};

export default TaskBoard;
