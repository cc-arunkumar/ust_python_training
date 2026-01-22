import React, { useState, useEffect } from "react";
import { X, Edit, Clock, MoreVertical, Paperclip } from "lucide-react";
import api from "../api/api";
import { API_BASE } from "../utils/constants";
import computeRemarkId from "../utils/remarkId";

function normalizeRemarks(task = {}) {
  const remarks = [];

  function pushRemark(from, text, by, ts, attachment = null) {
    // Allow remarks that have either text or an attachment (or both).
    const hasText = text && String(text).trim() !== "";
    const hasAttachment = !!attachment;
    if (!hasText && !hasAttachment) return;

    remarks.push({
      from: from || "unknown",
      text: hasText ? String(text).trim() : "",
      by: by || null,
      byEmpId: null,
      ts: ts || null,
      attachment: attachment || null,
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

        const attachmentRaw =
          it.attachment || it.file || it.file_id || it.fileId || null;

        pushRemark(from || "unknown", text, by, ts, attachmentRaw);
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
        r.ts || r.developer_ts || r.timestamp,
        r.attachment || null
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
        r.ts || r.reviewer_ts || r.timestamp,
        r.attachment || null
      )
    );
  }

  // client-side optimistic remarks (injected locally)
  if (Array.isArray(task._clientRemarks)) {
    task._clientRemarks.forEach((r) => {
      if (!r) return;
      remarks.push({
        from: r.from || "client",
        text: String(r.text || r.remark || r.comment || "").trim(),
        by: r.by || null,
        byEmpId: r.byEmpId || null,
        ts: r.ts || null,
        attachment: r.attachment || null,
      });
    });
  }

  // Single developer remark/review fields
  if (task.developer_remark && typeof task.developer_remark === "string") {
    pushRemark(
      "developer",
      task.developer_remark,
      task.developer_by,
      task.developer_ts,
      null
    );
  }

  if (task.developer_review && typeof task.developer_review === "string") {
    pushRemark(
      "developer",
      task.developer_review,
      task.developer_by,
      task.developer_ts,
      null
    );
  }

  // Single reviewer remark/review fields
  if (task.reviewer_remark && typeof task.reviewer_remark === "string") {
    pushRemark(
      "reviewer",
      task.reviewer_remark,
      task.reviewer_by,
      task.reviewer_ts,
      null
    );
  }

  if (task.reviewer_review && typeof task.reviewer_review === "string") {
    pushRemark(
      "reviewer",
      task.reviewer_review,
      task.reviewer_by,
      task.reviewer_ts,
      null
    );
  }

  return remarks;
}

export default function TaskDetailModal({
  task = {},
  employees = [],
  onClose = () => {},
  onEdit = () => {},
  currentEmpId = null,
  userRole = "",
  onMarkAllRead = () => {},
}) {
  const [readRemarks, setReadRemarks] = useState(new Set());
  const [serverReviews, setServerReviews] = useState([]);
  const [fetchError, setFetchError] = useState(null);
  const chatRef = React.useRef(null);

  useEffect(() => {
    let mounted = true;
    let intervalId = null;

    const fetchReviews = async () => {
      if (!task || !task.task_id) {
        if (mounted) setServerReviews([]);
        return;
      }
      try {
        const res = await api.getTaskReviews(task.task_id);
        console.log("TaskDetailModal: fetched reviews for", task.task_id, res);
        if (!mounted) return;
        setServerReviews(res || []);
        setFetchError(null);
      } catch (e) {
        if (!mounted) return;
        console.error("Failed to load task reviews:", e);
        setServerReviews([]);
        setFetchError(e.message || String(e));
      }
    };

    fetchReviews();
    intervalId = setInterval(fetchReviews, 5000);

    return () => {
      mounted = false;
      if (intervalId) clearInterval(intervalId);
    };
  }, [task.task_id]);

  useEffect(() => {
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

  const normalized = normalizeRemarks(task);
  const serverMapped = (serverReviews || []).map((s) => {
    const roleRaw = (s.role || "").toString().toLowerCase();
    let fromNorm = "reviewer";
    if (roleRaw.includes("dev") || roleRaw.includes("developer"))
      fromNorm = "developer";
    else if (roleRaw.includes("review") || roleRaw.includes("reviewer"))
      fromNorm = "reviewer";
    else if (roleRaw.includes("manager") || roleRaw.includes("admin"))
      fromNorm = "reviewer";

    let attachment = null;
    try {
      const a = s.attachment;
      if (a) {
        const fileId =
          a.file_id || a.fileId || (a._id && String(a._id)) || a.id || null;
        const filename =
          a.filename || a.name || a.file_name || a.original_name || null;
        const size = a.size || a.length || a.bytes || null;
        const content_type =
          a.content_type || a.contentType || a.mimetype || a.type || null;
        attachment = {
          file_id: fileId ? String(fileId) : null,
          filename: filename || null,
          size: typeof size === "number" ? size : null,
          content_type: content_type || null,
        };
      }
    } catch (e) {
      attachment = null;
    }

    return {
      from: fromNorm,
      text: s.review || s.message || s.comment || "",
      by:
        s.reviewed_by_name ||
        s.reviewed_by_emp_id ||
        s.reviewed_by_user_id ||
        null,
      byEmpId: s.reviewed_by_emp_id || s.reviewed_by_user_id || null,
      ts: s.created_at || null,
      attachment,
    };
  });

  const remarks = [...normalized, ...serverMapped].map((r) => ({
    ...r,
    ts: r.ts ? String(r.ts) : null,
  }));

  remarks.sort((a, b) => {
    if (!a.ts && !b.ts) return 0;
    if (!a.ts) return 1;
    if (!b.ts) return -1;
    const ta = Date.parse(a.ts);
    const tb = Date.parse(b.ts);
    if (isNaN(ta) && isNaN(tb)) return 0;
    if (isNaN(ta)) return 1;
    if (isNaN(tb)) return -1;
    return ta - tb;
  });

  const otherRemarks = remarks.filter((r) => {
    const from = String(r.from || "").toLowerCase();
    return (
      !from.includes("dev") &&
      !from.includes("review") &&
      !from.includes("developer") &&
      !from.includes("reviewer") &&
      !from.includes("manager") &&
      !from.includes("admin")
    );
  });

  function isNewRemark(r) {
    if (!r || !r.ts) return false;

    const remarkId = computeRemarkId(r);
    if (readRemarks.has(remarkId)) return false;

    if (r.byEmpId && currentEmpId && Number(r.byEmpId) === Number(currentEmpId))
      return false;

    const fromRaw = String(r.from || "").toLowerCase();
    const fromNorm =
      fromRaw.includes("dev") || fromRaw.includes("developer")
        ? "developer"
        : "reviewer";

    if (fromNorm === "reviewer") {
      if (currentEmpId && Number(currentEmpId) !== Number(task.assigned_to))
        return false;
    }

    if (fromNorm === "developer") {
      if (currentEmpId && Number(currentEmpId) !== Number(task.reviewer))
        return false;
    }

    const then = Date.parse(r.ts);
    if (isNaN(then)) return false;
    const age = Date.now() - then;
    return age < 7 * 24 * 60 * 60 * 1000;
  }

  const markAsRead = (r) => {
    const remarkId = computeRemarkId(r);
    const newReadRemarks = new Set(readRemarks);
    newReadRemarks.add(remarkId);
    setReadRemarks(newReadRemarks);

    const key = `task_${task.task_id}_read_remarks`;
    localStorage.setItem(key, JSON.stringify([...newReadRemarks]));

    try {
      const newValue = localStorage.getItem(key);
      const sev = new StorageEvent("storage", {
        key,
        newValue,
        oldValue: null,
        url: window.location.href,
        storageArea: localStorage,
      });
      window.dispatchEvent(sev);
      const { publish } = require("../utils/events");
      publish("remarks:updated", { taskId: task.task_id });
    } catch (e) {}
  };

  const [showRemarksMenu, setShowRemarksMenu] = useState(false);

  const markAllRead = () => {
    try {
      const newRead = new Set(readRemarks);
      remarks.forEach((r) => {
        if (!r || !r.ts) return;
        const id = computeRemarkId(r);
        newRead.add(id);
      });
      setReadRemarks(newRead);
      const key = `task_${task.task_id}_read_remarks`;
      localStorage.setItem(key, JSON.stringify([...newRead]));
      setShowRemarksMenu(false);

      try {
        onMarkAllRead();
      } catch (e) {
        console.warn("onMarkAllRead callback failed:", e);
      }

      try {
        const newValue = localStorage.getItem(key);
        const sev = new StorageEvent("storage", {
          key,
          newValue,
          oldValue: null,
          url: window.location.href,
          storageArea: localStorage,
        });
        window.dispatchEvent(sev);
        window.dispatchEvent(
          new CustomEvent("remarks:updated", {
            detail: { taskId: task.task_id },
          })
        );
      } catch (e) {}
    } catch (e) {
      console.error("Failed to mark all read:", e);
    }
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

  const getAttachmentUrl = (attachment) => {
    if (!attachment) {
      console.log("No attachment provided");
      return null;
    }
    
    console.log("Processing attachment:", attachment);
    
    const fileId =
      attachment.file_id ||
      attachment.fileId ||
      (attachment._id && String(attachment._id)) ||
      attachment.id ||
      null;
    
    if (!fileId) {
      console.error("Could not extract file_id from attachment:", attachment);
      return null;
    }
    
    const url = `${API_BASE}/tasks/${task.task_id}/attachments/${fileId}`;
    console.log("Generated attachment URL:", url);
    
    return url;
  };

  const handleDownloadAttachment = async (attachment) => {
    const url = getAttachmentUrl(attachment);
    if (!url) {
      alert("Could not generate download URL");
      return;
    }

    try {
      const token = localStorage.getItem("token");
      const response = await fetch(url, {
        method: "GET",
        headers: {
          ...(token && { Authorization: `Bearer ${token}` }),
        },
      });

      if (!response.ok) {
        const errorText = await response.text();
        console.error("Download failed:", response.status, errorText);
        alert(`Download failed: ${response.status} - ${errorText}`);
        return;
      }

      // Get the blob from response
      const blob = await response.blob();
      
      // Create a download link and trigger it
      const downloadUrl = window.URL.createObjectURL(blob);
      const link = document.createElement("a");
      link.href = downloadUrl;
      link.download = attachment.filename || "attachment";
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
      window.URL.revokeObjectURL(downloadUrl);
      
      console.log("Download successful:", attachment.filename);
    } catch (error) {
      console.error("Download error:", error);
      alert(`Download failed: ${error.message}`);
    }
  };

  const RemarksSection = ({ title, remarks, type }) => (
    <div>
      <h4 className="text-sm font-semibold text-gray-700 mb-2">{title}</h4>
      <div className="space-y-3">
        {remarks.length ? (
          remarks.map((r, i) => {
            const isNew = isNewRemark(r);
            const remarkId = `${type}_${i}`;
            const attachmentUrl = getAttachmentUrl(r.attachment);

            return (
              <div
                key={remarkId}
                className="relative bg-gray-50 rounded-lg p-3 border border-gray-200"
                onClick={() => isNew && markAsRead(r)}
              >
                {isNew && (
                  <span className="absolute -top-2 -left-2 bg-red-500 text-white text-[10px] font-bold px-2 py-0.5 rounded-full shadow-sm animate-pulse">
                    NEW
                  </span>
                )}

                <div className="flex items-start gap-3">
                  <div className="flex-shrink-0 w-6 h-6 rounded-full bg-indigo-100 text-indigo-600 flex items-center justify-center text-xs font-semibold">
                    {i + 1}
                  </div>

                  <div className="flex-1">
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

                    {r.text && (
                      <div className="text-sm text-gray-800 whitespace-pre-wrap mb-2">
                        {r.text}
                      </div>
                    )}

                    {attachmentUrl && (
                      <button
                        onClick={(e) => {
                          e.stopPropagation();
                          handleDownloadAttachment(r.attachment);
                        }}
                        className="inline-flex items-center gap-1 text-xs text-indigo-600 hover:text-indigo-800 font-medium underline cursor-pointer"
                      >
                        <Paperclip size={12} />
                        {r.attachment?.filename || "attachment"}
                        {r.attachment?.size &&
                          ` (${Math.round(r.attachment.size / 1024)} KB)`}
                      </button>
                    )}
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

  useEffect(() => {
    try {
      if (chatRef.current) {
        chatRef.current.scrollTop = chatRef.current.scrollHeight;
      }
    } catch (e) {}
  }, [remarks.length, serverReviews.length]);

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/50 p-4">
      <div className="w-full max-w-3xl bg-white rounded-xl shadow-2xl overflow-hidden max-h-[90vh] flex flex-col">
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

        <div className="flex-1 overflow-y-auto p-6 space-y-6">
          {fetchError && (
            <div className="bg-red-50 border border-red-200 text-red-700 p-3 rounded">
              Failed to load server reviews: {fetchError}
            </div>
          )}

          <div>
            <h3 className="text-sm font-semibold text-gray-600 mb-2">
              Description
            </h3>
            <p className="text-sm text-gray-700 bg-gray-50 p-3 rounded-lg">
              {task.description || "No description provided."}
            </p>
          </div>

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

          <div>
            <div className="flex items-center justify-between mb-2">
              <h4 className="text-sm font-semibold text-gray-700">Remarks</h4>
              <div className="relative">
                <button
                  onClick={(e) => {
                    e.stopPropagation();
                    setShowRemarksMenu((s) => !s);
                  }}
                  className="p-1 rounded hover:bg-gray-100"
                  title="More"
                >
                  <MoreVertical size={16} />
                </button>
                {showRemarksMenu && (
                  <div className="absolute right-0 mt-2 w-40 bg-white border rounded shadow-lg z-50">
                    <button
                      onClick={(e) => {
                        e.stopPropagation();
                        markAllRead();
                      }}
                      className="w-full text-left px-3 py-2 hover:bg-gray-50 text-sm"
                    >
                      Mark all read
                    </button>
                  </div>
                )}
              </div>
            </div>

            <div
              ref={chatRef}
              className="max-h-64 shadow-md border overflow-y-auto space-y-3 p-3 bg-gray-50 rounded"
            >
              {remarks.length ? (
                remarks.map((r, i) => {
                  const fromRaw = String(r.from || "").toLowerCase();
                  const fromNorm =
                    fromRaw.includes("dev") || fromRaw.includes("developer")
                      ? "developer"
                      : "reviewer";
                  const isLeft = fromNorm === "reviewer";
                  const isNew = isNewRemark(r);
                  const remarkId = `${fromNorm}_${i}`;
                  const attachmentUrl = getAttachmentUrl(r.attachment);

                  return (
                    <div
                      key={remarkId}
                      className={`flex ${
                        isLeft ? "justify-start" : "justify-end"
                      }`}
                      onClick={() => isNew && markAsRead(r)}
                    >
                      <div
                        className={`${
                          isLeft
                            ? "bg-white border border-gray-200"
                            : "bg-indigo-600 text-white"
                        } rounded-lg p-3 max-w-[70%]`}
                      >
                        <div
                          className={`flex items-center gap-2 text-xs mb-1 ${
                            isLeft ? "text-gray-500" : "text-white/80"
                          }`}
                        >
                          {r.by && (
                            <span
                              className={`font-medium ${
                                isLeft ? "text-gray-700" : "text-white"
                              }`}
                            >
                              {r.by}
                            </span>
                          )}
                          {r.ts && (
                            <>
                              <Clock size={10} />
                              <span>{formatTimestamp(r.ts)}</span>
                            </>
                          )}
                          {isNew && (
                            <span
                              className={`ml-2 ${
                                isLeft
                                  ? "bg-red-100 text-red-700"
                                  : "bg-red-500 text-white"
                              } text-[10px] font-bold px-2 py-0.5 rounded-full`}
                            >
                              NEW
                            </span>
                          )}
                        </div>

                        {r.text && (
                          <div className="text-sm whitespace-pre-wrap mb-2">
                            {r.text}
                          </div>
                        )}

                        {attachmentUrl && (
                          <button
                            onClick={(e) => {
                              e.stopPropagation();
                              handleDownloadAttachment(r.attachment);
                            }}
                            className={`inline-flex items-center gap-1 text-xs font-semibold underline cursor-pointer ${
                              isLeft
                                ? "text-indigo-600 hover:text-indigo-800"
                                : "text-white hover:text-white/80"
                            }`}
                          >
                            <Paperclip size={12} />
                            {r.attachment?.filename || "attachment"}
                            {r.attachment?.size &&
                              ` (${Math.round(r.attachment.size / 1024)} KB)`}
                          </button>
                        )}
                      </div>
                    </div>
                  );
                })
              ) : (
                <div className="text-center text-gray-400 text-sm py-4 bg-gray-50 rounded-lg">
                  No remarks yet
                </div>
              )}
            </div>
          </div>

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