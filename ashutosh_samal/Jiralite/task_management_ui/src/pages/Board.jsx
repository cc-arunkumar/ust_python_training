// import { useEffect, useState } from "react";
// import { getTasks } from "../api/task.api";
// import TaskCard from "../components/TaskCard";
// import { useAuth } from "../context/AuthContext";

// /* 🟦 Jira-style status config */
// const STATUSES = [
//   {
//     key: "TO_DO",
//     label: "TO DO",
//     columnBg: "bg-slate-50",
//     header: "bg-slate-100 text-slate-700 border-slate-300",
//   },
//   {
//     key: "IN_PROGRESS",
//     label: "IN PROGRESS",
//     columnBg: "bg-blue-50",
//     header: "bg-blue-100 text-blue-700 border-blue-300",
//   },
//   {
//     key: "REVIEW",
//     label: "REVIEW",
//     columnBg: "bg-purple-50",
//     header: "bg-purple-100 text-purple-700 border-purple-300",
//   },
//   {
//     key: "DONE",
//     label: "COMPLETED",
//     columnBg: "bg-green-50",
//     header: "bg-green-100 text-green-700 border-green-300",
//   },
// ];

// /* 🔥 Priority sorting */
// const priorityRank = {
//   HIGH: 1,
//   MEDIUM: 2,
//   LOW: 3,
// };

// export default function Board() {
//   const { activeRole } = useAuth();
//   const [tasks, setTasks] = useState([]);
//   const [grouped, setGrouped] = useState({});

//   /* Fetch tasks */
//   const fetchTasks = async () => {
//     const data = await getTasks();
//     setTasks(data);
//   };

//   useEffect(() => {
//     fetchTasks();
//   }, [activeRole]);

//   /* Group + sort tasks */
//   useEffect(() => {
//     const map = {
//       TO_DO: [],
//       IN_PROGRESS: [],
//       REVIEW: [],
//       DONE: [],
//     };

//     tasks.forEach((task) => {
//       map[task.status]?.push(task);
//     });

//     Object.keys(map).forEach((status) => {
//       map[status].sort(
//         (a, b) =>
//           priorityRank[a.priority] - priorityRank[b.priority]
//       );
//     });

//     setGrouped(map);
//   }, [tasks]);

//   return (
//     <div className="h-full px-6 py-4">
//       <div className="grid grid-cols-4 gap-4 h-full">

//         {STATUSES.map((col) => (
//           <div
//             key={col.key}
//             className={`flex flex-col rounded-lg shadow-sm ${col.columnBg}`}
//           >
//             {/* 🔹 COLUMN HEADER */}
//             <div
//               className={`px-3 py-2 border-b rounded-t-lg ${col.header}`}
//             >
//               <h2 className="text-sm font-semibold tracking-wide">
//                 {col.label}
//               </h2>
//             </div>

//             {/* 🔹 COLUMN BODY */}
//             <div className="flex-1 overflow-y-auto p-3 space-y-3">
//               {grouped[col.key]?.length === 0 && (
//                 <p className="text-sm text-gray-400 text-center mt-4">
//                   No tasks
//                 </p>
//               )}

//               {grouped[col.key]?.map((task) => (
//                 <TaskCard
//                   key={task.t_id}
//                   task={task}
//                   role={activeRole}
//                   refresh={fetchTasks}
//                 />
//               ))}
//             </div>
//           </div>
//         ))}

//       </div>
//     </div>
//   );
// }



// import { useEffect, useState } from "react";
// import { DragDropContext, Droppable } from "@hello-pangea/dnd";
// import { getTasks, updateTaskStatus } from "../api/task.api";
// import TaskCard from "../components/TaskCard";
// import { useAuth } from "../context/AuthContext";

// const STATUSES = [
//   { key: "TO_DO", label: "TO DO", color: "bg-gray-100" },
//   { key: "IN_PROGRESS", label: "IN PROGRESS", color: "bg-blue-50" },
//   { key: "REVIEW", label: "REVIEW", color: "bg-yellow-50" },
//   { key: "DONE", label: "COMPLETED", color: "bg-green-50" },
// ];

// const priorityRank = {
//   HIGH: 1,
//   MEDIUM: 2,
//   LOW: 3,
// };

// export default function Board() {
//   const { activeRole } = useAuth();
//   const [tasks, setTasks] = useState([]);

//   const fetchTasks = async () => {
//     const data = await getTasks();
//     setTasks(data);
//   };

//   useEffect(() => {
//     fetchTasks();
//   }, [activeRole]);

//   // 🔁 Group & sort tasks
//   const grouped = STATUSES.reduce((acc, s) => {
//     acc[s.key] = tasks
//       .filter((t) => t.status === s.key)
//       .sort(
//         (a, b) =>
//           priorityRank[a.priority] - priorityRank[b.priority]
//       );
//     return acc;
//   }, {});

//   // 🧲 HANDLE DRAG END
//   const onDragEnd = async (result) => {
//     const { source, destination, draggableId } = result;

//     if (!destination) return;
//     if (
//       source.droppableId === destination.droppableId
//     )
//       return;

//     const taskId = Number(draggableId);
//     const newStatus = destination.droppableId;

//     try {
//       // Optimistic UI update
//       setTasks((prev) =>
//         prev.map((t) =>
//           t.t_id === taskId
//             ? { ...t, status: newStatus }
//             : t
//         )
//       );

//       await updateTaskStatus(taskId, {
//         status: newStatus,
//       });
//     } catch {
//       fetchTasks(); // rollback if failed
//     }
//   };

//   return (
//     <DragDropContext onDragEnd={onDragEnd}>
//       <div className="h-full px-6 py-4">
//         <div className="grid grid-cols-4 gap-4 h-full">

//           {STATUSES.map((col) => (
//             <Droppable
//               key={col.key}
//               droppableId={col.key}
//             >
//               {(provided) => (
//                 <div
//                   ref={provided.innerRef}
//                   {...provided.droppableProps}
//                   className={`flex flex-col rounded-lg ${col.color}`}
//                 >
//                   {/* COLUMN HEADER */}
//                   <div className="px-3 py-2 border-b">
//                     <h2 className="text-sm font-semibold text-gray-700">
//                       {col.label}
//                     </h2>
//                   </div>

//                   {/* COLUMN BODY */}
//                   <div className="flex-1 overflow-y-auto p-3 space-y-3">
//                     {grouped[col.key]?.length === 0 && (
//                       <p className="text-sm text-gray-400 text-center mt-4">
//                         No tasks
//                       </p>
//                     )}

//                     {grouped[col.key]?.map((task, index) => (
//                       <TaskCard
//                         key={task.t_id}
//                         task={task}
//                         index={index}
//                         role={activeRole}
//                         refresh={fetchTasks}
//                       />
//                     ))}
//                     {provided.placeholder}
//                   </div>
//                 </div>
//               )}
//             </Droppable>
//           ))}

//         </div>
//       </div>
//     </DragDropContext>
//   );
// }


// import { useEffect, useState } from "react";
// import { DragDropContext, Droppable, Draggable } from "@hello-pangea/dnd";
// import { getTasks, updateTaskStatus } from "../api/task.api";
// import TaskCard from "../components/TaskCard";
// import ReviewModal from "../components/ReviewModal";
// import { useAuth } from "../context/AuthContext";

// const STATUSES = [
//   { key: "TO_DO", label: "TO DO", color: "bg-gray-100" },
//   { key: "IN_PROGRESS", label: "IN PROGRESS", color: "bg-blue-50" },
//   { key: "REVIEW", label: "REVIEW", color: "bg-yellow-50" },
//   { key: "DONE", label: "COMPLETED", color: "bg-green-50" },
// ];

// const priorityRank = {
//   HIGH: 1,
//   MEDIUM: 2,
//   LOW: 3,
// };

// export default function Board() {
//   const { activeRole } = useAuth();

//   const [tasks, setTasks] = useState([]);
//   const [grouped, setGrouped] = useState({});
//   const [pendingReview, setPendingReview] = useState(null);

//   // 🔹 Fetch tasks
//   const fetchTasks = async () => {
//     const data = await getTasks();
//     setTasks(data);
//   };

//   useEffect(() => {
//     fetchTasks();
//   }, [activeRole]);

//   // 🔹 Group + sort
//   useEffect(() => {
//     const map = {
//       TO_DO: [],
//       IN_PROGRESS: [],
//       REVIEW: [],
//       DONE: [],
//     };

//     tasks.forEach((t) => map[t.status]?.push(t));

//     Object.keys(map).forEach((status) => {
//       map[status].sort(
//         (a, b) =>
//           priorityRank[a.priority] -
//           priorityRank[b.priority]
//       );
//     });

//     setGrouped(map);
//   }, [tasks]);

//   // 🔹 Drag handler
//   const onDragEnd = async (result) => {
//     const { source, destination, draggableId } = result;
//     if (!destination) return;

//     const taskId = Number(draggableId);
//     const from = source.droppableId;
//     const to = destination.droppableId;

//     // 🔴 MANAGER REVIEW FLOW
//     if (
//       activeRole === "MANAGER" &&
//       from === "REVIEW" &&
//       (to === "IN_PROGRESS" || to === "DONE")
//     ) {
//       setPendingReview({
//         taskId,
//         newStatus: to,
//       });
//       return;
//     }

//     // ✅ NORMAL FLOW
//     try {
//       setTasks((prev) =>
//         prev.map((t) =>
//           t.t_id === taskId
//             ? { ...t, status: to }
//             : t
//         )
//       );

//       await updateTaskStatus(taskId, {
//         status: to,
//       });
//     } catch {
//       fetchTasks();
//     }
//   };

//   return (
//     <>
//       <DragDropContext onDragEnd={onDragEnd}>
//         <div className="h-full px-6 py-4">
//           <div className="grid grid-cols-4 gap-4 h-full">

//             {STATUSES.map((col) => (
//               <Droppable droppableId={col.key} key={col.key}>
//                 {(provided) => (
//                   <div
//                     ref={provided.innerRef}
//                     {...provided.droppableProps}
//                     className={`flex flex-col rounded-lg ${col.color}`}
//                   >
//                     <div className="px-3 py-2 border-b">
//                       <h2 className="text-sm font-semibold">
//                         {col.label}
//                       </h2>
//                     </div>

//                     <div className="flex-1 overflow-y-auto p-3 space-y-3">
//                       {grouped[col.key]?.length === 0 && (
//                         <p className="text-sm text-gray-400 text-center mt-4">
//                           No tasks
//                         </p>
//                       )}

//                       {grouped[col.key]?.map((task, index) => (
//                         <Draggable
//                           key={task.t_id}
//                           draggableId={String(task.t_id)}
//                           index={index}
//                         >
//                           {(provided) => (
//                             <div
//                               ref={provided.innerRef}
//                               {...provided.draggableProps}
//                               {...provided.dragHandleProps}
//                             >
//                               <TaskCard
//                                 task={task}
//                                 role={activeRole}
//                                 refresh={fetchTasks}
//                               />
//                             </div>
//                           )}
//                         </Draggable>
//                       ))}

//                       {provided.placeholder}
//                     </div>
//                   </div>
//                 )}
//               </Droppable>
//             ))}

//           </div>
//         </div>
//       </DragDropContext>

//       {/* 🔹 REVIEW MODAL */}
//       {pendingReview && (
//         <ReviewModal
//           targetStatus={pendingReview.newStatus}
//           onCancel={() => {
//             setPendingReview(null);
//             fetchTasks();
//           }}
//           onSubmit={async (remarks) => {
//             await updateTaskStatus(
//               pendingReview.taskId,
//               {
//                 status: pendingReview.newStatus,
//                 remarks: remarks || null,
//               }
//             );
//             setPendingReview(null);
//             fetchTasks();
//           }}
//         />
//       )}
//     </>
//   );
// }

import { useEffect, useState } from "react";
import { DragDropContext, Droppable, Draggable } from "@hello-pangea/dnd";
import { getTasks, updateTaskStatus } from "../api/task.api";
import TaskCard from "../components/TaskCard";
import { useAuth } from "../context/AuthContext";
import ReviewModal from "../components/ReviewModal";

const STATUSES = [
  { key: "TO_DO", label: "TO DO", bg: "bg-blue-50" },
  { key: "IN_PROGRESS", label: "IN PROGRESS", bg: "bg-cyan-50" },
  { key: "REVIEW", label: "REVIEW", bg: "bg-yellow-50" },
  { key: "DONE", label: "COMPLETED", bg: "bg-green-50" },
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
      map[s].sort(
        (a, b) => priorityRank[a.priority] - priorityRank[b.priority]
      )
    );

    setGrouped(map);
  }, [tasks]);

  const onDragEnd = async (result) => {
    if (!result.destination) return;

    const from = result.source.droppableId;
    const to = result.destination.droppableId;

    if (from === to) return;

    const task = grouped[from][result.source.index];

    if (activeRole === "MANAGER" && task.status === "REVIEW") {
      setReviewTask(task);
      setTargetStatus(to);
      return;
    }

    await updateTaskStatus(task.t_id, { status: to });
    fetchTasks();
  };

  const submitReview = async (remarks) => {
    await updateTaskStatus(reviewTask.t_id, {
      status: targetStatus,
      remarks: remarks || null,
    });

    setReviewTask(null);
    setTargetStatus(null);
    fetchTasks();
  };

  return (
    <div className="h-full px-6 py-4">
      <DragDropContext onDragEnd={onDragEnd}>
        <div className="grid grid-cols-4 gap-4 h-full">

          {STATUSES.map((col) => (
            <div
              key={col.key}
              className={`flex flex-col rounded-lg ${col.bg}`}
            >
              {/* HEADER */}
              <div className="px-3 py-2 border-b font-semibold text-sm">
                {col.label}
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
