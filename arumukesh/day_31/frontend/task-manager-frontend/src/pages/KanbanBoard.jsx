// src/pages/KanbanBoard.jsx
import React, { useState, useEffect, useMemo } from "react";
import { DndProvider, useDrag, useDrop } from "react-dnd";
import { HTML5Backend } from "react-dnd-html5-backend";
import { useAuth } from "../context/AuthContext";
import { getTasks, updateTaskStatus } from "../api/taskApi";

const ItemType = "TASK_CARD";

const priorityOrder = { high: 3, medium: 2, low: 1 };

const statusColumns = [
  { id: "pending", title: "Pending", color: "bg-gray-50 border-gray-300" },
  {
    id: "in_progress",
    title: "In Progress",
    color: "bg-blue-50 border-blue-300",
  },
  {
    id: "in_review",
    title: "In Review",
    color: "bg-yellow-50 border-yellow-300",
  },
  {
    id: "completed",
    title: "Completed",
    color: "bg-green-50 border-green-300",
  },
];

const priorityColors = {
  high: "bg-red-100 text-red-800 border-red-200 border-l-4",
  medium: "bg-yellow-100 text-yellow-800 border-yellow-200 border-l-4",
  low: "bg-green-100 text-green-800 border-green-200 border-l-4",
};

const TaskCard = ({ task, canDrag }) => {
  const [{ isDragging }, drag] = useDrag({
    type: ItemType,
    item: { id: task.t_id, currentStatus: task.status },
    canDrag: canDrag,
    collect: (monitor) => ({ isDragging: !!monitor.isDragging() }),
  });

  // time remaining
  const timeRemaining = useMemo(() => {
    try {
      const due = new Date(task.expected_closure);
      const now = new Date();
      const diff = due - now;
      const days = Math.floor(diff / (1000 * 60 * 60 * 24));
      if (diff < 0) return `Overdue by ${Math.abs(days)}d`;
      if (days === 0) return "Due today";
      return `${days}d left`;
    } catch {
      return "N/A";
    }
  }, [task.expected_closure]);

  return (
    <div
      ref={canDrag ? drag : null}
      className={`p-4 mb-4 bg-white rounded-lg shadow hover:shadow-md transition-all ${
        priorityColors[task.priority]
      } ${isDragging ? "opacity-50" : ""} ${
        canDrag ? "cursor-grab" : "cursor-default"
      }`}
    >
      <div className="flex justify-between items-start">
        <h4 className="font-bold text-md mb-2">{task.title}</h4>
        <span className="text-xs font-semibold uppercase px-2 py-1 rounded text-gray-700 bg-white/60">
          {task.priority}
        </span>
      </div>

      <p className="text-sm text-gray-600 mb-3 line-clamp-2">
        {task.description}
      </p>

      <div className="flex justify-between text-xs text-gray-500">
        <span className="font-medium capitalize">{timeRemaining}</span>
        <span>Due: {new Date(task.expected_closure).toLocaleDateString()}</span>
      </div>

      <div className="text-xs text-gray-500 mt-2 flex justify-between">
        <div>
          Assignee: <span className="font-medium">{task.assigned_to}</span>
        </div>
        <div>
          Reviewer: <span className="font-medium">{task.reviewer}</span>
        </div>
      </div>
    </div>
  );
};

const Column = ({ status, title, color, tasks, onDrop, canDrag }) => {
  const [, drop] = useDrop({
    accept: ItemType,
    drop: (item) => onDrop(item.id, status, item.currentStatus),
  });

  const sortedTasks = [...tasks].sort(
    (a, b) => priorityOrder[b.priority] - priorityOrder[a.priority]
  );

  return (
    <div
      ref={drop}
      className={`flex-1 p-6 rounded-lg ${color} min-h-[calc(100vh-200px)] border-2 border-dashed border-transparent`}
    >
      <h3 className="text-xl font-bold mb-6 text-gray-800">
        {title} ({tasks.length})
      </h3>
      <div className="space-y-4">
        {sortedTasks.map((task) => (
          <TaskCard
            key={task.t_id}
            task={task}
            canDrag={typeof canDrag === "function" ? canDrag(task) : !!canDrag}
          />
        ))}
        {tasks.length === 0 && (
          <p className="text-center text-gray-400 italic py-8">
            No tasks in this column
          </p>
        )}
      </div>
    </div>
  );
};

const KanbanBoard = () => {
  const { user } = useAuth();
  const [tasks, setTasks] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  const role = user?.role?.toLowerCase() || "";
  const isDeveloper = role.includes("developer") && !role.includes("admin");

  useEffect(() => {
    const fetchTasks = async () => {
      try {
        const res = await getTasks();
        setTasks(res.data || []);
      } catch (err) {
        console.error(err);
        setError("Failed to load tasks");
      } finally {
        setLoading(false);
      }
    };
    fetchTasks();
  }, []);

  const refresh = async () => {
    try {
      const res = await getTasks();
      setTasks(res.data || []);
    } catch {
      console.error("Failed to refresh tasks");
    }
  };

  const canDragTask = (task) => {
    if (!user) return false;

    const me = String(user.emp_id);
    // Completed tasks cannot be moved
    if (task.status === "completed") return false;

    // Backend allows only reviewer or assignee to change status
    if (me !== String(task.reviewer) && me !== String(task.assigned_to))
      return false;

    // If reviewer: only allow changes when task is in_review (to completed or back to in_progress)
    if (me === String(task.reviewer)) {
      return task.status === "in_review";
    }

    // If assignee (developer): allow Pending -> In Progress and In Progress -> In Review
    if (me === String(task.assigned_to) && isDeveloper) {
      return task.status === "pending" || task.status === "in_progress";
    }

    return false;
  };

  const handleDrop = async (taskId, newStatus, currentStatus) => {
    const task = tasks.find((t) => t.t_id === taskId);
    if (!task) return;

    const me = String(user?.emp_id);

    if (newStatus === currentStatus) return;

    if (currentStatus === "completed") {
      alert("Completed tasks cannot be moved");
      return;
    }

    // Cannot directly move to completed unless coming from in_review
    if (newStatus === "completed" && currentStatus !== "in_review") {
      alert("Tasks must be in 'In Review' before being marked Completed");
      return;
    }

    // Reviewer rules
    if (me === String(task.reviewer)) {
      // reviewer can move IN_REVIEW -> COMPLETED or IN_REVIEW -> IN_PROGRESS
      if (task.status !== "in_review") {
        alert("Reviewer actions are allowed only while task is In Review");
        return;
      }
      // allowed — proceed
    }

    // Developer rules (assignee)
    if (me === String(task.assigned_to) && isDeveloper) {
      const allowed =
        (currentStatus === "pending" && newStatus === "in_progress") ||
        (currentStatus === "in_progress" && newStatus === "in_review");
      if (!allowed) {
        alert("Developers can only move: Pending → In Progress → In Review");
        return;
      }
    }

    // If not reviewer or assignee, reject (backend would also reject)
    if (me !== String(task.reviewer) && me !== String(task.assigned_to)) {
      alert("You are not authorized to change this task's status");
      return;
    }

    try {
      await updateTaskStatus(taskId, newStatus);
      await refresh();
    } catch (err) {
      console.error(err);
      alert(err.response?.data?.detail || "Failed to update status");
    }
  };

  if (loading)
    return (
      <div className="p-10 text-center text-gray-600">Loading board...</div>
    );
  if (error)
    return <div className="p-10 text-center text-red-600">{error}</div>;

  return (
    <DndProvider backend={HTML5Backend}>
      <div className="p-6 bg-gray-50 min-h-screen">
        <h2 className="text-3xl font-bold text-gray-800 mb-8">Task Board</h2>

        <div className="grid grid-cols-1 lg:grid-cols-4 gap-6">
          {statusColumns.map((col) => (
            <Column
              key={col.id}
              status={col.id}
              title={col.title}
              color={col.color}
              tasks={tasks.filter((t) => t.status === col.id)}
              onDrop={handleDrop}
              // compute per-task drag permission
              canDrag={canDragTask}
            />
          ))}
        </div>

        {/* Optional message for users without permission */}
        <div className="mt-8 text-center text-gray-600 bg-white p-4 rounded-lg shadow">
          Drag tasks between columns according to your role and permissions.
        </div>
      </div>
    </DndProvider>
  );
};

export default KanbanBoard;
