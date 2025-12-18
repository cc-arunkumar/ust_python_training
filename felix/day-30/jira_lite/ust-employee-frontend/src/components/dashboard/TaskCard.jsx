import React, { useState, useCallback, useRef, useEffect } from "react";
import {
  User,
  Calendar,
  MessageSquare,
  MoreVertical,
  UserPlus,
  Send,
  Upload,
  Download,
  File,
  Loader2,
  Eye,
  X,
  Bell,
} from "lucide-react";
import { PRIORITY_COLORS } from "../../utils/constants";
import { api } from "../../services/api";

const TaskCard = ({
  task,
  onStatusChange,
  onAddRemark,
  canEdit,
  onAssign,
  employees = [],
  token,
  currentUserId,
}) => {
  const [showMenu, setShowMenu] = useState(false);
  const [activeModal, setActiveModal] = useState(null); // 'assign', 'status', 'remarks', 'files', 'addRemark'
  const [remark, setRemark] = useState("");
  const [addingRemark, setAddingRemark] = useState(false);
  const [assignee, setAssignee] = useState(task.assigned_to || "");

  // FILE STATES
  const [taskFiles, setTaskFiles] = useState(task.files || []);
  const [uploading, setUploading] = useState(false);
  const [selectedFileName, setSelectedFileName] = useState("");
  const [fileInputKey, setFileInputKey] = useState(0);
  const fileInputRef = useRef(null);
  const menuRef = useRef(null);

  // Close menu when clicking outside
  useEffect(() => {
    const handleClickOutside = (event) => {
      if (menuRef.current && !menuRef.current.contains(event.target)) {
        setShowMenu(false);
      }
    };
    document.addEventListener("mousedown", handleClickOutside);
    return () => document.removeEventListener("mousedown", handleClickOutside);
  }, []);

  // FILE HANDLERS
  const loadTaskFiles = useCallback(async () => {
    if (!token || !task._id) return;
    try {
      const response = await api.getTaskFiles(token, task._id);
      setTaskFiles(response.files || []);
    } catch (error) {
      console.error("Failed to load files:", error);
    }
  }, [token, task._id]);

  const handleFileUpload = useCallback(
    async (event) => {
      const file = event.target.files[0];
      if (!file || !token) return;

      setUploading(true);
      setSelectedFileName(file.name);
      try {
        await api.uploadFileToTask(token, task._id, file);
        await loadTaskFiles();

        setSelectedFileName("");
        setFileInputKey((prev) => prev + 1);
        if (fileInputRef.current) {
          fileInputRef.current.value = "";
        }

        alert(`✅ "${file.name}" uploaded successfully!`);
      } catch (error) {
        alert(`❌ Upload failed: ${error.message}`);
        setSelectedFileName("");
      } finally {
        setUploading(false);
      }
    },
    [token, task._id, loadTaskFiles]
  );

  const handleDownloadFile = useCallback(
    async (fileId, fileName) => {
      try {
        await api.downloadFileBlob(token, fileId, fileName);
      } catch (error) {
        alert(`❌ Download failed: ${error.message}`);
      }
    },
    [token]
  );

  const handlePreviewFile = useCallback(
    async (fileId) => {
      try {
        const fileData = await api.downloadFile(token, fileId);
        if (fileData.file_type.startsWith("image/")) {
          const imgWindow = window.open("", "_blank");
          imgWindow.document.write(`
          <html>
            <body style="margin:0;padding:20px;background:#f8fafc;">
              <img src="data:${fileData.file_type};base64,${fileData.file_data}" 
                   style="max-width:90vw;max-height:90vh;border-radius:12px;box-shadow:0 20px 40px rgba(0,0,0,0.1);">
              <p style="text-align:center;margin-top:20px;color:#64748b;">${fileData.file_name}</p>
            </body>
          </html>
        `);
        } else {
          await api.downloadFileBlob(token, fileId);
        }
      } catch (error) {
        alert(`❌ Preview failed: ${error.message}`);
      }
    },
    [token]
  );

  // Load files when files modal opens
  useEffect(() => {
    if (activeModal === "files") {
      loadTaskFiles();
    }
  }, [activeModal, loadTaskFiles]);

  const handleAddRemark = async () => {
    if (!remark.trim()) return;
    setAddingRemark(true);
    await onAddRemark(task._id, remark);
    setRemark("");
    setAddingRemark(false);
    setActiveModal(null);
  };

  // ✅ FIXED: Auto "In Progress" when manager assigns task
  const handleAssign = async () => {
    if (!assignee) {
      alert("Please select an employee to assign.");
      return;
    }
    if (!onAssign) return;

    try {
      // Step 1: Assign the task
      await onAssign(task._id, parseInt(assignee, 10));

      // Step 2: Auto-move to "In Progress" for newly assigned tasks
      if (
        canEdit &&
        (!task.assigned_to ||
          task.assigned_to === "" ||
          task.assigned_to === null)
      ) {
        try {
          await api.updateTaskStatus(token, task._id, "In Progress");
          alert(
            `✅ Task assigned to employee ID ${assignee} and moved to In Progress! 🎉`
          );
        } catch (statusError) {
          console.warn(
            "Auto status update failed after assignment:",
            statusError
          );
          alert(
            `✅ Task assigned to employee ID ${assignee} successfully! (Status unchanged)`
          );
        }
      } else {
        alert(`✅ Task assigned to employee ID ${assignee} successfully!`);
      }

      setActiveModal(null);
      setShowMenu(false);
    } catch (error) {
      console.error("Assignment failed:", error);
      alert("❌ Failed to assign task: " + (error.message || error));
    }
  };

  const canAddRemarkNow =
    task.status === "In Progress" || task.status === "Review";
  const canManageFiles = canEdit;

  const priorityConfig = {
    High: {
      gradient: "from-red-500 to-pink-500",
      bg: "bg-red-50",
      border: "border-red-200",
      text: "text-red-700",
    },
    Medium: {
      gradient: "from-yellow-500 to-orange-500",
      bg: "bg-yellow-50",
      border: "border-yellow-200",
      text: "text-yellow-700",
    },
    Low: {
      gradient: "from-green-500 to-emerald-500",
      bg: "bg-green-50",
      border: "border-green-200",
      text: "text-green-700",
    },
  };

  const config = priorityConfig[task.priority] || priorityConfig.Low;
  const assignedEmployee = employees.find(
    (e) => (e.emp_id ?? e.id) === task.assigned_to
  );
  const assignedByEmployee = employees.find(
    (e) => (e.emp_id ?? e.id) === task.assigned_by
  );
  const [notificationCount, setNotificationCount] = useState(
    (task.notifications && currentUserId
      ? task.notifications[currentUserId]
      : 0) || 0
  );

  useEffect(() => {
    setNotificationCount(
      (task.notifications && currentUserId
        ? task.notifications[currentUserId]
        : 0) || 0
    );
  }, [task, currentUserId]);

  // Due date calculations
  const dueDate = task.expected_completion_date
    ? new Date(task.expected_completion_date)
    : null;
  const now = new Date();
  const isOverdue = dueDate ? now > dueDate : false;
  const msInDay = 24 * 60 * 60 * 1000;
  // mark as due soon if within 3 days (but not overdue)
  const isDueSoon = dueDate
    ? dueDate - now > 0 && dateDiffInMs(dueDate, now) <= msInDay * 3
    : false;
  // days left (rounded up) for tooltip
  const daysLeft = dueDate
    ? Math.ceil(dateDiffInMs(dueDate, now) / msInDay)
    : null;

  // helper to compute difference in ms (dueDate - now)
  function dateDiffInMs(a, b) {
    return a.getTime() - b.getTime();
  }

  // Clear notifications when the remarks modal is opened (ensure badge removed)
  useEffect(() => {
    let cancelled = false;
    const maybeClear = async () => {
      if (
        activeModal === "remarks" &&
        notificationCount > 0 &&
        currentUserId &&
        token
      ) {
        // Optimistically clear local badge so UI reflects opened notifications immediately
        if (!cancelled) setNotificationCount(0);
        try {
          await api.clearTaskNotifications(token, task._id);
        } catch (err) {
          // If server clear fails, log it. We keep the badge cleared locally to reflect that
          // the user has opened the notifications; a full refresh will reconcile server state.
          console.error("Failed to clear notifications on modal open", err);
        }
      }
    };
    maybeClear();
    return () => {
      cancelled = true;
    };
  }, [activeModal, notificationCount, currentUserId, token, task._id]);

  return (
    <>
      <div className="bg-white rounded-2xl shadow-lg border-2 border-gray-100 hover:shadow-2xl hover:scale-[1.02] transition-all duration-300 overflow-hidden group">
        {/* Priority accent bar */}
        <div className={`h-2 bg-gradient-to-r ${config.gradient}`}></div>

        <div className="p-5">
          <div className="flex items-start justify-between mb-4">
            <h3 className="font-bold text-gray-900 text-base flex-1 pr-2 leading-tight group-hover:text-blue-600 transition-colors">
              {task.title}
            </h3>

            <div className="flex items-center gap-2">
              <span
                className={`${config.bg} ${config.border} ${config.text} text-xs px-3 py-1.5 rounded-xl font-bold border-2 shadow-sm whitespace-nowrap`}
              >
                {task.priority}
              </span>

              {/* Notification Bell */}
              <button
                onClick={async (e) => {
                  e.stopPropagation();
                  try {
                    if (currentUserId) {
                      await api.clearTaskNotifications(token, task._id);
                      setNotificationCount(0);
                    }
                  } catch (err) {
                    console.error("Failed to clear notification", err);
                  }
                  setActiveModal("remarks");
                }}
                className="relative p-2 hover:bg-gray-100 rounded-lg transition-colors group-hover:bg-gray-50"
                title={`Notifications: ${notificationCount}`}
              >
                <Bell size={18} className="text-gray-600" />
                {notificationCount > 0 && (
                  <span className="absolute -top-1 -right-1 bg-red-600 text-white text-[10px] w-5 h-5 rounded-full flex items-center justify-center font-bold">
                    {notificationCount}
                  </span>
                )}
              </button>

              {/* 3-Dot Menu Button */}
              <div className="relative" ref={menuRef}>
                <button
                  onClick={(e) => {
                    e.stopPropagation();
                    setShowMenu(!showMenu);
                  }}
                  className="p-2 hover:bg-gray-100 rounded-lg transition-colors group-hover:bg-gray-50"
                >
                  <MoreVertical
                    size={20}
                    className="text-gray-600 group-hover:text-gray-800"
                  />
                </button>

                {/* Dropdown Menu */}
                {showMenu && (
                  <div className="absolute right-0 top-10 w-56 bg-white/95 backdrop-blur-sm rounded-2xl shadow-2xl border border-gray-200/50 py-2 z-50 animate-in fade-in slide-in-from-top-2 duration-200">
                    {canEdit && task.status === "To Do" && (
                      <button
                        onClick={() => {
                          setShowMenu(false);
                          setActiveModal("assign");
                        }}
                        className="w-full px-4 py-3 text-left text-sm hover:bg-gradient-to-r hover:from-indigo-50 hover:to-blue-50 flex items-center gap-3 text-gray-700 hover:text-indigo-700 font-medium transition-all border-l-4 border-transparent hover:border-indigo-400"
                      >
                        <UserPlus size={18} />
                        Assign Task
                      </button>
                    )}

                    <button
                      onClick={() => {
                        setActiveModal("status");
                        setShowMenu(false);
                      }}
                      className="w-full px-4 py-3 text-left text-sm hover:bg-gradient-to-r hover:from-purple-50 hover:to-pink-50 flex items-center gap-3 text-gray-700 hover:text-purple-700 font-medium transition-all border-l-4 border-transparent hover:border-purple-400"
                    >
                      <Calendar size={18} />
                      Change Status
                    </button>

                    {task.remarks && task.remarks.length > 0 && (
                      <button
                        onClick={() => {
                          setActiveModal("remarks");
                          setShowMenu(false);
                        }}
                        className="w-full px-4 py-3 text-left text-sm hover:bg-gray-50 flex items-center gap-3 text-gray-700 font-medium transition-all border-l-4 border-transparent hover:border-gray-400"
                      >
                        <MessageSquare size={18} />
                        View Remarks ({task.remarks?.length || 0})
                      </button>
                    )}

                    {canAddRemarkNow && (
                      <button
                        onClick={() => {
                          setActiveModal("addRemark");
                          setShowMenu(false);
                        }}
                        className="w-full px-4 py-3 text-left text-sm hover:bg-gradient-to-r hover:from-blue-50 hover:to-cyan-50 flex items-center gap-3 text-gray-700 hover:text-blue-700 font-medium transition-all border-l-4 border-transparent hover:border-blue-400"
                      >
                        <Send size={18} />
                        Add Remark
                      </button>
                    )}

                    {canManageFiles && (
                      <button
                        onClick={() => {
                          setShowMenu(false);
                          setActiveModal("files");
                        }}
                        className="w-full px-4 py-3 text-left text-sm hover:bg-gradient-to-r hover:from-emerald-50 hover:to-teal-50 flex items-center gap-3 text-gray-700 hover:text-emerald-700 font-medium transition-all border-l-4 border-transparent hover:border-emerald-400"
                      >
                        <File size={18} />
                        Manage Files ({taskFiles.length})
                      </button>
                    )}
                  </div>
                )}
              </div>
            </div>
          </div>

          <p className="text-sm text-gray-600 mb-4 line-clamp-2 whitespace-pre-wrap leading-relaxed">
            {task.description}
          </p>

          <div className="flex flex-col gap-3 text-xs">
            {/* Assigned to (Developer) */}
            <div className="flex flex-col gap-2">
              <div className="flex items-center gap-2 bg-gradient-to-r from-blue-50 to-cyan-50 px-3 py-2 rounded-xl border border-blue-100">
                <div className="w-6 h-6 rounded-lg bg-gradient-to-br from-blue-500 to-cyan-500 flex items-center justify-center text-white shadow-sm">
                  <User size={14} />
                </div>
                <div className="flex-1 min-w-0">
                  <span className="text-gray-500 font-medium block">
                    Assigned to (Developer)
                  </span>
                  <span className="font-bold text-gray-800 truncate block">
                    {assignedEmployee
                      ? assignedEmployee.name
                      : task.assigned_to || "Not assigned"}
                  </span>
                </div>
              </div>

              {/* Assigned by (Manager) */}
              <div className="flex items-center gap-2 px-3 py-2 rounded-xl">
                <div className="flex-1 min-w-0">
                  <span className="text-gray-500 font-medium block">
                    Assigned by (Manager)
                  </span>
                  <span className="font-bold text-gray-800 block truncate">
                    {assignedByEmployee
                      ? assignedByEmployee.name
                      : task.assigned_by
                      ? `ID: ${task.assigned_by}`
                      : "—"}
                  </span>
                </div>
              </div>
            </div>

            {/* Due date */}
            <div className="flex items-center gap-2 bg-gradient-to-r from-purple-50 to-pink-50 px-3 py-2 rounded-xl border border-purple-100">
              <div className="w-6 h-6 rounded-lg bg-gradient-to-br from-purple-500 to-pink-500 flex items-center justify-center text-white shadow-sm">
                <Calendar size={14} />
              </div>
              
              <div className="flex-1">
                <span className="text-gray-500 font-medium block">
                  Due date
                </span>
                <span className="font-bold text-gray-800 block">
                  {task.expected_completion_date
                    ? new Date(
                        task.expected_completion_date
                      ).toLocaleDateString()
                    : "Not set"}
                </span>
              </div>
              {isOverdue ? (
                <div className="flex items-center">
                  <span
                    className="ml-2 w-3 h-3 rounded-full bg-red-500 animate-pulse ring-2 ring-red-300"
                    title="Overdue"
                    aria-label="Overdue"
                  ></span>
                </div>
              ) : isDueSoon ? (
                <div className="flex items-center">
                  <span
                    className="ml-2 w-3 h-3 rounded-full bg-amber-400 animate-pulse ring-2 ring-amber-200"
                    title={`Due in ${daysLeft} day${daysLeft === 1 ? "" : "s"}`}
                    aria-label={`Due in ${daysLeft} day${
                      daysLeft === 1 ? "" : "s"
                    }`}
                  ></span>
                </div>
              ) : null}
            </div>
          </div>
        </div>
      </div>

      {/* Modals */}
      {activeModal && (
        <div
          className="fixed inset-0 bg-black/50 backdrop-blur-sm flex items-center justify-center z-50 p-4"
          onClick={() => setActiveModal(null)}
        >
          <div
            className="bg-white/95 backdrop-blur-xl rounded-3xl shadow-2xl max-w-md w-full max-h-[90vh] overflow-hidden border border-gray-200/50"
            onClick={(e) => e.stopPropagation()}
          >
            <div className="sticky top-0 bg-gradient-to-r from-gray-50 to-white/50 backdrop-blur border-b-2 border-gray-200 p-6 flex items-center justify-between shadow-sm">
              <h3 className="font-bold text-xl bg-gradient-to-r from-gray-900 via-gray-800 to-gray-700 bg-clip-text text-transparent">
                {activeModal === "assign" && "👤 Assign Task"}
                {activeModal === "status" && "📋 Change Status"}
                {activeModal === "remarks" && "💬 Task Remarks"}
                {activeModal === "files" && "📎 Manage Files"}
                {activeModal === "addRemark" && "✍️ Add Remark"}
              </h3>
              <button
                onClick={() => setActiveModal(null)}
                className="p-2 hover:bg-gray-200 rounded-xl transition-all group"
              >
                <X
                  size={24}
                  className="text-gray-500 group-hover:text-gray-700"
                />
              </button>
            </div>

            <div className="p-6 max-h-[60vh] overflow-y-auto custom-scrollbar">
              {/* Assign Modal */}
              {activeModal === "assign" && (
                <div className="space-y-4">
                  <select
                    value={assignee}
                    onChange={(e) => setAssignee(e.target.value)}
                    className="w-full px-4 py-4 border-2 border-indigo-200 rounded-2xl text-sm focus:ring-4 focus:ring-indigo-500/20 focus:border-indigo-500 bg-white/50 backdrop-blur-sm font-semibold shadow-sm"
                  >
                    <option value="">Select developer to assign</option>
                    {employees.map((emp) => (
                      <option
                        key={emp.id || emp.emp_id}
                        value={emp.emp_id ?? emp.id}
                      >
                        {emp.name} (ID: {emp.emp_id ?? emp.id})
                      </option>
                    ))}
                  </select>
                  <button
                    onClick={handleAssign}
                    disabled={!assignee}
                    className="w-full px-6 py-4 bg-gradient-to-r from-indigo-600 to-blue-600 text-white text-sm rounded-2xl font-bold shadow-lg hover:from-indigo-700 hover:to-blue-700 hover:shadow-xl hover:scale-[1.02] transition-all disabled:opacity-50 disabled:cursor-not-allowed flex items-center justify-center gap-2"
                  >
                    <UserPlus size={20} />
                    Assign Task
                  </button>
                </div>
              )}

              {/* Status Modal */}
              {activeModal === "status" && (
                <div className="space-y-4">
                  {task.status === "To Do" && !task.assigned_to && (
                    <div className="text-sm text-orange-600 bg-gradient-to-r from-orange-50 to-red-50 px-4 py-3 rounded-2xl border-2 border-orange-200 font-medium shadow-sm">
                      ⚠️ Please assign this task before changing status
                    </div>
                  )}
                  <select
                    value={task.status}
                    onChange={(e) => {
                      onStatusChange(task, e.target.value);
                      setActiveModal(null);
                    }}
                    disabled={
                      !canEdit || (task.status === "To Do" && !task.assigned_to)
                    }
                    className="w-full px-4 py-4 border-2 border-purple-200 rounded-2xl text-sm focus:ring-4 focus:ring-purple-500/20 focus:border-purple-500 disabled:bg-gray-100 disabled:cursor-not-allowed font-semibold shadow-sm bg-white/50 backdrop-blur-sm"
                  >
                    <option value="To Do">📋 To Do</option>
                    <option value="In Progress">⚡ In Progress</option>
                    <option value="Review">👁️ Review</option>
                    <option value="Done">✅ Done</option>
                  </select>
                </div>
              )}

              {/* Remarks Modal */}
              {activeModal === "remarks" && (
                <div className="space-y-3">
                  {!task.remarks || task.remarks.length === 0 ? (
                    <div className="text-center py-12 text-gray-500">
                      <MessageSquare
                        size={48}
                        className="mx-auto mb-4 opacity-30"
                      />
                      <p className="text-lg font-medium">No remarks yet</p>
                      <p className="text-sm">Remarks will appear here</p>
                    </div>
                  ) : (
                    task.remarks.map((r, i) => (
                      <div
                        key={i}
                        className="bg-gradient-to-r from-gray-50 to-blue-50 p-4 rounded-2xl border border-gray-200 shadow-sm hover:shadow-md transition-all"
                      >
                        <div className="flex items-start gap-3">
                          <div className="w-8 h-8 rounded-xl bg-gradient-to-br from-gray-400 to-gray-500 flex items-center justify-center text-white text-sm font-bold flex-shrink-0 shadow-md">
                            {i + 1}
                          </div>
                          <div className="flex-1 min-w-0">
                            <p className="text-gray-800 font-medium mb-1">
                              {typeof r === "object"
                                ? Object.keys(r)[0] || "Remark"
                                : "Remark"}
                            </p>
                            <p className="text-sm text-gray-700 leading-relaxed">
                              {typeof r === "object"
                                ? Object.entries(r)
                                    .map(([k, v]) => `${k}: ${v}`)
                                    .join(", ")
                                : r}
                            </p>
                          </div>
                        </div>
                      </div>
                    ))
                  )}
                </div>
              )}

              {/* Files Modal */}
              {activeModal === "files" && (
                <div className="space-y-4">
                  <div className="p-5 bg-gradient-to-br from-emerald-50 to-teal-50 rounded-2xl border-2 border-dashed border-emerald-200 shadow-inner">
                    <input
                      key={fileInputKey}
                      ref={fileInputRef}
                      type="file"
                      onChange={handleFileUpload}
                      className="hidden"
                      accept=".pdf,.doc,.docx,.jpg,.jpeg,.png,.gif"
                    />
                    <button
                      onClick={() => fileInputRef.current?.click()}
                      disabled={uploading}
                      className="w-full flex items-center justify-center gap-3 px-6 py-4 text-sm font-bold bg-gradient-to-r from-emerald-500 to-teal-500 text-white rounded-xl hover:from-emerald-600 hover:to-teal-600 disabled:opacity-50 disabled:cursor-not-allowed transition-all shadow-lg hover:shadow-xl hover:scale-[1.02]"
                    >
                      {uploading ? (
                        <>
                          <Loader2 className="w-5 h-5 animate-spin" />
                          Uploading...
                        </>
                      ) : (
                        <>
                          <Upload size={20} />
                          {selectedFileName || "Choose file to upload"}
                        </>
                      )}
                    </button>
                    <p className="text-xs text-emerald-600 mt-3 text-center font-medium">
                      📎 Supports PDF, DOC, Images (Max 10MB)
                    </p>
                  </div>

                  {taskFiles.length > 0 ? (
                    <div className="space-y-3 max-h-64 overflow-y-auto custom-scrollbar">
                      {taskFiles.map((file) => (
                        <div
                          key={file.file_id}
                          className="flex items-center justify-between p-4 bg-white rounded-xl border border-gray-200 hover:shadow-lg hover:border-emerald-300 transition-all group"
                        >
                          <div className="flex items-center gap-3 flex-1 min-w-0">
                            <div className="w-10 h-10 bg-gradient-to-br from-gray-400 to-gray-500 rounded-xl flex items-center justify-center text-white font-bold text-sm shadow-md flex-shrink-0">
                              {file.file_name.split(".").pop()?.toUpperCase() ||
                                "F"}
                            </div>
                            <div className="min-w-0 flex-1">
                              <p className="font-semibold text-sm text-gray-900 truncate group-hover:text-emerald-700">
                                {file.file_name}
                              </p>
                              <p className="text-xs text-gray-500 font-mono">
                                {(file.file_size / 1024).toFixed(1)} KB
                              </p>
                            </div>
                          </div>
                          <div className="flex items-center gap-2">
                            <button
                              onClick={() => handlePreviewFile(file.file_id)}
                              className="p-2.5 text-gray-500 hover:text-emerald-600 hover:bg-emerald-50 rounded-xl transition-all shadow-sm hover:shadow-md group-hover:scale-110"
                              title="Preview"
                            >
                              <Eye size={18} />
                            </button>
                            <button
                              onClick={() =>
                                handleDownloadFile(file.file_id, file.file_name)
                              }
                              className="p-3 text-gray-500 hover:text-blue-600 hover:bg-blue-50 rounded-xl transition-all shadow-sm hover:shadow-md group-hover:scale-110"
                              title="Download"
                            >
                              <Download size={20} />
                            </button>
                          </div>
                        </div>
                      ))}
                    </div>
                  ) : (
                    <div className="text-center py-12 text-gray-500 border-2 border-dashed border-gray-200 rounded-2xl">
                      <File size={48} className="mx-auto mb-4 opacity-30" />
                      <p className="text-lg font-semibold">No files attached</p>
                      <p className="text-sm mt-1">
                        Upload files using the button above
                      </p>
                    </div>
                  )}
                </div>
              )}

              {/* Add Remark Modal */}
              {activeModal === "addRemark" && (
                <div className="space-y-4">
                  <input
                    type="text"
                    value={remark}
                    onChange={(e) => setRemark(e.target.value)}
                    placeholder="Enter your remark here..."
                    className="w-full px-5 py-4 border-2 border-blue-200 rounded-2xl text-sm focus:ring-4 focus:ring-blue-500/20 focus:border-blue-500 bg-white/50 backdrop-blur-sm font-semibold shadow-sm"
                    onKeyDown={(e) => {
                      if (e.key === "Enter" && !addingRemark && remark.trim()) {
                        handleAddRemark();
                      }
                    }}
                  />
                  <button
                    onClick={handleAddRemark}
                    disabled={addingRemark || !remark.trim()}
                    className="w-full px-6 py-4 bg-gradient-to-r from-blue-600 to-cyan-600 text-white rounded-2xl text-sm font-bold hover:from-blue-700 hover:to-cyan-700 disabled:opacity-50 disabled:cursor-not-allowed transition-all shadow-lg hover:shadow-xl hover:scale-[1.02] flex items-center justify-center gap-2"
                  >
                    {addingRemark ? (
                      <>
                        <Loader2 className="w-5 h-5 animate-spin" />
                        Adding Remark...
                      </>
                    ) : (
                      <>
                        <Send size={20} />
                        Add Remark
                      </>
                    )}
                  </button>
                </div>
              )}
            </div>
          </div>
        </div>
      )}
    </>
  );
};

export default TaskCard;
