// import { useState } from "react";
// import { updateTaskStatus } from "../api/task.api";
// import { useNavigate } from "react-router-dom";

// const priorityColors = {
//   HIGH: "border-red-500 text-red-600",
//   MEDIUM: "border-yellow-500 text-yellow-600",
//   LOW: "border-green-500 text-green-600",
// };

// export default function TaskCard({ task, role, refresh }) {
//   const navigate = useNavigate();

//   const [status, setStatus] = useState(task.status);
//   const [remarks, setRemarks] = useState("");
//   const [showRemarks, setShowRemarks] = useState(false);
//   const [loading, setLoading] = useState(false);

//   /* 🔹 CLICK CARD → EDIT TASK */
//   const handleCardClick = () => {
//     if (role === "ADMIN" || role === "MANAGER") {
//       navigate(`/tasks/${task.t_id}/edit`);
//     }
//   };

//   const handleStatusChange = async (newStatus) => {
//     // Manager reviewing
//     if (role === "MANAGER" && task.status === "REVIEW") {
//       setShowRemarks(true);
//       setStatus(newStatus);
//       return;
//     }
//     await updateStatus(newStatus);
//   };

//   const updateStatus = async (newStatus) => {
//     try {
//       setLoading(true);
//       await updateTaskStatus(task.t_id, {
//         status: newStatus,
//         remarks: remarks || null,
//       });
//       refresh(); // 🔥 realtime update
//     } finally {
//       setLoading(false);
//       setShowRemarks(false);
//       setRemarks("");
//     }
//   };

//   return (
//     <div
//       onClick={handleCardClick}
//       className={`bg-white rounded-lg shadow p-4 space-y-2 cursor-pointer
//         ${
//           role === "DEVELOPER"
//             ? "cursor-not-allowed opacity-90"
//             : "hover:shadow-md transition"
//         }`}
//     >
//       {/* Task ID + Priority */}
//       <div className="flex justify-between items-center">
//         <span className="text-xs text-gray-500">
//           TASK-{task.t_id}
//         </span>

//         <span
//           className={`text-xs font-semibold px-2 py-1 rounded border ${
//             priorityColors[task.priority]
//           }`}
//         >
//           {task.priority}
//         </span>
//       </div>

//       {/* Title */}
//       <h3 className="font-semibold text-gray-800">
//         {task.title}
//       </h3>

//       {/* Description */}
//       <p className="text-sm text-gray-600 line-clamp-3">
//         {task.description}
//       </p>

//       {/* STOP PROPAGATION FOR STATUS */}
//       <div onClick={(e) => e.stopPropagation()}>
//         <select
//           value={status}
//           onChange={(e) => handleStatusChange(e.target.value)}
//           disabled={loading}
//           className="w-full border rounded px-2 py-1 text-sm"
//         >
//           <option value="TO_DO">TO DO</option>
//           <option value="IN_PROGRESS">IN PROGRESS</option>
//           <option value="REVIEW">REVIEW</option>
//           {role === "MANAGER" && (
//             <option value="DONE">DONE</option>
//           )}
//         </select>
//       </div>

//       {/* Manager Review Box */}
//       {showRemarks && role === "MANAGER" && (
//         <div
//           className="space-y-2"
//           onClick={(e) => e.stopPropagation()}
//         >
//           <textarea
//             placeholder="Add review remarks (optional)"
//             className="w-full border rounded p-2 text-sm"
//             value={remarks}
//             onChange={(e) => setRemarks(e.target.value)}
//           />

//           <div className="flex justify-end gap-2">
//             <button
//               onClick={() => setShowRemarks(false)}
//               className="text-sm px-3 py-1 border rounded"
//             >
//               Cancel
//             </button>

//             <button
//               onClick={() => updateStatus(status)}
//               className="text-sm px-3 py-1 bg-blue-600 text-white rounded"
//             >
//               Submit Review
//             </button>
//           </div>
//         </div>
//       )}
//     </div>
//   );
// }

import { useState } from "react";
import { updateTaskStatus, deleteTask } from "../api/task.api";
import { useNavigate } from "react-router-dom";

const priorityColors = {
  HIGH: "border-red-500 text-red-600",
  MEDIUM: "border-yellow-500 text-yellow-600",
  LOW: "border-green-500 text-green-600",
};

export default function TaskCard({ task, role, refresh }) {
  const [status, setStatus] = useState(task.status);
  const [remarks, setRemarks] = useState("");
  const [showRemarks, setShowRemarks] = useState(false);
  const [loading, setLoading] = useState(false);
  const navigate = useNavigate();

  const handleStatusChange = async (newStatus) => {
    if (role === "MANAGER" && task.status === "REVIEW") {
      setShowRemarks(true);
      setStatus(newStatus);
      return;
    }
    await updateStatus(newStatus);
  };

  const updateStatus = async (newStatus) => {
    try {
      setLoading(true);
      await updateTaskStatus(task.t_id, {
        status: newStatus,
        remarks: remarks || null,
      });
      refresh();
    } finally {
      setLoading(false);
      setShowRemarks(false);
      setRemarks("");
    }
  };

  // ✅ DELETE TASK
  const handleDelete = async () => {
    const confirm = window.confirm(
      `Delete TASK-${task.t_id}? This cannot be undone.`
    );
    if (!confirm) return;

    await deleteTask(task.t_id);
    refresh();
  };

  return (
    <div className="bg-white rounded-lg shadow p-4 space-y-2">
      {/* Task ID + Priority */}
      <div className="flex justify-between items-center">
        <span className="text-xs text-gray-500">
          TASK-{task.t_id}
        </span>

        <span
          className={`text-xs font-semibold px-2 py-1 rounded border ${
            priorityColors[task.priority]
          }`}
        >
          {task.priority}
        </span>
      </div>

      {/* Click to Edit */}
      <div
        onClick={() => navigate(`/tasks/${task.t_id}/edit`)}
        className="cursor-pointer"
      >
        <h3 className="font-semibold text-gray-800">
          {task.title}
        </h3>

        <p className="text-sm text-gray-600">
          {task.description}
        </p>
      </div>

      {/* Status */}
      <select
        value={status}
        onChange={(e) => handleStatusChange(e.target.value)}
        disabled={loading}
        className="w-full border rounded px-2 py-1 text-sm"
      >
        <option value="TO_DO">TO DO</option>
        <option value="IN_PROGRESS">IN PROGRESS</option>
        <option value="REVIEW">REVIEW</option>
        {role === "MANAGER" && <option value="DONE">DONE</option>}
      </select>

      {/* Manager Remarks */}
      {showRemarks && role === "MANAGER" && (
        <div className="space-y-2">
          <textarea
            placeholder="Add review remarks (optional)"
            className="w-full border rounded p-2 text-sm"
            value={remarks}
            onChange={(e) => setRemarks(e.target.value)}
          />

          <div className="flex justify-end gap-2">
            <button
              onClick={() => setShowRemarks(false)}
              className="text-sm px-3 py-1 border rounded"
            >
              Cancel
            </button>

            <button
              onClick={() => updateStatus(status)}
              className="text-sm px-3 py-1 bg-blue-600 text-white rounded"
            >
              Submit Review
            </button>
          </div>
        </div>
      )}

      {/* 🔴 DELETE BUTTON */}
      {(role === "ADMIN" || role === "MANAGER") && (
        <button
          onClick={handleDelete}
          className="text-xs text-red-600 hover:underline mt-2"
        >
          Delete Task
        </button>
      )}
    </div>
  );
}
