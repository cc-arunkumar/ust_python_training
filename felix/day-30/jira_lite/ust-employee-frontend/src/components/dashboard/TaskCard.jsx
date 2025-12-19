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
  Edit,
} from "lucide-react";
import { PRIORITY_COLORS } from "../../utils/constants";
import { api } from "../../services/api";

const TaskCard = ({
  task,
  onStatusChange,
  onAddRemark,
  canEdit,
  onAssign,
  onOpenPanel,
  employees = [],
  token,
  currentUserId,
}) => {
  const [showMenu, setShowMenu] = useState(false);
  // activeModal removed: panels are rendered at Dashboard-level now
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

  // Files loading will be handled by the dashboard panel when opened

  // Adding remarks is handled by the dashboard panel (calls onAddRemark)

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

      // close menu; dashboard panel will handle status changes if needed
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

  // Local editable due-date state
  const [editingDue, setEditingDue] = useState(false);
  const [newDueDate, setNewDueDate] = useState(
    dueDate ? dueDate.toISOString().slice(0, 10) : ""
  );
  const [localDueDate, setLocalDueDate] = useState(
    task.expected_completion_date ? task.expected_completion_date : null
  );

  useEffect(() => {
    setLocalDueDate(
      task.expected_completion_date ? task.expected_completion_date : null
    );
    const d = task.expected_completion_date
      ? new Date(task.expected_completion_date)
      : null;
    setNewDueDate(d ? d.toISOString().slice(0, 10) : "");
  }, [task.expected_completion_date]);

  const openDueEditor = (e) => {
    e && e.stopPropagation();
    setEditingDue(true);
  };

  const cancelDueEdit = (e) => {
    e && e.stopPropagation();
    setEditingDue(false);
    const d = task.expected_completion_date
      ? new Date(task.expected_completion_date)
      : null;
    setNewDueDate(d ? d.toISOString().slice(0, 10) : "");
  };

  const saveDueDate = async (e) => {
  e && e.stopPropagation();
  if (!token) {
    alert("Not authenticated");
    return;
  }
  if (!currentUserId) {
    alert("Unknown user id");
    return;
  }

  try {
    // ✅ ONLY send the fields we want to update
    const payload = {
      expected_completion_date: newDueDate || null,
      updated_by: currentUserId,
    };
    
    await api.updateTask(token, task._id, payload);

    // update local display
    setLocalDueDate(newDueDate || null);
    setEditingDue(false);
    alert("✅ Due date updated");
  } catch (err) {
    console.error("Failed to update due date", err);
    alert("❌ Failed to update due date: " + (err.message || err));
  }
};

  // helper to compute difference in ms (dueDate - now)
  function dateDiffInMs(a, b) {
    return a.getTime() - b.getTime();
  }

  // Notification clearing is handled at the Dashboard level when the remarks panel opens.

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
                onClick={(e) => {
                  e.stopPropagation();
                  // Ask dashboard to open the remarks panel for this task
                  if (typeof onOpenPanel === "function")
                    onOpenPanel("remarks", task);
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
                          if (typeof onOpenPanel === "function")
                            onOpenPanel("assign", task);
                        }}
                        className="w-full px-4 py-3 text-left text-sm hover:bg-gradient-to-r hover:from-indigo-50 hover:to-blue-50 flex items-center gap-3 text-gray-700 hover:text-indigo-700 font-medium transition-all border-l-4 border-transparent hover:border-indigo-400"
                      >
                        <UserPlus size={18} />
                        Assign Task
                      </button>
                    )}

                    <button
                      onClick={() => {
                        setShowMenu(false);
                        if (typeof onOpenPanel === "function")
                          onOpenPanel("status", task);
                      }}
                      className="w-full px-4 py-3 text-left text-sm hover:bg-gradient-to-r hover:from-purple-50 hover:to-pink-50 flex items-center gap-3 text-gray-700 hover:text-purple-700 font-medium transition-all border-l-4 border-transparent hover:border-purple-400"
                    >
                      <Calendar size={18} />
                      Change Status
                    </button>

                    {task.remarks && task.remarks.length > 0 && (
                      <button
                        onClick={() => {
                          setShowMenu(false);
                          if (typeof onOpenPanel === "function")
                            onOpenPanel("remarks", task);
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
                          setShowMenu(false);
                          if (typeof onOpenPanel === "function")
                            onOpenPanel("addRemark", task);
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
                          if (typeof onOpenPanel === "function")
                            onOpenPanel("files", task);
                        }}
                        className="w-full px-4 py-3 text-left text-sm hover:bg-gradient-to-r hover:from-emerald-50 hover:to-teal-50 flex items-center gap-3 text-gray-700 hover:text-emerald-700 font-medium transition-all border-l-4 border-transparent hover:border-emerald-400"
                      >
                        <File size={18} />
                        Manage Files ({taskFiles.length})
                      </button>
                    )}
                    {canEdit && (
  <button
    onClick={() => {
      setShowMenu(false);
      if (typeof onOpenPanel === "function")
        onOpenPanel("edit", task);
    }}
    className="w-full px-4 py-3 text-left text-sm hover:bg-gradient-to-r hover:from-amber-50 hover:to-yellow-50 flex items-center gap-3 text-gray-700 hover:text-amber-700 font-medium transition-all border-l-4 border-transparent hover:border-amber-400"
  >
    <Edit size={18} />
    Edit Task
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

            {/* Due date (click to edit) */}
            {editingDue ? (
              <div
                className="flex items-center gap-2 px-3 py-2 rounded-xl border border-purple-100"
                onClick={(e) => e.stopPropagation()}
              >
                <div className="w-6 h-6 rounded-lg bg-purple-500 flex items-center justify-center text-white shadow-sm">
                  <Calendar size={14} />
                </div>

                <div className="flex-1 flex items-center gap-3">
                  <input
                    type="date"
                    value={newDueDate}
                    onChange={(e) => setNewDueDate(e.target.value)}
                    className="px-3 py-2 border rounded-lg text-sm outline-none"
                  />

                  <div className="ml-auto flex items-center gap-2">
                    <button
                      onClick={saveDueDate}
                      className="px-3 py-1 bg-blue-600 text-white rounded-md text-sm font-semibold"
                    >
                      Save
                    </button>
                    <button
                      onClick={cancelDueEdit}
                      className="px-3 py-1 bg-gray-100 text-gray-700 rounded-md text-sm"
                    >
                      Cancel
                    </button>
                  </div>
                </div>
              </div>
            ) : (
              <div
                className="flex items-center gap-2 bg-gradient-to-r from-purple-50 to-pink-50 px-3 py-2 rounded-xl border border-purple-100 cursor-pointer"
                onClick={openDueEditor}
              >
                <div className="w-6 h-6 rounded-lg bg-gradient-to-br from-purple-500 to-pink-500 flex items-center justify-center text-white shadow-sm">
                  <Calendar size={14} />
                </div>

                <div className="flex-1">
                  <span className="text-gray-500 font-medium block">
                    Due date
                  </span>
                  <span className="font-bold text-gray-800 block">
                    {localDueDate
                      ? new Date(localDueDate).toLocaleDateString()
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
                      title={`Due in ${daysLeft} day${
                        daysLeft === 1 ? "" : "s"
                      }`}
                      aria-label={`Due in ${daysLeft} day${
                        daysLeft === 1 ? "" : "s"
                      }`}
                    ></span>
                  </div>
                ) : null}
              </div>
            )}
          </div>
        </div>
      </div>

      {/* Modals removed: dashboard-level panel handles assign/status/remarks/files */}
    </>
  );
};

export default TaskCard;
