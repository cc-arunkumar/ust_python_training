import React, { useState } from "react";
import {
  User,
  CheckCircle,
  Clock,
  PlayCircle,
  Pause,
  Edit2,
  ChevronDown,
  AlertCircle,
  GripVertical,
  Calendar,
  Tag,
} from "lucide-react";
import { STATUS_CONFIG, PRIORITY_COLORS } from "../utils/constants";

function TaskCard({
  task = {},
  employees = [],
  userRole = "",
  onUpdateStatus,
  onEdit,
  currentEmpId = null,
  statusConfig = null,
}) {
  const [showStatusMenu, setShowStatusMenu] = useState(false);
  const [showReviewInput, setShowReviewInput] = useState(false);
  const [pendingStatus, setPendingStatus] = useState(null);
  const [reviewText, setReviewText] = useState("");
  const [isDragging, setIsDragging] = useState(false);

  const statusIcons = {
    TO_DO: Clock,
    IN_PROGRESS: PlayCircle,
    REVIEW: Pause,
    DONE: CheckCircle,
    BLOCKED: AlertCircle,
  };

  const assignee = (employees || []).find((e) => e.emp_id === task.assigned_to);
  const reviewer = (employees || []).find((e) => e.emp_id === task.reviewer);
  const isReviewer =
    currentEmpId != null && Number(currentEmpId) === Number(task.reviewer);

  // return human readable days-left string for expected_closure
  const formatExpected = (dt) => {
    if (!dt) return null;
    try {
      const d = new Date(dt);
      if (isNaN(d)) return null;

      // normalize to local midnight for day-diff calculation
      const today = new Date();
      const utc1 = Date.UTC(
        today.getFullYear(),
        today.getMonth(),
        today.getDate()
      );
      const utc2 = Date.UTC(d.getFullYear(), d.getMonth(), d.getDate());
      const diffDays = Math.ceil((utc2 - utc1) / (1000 * 60 * 60 * 24));

      if (diffDays > 1) return `Due in ${diffDays} days`;
      if (diffDays === 1) return `Due in 1 day`;
      if (diffDays === 0) return `Due today`;
      return `Overdue by ${Math.abs(diffDays)} day${
        Math.abs(diffDays) > 1 ? "s" : ""
      }`;
    } catch (e) {
      return null;
    }
  };

  const formatSubmission = (dt) => {
    if (!dt) return null;
    try {
      const d = new Date(dt);
      if (isNaN(d)) return null;
      return d.toLocaleString(undefined, {
        day: "2-digit",
        month: "short",
        year: "numeric",
        hour: "2-digit",
        minute: "2-digit",
      });
    } catch (e) {
      return null;
    }
  };

  const statusCfg =
    statusConfig || STATUS_CONFIG[task.status] || STATUS_CONFIG.TO_DO;
  const priorityClasses = PRIORITY_COLORS[task.priority] || "text-gray-600";

  const canMarkDone =
    (userRole || "").toUpperCase().includes("ADMIN") ||
    (userRole || "").toUpperCase().includes("MANAGER");

  const getAvailableStatuses = () => {
    const TRANSITIONS = {
      TO_DO: ["IN_PROGRESS"],
      IN_PROGRESS: ["REVIEW"],
      REVIEW: ["IN_PROGRESS", "DONE"],
      DONE: [],
    };
    const current = task.status || "TO_DO";
    const allowed = TRANSITIONS[current] || [];
    // include current status as a no-op option for clarity
    const result = [current, ...allowed.filter((s) => s !== current)];
    // remove DONE if user can't mark done
    return result.filter((s) => s !== "DONE" || canMarkDone);
  };

  const handleStatusSelect = (newStatus) => {
    // ensure the selected status is allowed (safety check)
    const allowed = getAvailableStatuses();
    if (!allowed.includes(newStatus)) {
      alert("Invalid status transition");
      setShowStatusMenu(false);
      return;
    }

    if (newStatus === "REVIEW") {
      // Debug: log selection so we know the menu path is executed
      console.debug("TaskCard.handleStatusSelect -> REVIEW selected", {
        taskId: task.task_id,
        currentEmpId,
        reviewer: task.reviewer,
      });

      // Always prompt for remarks when submitting for review (developer or reviewer)
      setPendingStatus(newStatus);
      setShowReviewInput(true);
      setShowStatusMenu(false);
      return;
    }

    if (newStatus === "DONE") {
      // Only the designated reviewer will get the review input when marking DONE;
      // others (e.g., Admins/Managers who are not the reviewer) will apply status without remarks.
      if (!isReviewer) {
        onUpdateStatus && onUpdateStatus(task.task_id, newStatus, null);
        setShowStatusMenu(false);
        return;
      }
      setPendingStatus(newStatus);
      setShowReviewInput(true);
      setShowStatusMenu(false);
      return;
    }

    if (newStatus === "IN_PROGRESS") {
      setPendingStatus(newStatus);
      setShowReviewInput(true);
      setShowStatusMenu(false);
      return;
    }

    onUpdateStatus && onUpdateStatus(task.task_id, newStatus, null);
    setShowStatusMenu(false);
  };

  const submitReview = () => {
    console.debug("TaskCard.submitReview -> submitting review", {
      taskId: task.task_id,
      pendingStatus,
      isReviewer,
      reviewText,
    });
    // Only block adding reviewer remarks when attempting to add reviewer remarks
    // for marking DONE if the current user is not the designated reviewer.
    if (
      reviewText &&
      reviewText.trim() &&
      pendingStatus === "DONE" &&
      !isReviewer
    ) {
      alert("Only the designated reviewer can add reviewer remarks.");
      return;
    }

    onUpdateStatus &&
      onUpdateStatus(task.task_id, pendingStatus, reviewText.trim() || null);

    setShowReviewInput(false);
    setPendingStatus(null);
    setReviewText("");
  };

  const cancelReview = () => {
    setShowReviewInput(false);
    setPendingStatus(null);
    setReviewText("");
  };

  const handleDragStart = (e) => {
    // prevent dragging if the task is DONE
    if (task.status === "DONE") {
      e.preventDefault();
      return;
    }
    setIsDragging(true);
    e.dataTransfer.effectAllowed = "move";
    e.dataTransfer.setData("taskId", task.task_id);
    e.dataTransfer.setData("currentStatus", task.status);
  };

  const handleDragEnd = () => {
    setIsDragging(false);
  };

  const StatusIcon = statusIcons[task.status] || Clock;

  return (
    <div
      draggable={task.status !== "DONE"}
      onDragStart={handleDragStart}
      onDragEnd={handleDragEnd}
      className={`bg-white rounded-xl p-3 hover:shadow-xl transition-all cursor-pointer relative  group ${
        isDragging
          ? "opacity-50 shadow-none scale-95"
          : "shadow-md hover:scale-[1.02]"
      }`}
      style={{ borderLeftColor: statusCfg.color.replace("bg-", "#") }}
    >
      {/* Drag Handle */}
      <div className="absolute top-2 left-2 text-gray-300 group-hover:text-gray-400 cursor-grab active:cursor-grabbing transition-colors">
        <GripVertical size={14} />
      </div>

      {/* Priority Badge */}
      <div className="absolute top-2 right-2">
        <span
          className={`text-[10px] font-bold px-2 py-0.5 rounded-full ${priorityClasses} shadow-sm`}
        >
          {task.priority || "MEDIUM"}
        </span>
      </div>

      {/* Title */}
      <div className="px-5 pr-16 mb-2 mt-1">
        <h3 className="text-xs font-bold text-gray-800 line-clamp-2 leading-snug">
          {task.title}
        </h3>
      </div>

      {/* Description */}
      <p className="text-[11px] text-gray-600 line-clamp-2 mb-2 px-0.5">
        {task.description || "No description provided"}
      </p>

      {/* Info Section with Icons */}
      <div className="space-y-1 mb-2 px-0.5">
        {task.expected_closure && (
          <div className="flex items-center gap-1 text-[11px]">
            <Calendar size={11} className="text-gray-400" />
            <span
              className={`font-semibold ${(() => {
                const d = new Date(task.expected_closure);
                const today = new Date();
                const utc1 = Date.UTC(
                  today.getFullYear(),
                  today.getMonth(),
                  today.getDate()
                );
                const utc2 = Date.UTC(
                  d.getFullYear(),
                  d.getMonth(),
                  d.getDate()
                );
                const diffDays = Math.ceil(
                  (utc2 - utc1) / (1000 * 60 * 60 * 24)
                );
                return diffDays < 0 ? "text-red-600" : "text-gray-700";
              })()}`}
            >
              {formatExpected(task.expected_closure)}
            </span>
          </div>
        )}
        {/* show submission/closure date when task is done or actual_closure exists */}
        {(task.status === "DONE" || task.actual_closure) && (
          <div className="flex items-center gap-1 text-[11px]">
            <Calendar size={11} className="text-green-500" />
            <span className="text-green-700 font-medium">
              {formatSubmission(task.actual_closure || task.actual_closure)}
            </span>
          </div>
        )}
        {task.dept_name && (
          <div className="flex items-center gap-1 text-[11px]">
            <Tag size={11} className="text-gray-400" />
            <span className="text-gray-700 bg-gray-100 px-1.5 py-0.5 rounded font-medium">
              {task.dept_name}
            </span>
          </div>
        )}
      </div>

      {/* People Section */}
      <div className="flex items-center gap-1.5 mb-2 px-0.5 flex-wrap">
        {assignee && (
          <div className="flex items-center gap-1 bg-blue-50 px-1.5 py-0.5 rounded text-[10px]">
            <User size={10} className="text-blue-600" />
            <span className="text-blue-700 font-medium">
              {assignee.emp_name}
            </span>
          </div>
        )}
        {reviewer && (
          <div className="flex items-center gap-1 bg-purple-50 px-1.5 py-0.5 rounded text-[10px]">
            <CheckCircle size={10} className="text-purple-600" />
            <span className="text-purple-700 font-medium">
              {reviewer.emp_name}
            </span>
          </div>
        )}
      </div>

      {/* Status and Edit Row */}
      <div className="flex items-center justify-between gap-2 px-0.5">
        <div className="relative flex-1">
          <button
            onClick={(e) => {
              e.stopPropagation();
              // don't open menu for DONE tasks
              if (task.status === "DONE") return;
              setShowStatusMenu((s) => !s);
            }}
            disabled={task.status === "DONE"}
            className={`flex items-center gap-1.5 px-2 py-1.5 rounded-lg text-[11px] font-semibold w-full justify-center ${
              statusCfg.color
            } text-white shadow-sm hover:shadow-md transition-all ${
              task.status === "DONE" ? "opacity-70 cursor-not-allowed" : ""
            }`}
          >
            <StatusIcon size={12} />
            <span className="truncate">{statusCfg.label}</span>
            <ChevronDown size={12} />
          </button>

          {showStatusMenu && (
            <>
              <div
                className="fixed inset-0 z-10"
                onClick={(e) => {
                  e.stopPropagation();
                  setShowStatusMenu(false);
                }}
              />

              <div className="absolute left-0 bottom-full mb-2 bg-white rounded-xl shadow-2xl border-2 border-gray-100 z-20 min-w-[140px] overflow-hidden">
                {getAvailableStatuses().map((s) => {
                  const cfg = STATUS_CONFIG[s];
                  const Icon = statusIcons[s] || Clock;
                  const disabled = s === "DONE" && !canMarkDone;
                  return (
                    <button
                      key={s}
                      onClick={(e) => {
                        e.stopPropagation();
                        handleStatusSelect(s);
                      }}
                      disabled={disabled}
                      className={`w-full text-left px-3 py-2 hover:bg-gray-50 flex items-center gap-2 text-[11px] font-medium transition-colors ${
                        disabled ? "opacity-50 cursor-not-allowed" : ""
                      } ${task.status === s ? "bg-indigo-50" : ""}`}
                    >
                      <Icon size={12} className={cfg.textColor} />
                      <span className={cfg.textColor}>{cfg.label}</span>
                      {disabled && <span className="ml-auto">🔒</span>}
                    </button>
                  );
                })}
              </div>
            </>
          )}
        </div>

        <button
          onClick={(e) => {
            e.stopPropagation();
            onEdit && onEdit(task);
          }}
          className="p-1.5 hover:bg-indigo-50 text-indigo-600 rounded-lg transition-all hover:scale-110"
          title="Edit Task"
        >
          <Edit2 size={14} />
        </button>
      </div>

      {/* Review Input Section */}
      {showReviewInput && (
        <div
          className="mt-3 pt-3 border-t-2 border-gray-100 bg-gradient-to-br from-indigo-50 to-purple-50 rounded-lg p-2"
          onClick={(e) => e.stopPropagation()}
        >
          <div className="mb-2">
            <p className="text-[10px] text-gray-700 mb-0.5 font-semibold">
              Changing status to:{" "}
              <span className="text-indigo-600">
                {STATUS_CONFIG[pendingStatus]?.label}
              </span>
            </p>
            <p className="text-[10px] text-gray-600">
              Add remarks as{" "}
              <strong className="text-purple-600">
                {isReviewer ? "Reviewer" : "Developer"}
              </strong>
            </p>
          </div>
          <textarea
            value={reviewText}
            onChange={(e) => setReviewText(e.target.value)}
            placeholder={`Add ${
              isReviewer ? "reviewer" : "developer"
            } remarks... (optional)`}
            className="w-full px-2 py-1.5 border-2 border-gray-200 rounded-lg text-[11px] mb-2 focus:ring-2 focus:ring-indigo-400 focus:outline-none bg-white"
            rows="2"
            autoFocus
          />
          <div className="flex gap-2">
            <button
              onClick={submitReview}
              className="flex-1 bg-gradient-to-r from-indigo-600 to-purple-600 text-white py-1.5 rounded-lg text-[10px] font-semibold hover:shadow-lg transition-all"
            >
              {reviewText.trim() ? "Submit" : "Submit"}
            </button>
            <button
              onClick={cancelReview}
              className="flex-1 bg-gray-200 text-gray-700 py-1.5 rounded-lg text-[10px] font-semibold hover:bg-gray-300 transition-all"
            >
              Cancel
            </button>
          </div>
        </div>
      )}
    </div>
  );
}

export default TaskCard;
