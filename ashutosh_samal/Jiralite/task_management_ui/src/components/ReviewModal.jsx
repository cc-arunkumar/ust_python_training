// import { useState } from "react";
// import { createPortal } from "react-dom";

// export default function ReviewModal({
//   targetStatus,
//   onSubmit,
//   onCancel,
// }) {
//   const [remarks, setRemarks] = useState("");

//   return createPortal(
//     <div className="fixed inset-0 z-[9999] bg-black/40 flex items-center justify-center">
//       <div className="bg-white rounded-lg w-96 p-6 space-y-4 shadow-2xl">
//         <h2 className="text-lg font-semibold">
//           Manager Review
//         </h2>

//         <p className="text-sm text-gray-500">
//           Move task to <b>{targetStatus}</b>
//         </p>

//         <textarea
//           placeholder="Add remarks (optional)"
//           className="w-full border rounded p-2 text-sm"
//           rows={4}
//           value={remarks}
//           onChange={(e) => setRemarks(e.target.value)}
//         />

//         <div className="flex justify-end gap-2">
//           <button
//             onClick={onCancel}
//             className="px-4 py-1.5 border rounded"
//           >
//             Cancel
//           </button>

//           <button
//             onClick={() => onSubmit(remarks)}
//             className="px-4 py-1.5 bg-blue-600 text-white rounded"
//           >
//             Submit
//           </button>
//         </div>
//       </div>
//     </div>,
//     document.body
//   );
// }


import { useState, useEffect } from "react";

export default function ReviewModal({
  targetStatus,
  onCancel,
  onSubmit,
}) {
  const [remarks, setRemarks] = useState("");

  // 🔒 Lock background scroll while modal is open
  useEffect(() => {
    document.body.style.overflow = "hidden";
    return () => {
      document.body.style.overflow = "auto";
    };
  }, []);

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center">
      {/* 🔲 Overlay */}
      <div
        className="absolute inset-0 bg-black/40 backdrop-blur-sm"
        onClick={onCancel}
      />

      {/* 📦 Modal */}
      <div className="relative bg-white rounded-xl shadow-2xl w-[380px] p-6 animate-scale-in">
        {/* Header */}
        <h3 className="text-lg font-semibold text-gray-900 mb-1">
          Manager Review
        </h3>

        <p className="text-sm text-gray-500 mb-4">
          Move task to{" "}
          <span className="font-medium text-gray-800">
            {targetStatus}
          </span>
        </p>

        {/* Remarks */}
        <textarea
          placeholder="Add remarks (optional)"
          className="w-full h-24 border rounded-lg p-2 text-sm
                     focus:outline-none focus:ring-2 focus:ring-blue-500
                     resize-none"
          value={remarks}
          onChange={(e) => setRemarks(e.target.value)}
          autoFocus
        />

        {/* Actions */}
        <div className="flex justify-end gap-2 mt-5">
          <button
            onClick={onCancel}
            className="px-4 py-1.5 text-sm border rounded-lg
                       hover:bg-gray-100 transition"
          >
            Cancel
          </button>

          <button
            onClick={() => onSubmit(remarks)}
            className="px-4 py-1.5 text-sm bg-blue-600 text-white
                       rounded-lg hover:bg-blue-700 transition"
          >
            Submit
          </button>
        </div>
      </div>

      {/* 🎞 Animation */}
      <style>
        {`
          @keyframes scale-in {
            0% {
              opacity: 0;
              transform: scale(0.9);
            }
            100% {
              opacity: 1;
              transform: scale(1);
            }
          }

          .animate-scale-in {
            animation: scale-in 0.2s ease-out;
          }
        `}
      </style>
    </div>
  );
}
