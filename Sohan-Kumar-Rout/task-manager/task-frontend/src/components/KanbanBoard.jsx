import React, { useEffect, useState } from "react";
import {
  DragDropContext,
  Droppable,
  Draggable,
} from "@hello-pangea/dnd";
import { getTasks, updateTask, createTask } from "../services/taskService";
import { getAttachmentsForTask, uploadAttachment, deleteAttachment, getDownloadUrl } from "../services/attachmentService";
import { getEmployees } from "../services/employeeService";
import { toast } from "react-toastify";
import { FaPlus, FaPaperclip, FaUpload, FaTrash, FaDownload } from "react-icons/fa";

// 🌈 Header colors (medium pastel tones)
const statusColors = {
  TO_DO: "#6cabeb",
  IN_PROGRESS: "#e7d16f",    // Medium pastel yellow
  REVIEW: "#d7bde2",         // Medium pastel purple
  COMPLETED: "#7dcea0",      // Medium pastel green
};

// 🌈 Column backgrounds
const pastelColumnColors = {
  TO_DO: "bg-[#DCEBFA] dark:bg-[#4A637A]",
  IN_PROGRESS: "bg-[#FFF8CC] dark:bg-[#7A6F2A]",
  REVIEW: "bg-[#F2E6FF] dark:bg-[#5A3A7A]",
  COMPLETED: "bg-[#DFF5E1] dark:bg-[#2F6B3F]",
};

// 🌈 Card backgrounds
// 🌈 Card backgrounds (PASTEL COLOURS instead of white)
const pastelCardColors = {
  // eye-catching gradients while keeping readable text and gentle borders
  // switch to white cards with a subtle light-gray border
  TO_DO: "bg-white border-[#e5e7eb]",
  IN_PROGRESS: "bg-white border-[#e5e7eb]",
  REVIEW: "bg-white border-[#e5e7eb]",
  COMPLETED: "bg-white border-[#e5e7eb]",
};


const initialColumns = {
  TO_DO: { name: "TO DO", items: [] },
  IN_PROGRESS: { name: "IN PROGRESS", items: [] },
  REVIEW: { name: "REVIEW", items: [] },
  COMPLETED: { name: "COMPLETED", items: [] },
};

const isMoveAllowedFrontend = (role, from, to) => {
  const employeeRules = {
    TO_DO: ["IN_PROGRESS"],
    IN_PROGRESS: ["REVIEW"],
  };

  const managerRules = {
    ...employeeRules,
    REVIEW: ["COMPLETED", "IN_PROGRESS"],
  };

  if (role === "Employee") return employeeRules[from]?.includes(to) || false;
  if (role === "Manager" || role === "Admin")
    return managerRules[from]?.includes(to) || false;

  return false;
};

const KanbanBoard = () => {
  const [columns, setColumns] = useState(initialColumns);
  

  // Helper: small priority pill background
  const getPriorityPillClass = (priority) => {
    switch ((priority || "").toLowerCase()) {
      case "low":
        return "bg-gray-200 text-gray-800";
      case "medium":
        return "bg-blue-200 text-blue-800";
      case "high":
        return "bg-orange-200 text-orange-800";
      case "critical":
        return "bg-red-200 text-red-800";
      default:
        return "bg-gray-100 text-gray-800";
    }
  };

  // Helper: derive initials from assigned_to (if a name) or fall back to first chars
  const getInitials = (assignedTo) => {
    if (!assignedTo) return "U";
    const s = String(assignedTo).trim();
    if (s.includes(" ")) {
      return s
        .split(" ")
        .filter(Boolean)
        .map((p) => p[0].toUpperCase())
        .slice(0, 2)
        .join("");
    }
    return s.slice(0, 2).toUpperCase();
  };

  // Helper: try to find an image URL inside an employee object by scanning common fields
  const findImageInObject = (obj) => {
    if (!obj || typeof obj !== 'object') return null;
    const candidates = [];
    const visit = (o, depth = 0) => {
      if (!o || typeof o !== 'object' || depth > 2) return;
      for (const k of Object.keys(o)) {
        try {
          const v = o[k];
          if (typeof v === 'string') {
            const s = v.toLowerCase();
            if (s.startsWith('http') || s.includes('/uploads/') || s.endsWith('.png') || s.endsWith('.jpg') || s.endsWith('.jpeg') || s.endsWith('.webp') || s.includes('cdn')) {
              candidates.push(v);
            }
          } else if (typeof v === 'object') {
            visit(v, depth + 1);
          }
        } catch (e) {
          // ignore
        }
      }
    };
    visit(obj, 0);
    return candidates.length ? candidates[0] : null;
  };

  // Helper: return shadow classes (normal + hover) based on priority
  const getShadowClass = (priority) => {
    switch ((priority || "").toLowerCase()) {
      case "low":
        return "shadow-[0_4px_10px_rgba(0,0,0,0.08)] hover:shadow-[0_6px_14px_rgba(0,0,0,0.12)]";
      case "medium":
        return "shadow-[0_6px_14px_rgba(0,0,0,0.14)] hover:shadow-[0_10px_22px_rgba(0,0,0,0.2)]";
      case "high":
        return "shadow-[0_10px_26px_rgba(0,0,0,0.28)] hover:shadow-[0_14px_38px_rgba(0,0,0,0.36)]";
      case "critical":
        return "shadow-[0_14px_36px_rgba(0,0,0,0.4)] hover:shadow-[0_18px_52px_rgba(0,0,0,0.52)]";
      default:
        return "shadow-md hover:shadow-lg";
    }
  };

  const loadTasks = async () => {
    try {
      const res = await getTasks();
      const tasks = res.data;
      // Ensure we have employee info to render profile photos
      let emps = employees || [];
      if ((!emps || emps.length === 0)) {
        try {
          const fetched = await getEmployees();
          emps = fetched || [];
          setEmployees(emps);
        } catch (e) {
          // non-blocking; we'll still render initials if no employee data
          emps = employees || [];
        }
      }

      const newCols = {
        TO_DO: { ...initialColumns.TO_DO, items: [] },
        IN_PROGRESS: { ...initialColumns.IN_PROGRESS, items: [] },
        REVIEW: { ...initialColumns.REVIEW, items: [] },
        COMPLETED: { ...initialColumns.COMPLETED, items: [] },
      };

      tasks.forEach((task) => {
        // ensure `remarks_read` local flag exists (default false) so UI can mark read/unread locally
        const t = { ...task, remarks_read: Boolean(task.remarks_read) };
        // compute expected closure urgency (days to expected closure)
        const dueRaw = task.expected_closure_date || task.expected_closure || task.expected_closure_date;
        let daysTo = null;
        if (dueRaw) {
          try {
            const now = new Date();
            const dueDate = new Date(dueRaw);
            // difference in days (ceil so within 2 calendar days counts)
            const diffDays = Math.ceil((dueDate - now) / (1000 * 60 * 60 * 24));
            daysTo = diffDays;
          } catch (e) {
            daysTo = null;
          }
        }
        t.days_to_expected = daysTo;
        // resolve assigned_to to employee metadata (name, avatar) so UI shows photo instead of id
        try {
          const emp = emps.find((e) => String(e.id) === String(task.assigned_to));
          if (emp) {
            t.assigned_to_name = emp.name || '';
            // various possible avatar/photo fields, including scanning nested keys for an image URL
            t.assigned_to_avatar = emp.avatar || emp.photo || emp.photo_url || emp.profile_pic || emp.profileUrl || emp.picture || findImageInObject(emp) || null;
          } else {
            t.assigned_to_name = null;
            t.assigned_to_avatar = null;
          }
        } catch (e) {
          t.assigned_to_name = null;
          t.assigned_to_avatar = null;
        }
        // urgent if due within 2 days (including overdue) and not completed
        t.urgent_by_date = daysTo !== null && daysTo <= 2 && task.status !== 'COMPLETED';
        if (newCols[t.status]) newCols[t.status].items.push(t);
      });

      setColumns(newCols);
    } catch (err) {
      toast.error("Failed to load tasks!");
    }
  };

  // State for remark modal
  const [activeRemarkTask, setActiveRemarkTask] = useState(null);
  const [activeTaskDetails, setActiveTaskDetails] = useState(null);
  const [createModalOpen, setCreateModalOpen] = useState(false);
  const [employees, setEmployees] = useState([]);
  const [activeAttachmentTask, setActiveAttachmentTask] = useState(null);
  const [expectedClosureDate, setExpectedClosureDate] = useState("");
  const [savingExpected, setSavingExpected] = useState(false);
  const [attachments, setAttachments] = useState([]);
  const [uploading, setUploading] = useState(false);
  const [selectedFile, setSelectedFile] = useState(null);
  const [createForm, setCreateForm] = useState({
    title: "",
    description: "",
    assigned_to: "",
    priority: "Medium",
    status: "TO_DO",
  });
  const roleRaw = localStorage.getItem("role");
  const role = roleRaw; // keep original casing for move rules
  const roleLower = roleRaw ? roleRaw.toLowerCase() : "";
  const empId = localStorage.getItem("emp_id");
  const empIdNumber = empId ? Number(empId) : null;
  const userName = localStorage.getItem("user_name") || "Employee";
  const [replyText, setReplyText] = useState("");
  const [replySending, setReplySending] = useState(false);

  const openRemarkModal = (task, e) => {
    if (e) e.stopPropagation();

    // Mark this task's remark as read in local columns state so the red dot is removed
    setColumns((prev) => {
      const newCols = {};
      Object.entries(prev).forEach(([key, col]) => {
        newCols[key] = {
          ...col,
          items: col.items.map((t) =>
            t.task_id === task.task_id ? { ...t, remarks_read: true } : t
          ),
        };
      });
      return newCols;
    });

    // Use an updated task object for the modal (reflects read state)
    setActiveRemarkTask({ ...task, remarks_read: true });
  };

  // Open a full task details modal when clicking the card
  const openTaskDetails = (task, e) => {
    if (e) e.stopPropagation();

    // set expectedClosureDate from task if present (assume ISO string or YYYY-MM-DD)
    const existing = task.expected_closure_date || task.expected_closure || "";
    let short = "";
    if (existing) {
      // normalize to YYYY-MM-DD if possible
      try {
        short = existing.split('T')[0];
      } catch {
        short = existing;
      }
    }

    setExpectedClosureDate(short);
    setActiveTaskDetails({ ...task });
  };

  const closeTaskDetails = (e) => {
    if (e) e.stopPropagation();
    setActiveTaskDetails(null);
    setExpectedClosureDate("");
  };

  const saveExpectedClosure = async () => {
    if (!activeTaskDetails) return;
    setSavingExpected(true);
    try {
      // Backend expects `expected_closure` (see backend models/schemas). Send YYYY-MM-DD or null.
      await updateTask(activeTaskDetails.task_id, { expected_closure: expectedClosureDate || null });
      toast.success('Expected closure date saved');
      await loadTasks();
      setActiveTaskDetails(null);
    } catch (err) {
      console.error('save expected date failed', err);
      toast.error('Failed to save expected closure date');
    } finally {
      setSavingExpected(false);
    }
  };

  const openAttachmentsModal = async (task, e) => {
    if (e) e.stopPropagation();
    setActiveAttachmentTask(task);
    try {
      const atts = await getAttachmentsForTask(task.task_id);
      setAttachments(atts || []);
    } catch (err) {
      console.error('load attachments failed', err);
      toast.error('Failed to load attachments');
    }
  };

  const closeAttachmentsModal = (e) => {
    if (e) e.stopPropagation();
    setActiveAttachmentTask(null);
    setAttachments([]);
  };

  const handleFileUpload = async (file) => {
    if (!file || !activeAttachmentTask) return;
    setUploading(true);
    try {
      const result = await uploadAttachment(activeAttachmentTask.task_id, file);
      toast.success('Uploaded');
      // reload attachments
      const atts = await getAttachmentsForTask(activeAttachmentTask.task_id);
      setAttachments(atts || []);
    } catch (err) {
      console.error('upload failed', err);
      toast.error('Upload failed');
    } finally {
      setUploading(false);
    }
  };

  const handleDeleteAttachment = async (id) => {
    if (!confirm('Delete attachment?')) return;
    try {
      await deleteAttachment(id);
      toast.success('Deleted');
      const atts = await getAttachmentsForTask(activeAttachmentTask.task_id);
      setAttachments(atts || []);
    } catch (err) {
      console.error(err);
      toast.error('Delete failed');
    }
  };

  const closeRemarkModal = (e) => {
    if (e) e.stopPropagation();
    setActiveRemarkTask(null);
  };

  useEffect(() => {
    loadTasks();
    // load employees for create form dropdown
    (async () => {
      try {
        const e = await getEmployees();
        setEmployees(e || []);
      } catch (err) {
        // non-blocking
      }
    })();
  }, []);

  const onDragEnd = async (result) => {
    const { source, destination } = result;
    if (!destination) return;

    const from = source.droppableId;
    const to = destination.droppableId;

    if (from === to) {
      const col = columns[from];
      const items = [...col.items];
      const [moved] = items.splice(source.index, 1);
      items.splice(destination.index, 0, moved);

      setColumns({ ...columns, [from]: { ...col, items } });
      return;
    }

    if (!isMoveAllowedFrontend(role, from, to)) {
      toast.error(`You cannot move from ${from} → ${to}`);
      return;
    }

    const sourceCol = columns[from];
    const destCol = columns[to];

    const sourceItems = [...sourceCol.items];
    const destItems = [...destCol.items];

    const [moved] = sourceItems.splice(source.index, 1);
    moved.status = to;

    destItems.splice(destination.index, 0, moved);

    setColumns({
      ...columns,
      [from]: { ...sourceCol, items: sourceItems },
      [to]: { ...destCol, items: destItems },
    });

    try {
      await updateTask(moved.task_id, { status: moved.status });
      toast.success(`Task moved to ${to}!`);
    } catch (err) {
      toast.error("Backend rejected this move. Reloading.");
      loadTasks();
    }
  };

  return (
    <div className="flex gap-6 p-4 w-full">
      {/* Inline vibration animation for bell icons (scoped here) */}
  <style>{`
        @keyframes vibrate { 
          0% { transform: translateX(0); }
          20% { transform: translateX(-2px); }
          40% { transform: translateX(2px); }
          60% { transform: translateX(-2px); }
          80% { transform: translateX(2px); }
          100% { transform: translateX(0); }
        }
        .vibrate { animation: vibrate 0.6s linear infinite; }
        /* Red pulse for high priority tasks */
        @keyframes pulse-red {
          0% { box-shadow: 0 0 0 0 rgba(239,68,68,0); }
          50% { box-shadow: 0 0 0 8px rgba(239,68,68,0.12); }
          100% { box-shadow: 0 0 0 0 rgba(239,68,68,0); }
        }
        .blink-red { animation: pulse-red 1.6s ease-in-out infinite; border-color: #ef4444 !important; }
        /* Stronger urgent pulse for expected-closure within 2 days */
        @keyframes urgent-pulse {
          0% { box-shadow: 0 0 0 0 rgba(220,38,38,0); }
          40% { box-shadow: 0 0 0 12px rgba(220,38,38,0.16); }
          100% { box-shadow: 0 0 0 0 rgba(220,38,38,0); }
        }
        .blink-urgent { animation: urgent-pulse 1s ease-in-out infinite; border-color: #dc2626 !important; }
      `}</style>

      

      <DragDropContext onDragEnd={onDragEnd}>
        {Object.entries(columns).map(([colId, col]) => (
          <div key={colId} className="w-1/4">
            <h2
              className="text-xl font-bold mb-4 p-2 rounded text-white flex items-center justify-between"
              style={{ backgroundColor: statusColors[colId] }}
            >
              <span>{col.name}</span>
              {/* Count pill next to header name - place Create button beside TO_DO count */}
              <div className="flex items-center gap-2">
                <span className="inline-block bg-white text-black text-sm font-semibold px-2 py-0.5 rounded-full">
                  {Array.isArray(col.items) ? col.items.length : 0}
                </span>
                {colId === "TO_DO" && (
                  <button
                    onClick={(e) => {
                      e.stopPropagation();
                      setCreateForm({ ...createForm, status: "TO_DO" });
                      setCreateModalOpen(true);
                    }}
                    title="Create Task"
                    className="p-1.5 bg-white/90 text-green-600 rounded hover:bg-white flex items-center justify-center"
                  >
                    <FaPlus />
                  </button>
                )}
              </div>
            </h2>

            <Droppable droppableId={colId}>
              {(provided) => (
                <div
                  ref={provided.innerRef}
                  {...provided.droppableProps}
                  className={`${pastelColumnColors[colId]} p-4 rounded-lg min-h-[500px] transition-all duration-300`}
                >
                  {col.items.map((task, index) => (
                    <Draggable
                      key={task.task_id}
                      draggableId={task.task_id.toString()}
                      index={index}
                    >
                      {(provided) => (
                        <div
                          ref={provided.innerRef}
                          {...provided.draggableProps}
                          {...provided.dragHandleProps}
                          onClick={(e) => openTaskDetails(task, e)}
                          className={`p-4 rounded-lg mb-3 transition border ${pastelCardColors[colId]} dark:bg-gray-700 dark:border-gray-600 ${getShadowClass(task.priority)} ${task.urgent_by_date ? 'blink-urgent border-red-600' : (((task.priority || '').toLowerCase() === 'high' && String(task.status) !== 'COMPLETED') ? 'blink-red border-red-500' : '')}`}
                        >
                          <span
                            className="text-white px-2 py-1 rounded text-xs font-semibold inline-block mb-2"
                            style={{ backgroundColor: statusColors[task.status] }}
                          >
                            {task.status}
                          </span>

                          <h3 className="font-bold text-black dark:text-white">
                            {task.title}
                          </h3>

                          {task.description && (
                            <p className="text-gray-700 dark:text-gray-300 text-sm mt-1">
                              {task.description}
                            </p>
                          )}

                          {/* Footer: Profile photo / initials -> Priority badge -> Bell */}
                          <div className="flex items-center justify-between mt-3">
                            <div className="flex items-center gap-3">
                              {/* Profile photo (if available) or initials */}
                              {task.assigned_to_avatar ? (
                                <img src={task.assigned_to_avatar} alt={task.assigned_to_name || task.assigned_to} className="w-8 h-8 rounded-full object-cover" />
                              ) : (
                                <div className="w-8 h-8 rounded-full bg-gray-200 dark:bg-gray-600 flex items-center justify-center text-sm font-medium text-gray-700 dark:text-gray-100">
                                  {getInitials(task.assigned_to_name || task.assigned_to)}
                                </div>
                              )}

                              <span className={`px-2 py-1 text-xs rounded-full ${getPriorityPillClass(task.priority)}`}>
                                {task.priority}
                              </span>
                            </div>

                            <div className="relative flex items-center gap-2">
                              {/* Attachments: open attachment modal */}
                              <button onClick={(e) => openAttachmentsModal(task, e)} className="p-2 rounded-full hover:bg-gray-100 dark:hover:bg-gray-700" aria-label="attachments" title="Attachments">
                                <FaPaperclip className="h-4 w-4 text-gray-700 dark:text-gray-200" />
                              </button>
                              {/* show count if attachments are present on task object */}
                              {task.attachments && task.attachments.length > 0 && (
                                <span className="text-xs font-semibold text-gray-600">{task.attachments.length}</span>
                              )}

                              {/** vibrate when there's an unread remark for this task **/}
                              {(() => {
                                const shouldVibrate = task.remarks && task.remarks.trim() && !task.remarks_read;
                                return (
                                  <button onClick={(e) => openRemarkModal(task, e)} className={`p-2 rounded-full hover:bg-gray-100 dark:hover:bg-gray-700 ${shouldVibrate ? 'vibrate' : ''}`} aria-label="remarks" title="Remarks">
                                    <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5 text-gray-700 dark:text-gray-200" viewBox="0 0 20 20" fill="currentColor">
                                      <path d="M10 2a4 4 0 00-4 4v2.586l-.707.707A1 1 0 005 11h10a1 1 0 00.707-1.707L15 8.586V6a4 4 0 00-4-4z" />
                                      <path d="M9 14a2 2 0 104 0H9z" />
                                    </svg>
                                  </button>
                                );
                              })()}
                              {/* Simple unread indicator: show dot if remarks exist AND not marked read locally */}
                              {task.remarks && task.remarks.trim() && !task.remarks_read && (
                                <span className="absolute -top-1 -right-1 inline-block w-2 h-2 bg-red-600 rounded-full" />
                              )}
                            </div>
                          </div>
                        </div>
                      )}
                    </Draggable>
                  ))}

                  {provided.placeholder}

                  {/* Remark modal (shows single stored remark from manager) */}
                  {activeRemarkTask && (
                    <div className="fixed inset-0 z-50 flex items-center justify-center bg-black bg-opacity-40" onClick={closeRemarkModal}>
                      <div className="w-full max-w-md bg-white rounded-md p-5 shadow-lg" onClick={(e) => e.stopPropagation()}>
                        <div className="flex justify-between items-center mb-3">
                          <h3 className="text-lg font-semibold">Remarks — {activeRemarkTask.title}</h3>
                          <button onClick={closeRemarkModal} className="text-gray-500 hover:text-gray-800">Close</button>
                        </div>

                        <div className="mb-4 max-h-40 overflow-auto space-y-3">
                          {/* Render only the most recent remark (JSON object) or fallback to legacy text */}
                          {(() => {
                            if (!activeRemarkTask || !activeRemarkTask.remarks) return <div className="text-sm text-gray-600">No remark available.</div>;
                            try {
                              const m = JSON.parse(activeRemarkTask.remarks);
                              const senderType = String(m.sender || '').toLowerCase() === 'employee' ? 'employee' : (String(m.sender || '').toLowerCase() === 'manager' ? 'manager' : 'system');
                              return (
                                <div className={`max-w-[85%] ${senderType === 'employee' ? 'ml-auto text-right' : 'mr-auto text-left'}`}>
                                  <div className={`inline-block px-3 py-2 rounded-lg ${senderType === 'employee' ? 'bg-indigo-600 text-white' : 'bg-gray-100 text-gray-800'}`}>
                                    <div className="text-xs opacity-70 mb-1">{m.sender}{m.sender_id ? ` • ${m.sender_id}` : ''} • {m.ts ? new Date(m.ts).toLocaleString() : ''}</div>
                                    <div className="whitespace-pre-wrap">{m.text}</div>
                                  </div>
                                  <div className="text-xs opacity-60 mt-1">{senderType === 'employee' ? 'You' : (senderType === 'system' ? 'System' : 'Manager')}</div>
                                </div>
                              );
                            } catch (e) {
                              return <div className="text-sm text-gray-600 whitespace-pre-wrap">{String(activeRemarkTask.remarks)}</div>;
                            }
                          })()}
                        </div>

                        {roleLower === "employee" ? (
                          <div className="space-y-3">
                            <textarea
                              rows={3}
                              value={replyText}
                              onChange={(e) => setReplyText(e.target.value)}
                              className="w-full p-2 border rounded"
                              placeholder="Write a reply to the manager..."
                            />

                            <div className="flex justify-end gap-2">
                              <button onClick={() => { setReplyText(""); closeRemarkModal(); }} className="px-4 py-2 border rounded">Cancel</button>
                              <button
                                onClick={async () => {
                                    if (!replyText || !replyText.trim()) return toast.error("Please enter a reply.");
                                    if (!empIdNumber) return toast.error("Employee not authenticated. Please login again.");
                                    try {
                                      const token = localStorage.getItem("token");
                                      if (!token) { toast.error("Not authenticated. Please login again."); return; }

                                      setReplySending(true);
                                      const newMsg = { sender: 'Employee', sender_id: empId, text: replyText.trim(), ts: new Date().toISOString() };
                                      // Replace remarks with the latest message. Backend will set notification flags (do not send updated_by from client)
                                      await updateTask(activeRemarkTask.task_id, { remarks: JSON.stringify(newMsg) });
                                      toast.success("Reply sent to manager.");
                                      setReplyText("");
                                      setActiveRemarkTask(null);
                                      await loadTasks();
                                    } catch (err) {
                                      console.error("send reply failed", err);
                                      const serverMsg = err?.response?.data?.detail || err?.response?.data || err?.message;
                                      toast.error(serverMsg || "Failed to send reply.");
                                    } finally {
                                      setReplySending(false);
                                    }
                                  }}
                                className={`px-4 py-2 bg-indigo-600 text-white rounded ${replySending ? 'opacity-60 cursor-wait' : ''}`}
                                disabled={replySending}
                              >
                                {replySending ? 'Sending...' : 'Send Reply'}
                              </button>
                            </div>
                          </div>
                        ) : (
                          <div className="text-right">
                            <button onClick={closeRemarkModal} className="px-4 py-2 bg-indigo-600 text-white rounded">OK</button>
                          </div>
                        )}
                        
                      </div>
                    </div>
                  )}

                  {/* Task Details Modal (opened by clicking the card) */}
                  {activeTaskDetails && (
                    <div className="fixed inset-0 z-50 flex items-center justify-center bg-black bg-opacity-40" onClick={closeTaskDetails}>
                      <div className="w-full max-w-2xl bg-white rounded-md p-5 shadow-lg" onClick={(e) => e.stopPropagation()}>
                        <div className="flex justify-between items-center mb-3">
                          <h3 className="text-lg font-semibold">Task Details — {activeTaskDetails.title}</h3>
                          <button onClick={closeTaskDetails} className="text-gray-500 hover:text-gray-800">Close</button>
                        </div>

                        <div className="grid grid-cols-1 md:grid-cols-2 gap-4 mb-4">
                          <div>
                            <div className="text-sm opacity-70">Title</div>
                            <div className="font-medium">{activeTaskDetails.title}</div>
                          </div>
                          <div>
                            <div className="text-sm opacity-70">Assigned To</div>
                            <div className="font-medium flex items-center gap-3">
                              {(() => {
                                const emp = employees.find(e => String(e.id) === String(activeTaskDetails.assigned_to));
                                const avatar = emp && (emp.avatar || emp.photo || emp.photo_url || emp.profile_pic || emp.profileUrl || emp.picture || findImageInObject(emp) || null);
                                const name = emp?.name || activeTaskDetails.assigned_to || 'Unassigned';
                                return (
                                  <>
                                    {avatar ? (
                                      <img src={avatar} alt={name} className="w-8 h-8 rounded-full object-cover" />
                                    ) : (
                                      <div className="w-8 h-8 rounded-full bg-gray-200 dark:bg-gray-600 flex items-center justify-center text-sm font-medium text-gray-700 dark:text-gray-100">{getInitials(name)}</div>
                                    )}
                                    <span>{name}</span>
                                  </>
                                );
                              })()}
                            </div>
                          </div>
                          <div className="md:col-span-2">
                            <div className="text-sm opacity-70">Description</div>
                            <div className="text-sm text-gray-700 whitespace-pre-wrap">{activeTaskDetails.description || '—'}</div>
                          </div>
                          <div>
                            <div className="text-sm opacity-70">Priority</div>
                            <div className="font-medium">{activeTaskDetails.priority}</div>
                          </div>
                          <div>
                            <div className="text-sm opacity-70">Status</div>
                            <div className="font-medium">{activeTaskDetails.status}</div>
                          </div>
                        </div>

                        <div className="mb-4">
                          <label className="block text-sm font-medium text-gray-700">Expected closure date</label>
                          {roleLower === 'employee' ? (
                            <div className="mt-2 p-2 rounded bg-gray-50 text-sm">{expectedClosureDate ? new Date(expectedClosureDate).toLocaleDateString() : '—'}</div>
                          ) : (
                            <>
                              <input
                                type="date"
                                value={expectedClosureDate}
                                onChange={(e) => setExpectedClosureDate(e.target.value)}
                                className="mt-2 p-2 border rounded w-full"
                              />
                              <div className="text-xs opacity-60 mt-1">Set or update the expected closure date for this task.</div>
                            </>
                          )}
                        </div>

                        {/* Show latest remark if present */}
                        <div className="mb-4">
                          <div className="text-sm opacity-70 mb-2">Latest remark</div>
                          <div className="max-h-36 overflow-auto p-3 bg-gray-50 rounded">
                            {(() => {
                              if (!activeTaskDetails || !activeTaskDetails.remarks) return <div className="text-sm text-gray-600">No remark available.</div>;
                              try {
                                const m = JSON.parse(activeTaskDetails.remarks);
                                return (
                                  <div>
                                    <div className="text-xs opacity-70">{m.sender}{m.sender_id ? ` • ${m.sender_id}` : ''} • {m.ts ? new Date(m.ts).toLocaleString() : ''}</div>
                                    <div className="mt-1 text-sm whitespace-pre-wrap">{m.text}</div>
                                  </div>
                                );
                              } catch (e) {
                                return <div className="text-sm text-gray-600 whitespace-pre-wrap">{String(activeTaskDetails.remarks)}</div>;
                              }
                            })()}
                          </div>
                        </div>

                        <div className="flex justify-end gap-2">
                          <button onClick={closeTaskDetails} className="px-4 py-2 border rounded">Cancel</button>
                          {roleLower !== 'employee' && (
                            <button onClick={saveExpectedClosure} disabled={savingExpected} className={`px-4 py-2 bg-blue-600 text-white rounded ${savingExpected ? 'opacity-60 cursor-wait' : ''}`}>{savingExpected ? 'Saving...' : 'Save'}</button>
                          )}
                        </div>
                      </div>
                    </div>
                  )}
                </div>
              )}
            </Droppable>
          </div>
        ))}
      </DragDropContext>
      {/* Global Create Task Modal (single instance) */}
      {createModalOpen && (
        <div className="fixed inset-0 z-50 flex items-center justify-center bg-black bg-opacity-40" onClick={() => setCreateModalOpen(false)}>
          <div className="w-full max-w-lg bg-white rounded-md p-5 shadow-lg" onClick={(e) => e.stopPropagation()}>
            <div className="flex justify-between items-center mb-3">
              <h3 className="text-lg font-semibold">Create Task (will go to TO DO)</h3>
              <button onClick={() => setCreateModalOpen(false)} className="text-gray-500 hover:text-gray-800">Close</button>
            </div>

            <div className="space-y-3">
              <input autoFocus value={createForm.title} onChange={(e) => setCreateForm({ ...createForm, title: e.target.value })} className="w-full p-2 border rounded" placeholder="Title" />
              <textarea value={createForm.description} onChange={(e) => setCreateForm({ ...createForm, description: e.target.value })} rows={3} className="w-full p-2 border rounded" placeholder="Description" />
              <select value={createForm.assigned_to} onChange={(e) => setCreateForm({ ...createForm, assigned_to: e.target.value })} className="w-full p-2 border rounded">
                <option value="">Assign To</option>
                {employees.map((emp) => (
                  <option key={emp.id} value={emp.id}>{emp.name}</option>
                ))}
              </select>
              <select value={createForm.priority} onChange={(e) => setCreateForm({ ...createForm, priority: e.target.value })} className="w-full p-2 border rounded">
                <option>Low</option>
                <option>Medium</option>
                <option>High</option>
                <option>Critical</option>
              </select>

              <div className="flex justify-end gap-2">
                <button onClick={() => setCreateModalOpen(false)} className="px-4 py-2 border rounded">Cancel</button>
                <button onClick={async () => {
                  if (!createForm.title) { toast.error('Title required'); return; }
                  try {
                    await createTask(createForm);
                    toast.success('Task created');
                    setCreateModalOpen(false);
                    setCreateForm({ title: '', description: '', assigned_to: '', priority: 'Medium', status: 'TO_DO' });
                    await loadTasks();
                  } catch (err) {
                    console.error(err);
                    toast.error('Failed to create task');
                  }
                }} className="px-4 py-2 bg-blue-600 text-white rounded">Create</button>
              </div>
            </div>
          </div>
        </div>
      )}
      {/* Attachments Modal (single instance) */}
      {activeAttachmentTask && (
        <div className="fixed inset-0 z-50 flex items-center justify-center bg-black bg-opacity-40" onClick={closeAttachmentsModal}>
          <div className="w-full max-w-lg bg-white rounded-md p-5 shadow-lg" onClick={(e) => e.stopPropagation()}>
            <div className="flex justify-between items-center mb-3">
              <h3 className="text-lg font-semibold">Attachments — {activeAttachmentTask.title}</h3>
              <button onClick={closeAttachmentsModal} className="text-gray-500 hover:text-gray-800">Close</button>
            </div>

            <div className="space-y-3">
              <div className="max-h-60 overflow-auto space-y-2">
                {attachments.length === 0 && (
                  <div className="text-sm text-gray-600">No attachments yet.</div>
                )}
                {attachments.map((a) => (
                  <div key={a.id} className="flex items-center justify-between p-2 border rounded">
                    <div className="flex items-center gap-3">
                      <FaPaperclip />
                      <div>
                        <div className="text-sm font-medium">{a.file_name}</div>
                        <div className="text-xs text-gray-500">{(a.file_size/1024).toFixed(1)} KB</div>
                      </div>
                    </div>
                    <div className="flex items-center gap-2">
                      <a href={getDownloadUrl(a.file_path)} target="_blank" rel="noreferrer" className="text-blue-600 hover:underline flex items-center gap-1"><FaDownload />Download</a>
                      <button onClick={() => handleDeleteAttachment(a.id)} className="text-red-600 flex items-center gap-1"><FaTrash />Delete</button>
                    </div>
                  </div>
                ))}
              </div>

              <div className="pt-2 border-t">
                <label className="block text-sm font-medium text-gray-700">Upload file</label>
                <input type="file" className="mt-2" onChange={(e) => setSelectedFile(e.target.files?.[0] || null)} />
                <div className="flex justify-end mt-3">
                  <button onClick={closeAttachmentsModal} className="px-4 py-2 border rounded mr-2">Close</button>
                  <button
                    onClick={async () => {
                      if (!selectedFile) { toast.error('Select a file first'); return; }
                      await handleFileUpload(selectedFile);
                      setSelectedFile(null);
                    }}
                    disabled={uploading || !selectedFile}
                    className={`px-4 py-2 bg-indigo-600 text-white rounded ${uploading ? 'opacity-60' : ''}`}
                  >
                    {uploading ? 'Uploading...' : 'Upload'}
                  </button>
                </div>
              </div>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};

export default KanbanBoard;
