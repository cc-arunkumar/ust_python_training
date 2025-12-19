import { useEffect, useState } from "react";
import { DragDropContext, Droppable, Draggable } from "@hello-pangea/dnd";
import { getTasks, updateTaskStatus, updateTask } from "../api/task.api";
import TaskCard from "../components/TaskCard";
import { useAuth } from "../context/AuthContext";
import ReviewModal from "../components/ReviewModal";

const STATUSES = [
  { key: "TO_DO", label: "TO DO", bg: "bg-blue-50 border border-blue-200" },
  {
    key: "IN_PROGRESS",
    label: "IN PROGRESS",
    bg: "bg-amber-50 border border-amber-200",
  },
  {
    key: "REVIEW",
    label: "REVIEW",
    bg: "bg-violet-50 border border-violet-200",
  },
  {
    key: "DONE",
    label: "COMPLETED",
    bg: "bg-green-50 border border-green-200",
  },
];

const priorityRank = { HIGH: 1, MEDIUM: 2, LOW: 3 };

export default function Board() {
  const { activeRole } = useAuth();
  const [tasks, setTasks] = useState([]);
  const [grouped, setGrouped] = useState({});
  const [reviewTask, setReviewTask] = useState(null);
  const [targetStatus, setTargetStatus] = useState(null);

  const fetchTasks = async () => {
    const data = await getTasks();
    setTasks(data);
  };

  useEffect(() => {
    fetchTasks();
  }, [activeRole]);

  useEffect(() => {
    const map = { TO_DO: [], IN_PROGRESS: [], REVIEW: [], DONE: [] };

    tasks.forEach((t) => map[t.status]?.push(t));

    Object.keys(map).forEach((s) =>
      map[s].sort((a, b) => priorityRank[a.priority] - priorityRank[b.priority])
    );

    setGrouped(map);
  }, [tasks]);

  const onDragEnd = async (result) => {
    if (!result.destination) return;

    const from = result.source.droppableId;
    const to = result.destination.droppableId;

    if (from === to) return;

    const taskId = grouped[from][result.source.index].t_id;
    const task = grouped[from][result.source.index];

    if (activeRole === "MANAGER" && task.status === "REVIEW") {
      setReviewTask(task);
      setTargetStatus(to);
      return;
    }

    await updateTaskStatus(taskId, { status: to });
    fetchTasks();

    // --- persist manager remark as notification when manager moves task out of REVIEW ---
    try {
      // only ask for remark when manager moves item from REVIEW to another column
      if (
        activeRole === "MANAGER" &&
        result.source?.droppableId === "REVIEW" &&
        result.destination?.droppableId !== "REVIEW"
      ) {
        const remark = window.prompt(
          "Add a remark for the developer (optional)"
        );
        if (remark && remark.trim() !== "") {
          const notif = {
            message: remark.trim(),
            from: activeRole,
            read: false,
            ts: new Date().toISOString(),
          };

          // persist on server
          await updateTask(taskId, { notification: notif });

          // update local tasks so bell / unread badge shows immediately
          setTasks((prev) =>
            prev.map((t) =>
              t.t_id === taskId ? { ...t, notification: notif } : t
            )
          );
        }
      }
    } catch (err) {
      console.warn("Failed to persist manager remark notification", err);
    }
  };

  const submitReview = async (remarks) => {
    try {
      // update status + remarks
      await updateTaskStatus(reviewTask.t_id, {
        status: targetStatus,
        remarks: remarks || null,
      });

      // if manager provided remarks, persist a notification so developer sees it
      if (remarks && remarks.trim() !== "") {
        const notif = {
          message: remarks.trim(),
          from: activeRole,
          read: false,
          ts: new Date().toISOString(),
        };
        try {
          await updateTask(reviewTask.t_id, { notification: notif });
          // update local tasks immediately so bell shows without waiting for full refetch
          setTasks((prev) =>
            prev.map((t) =>
              t.t_id === reviewTask.t_id ? { ...t, notification: notif } : t
            )
          );
        } catch (err) {
          console.warn("Failed to persist notification:", err);
        }
      }

      // refresh list to pick up any server-side changes
      await fetchTasks();
    } catch (err) {
      console.error("Failed to submit review:", err);
    } finally {
      setReviewTask(null);
      setTargetStatus(null);
    }
  };

  return (
    <div className="h-full px-6 py-4">
      <DragDropContext onDragEnd={onDragEnd}>
        <div className="grid grid-cols-4 gap-4 h-full">
          {STATUSES.map((col) => (
            <div key={col.key} className={`flex flex-col rounded-lg ${col.bg}`}>
              {/* HEADER */}
              <div className="px-3 py-2 border-b flex items-center justify-between">
                <span className="font-semibold text-sm">{col.label}</span>
                <span
                  className="text-sm font-semibold px-3 py-1 rounded-full bg-white text-gray-800 border border-gray-200 shadow-sm"
                  aria-live="polite"
                  aria-label={`${col.label} count`}
                >
                  {grouped[col.key]?.length ?? 0}
                </span>
              </div>

              {/* BODY */}
              <Droppable
                droppableId={col.key}
                renderClone={(provided, snapshot, rubric) => (
                  <div
                    ref={provided.innerRef}
                    {...provided.draggableProps}
                    {...provided.dragHandleProps}
                    style={provided.draggableProps.style}
                  >
                    <TaskCard
                      task={grouped[col.key][rubric.source.index]}
                      role={activeRole}
                      refresh={fetchTasks}
                    />
                  </div>
                )}
              >
                {(provided) => (
                  <div
                    ref={provided.innerRef}
                    {...provided.droppableProps}
                    className="flex-1 overflow-y-auto p-3 space-y-3"
                  >
                    {grouped[col.key]?.length === 0 && (
                      <p className="text-sm text-gray-400 text-center mt-4">
                        No tasks
                      </p>
                    )}

                    {grouped[col.key]?.map((task, index) => (
                      <Draggable
                        key={task.t_id}
                        draggableId={String(task.t_id)}
                        index={index}
                      >
                        {(provided) => (
                          <div
                            ref={provided.innerRef}
                            {...provided.draggableProps}
                            {...provided.dragHandleProps}
                            className="select-none"
                            style={{
                              ...provided.draggableProps.style,
                            }}
                          >
                            <TaskCard
                              task={task}
                              role={activeRole}
                              refresh={fetchTasks}
                            />
                          </div>
                        )}
                      </Draggable>
                    ))}

                    {provided.placeholder}
                  </div>
                )}
              </Droppable>
            </div>
          ))}
        </div>
      </DragDropContext>

      {/* 🔥 FIXED CENTERED REVIEW MODAL */}
      {reviewTask && (
        <ReviewModal
          targetStatus={targetStatus}
          onCancel={() => {
            setReviewTask(null);
            setTargetStatus(null);
          }}
          onSubmit={submitReview}
        />
      )}
    </div>
  );
}
