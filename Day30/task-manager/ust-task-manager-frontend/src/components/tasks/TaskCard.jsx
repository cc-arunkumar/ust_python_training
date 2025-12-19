import { useDraggable } from "@dnd-kit/core";
import { CSS } from "@dnd-kit/utilities";
import { Clock, Paperclip, UserCircle, Edit } from "lucide-react";
import { useRef } from "react";

const DOUBLE_TAP_DELAY = 300; // ms

// onDoubleTap: function called when card is double-tapped/clicked
const TaskCard = ({ task, onDoubleTap, onEdit }) => {
  const { attributes, listeners, setNodeRef, transform, isDragging } =
    useDraggable({
      id: task.task_id.toString(),
      data: { task },
    });

  const style = {
    transform: CSS.Translate.toString(transform),
    opacity: isDragging ? 0.5 : 1,
  };

  const lastTapRef = useRef(0);
  const singleTapTimeout = useRef(null);

  const priorityColors = {
    high: "border-l-4 border-red-500",
    medium: "border-l-4 border-yellow-500",
    low: "border-l-4 border-green-500",
  };

  const handlePointerUp = (e) => {
    if (isDragging) return;
    const now = Date.now();
    const dt = now - (lastTapRef.current || 0);
    if (dt < DOUBLE_TAP_DELAY) {
      // Double tap detected
      clearTimeout(singleTapTimeout.current);
      lastTapRef.current = 0;
      if (onDoubleTap) onDoubleTap(task);
    } else {
      // Start/record single tap; wait to see if another tap follows
      lastTapRef.current = now;
      clearTimeout(singleTapTimeout.current);
      singleTapTimeout.current = setTimeout(() => {
        lastTapRef.current = 0;
        // Single tap -- do nothing by design (we want double-tap to edit)
      }, DOUBLE_TAP_DELAY + 20);
    }
  };

  const handleDoubleClick = (e) => {
    if (isDragging) return;
    if (onDoubleTap) onDoubleTap(task);
  };

  return (
    <div
      ref={setNodeRef}
      style={style}
      {...attributes}
      {...listeners}
      onPointerUp={handlePointerUp}
      onDoubleClick={handleDoubleClick}
      onContextMenu={(e) => {
        // Support right-click to open editor (matches previous behavior)
        e.preventDefault();
        e.stopPropagation();
        if (isDragging) return;
        if (onEdit) onEdit(task);
      }}
      role="button"
      tabIndex={0}
      className={`relative bg-white p-4 rounded shadow-sm border border-gray-200 mb-3 cursor-grab active:cursor-grabbing hover:shadow-md transition-shadow ${
        priorityColors[task.priority]
      }`}
    >
      {/* Visible Edit button: reliable affordance for desktop & touch */}
      {onEdit && (
        <button
          onClick={(e) => {
            e.stopPropagation();
            if (onEdit) onEdit(task);
          }}
          className="absolute top-2 right-2 text-xs text-blue-600 hover:text-blue-800 bg-white/90 px-2 py-1 rounded flex items-center gap-1"
          title="Edit"
        >
          <Edit size={14} />
          <span className="sr-only">Edit</span>
        </button>
      )}
      <div className="flex justify-between items-start mb-2">
        <span className="text-xs text-gray-500 font-mono">#{task.task_id}</span>
        <span
          className={`text-[10px] px-2 py-0.5 rounded-full uppercase font-bold tracking-wide
          ${
            task.priority === "high"
              ? "bg-red-100 text-red-700"
              : task.priority === "medium"
              ? "bg-yellow-100 text-yellow-700"
              : "bg-green-100 text-green-700"
          }`}
        >
          {task.priority}
        </span>
      </div>

      <h4 className="font-semibold text-gray-800 text-sm mb-3 line-clamp-2">
        {task.title}
      </h4>

      <div className="flex items-center justify-between text-gray-400 text-xs mt-3">
        <div className="flex items-center gap-2">
          <UserCircle size={14} />
          <span>{task.assigned_to}</span>
        </div>
        {task.actual_closure ? (
          <span className="text-green-600 font-bold">completed</span>
        ) : (
          <div className="flex items-center gap-1">
            <Clock size={12} />
            <span>{task.expected_closure || "No Date"}</span>
          </div>
        )}
      </div>
    </div>
  );
};

export default TaskCard;
