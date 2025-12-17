import React, { useState, useEffect } from "react";
import { X, Edit, Clock } from "lucide-react";
import api from "../api/api";

function normalizeRemarks(task = {}) {
  const remarks = [];

  function pushRemark(from, text, by, ts) {
    if (!text || String(text).trim() === "") return;
    remarks.push({
      from: from || "unknown",
      text: String(text).trim(),
      by: by || null,
      ts: ts || null,
    });
  }

  // Single review field
  if (task.review && typeof task.review === "string") {
    pushRemark("review", task.review, task.reviewed_by, task.review_ts);
  }

  // Arrays: remarks, comments, reviews, history
  const arrays = [
    "remarks",
    "comments",
    "reviews",
    "status_history",
    "history",
  ];

  arrays.forEach((k) => {
    const a = task[k];
    if (Array.isArray(a)) {
      a.forEach((it) => {
        if (!it) return;
        const text =
          it.text ||
          it.comment ||
          it.remark ||
          it.message ||
          it.review ||
          it.note ||
          null;
        const from =
          it.from ||
          it.by_role ||
          it.role ||
          it.type ||
          (it.by ? (typeof it.by === "object" ? it.by.role : it.by) : null) ||
          null;
        const by =
          typeof it.by === "object"
            ? it.by.name || it.by.username
            : it.by || it.author || it.user || null;
        const ts =
          it.ts ||
          it.time ||
          it.created_at ||
          it.createdAt ||
          it.timestamp ||
          null;
        pushRemark(from || "unknown", text, by, ts);
      });
    }
  });

  // Developer remarks array
  if (Array.isArray(task.developer_remarks)) {
    task.developer_remarks.forEach((r) =>
      pushRemark(
        "developer",
        r.text || r.remark || r.comment || r.review,
        r.by || r.developer_by,
        r.ts || r.developer_ts || r.timestamp
      )
    );
  }

  // Reviewer remarks array
  if (Array.isArray(task.reviewer_remarks)) {
    task.reviewer_remarks.forEach((r) =>
      pushRemark(
        "reviewer",
        r.text || r.remark || r.comment || r.review,
        r.by || r.reviewer_by,
        r.ts || r.reviewer_ts || r.timestamp
      )
    );
  }

  // client-side optimistic remarks (injected locally)
  if (Array.isArray(task._clientRemarks)) {
    task._clientRemarks.forEach((r) => {
      pushRemark(
        r.from || "client",
        r.text || r.remark || r.comment,
        r.by || null,
        r.ts || null
      );
    });
  }

  // Single developer remark/review fields
  if (task.developer_remark && typeof task.developer_remark === "string") {
    pushRemark(
      "developer",
      task.developer_remark,
      task.developer_by,
      task.developer_ts
    );
  }

  if (task.developer_review && typeof task.developer_review === "string") {
    pushRemark(
      "developer",
      task.developer_review,
      task.developer_by,
      task.developer_ts
    );
  }

  // Single reviewer remark/review fields
  if (task.reviewer_remark && typeof task.reviewer_remark === "string") {
    pushRemark(
      "reviewer",
      task.reviewer_remark,
      task.reviewer_by,
      task.reviewer_ts
    );
  }

  if (task.reviewer_review && typeof task.reviewer_review === "string") {
    pushRemark(
      "reviewer",
      task.reviewer_review,
      task.reviewer_by,
      task.reviewer_ts
    );
  }

  return remarks;
}

export default function TaskDetailModal({
  task = {},
  employees = [],
  onClose = () => {},
  onEdit = () => {},
}) {
  const [readRemarks, setReadRemarks] = useState(new Set());
  const [serverReviews, setServerReviews] = useState([]);

  useEffect(() => {
    let mounted = true;
    if (task && task.task_id) {
      api
        .getTaskReviews(task.task_id)
        .then((res) => {
          if (!mounted) return;
          setServerReviews(res || []);
        })
        .catch((e) => {
          if (!mounted) return;
          console.error("Failed to load task reviews:", e);
          setServerReviews([]);
        });
    } else {
      setServerReviews([]);
    }
    return () => {
      mounted = false;
    };
  }, [task.task_id]);

  useEffect(() => {
    // Load read remarks from localStorage
    const key = `task_${task.task_id}_read_remarks`;
    const stored = localStorage.getItem(key);
    if (stored) {
      try {
        setReadRemarks(new Set(JSON.parse(stored)));
      } catch (e) {
        setReadRemarks(new Set());
      }
    }
  }, [task.task_id]);

  const assignee = employees.find((e) => e.emp_id === task.assigned_to);
  const reviewer = employees.find((e) => e.emp_id === task.reviewer);

  // combine normalized task remarks with server-stored reviews
  const normalized = normalizeRemarks(task);
  const serverMapped = (serverReviews || []).map((s) => ({
    from: s.role || "reviewer",
    text: s.review || s.message || s.comment,
    by:
      s.reviewed_by_name ||
      s.reviewed_by_emp_id ||
      s.reviewed_by_user_id ||
      null,
    ts: s.created_at || null,
  }));

  const remarks = [...normalized, ...serverMapped];

  // Separate remarks by role
  const devRemarks = remarks.filter(
    (r) =>
      String(r.from).toLowerCase().includes("dev") ||
      String(r.from).toLowerCase() === "developer"
  );

  const reviewerRemarks = remarks.filter(
    (r) =>
      String(r.from).toLowerCase().includes("review") ||
      String(r.from).toLowerCase() === "reviewer"
  );

  const otherRemarks = remarks.filter(
    (r) => !devRemarks.includes(r) && !reviewerRemarks.includes(r)
  );

  function isNewRemark(r, index) {
    if (!r || !r.ts) return false;

    // Create unique ID for this remark
    const remarkId = `${r.from}_${r.ts}_${index}`;

    // Check if already read
    if (readRemarks.has(remarkId)) return false;

    const then = Date.parse(r.ts);
    if (isNaN(then)) return false;

    const age = Date.now() - then;
    // Mark as new if within last 7 days
    return age < 7 * 24 * 60 * 60 * 1000;
  }

  const markAsRead = (r, index) => {
    const remarkId = `${r.from}_${r.ts}_${index}`;
    const newReadRemarks = new Set(readRemarks);
    newReadRemarks.add(remarkId);
    setReadRemarks(newReadRemarks);

    // Save to localStorage
    const key = `task_${task.task_id}_read_remarks`;
    localStorage.setItem(key, JSON.stringify([...newReadRemarks]));
  };

  const formatTimestamp = (ts) => {
    if (!ts) return "";
    try {
      const date = new Date(ts);
      return date.toLocaleString("en-US", {
        month: "short",
        day: "numeric",
        year: "numeric",
        hour: "2-digit",
        minute: "2-digit",
      });
    } catch (e) {
      return ts;
    }
  };

  const RemarksSection = ({ title, remarks, type }) => (
    <div>
      <h4 className="text-sm font-semibold text-gray-700 mb-2">{title}</h4>
      <div className="space-y-3">
        {remarks.length ? (
          remarks.map((r, i) => {
            const isNew = isNewRemark(r, i);
            const remarkId = `${type}_${i}`;

            return (
              <div
                key={remarkId}
                className="relative bg-gray-50 rounded-lg p-3 border border-gray-200"
                onClick={() => isNew && markAsRead(r, i)}
              >
                {/* New Badge */}
                {isNew && (
                  <span className="absolute -top-2 -left-2 bg-red-500 text-white text-[10px] font-bold px-2 py-0.5 rounded-full shadow-sm animate-pulse">
                    NEW
                  </span>
                )}

                {/* Index Number */}
                <div className="flex items-start gap-3">
                  <div className="flex-shrink-0 w-6 h-6 rounded-full bg-indigo-100 text-indigo-600 flex items-center justify-center text-xs font-semibold">
                    {i + 1}
                  </div>

                  <div className="flex-1">
                    {/* Metadata */}
                    <div className="flex items-center gap-2 text-xs text-gray-500 mb-1">
                      {r.by && (
                        <span className="font-medium text-gray-700">
                          {r.by}
                        </span>
                      )}
                      {r.ts && (
                        <>
                          <Clock size={10} />
                          <span>{formatTimestamp(r.ts)}</span>
                        </>
                      )}
                    </div>

                    {/* Remark Text */}
                    <div className="text-sm text-gray-800 whitespace-pre-wrap">
                      {r.text}
                    </div>
                  </div>
                </div>
              </div>
            );
          })
        ) : (
          <div className="text-center text-gray-400 text-sm py-4 bg-gray-50 rounded-lg">
            No {title.toLowerCase()} yet
          </div>
        )}
      </div>
    </div>
  );

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/50 p-4">
      <div className="w-full max-w-3xl bg-white rounded-xl shadow-2xl overflow-hidden max-h-[90vh] flex flex-col">
        {/* Header */}
        <div className="flex items-center justify-between px-6 py-4 border-b bg-gradient-to-r from-indigo-50 to-purple-50">
          <div className="flex-1">
            <h2 className="text-lg font-bold text-gray-800">{task.title}</h2>
            <div className="flex items-center gap-3 mt-1 text-sm text-gray-600">
              <span className="px-2 py-0.5 bg-white rounded text-xs font-medium">
                {task.status}
              </span>
              {task.dept_name && <span>• {task.dept_name}</span>}
              {task.priority && (
                <span className="font-semibold">• {task.priority}</span>
              )}
            </div>
          </div>
          <div className="flex items-center gap-2">
            <button
              onClick={() => onEdit()}
              className="px-4 py-2 rounded-lg bg-indigo-600 text-white hover:bg-indigo-700 transition flex items-center gap-2"
            >
              <Edit size={16} />
              Edit
            </button>
            <button
              onClick={onClose}
              className="p-2 rounded-lg hover:bg-gray-100 transition"
            >
              <X size={20} />
            </button>
          </div>
        </div>

        {/* Scrollable Content */}
        <div className="flex-1 overflow-y-auto p-6 space-y-6">
          {/* Description */}
          <div>
            <h3 className="text-sm font-semibold text-gray-600 mb-2">
              Description
            </h3>
            <p className="text-sm text-gray-700 bg-gray-50 p-3 rounded-lg">
              {task.description || "No description provided."}
            </p>
          </div>

          {/* Assignment Info */}
          <div className="grid grid-cols-2 gap-4">
            <div className="bg-blue-50 p-3 rounded-lg">
              <h4 className="text-xs font-semibold text-blue-900 mb-1">
                Assignee
              </h4>
              <div className="text-sm font-medium text-blue-700">
                {assignee ? assignee.emp_name : "Unassigned"}
              </div>
            </div>
            <div className="bg-purple-50 p-3 rounded-lg">
              <h4 className="text-xs font-semibold text-purple-900 mb-1">
                Reviewer
              </h4>
              <div className="text-sm font-medium text-purple-700">
                {reviewer ? reviewer.emp_name : "Not assigned"}
              </div>
            </div>
          </div>

          {/* Developer Remarks */}
          <RemarksSection
            title="Developer Remarks"
            remarks={devRemarks}
            type="developer"
          />

          {/* Reviewer Remarks */}
          <RemarksSection
            title="Reviewer Remarks"
            remarks={reviewerRemarks}
            type="reviewer"
          />

          {/* Other Remarks */}
          {otherRemarks.length > 0 && (
            <RemarksSection
              title="Other Remarks"
              remarks={otherRemarks}
              type="other"
            />
          )}
        </div>
      </div>
    </div>
  );
}
