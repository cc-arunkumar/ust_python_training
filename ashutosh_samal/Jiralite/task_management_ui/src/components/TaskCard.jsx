// import { useState, useRef, useEffect } from "react";
// import { createPortal } from "react-dom";
// import TaskFilesModal from "./TaskFilesModal";
// import toast from "react-hot-toast";
// import {
//   updateTaskStatus,
//   deleteTask,
//   updateTaskPriority,
//   updateTask,
// } from "../api/task.api";

// /* 🎨 Priority styles */
// const priorityStyles = {
//   HIGH: "border-red-500 text-red-600",
//   MEDIUM: "border-yellow-500 text-yellow-600",
//   LOW: "border-green-500 text-green-600",
// };

// const toISODate = (v) => {
//   if (!v) return "";
//   const d = new Date(v);
//   if (Number.isNaN(d.getTime())) return "";
//   return d.toISOString().slice(0, 10);
// };

// export default function TaskCard({ task, role, refresh }) {
//   const [status, setStatus] = useState(task.status);
//   const [priority, setPriority] = useState(task.priority);
//   const [remarks, setRemarks] = useState("");
//   const [showRemarks, setShowRemarks] = useState(false);
//   const [loading, setLoading] = useState(false);

//   // modal + edit fields
//   const [modalOpen, setModalOpen] = useState(false);
//   const [editTitle, setEditTitle] = useState(task.title);
//   const [editDescription, setEditDescription] = useState(task.description);
//   const [editAssignedTo, setEditAssignedTo] = useState(
//     task.assigned_to ?? task.assignedTo ?? ""
//   );
//   const [editExpectedClosure, setEditExpectedClosure] = useState(
//     toISODate(
//       task.expected_closure ?? task.expectedClosure ?? task.expectedClosureDate
//     )
//   );

//   // notification state (persisted via updateTask.notification when possible)
//   const [notification, setNotification] = useState(task.notification ?? null);

//   // keep local notification in sync when parent task prop updates
//   useEffect(() => {
//     setNotification(task.notification ?? null);
//   }, [task.notification]);

//   // bell popover state + anchor for portal positioning
//   const [bellOpen, setBellOpen] = useState(false);
//   const bellRef = useRef(null);
//   const [anchorRect, setAnchorRect] = useState(null);

//   /* 🔁 STATUS CHANGE */
//   const handleStatusChange = async (newStatus) => {
//     // Manager review → show remark box
//     if (role === "MANAGER" && task.status === "REVIEW") {
//       setStatus(newStatus);
//       setShowRemarks(true);
//       return;
//     }

//     await submitStatus(newStatus);
//   };

//   const submitStatus = async (newStatus) => {
//     try {
//       setLoading(true);

//       // update status + persist manager remarks (server-side)
//       await updateTaskStatus(task.t_id, {
//         status: newStatus,
//         remarks: remarks || null,
//       });

//       // If current user provided remarks (e.g. manager review), create a notification
//       // so the other party (developer/manager) sees it in the bell.
//       if (remarks && remarks.trim() !== "") {
//         const notif = {
//           message: remarks.trim(),
//           from: role,
//           read: false,
//           ts: new Date().toISOString(),
//         };
//         try {
//           // persist notification on task and update local state immediately
//           await updateTask(task.t_id, { notification: notif });
//           setNotification(notif);
//         } catch {
//           // non-blocking — status already updated; notify user if needed
//           console.warn("Failed to persist notification");
//         }
//       }

//       toast.success(`Task moved to ${newStatus.replace("_", " ")}`);
//       refresh();
//       setStatus(newStatus);
//     } catch {
//       toast.error("Failed to update status");
//     } finally {
//       setLoading(false);
//       setShowRemarks(false);
//       setRemarks("");
//     }
//   };

//   /* 🔁 PRIORITY CHANGE */
//   const handlePriorityChange = async (newPriority) => {
//     try {
//       setPriority(newPriority);
//       await updateTaskPriority(task.t_id, newPriority);
//       toast.success(`Priority set to ${newPriority}`);
//       refresh();
//     } catch {
//       toast.error("Failed to update priority");
//     }
//   };

//   /* ✏️ SAVE EDITS (title/description/assigned/expected closure) */
//   const handleSave = async () => {
//     try {
//       setLoading(true);
//       await updateTask(task.t_id, {
//         title: editTitle,
//         description: editDescription,
//         assigned_to: editAssignedTo || null,
//         expected_closure: editExpectedClosure || null,
//       });
//       toast.success("Task updated");
//       refresh();
//       setModalOpen(false);
//     } catch {
//       toast.error("Failed to update task");
//     } finally {
//       setLoading(false);
//     }
//   };

//   /* ❌ DELETE TASK */
//   const handleDelete = async () => {
//     if (!window.confirm(`Delete TASK-${task.t_id}? This cannot be undone.`))
//       return;

//     try {
//       await deleteTask(task.t_id);
//       toast.success(`TASK-${task.t_id} deleted`);
//       refresh();
//       setModalOpen(false);
//     } catch {
//       toast.error("Failed to delete task");
//     }
//   };

//   const openModal = () => {
//     setEditTitle(task.title);
//     setEditDescription(task.description);
//     setEditAssignedTo(task.assigned_to ?? task.assignedTo ?? "");
//     setEditExpectedClosure(
//       toISODate(
//         task.expected_closure ??
//           task.expectedClosure ??
//           task.expectedClosureDate
//       )
//     );
//     setModalOpen(true);
//   };

//   // mark notification as seen (stop jiggle)
//   const markNotificationSeen = async () => {
//     if (!notification || notification.read) {
//       // just toggle viewer open/close when already read or no notification
//       setBellOpen((s) => !s);
//       return;
//     }
//     try {
//       await updateTask(task.t_id, {
//         notification: { ...notification, read: true },
//       });
//       setNotification((n) => (n ? { ...n, read: true } : n));
//       setBellOpen(true);
//       refresh();
//     } catch {
//       toast.error("Failed to mark notification read");
//     }
//   };

//   /* ---------- UI ---------- */

//   // jiggle when there's an unread notification
//   const bellJiggleStyle =
//     notification && notification.read === false
//       ? {
//           animation: "jiggle .8s ease-in-out infinite",
//           transformOrigin: "center",
//           display: "inline-block",
//         }
//       : {};

//   return (
//     <>
//       {/* small keyframes injected here so jiggle works without global css */}
//       <style>
//         {`@keyframes jiggle {
//             0% { transform: rotate(0deg); }
//             25% { transform: rotate(-10deg); }
//             50% { transform: rotate(10deg); }
//             75% { transform: rotate(-6deg); }
//             100% { transform: rotate(0deg); }
//           }`}
//       </style>

//       <div
//         className="bg-white rounded-lg shadow p-4 space-y-2 cursor-pointer hover:ring-1 hover:ring-gray-300 transition"
//         onClick={openModal}
//       >
//         {/* 🔹 TASK ID + PRIORITY */}
//         <div
//           className="flex justify-between items-center"
//           onClick={(e) => e.stopPropagation()}
//         >
//           <span className="text-xs text-gray-500">TASK-{task.t_id}</span>

//           {role === "ADMIN" || role === "MANAGER" ? (
//             <select
//               value={priority}
//               onChange={(e) => handlePriorityChange(e.target.value)}
//               className={`text-xs font-semibold px-2 py-1 rounded border ${priorityStyles[priority]}`}
//             >
//               <option value="HIGH">HIGH</option>
//               <option value="MEDIUM">MEDIUM</option>
//               <option value="LOW">LOW</option>
//             </select>
//           ) : (
//             <span
//               className={`text-xs font-semibold px-2 py-1 rounded border ${priorityStyles[priority]}`}
//             >
//               {priority}
//             </span>
//           )}
//         </div>

//         {/* 🔹 TITLE */}
//         <h3 className="font-semibold text-gray-800">{task.title}</h3>

//         {/* 🔹 DESCRIPTION */}
//         <p className="text-sm text-gray-600 line-clamp-3">{task.description}</p>

//         {/* 🔴 ACTIONS: notification bell + delete */}
//         <div
//           className="flex items-center justify-end gap-2 mt-2"
//           onClick={(e) => e.stopPropagation()}
//         >
//           {/* Delete icon (left of bell) */}
//           {(role === "ADMIN" || role === "MANAGER") && (
//             <button
//               onClick={(e) => {
//                 e.stopPropagation();
//                 handleDelete();
//               }}
//               title="Delete task"
//               aria-label="Delete task"
//               className="p-1 text-red-500 hover:text-red-700 transition rounded flex items-center justify-center"
//             >
//               <svg
//                 xmlns="http://www.w3.org/2000/svg"
//                 className="w-4 h-4"
//                 fill="none"
//                 viewBox="0 0 24 24"
//                 stroke="currentColor"
//                 strokeWidth={2}
//               >
//                 <path
//                   strokeLinecap="round"
//                   strokeLinejoin="round"
//                   d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6M9 7h6m-7 0V5a1 1 0 011-1h4a1 1 0 011 1v2"
//                 />
//               </svg>
//             </button>
//           )}

//           {/* Notification bell (viewer only) */}
//           <div className="relative">
//             <button
//               ref={bellRef}
//               onClick={async (e) => {
//                 e.stopPropagation();
//                 if (bellRef.current) {
//                   const rect = bellRef.current.getBoundingClientRect();
//                   setAnchorRect(rect);
//                 } else {
//                   setAnchorRect(null);
//                 }

//                 if (notification && notification.read === false) {
//                   await markNotificationSeen();
//                 } else {
//                   setBellOpen((s) => !s);
//                 }
//               }}
//               aria-label="View remarks"
//               className="p-1 text-gray-600 hover:text-gray-800 rounded flex items-center justify-center"
//               style={bellJiggleStyle}
//             >
//               <svg
//                 xmlns="http://www.w3.org/2000/svg"
//                 className="w-5 h-5"
//                 fill="none"
//                 viewBox="0 0 24 24"
//                 stroke="currentColor"
//                 strokeWidth={2}
//               >
//                 <path
//                   strokeLinecap="round"
//                   strokeLinejoin="round"
//                   d="M15 17h5l-1.405-1.405A2.032 2.032 0 0118 14.158V11a6 6 0 10-12 0v3.159c0 .538-.214 1.055-.595 1.436L4 17h5m6 0a3 3 0 11-6 0h6z"
//                 />
//               </svg>
//             </button>

//             {/* unread badge */}
//             {notification && notification.read === false && (
//               <span className="absolute -top-1 -right-1 w-2.5 h-2.5 bg-red-500 rounded-full" />
//             )}

//             {/* bell popover rendered via portal to avoid parent stacking/transform issues */}
//             {bellOpen &&
//               createPortal(
//                 <div
//                   role="dialog"
//                   aria-label={`Remarks for TASK-${task.t_id}`}
//                   onClick={(e) => e.stopPropagation()}
//                   style={{
//                     position: "fixed",
//                     top: anchorRect ? anchorRect.bottom + 8 : "50%",
//                     left: anchorRect
//                       ? Math.max(8, anchorRect.right - 288)
//                       : "50%",
//                     width: 288,
//                     zIndex: 9999,
//                     transform: anchorRect ? "none" : "translate(-50%, -50%)",
//                   }}
//                 >
//                   <div className="bg-white border rounded shadow-lg p-3">
//                     {notification ? (
//                       <div>
//                         <div className="text-xs text-gray-500 mb-1">Remark</div>
//                         <div className="text-sm text-gray-800 mb-2 whitespace-pre-wrap">
//                           {notification.message}
//                         </div>
//                         <div className="text-xs text-gray-400">
//                           From: {notification.from} •{" "}
//                           {new Date(notification.ts).toLocaleString()}
//                         </div>
//                         <div className="mt-2 flex justify-end">
//                           <button
//                             onClick={(e) => {
//                               e.stopPropagation();
//                               setBellOpen(false);
//                             }}
//                             className="text-xs px-2 py-1 bg-gray-100 rounded"
//                           >
//                             Close
//                           </button>
//                           <button
//                             onClick={async (e) => {
//                               e.stopPropagation();
//                               await updateTask(task.t_id, {
//                                 notification: null,
//                               });
//                               setNotification(null);
//                               refresh();
//                               setBellOpen(false);
//                             }}
//                             className="ml-2 text-xs px-2 py-1 bg-red-600 text-white rounded"
//                           >
//                             Clear
//                           </button>
//                         </div>
//                       </div>
//                     ) : (
//                       <div className="text-sm text-gray-600">No remarks</div>
//                     )}
//                   </div>
//                 </div>,
//                 document.body
//               )}
//           </div>
//         </div>
//       </div>

//       {/* MODAL - centered with blurred background */}
//       {modalOpen && (
//         <div
//           className="fixed inset-0 z-40 flex items-center justify-center"
//           onClick={() => setModalOpen(false)}
//         >
//           <div className="absolute inset-0 bg-black/30 backdrop-blur-sm" />

//           <div
//             className="relative z-50 w-full max-w-lg bg-white rounded-lg shadow-lg p-5 mx-4"
//             onClick={(e) => e.stopPropagation()}
//           >
//             <div className="flex items-start justify-between">
//               <h3 className="text-lg font-semibold">Edit TASK-{task.t_id}</h3>
//               <button
//                 aria-label="Close"
//                 onClick={() => setModalOpen(false)}
//                 className="text-gray-500 hover:text-gray-700"
//               >
//                 ✕
//               </button>
//             </div>

//             <div className="mt-4 space-y-3">
//               <div>
//                 <label className="block text-xs text-gray-600">Title</label>
//                 <input
//                   value={editTitle}
//                   onChange={(e) => setEditTitle(e.target.value)}
//                   className="mt-1 w-full text-sm px-2 py-1 rounded border"
//                 />
//               </div>

//               <div>
//                 <label className="block text-xs text-gray-600">
//                   Description
//                 </label>
//                 <textarea
//                   value={editDescription}
//                   onChange={(e) => setEditDescription(e.target.value)}
//                   className="mt-1 w-full text-sm px-2 py-2 rounded border"
//                 />
//               </div>

//               <div>
//                 <label className="block text-xs text-gray-600">
//                   Assigned To
//                 </label>
//                 <input
//                   value={editAssignedTo}
//                   onChange={(e) => setEditAssignedTo(e.target.value)}
//                   placeholder="Employee id or name"
//                   className="mt-1 w-full text-sm px-2 py-1 rounded border"
//                 />
//               </div>

//               <div>
//                 <label className="block text-xs text-gray-600">
//                   Expected Closure
//                 </label>
//                 <input
//                   type="date"
//                   value={editExpectedClosure}
//                   onChange={(e) => setEditExpectedClosure(e.target.value)}
//                   className="mt-1 w-full text-sm px-2 py-1 rounded border"
//                 />
//               </div>

//               <div>
//                 <label className="block text-xs text-gray-600">Priority</label>
//                 <select
//                   value={priority}
//                   onChange={(e) => handlePriorityChange(e.target.value)}
//                   className={`mt-1 w-full text-sm px-2 py-1 rounded border ${priorityStyles[priority]}`}
//                 >
//                   <option value="HIGH">HIGH</option>
//                   <option value="MEDIUM">MEDIUM</option>
//                   <option value="LOW">LOW</option>
//                 </select>
//               </div>

//               <div>
//                 <label className="block text-xs text-gray-600">Status</label>
//                 <select
//                   value={status}
//                   onChange={(e) => handleStatusChange(e.target.value)}
//                   disabled={loading}
//                   className="mt-1 w-full text-sm px-2 py-1 rounded border"
//                 >
//                   <option value="TO_DO">TO DO</option>
//                   <option value="IN_PROGRESS">IN PROGRESS</option>
//                   <option value="REVIEW">REVIEW</option>
//                   {(role === "MANAGER" || role === "ADMIN") && (
//                     <option value="DONE">DONE</option>
//                   )}
//                 </select>
//               </div>
//             </div>

//             <div className="mt-4 flex justify-end gap-2">
//               <button
//                 onClick={() => setModalOpen(false)}
//                 className="text-sm px-3 py-1 bg-gray-100 rounded"
//                 disabled={loading}
//               >
//                 Cancel
//               </button>

//               <button
//                 onClick={handleSave}
//                 className="text-sm px-3 py-1 bg-blue-600 text-white rounded"
//                 disabled={loading}
//               >
//                 {loading ? "Saving..." : "Save"}
//               </button>
//             </div>
//           </div>
//         </div>
//       )}
//     </>
//   );
// }


import { useState, useRef, useEffect } from "react";
import { createPortal } from "react-dom";
import toast from "react-hot-toast";
import TaskFilesModal from "./TaskFilesModal";  // Import the TaskFilesModal component
import {
  updateTaskStatus,
  deleteTask,
  updateTaskPriority,
  updateTask,  
} from "../api/task.api";  

import {
  uploadTaskFile,  // Add function for uploading task files
  getTaskFiles,     // Add function for getting task files
} from "../api/taskFiles.api";

/* 🎨 Priority styles */
const priorityStyles = {
  HIGH: "border-red-500 text-red-600",
  MEDIUM: "border-yellow-500 text-yellow-600",
  LOW: "border-green-500 text-green-600",
};

const toISODate = (v) => {
  if (!v) return "";
  const d = new Date(v);
  if (Number.isNaN(d.getTime())) return "";
  return d.toISOString().slice(0, 10);
};

export default function TaskCard({ task, role, refresh }) {
  const [status, setStatus] = useState(task.status);
  const [priority, setPriority] = useState(task.priority);
  const [remarks, setRemarks] = useState("");
  const [showRemarks, setShowRemarks] = useState(false);
  const [loading, setLoading] = useState(false);

  // New state for file modal
  const [showFiles, setShowFiles] = useState(false);

  // modal + edit fields
  const [modalOpen, setModalOpen] = useState(false);
  const [editTitle, setEditTitle] = useState(task.title);
  const [editDescription, setEditDescription] = useState(task.description);
  const [editAssignedTo, setEditAssignedTo] = useState(task.assigned_to ?? task.assignedTo ?? "");
  const [editExpectedClosure, setEditExpectedClosure] = useState(toISODate(task.expected_closure ?? task.expectedClosure ?? task.expectedClosureDate));

  // notification state (persisted via updateTask.notification when possible)
  const [notification, setNotification] = useState(task.notification ?? null);

  // keep local notification in sync when parent task prop updates
  useEffect(() => {
    setNotification(task.notification ?? null);
  }, [task.notification]);

  // bell popover state + anchor for portal positioning
  const [bellOpen, setBellOpen] = useState(false);
  const bellRef = useRef(null);
  const [anchorRect, setAnchorRect] = useState(null);

  /* 🔁 STATUS CHANGE */
  const handleStatusChange = async (newStatus) => {
    // Manager review → show remark box
    if (role === "MANAGER" && task.status === "REVIEW") {
      setStatus(newStatus);
      setShowRemarks(true);
      return;
    }
    await submitStatus(newStatus);
  };

  const submitStatus = async (newStatus) => {
    try {
      setLoading(true);

      // update status + persist manager remarks (server-side)
      await updateTaskStatus(task.t_id, { status: newStatus, remarks: remarks || null });

      // If current user provided remarks (e.g. manager review), create a notification
      // so the other party (developer/manager) sees it in the bell.
      if (remarks && remarks.trim() !== "") {
        const notif = { message: remarks.trim(), from: role, read: false, ts: new Date().toISOString() };
        try {
          // persist notification on task and update local state immediately
          await updateTask(task.t_id, { notification: notif });
          setNotification(notif);
        } catch {
          console.warn("Failed to persist notification");
        }
      }

      toast.success(`Task moved to ${newStatus.replace("_", " ")}`);
      refresh();
      setStatus(newStatus);
    } catch {
      toast.error("Failed to update status");
    } finally {
      setLoading(false);
      setShowRemarks(false);
      setRemarks("");
    }
  };

  /* 🔁 PRIORITY CHANGE */
  const handlePriorityChange = async (newPriority) => {
    try {
      setPriority(newPriority);
      await updateTaskPriority(task.t_id, newPriority);
      toast.success(`Priority set to ${newPriority}`);
      refresh();
    } catch {
      toast.error("Failed to update priority");
    }
  };

  /* ✏️ SAVE EDITS (title/description/assigned/expected closure) */
  const handleSave = async () => {
    try {
      setLoading(true);
      await updateTask(task.t_id, {
        title: editTitle,
        description: editDescription,
        assigned_to: editAssignedTo || null,
        expected_closure: editExpectedClosure || null,
      });
      toast.success("Task updated");
      refresh();
      setModalOpen(false);
    } catch {
      toast.error("Failed to update task");
    } finally {
      setLoading(false);
    }
  };

  /* ❌ DELETE TASK */
  const handleDelete = async () => {
    if (!window.confirm(`Delete TASK-${task.t_id}? This cannot be undone.`)) return;

    try {
      await deleteTask(task.t_id);
      toast.success(`TASK-${task.t_id} deleted`);
      refresh();
      setModalOpen(false);
    } catch {
      toast.error("Failed to delete task");
    }
  };

  const openModal = () => {
    setEditTitle(task.title);
    setEditDescription(task.description);
    setEditAssignedTo(task.assigned_to ?? task.assignedTo ?? "");
    setEditExpectedClosure(toISODate(task.expected_closure ?? task.expectedClosure ?? task.expectedClosureDate));
    setModalOpen(true);
  };

  // mark notification as seen (stop jiggle)
  const markNotificationSeen = async () => {
    if (!notification || notification.read) {
      setBellOpen((s) => !s);
      return;
    }
    try {
      await updateTask(task.t_id, { notification: { ...notification, read: true } });
      setNotification((n) => (n ? { ...n, read: true } : n));
      setBellOpen(true);
      refresh();
    } catch {
      toast.error("Failed to mark notification read");
    }
  };

  /* ---------- UI ---------- */

  // jiggle when there's an unread notification
  const bellJiggleStyle = notification && notification.read === false
    ? {
        animation: "jiggle .8s ease-in-out infinite",
        transformOrigin: "center",
        display: "inline-block",
      }
    : {};

  return (
    <>
      {/* small keyframes injected here so jiggle works without global css */}
      <style>
        {`@keyframes jiggle {
            0% { transform: rotate(0deg); }
            25% { transform: rotate(-10deg); }
            50% { transform: rotate(10deg); }
            75% { transform: rotate(-6deg); }
            100% { transform: rotate(0deg); }
          }`}
      </style>

      <div
        className="bg-white rounded-lg shadow p-4 space-y-2 cursor-pointer hover:ring-1 hover:ring-gray-300 transition"
        onClick={openModal}
      >
        {/* 🔹 TASK ID + PRIORITY */}
        <div
          className="flex justify-between items-center"
          onClick={(e) => e.stopPropagation()}
        >
          <span className="text-xs text-gray-500">TASK-{task.t_id}</span>

          {role === "ADMIN" || role === "MANAGER" ? (
            <select
              value={priority}
              onChange={(e) => handlePriorityChange(e.target.value)}
              className={`text-xs font-semibold px-2 py-1 rounded border ${priorityStyles[priority]}`}
            >
              <option value="HIGH">HIGH</option>
              <option value="MEDIUM">MEDIUM</option>
              <option value="LOW">LOW</option>
            </select>
          ) : (
            <span
              className={`text-xs font-semibold px-2 py-1 rounded border ${priorityStyles[priority]}`}
            >
              {priority}
            </span>
          )}
        </div>

        {/* 🔹 TITLE */}
        <h3 className="font-semibold text-gray-800">{task.title}</h3>

        {/* 🔹 DESCRIPTION */}
        <p className="text-sm text-gray-600 line-clamp-3">{task.description}</p>

        {/* 🔴 ACTIONS: notification bell + delete */}
        <div
          className="flex items-center justify-end gap-2 mt-2"
          onClick={(e) => e.stopPropagation()}
        >
          {/* File upload/download button */}
          <button
            onClick={(e) => {
              e.stopPropagation();
              setShowFiles(true);
            }}
            title="Files"
            className="p-1 text-gray-600 hover:text-gray-800"
          >
            📎
          </button>

          {/* Delete icon */}
          {(role === "ADMIN" || role === "MANAGER") && (
            <button
              onClick={(e) => {
                e.stopPropagation();
                handleDelete();
              }}
              title="Delete task"
              aria-label="Delete task"
              className="p-1 text-red-500 hover:text-red-700 transition rounded flex items-center justify-center"
            >
              <svg
                xmlns="http://www.w3.org/2000/svg"
                className="w-4 h-4"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
                strokeWidth={2}
              >
                <path
                  strokeLinecap="round"
                  strokeLinejoin="round"
                  d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6M9 7h6m-7 0V5a1 1 0 011-1h4a1 1 0 011 1v2"
                />
              </svg>
            </button>
          )}

          {/* Notification bell */}
          <div className="relative">
            <button
              ref={bellRef}
              onClick={async (e) => {
                e.stopPropagation();
                if (bellRef.current) {
                  const rect = bellRef.current.getBoundingClientRect();
                  setAnchorRect(rect);
                } else {
                  setAnchorRect(null);
                }

                if (notification && notification.read === false) {
                  await markNotificationSeen();
                } else {
                  setBellOpen((s) => !s);
                }
              }}
              aria-label="View remarks"
              className="p-1 text-gray-600 hover:text-gray-800 rounded flex items-center justify-center"
              style={bellJiggleStyle}
            >
              <svg
                xmlns="http://www.w3.org/2000/svg"
                className="w-5 h-5"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
                strokeWidth={2}
              >
                <path
                  strokeLinecap="round"
                  strokeLinejoin="round"
                  d="M15 17h5l-1.405-1.405A2.032 2.032 0 0118 14.158V11a6 6 0 10-12 0v3.159c0 .538-.214 1.055-.595 1.436L4 17h5m6 0a3 3 0 11-6 0h6z"
                />
              </svg>
            </button>

            {/* unread badge */}
            {notification && notification.read === false && (
              <span className="absolute -top-1 -right-1 w-2.5 h-2.5 bg-red-500 rounded-full" />
            )}
          </div>
        </div>
      </div>

      {/* Task Files Modal */}
      {showFiles && (
        <TaskFilesModal
          task={task}
          onClose={() => setShowFiles(false)}
        />
      )}

      {/* MODAL - centered with blurred background */}
      {modalOpen && (
        <div
          className="fixed inset-0 z-40 flex items-center justify-center"
          onClick={() => setModalOpen(false)}
        >
          <div className="absolute inset-0 bg-black/30 backdrop-blur-sm" />

          <div
            className="relative z-50 w-full max-w-lg bg-white rounded-lg shadow-lg p-5 mx-4"
            onClick={(e) => e.stopPropagation()}
          >
            <div className="flex items-start justify-between">
              <h3 className="text-lg font-semibold">Edit TASK-{task.t_id}</h3>
              <button
                aria-label="Close"
                onClick={() => setModalOpen(false)}
                className="text-gray-500 hover:text-gray-700"
              >
                ✕
              </button>
            </div>

            <div className="mt-4 space-y-3">
              <div>
                <label className="block text-xs text-gray-600">Title</label>
                <input
                  value={editTitle}
                  onChange={(e) => setEditTitle(e.target.value)}
                  className="mt-1 w-full text-sm px-2 py-1 rounded border"
                />
              </div>

              <div>
                <label className="block text-xs text-gray-600">
                  Description
                </label>
                <textarea
                  value={editDescription}
                  onChange={(e) => setEditDescription(e.target.value)}
                  className="mt-1 w-full text-sm px-2 py-2 rounded border"
                />
              </div>

              <div>
                <label className="block text-xs text-gray-600">
                  Assigned To
                </label>
                <input
                  value={editAssignedTo}
                  onChange={(e) => setEditAssignedTo(e.target.value)}
                  placeholder="Employee id or name"
                  className="mt-1 w-full text-sm px-2 py-1 rounded border"
                />
              </div>

              <div>
                <label className="block text-xs text-gray-600">
                  Expected Closure
                </label>
                <input
                  type="date"
                  value={editExpectedClosure}
                  onChange={(e) => setEditExpectedClosure(e.target.value)}
                  className="mt-1 w-full text-sm px-2 py-1 rounded border"
                />
              </div>

              <div>
                <label className="block text-xs text-gray-600">Priority</label>
                <select
                  value={priority}
                  onChange={(e) => handlePriorityChange(e.target.value)}
                  className={`mt-1 w-full text-sm px-2 py-1 rounded border ${priorityStyles[priority]}`}
                >
                  <option value="HIGH">HIGH</option>
                  <option value="MEDIUM">MEDIUM</option>
                  <option value="LOW">LOW</option>
                </select>
              </div>

              <div>
                <label className="block text-xs text-gray-600">Status</label>
                <select
                  value={status}
                  onChange={(e) => handleStatusChange(e.target.value)}
                  disabled={loading}
                  className="mt-1 w-full text-sm px-2 py-1 rounded border"
                >
                  <option value="TO_DO">TO DO</option>
                  <option value="IN_PROGRESS">IN PROGRESS</option>
                  <option value="REVIEW">REVIEW</option>
                  {(role === "MANAGER" || role === "ADMIN") && (
                    <option value="DONE">DONE</option>
                  )}
                </select>
              </div>
            </div>

            <div className="mt-4 flex justify-end gap-2">
              <button
                onClick={() => setModalOpen(false)}
                className="text-sm px-3 py-1 bg-gray-100 rounded"
                disabled={loading}
              >
                Cancel
              </button>

              <button
                onClick={handleSave}
                className="text-sm px-3 py-1 bg-blue-600 text-white rounded"
                disabled={loading}
              >
                {loading ? "Saving..." : "Save"}
              </button>
            </div>
          </div>
        </div>
      )}
    </>
  );
}
