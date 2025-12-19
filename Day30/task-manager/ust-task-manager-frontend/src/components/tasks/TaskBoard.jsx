import { DndContext, DragOverlay, closestCorners } from "@dnd-kit/core";
import { useState } from "react";
import { toast } from "react-toastify";
import { useDroppable } from "@dnd-kit/core";
import TaskCard from "./TaskCard";

const COLUMNS = [
  { id: "TO_DO", title: "To Do", color: "bg-gray-100" },
  { id: "IN_PROGRESS", title: "In Progress", color: "bg-blue-50" },
  { id: "REVIEW", title: "Review", color: "bg-orange-50" },
  { id: "COMPLETED", title: "Completed", color: "bg-green-50" },
];

const STATUS_FLOW = ["TO_DO", "IN_PROGRESS", "REVIEW", "COMPLETED"];

const TaskBoard = ({ tasks, onStatusChange, onTaskClick }) => {
  const [activeId, setActiveId] = useState(null);
  const [activeTask, setActiveTask] = useState(null);

  const handleDragStart = (event) => {
    setActiveId(event.active.id);
    setActiveTask(event.active.data.current?.task);
  };

  const handleDragEnd = (event) => {
    const { active, over } = event;

    if (over && active.id !== over.id) {
      // Determine task id and the target status.
      const taskId = parseInt(active.id);

      // over.id may be a column id (e.g. 'REVIEW') or another task id if dropped on a card.
      let newStatus = over.id;

      // If dropped on a task card (numeric id), find that task and use its status as the target column.
      if (!STATUS_FLOW.includes(newStatus)) {
        const overTaskId = parseInt(over.id);
        const overTask = tasks.find((t) => t.task_id === overTaskId);
        if (overTask) newStatus = overTask.status;
      }

      // Find the dragged task
      const task = tasks.find((t) => t.task_id === taskId);

      // If the task is already completed, do not allow moving it
      if (task && task.status === "COMPLETED") {
        toast.error("Completed tasks cannot be moved");
        setActiveId(null);
        setActiveTask(null);
        return;
      }

      if (task && task.status !== newStatus) {
        // Enforce strict adjacent-only transitions: TO_DO -> IN_PROGRESS -> REVIEW -> COMPLETED
        const fromIdx = STATUS_FLOW.indexOf(task.status);
        const toIdx = STATUS_FLOW.indexOf(newStatus);

        if (fromIdx === -1 || toIdx === -1) {
          toast.error("Invalid status target");
        } else if (Math.abs(fromIdx - toIdx) === 1) {
          onStatusChange(task, newStatus);
        } else {
          toast.error(
            "Invalid status transition. Follow: To Do → In Progress → Review → Completed"
          );
        }
      }
    }
    setActiveId(null);
    setActiveTask(null);
  };

  return (
    <DndContext
      onDragStart={handleDragStart}
      onDragEnd={handleDragEnd}
      collisionDetection={closestCorners}
    >
      <div className="grid grid-cols-1 md:grid-cols-4 gap-4 h-full overflow-x-auto pb-4">
        {COLUMNS.map((col) => (
          <DroppableColumn
            key={col.id}
            col={col}
            // Ensure tasks are grouped by status and ordered by priority (High -> Medium -> Low), then by id
            tasks={tasks
              .filter((t) => t.status === col.id)
              .sort((a, b) => {
                const order = { high: 0, medium: 1, low: 2 };
                const pa = order[a.priority] ?? 3;
                const pb = order[b.priority] ?? 3;
                if (pa !== pb) return pa - pb;
                return (a.task_id || 0) - (b.task_id || 0);
              })}
            onTaskClick={onTaskClick}
          />
        ))}
      </div>

      {/* Drag Overlay - Shows the card while dragging */}
      <DragOverlay>
        {activeId ? (
          <div className="opacity-90 rotate-2 scale-105">
            {/* We can't pass full task data easily here without state, generic placeholder for now */}
            <div className="bg-white p-4 rounded shadow-lg border border-blue-500">
              Moving Task #{activeId}...
            </div>
          </div>
        ) : null}
      </DragOverlay>
    </DndContext>
  );
};

// Internal Column Component
const DroppableColumn = ({ col, tasks, onTaskClick }) => {
  const { setNodeRef } = useDroppable({
    id: col.id,
  });

  return (
    <div
      ref={setNodeRef}
      className={`p-4 rounded-lg ${col.color} min-h-[500px] flex flex-col`}
    >
      <h3 className="font-bold text-gray-700 mb-4 flex justify-between items-center">
        {col.title}
        <span className="bg-white px-2 py-0.5 rounded-full text-xs text-gray-500 shadow-sm border">
          {tasks.length}
        </span>
      </h3>
      <div className="flex-1">
        {tasks.map((task) => (
          <TaskCard
            key={task.task_id}
            task={task}
            onDoubleTap={() => onTaskClick(task)}
            onEdit={() => onTaskClick(task)}
          />
        ))}
        {tasks.length === 0 && (
          <div className="text-center text-gray-400 text-sm mt-10 border-2 border-dashed border-gray-300 rounded p-4">
            No tasks
          </div>
        )}
      </div>
    </div>
  );
};

export default TaskBoard;
