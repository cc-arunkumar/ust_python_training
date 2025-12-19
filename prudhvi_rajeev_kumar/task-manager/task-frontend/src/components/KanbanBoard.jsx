import React, { useEffect, useState, useRef } from "react";
import {
  DragDropContext,
  Droppable,
  Draggable,
} from "@hello-pangea/dnd";
import { getTasks, updateTask, createTask, deleteTask } from "../services/taskService";
import { getAttachments, createAttachment, deleteAttachment, uploadAttachment } from "../services/attachmentService";
import api from "../services/api";
import { getEmployees } from "../services/employeeService";
import { toast, ToastContainer } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";
import { FiEye, FiEdit3, FiTrash2, FiBell, FiPaperclip, FiClock, FiUser, FiPlus, FiList, FiFilter } from 'react-icons/fi';
import { createPortal } from 'react-dom';

// Jira-inspired colors: header chips and column accents
const statusColors = {
  TO_DO: "#5E6C84",        // neutral slate (Jira muted)
  IN_PROGRESS: "#FFAB00",  // Jira amber (in progress)
  REVIEW: "#2684FF",       // Atlassian blue
  COMPLETED: "#36B37E",    // Atlassian green
};

// helper: convert hex color to rgba with alpha
const hexToRgba = (hex, alpha = 1) => {
  if (!hex) return `rgba(0,0,0,${alpha})`;
  const h = hex.replace('#', '');
  const bigint = parseInt(h, 16);
  const r = (bigint >> 16) & 255;
  const g = (bigint >> 8) & 255;
  const b = bigint & 255;
  return `rgba(${r}, ${g}, ${b}, ${alpha})`;
};

// Column background tints (soft, Jira-like)
const pastelColumnColors = {
  TO_DO: "bg-[#F4F5F7]",         // light neutral
  IN_PROGRESS: "bg-[#FFF7E6]",   // light amber
  REVIEW: "bg-[#E9F2FF]",        // light blue
  COMPLETED: "bg-[#E9F9F0]",     // light green
};

// Priority colors used for subtle card accent/border
const priorityColors = {
  Low: "border-[#36B37E]",      // green
  Medium: "border-[#FFAB00]",   // amber
  High: "border-[#FF7A7A]",     // light red
  Critical: "border-[#AE0E0E]", // dark red
};

// Hex colors for stronger left-edge accents on cards (Jira-like)
const priorityHex = {
  Low: "#36B37E",
  Medium: "#FFAB00",
  High: "#FF7A7A",
  Critical: "#AE0E0E",
};

const initialColumns = {
  TO_DO: { name: "TO_DO", items: [] },
  IN_PROGRESS: { name: "IN_PROGRESS", items: [] },
  REVIEW: { name: "REVIEW", items: [] },
  COMPLETED: { name: "COMPLETED", items: [] },
};

const KanbanBoard = () => {
  const [columns, setColumns] = useState(initialColumns);
  const [selectedTask, setSelectedTask] = useState(null);
  const [taskTitle, setTaskTitle] = useState("");
  const [taskDescription, setTaskDescription] = useState("");
  const [taskPriority, setTaskPriority] = useState("");
  const [taskRemarks, setTaskRemarks] = useState(""); // State to hold remarks
  const [showForm, setShowForm] = useState(false); // Control the visibility of the Create Task form
  const [employees, setEmployees] = useState([]);
  const managerId = localStorage.getItem("emp_id");
  const [form, setForm] = useState({
    title: "",
    description: "",
    assigned_to: "",
    assigned_by: managerId,
    priority: "Medium",
    status: "TO_DO",
    expected_closure: "",
    reviewer: "",
  });
  const titleInputRef = useRef(null);
  const [pendingMove, setPendingMove] = useState(null);
  const [remarkInput, setRemarkInput] = useState("");
  const [showRemarkModal, setShowRemarkModal] = useState(false);
  const [attachments, setAttachments] = useState([]);
  const [newFile, setNewFile] = useState(null);
  const [attachmentCounts, setAttachmentCounts] = useState({});
  const [prevNotifCounts, setPrevNotifCounts] = useState({});
  const [ringingTasks, setRingingTasks] = useState([]);
  const [seenNotifications, setSeenNotifications] = useState([]);
  const [employeeRemark, setEmployeeRemark] = useState("");
  const [deleteTarget, setDeleteTarget] = useState(null); // task to be deleted
  const [attachmentsTarget, setAttachmentsTarget] = useState(null);
  const [showDeleteConfirm, setShowDeleteConfirm] = useState(false);
  const [isEditMode, setIsEditMode] = useState(false);
  const [notificationsTarget, setNotificationsTarget] = useState(null);
  const [assigneeTarget, setAssigneeTarget] = useState(null);
  const [hoverUserTaskId, setHoverUserTaskId] = useState(null);
  const [hoverPos, setHoverPos] = useState(null);
  const [searchTerm, setSearchTerm] = useState("");
  const [priorityFilter, setPriorityFilter] = useState('All');
  const [showPriorityDropdown, setShowPriorityDropdown] = useState(false);
  const [showMyTasks, setShowMyTasks] = useState(false);
  const [myTasks, setMyTasks] = useState([]);
  const [showAssignedTasks, setShowAssignedTasks] = useState(false);
  const [assignedTasks, setAssignedTasks] = useState([]);
  const [showEmployeesModal, setShowEmployeesModal] = useState(false);
  const [employeesSummary, setEmployeesSummary] = useState([]);

  // Load tasks from the API
  const loadTasks = async () => {
    const res = await getTasks();
    const tasks = res.data;

    const newCols = {
      TO_DO: { ...initialColumns.TO_DO, items: [] },
      IN_PROGRESS: { ...initialColumns.IN_PROGRESS, items: [] },
      REVIEW: { ...initialColumns.REVIEW, items: [] },
      COMPLETED: { ...initialColumns.COMPLETED, items: [] },
    };

    tasks.forEach((task) => {
      if (newCols[task.status]) newCols[task.status].items.push(task);
    });

    setColumns(newCols);
  };

  // Load attachment counts for notification badges and trigger bell ringing when new notifications appear
  const loadAttachmentCounts = async () => {
    try {
      const atts = await getAttachments();
      // atts is an array of attachments
      const counts = {};
      (atts || []).forEach((a) => {
        const id = Number(a.task_id);
        counts[id] = (counts[id] || 0) + 1;
      });

      // compute notification totals per task (remarks lines + attachments)
      const totals = {};
      Object.values(columns).forEach((col) => {
        col.items.forEach((t) => {
          const remarksCount = t.remarks ? String(t.remarks).split('\n').filter(Boolean).length : 0;
          const attachCount = counts[Number(t.task_id)] || 0;
          totals[t.task_id] = remarksCount + attachCount;
        });
      });

      // if prevNotifCounts is empty (first load), initialize and do not trigger ringing
      if (Object.keys(prevNotifCounts).length === 0) {
        setAttachmentCounts(counts);
        setPrevNotifCounts(totals);
        return;
      }

      // compare with prevNotifCounts to detect increases
      const increased = [];
      for (const tid in totals) {
        const prev = prevNotifCounts[tid] || 0;
        if (totals[tid] > prev) increased.push(Number(tid));
      }

      if (increased.length > 0) {
        setRingingTasks((r) => Array.from(new Set([...r, ...increased])));
        // if new notifications arrived, make sure the task is no longer marked as "seen"
        setSeenNotifications((prev) => prev.filter((id) => !increased.includes(Number(id))));
        // clear ringing after 1s
        setTimeout(() => {
          setRingingTasks((r) => r.filter(id => !increased.includes(id)));
        }, 1000);
      }

      setAttachmentCounts(counts);
      setPrevNotifCounts(totals);
    } catch (err) {
      // ignore
    }
  };

  useEffect(() => {
    loadTasks();
  }, []);

  // whenever columns change, refresh attachment counts (so badge updates)
  useEffect(() => {
    loadAttachmentCounts();
  }, [columns]);

  // Listen for global attachment changes (other components can dispatch 'attachments:changed')
  useEffect(() => {
    const handler = () => loadAttachmentCounts();
    window.addEventListener('attachments:changed', handler);
    return () => window.removeEventListener('attachments:changed', handler);
  }, []);

  // Current user role (set at login into localStorage)
  const role = localStorage.getItem("role");

  // Determine whether a user with `role` is allowed to move a task from `from` to `to`.
  // Rules (per requirements):
  // - Managers/Admins cannot move between TO_DO <-> IN_PROGRESS
  // - Managers/Admins cannot move IN_PROGRESS -> REVIEW
  // - Managers/Admins CAN move REVIEW -> COMPLETED
  // - Managers/Admins CANNOT move COMPLETED -> REVIEW (not vice versa)
  // - Managers/Admins CAN move REVIEW -> IN_PROGRESS (move back)
  // Employees keep full drag privileges (handled by default)
  const isMoveAllowed = (role, from, to) => {
    if (!role) return true; // unknown role -> allow by default
    const r = role.toLowerCase();
    if (r === "manager" || r === "admin") {
      // disallow TODO <-> IN_PROGRESS
      if ((from === "TO_DO" && to === "IN_PROGRESS") || (from === "IN_PROGRESS" && to === "TO_DO")) {
        return false;
      }

      // disallow IN_PROGRESS -> REVIEW
      if (from === "IN_PROGRESS" && to === "REVIEW") return false;

      // allow REVIEW -> COMPLETED and REVIEW -> IN_PROGRESS
      if (from === "REVIEW" && (to === "COMPLETED" || to === "IN_PROGRESS")) return true;

      // disallow moving away from COMPLETED (no reverse)
      if (from === "COMPLETED") return false;

      // For any other transitions not explicitly allowed above, deny by default for managers/admins.
      return false;
    }

    // Employees: strict workflow
    if (r === "employee") {
      // allow reorder within same column
      if (from === to) return true;

      // allow TO_DO -> IN_PROGRESS
      if (from === "TO_DO" && to === "IN_PROGRESS") return true;

      // allow IN_PROGRESS -> REVIEW
      if (from === "IN_PROGRESS" && to === "REVIEW") return true;

      // disallow any other transitions for employees
      return false;
    }

    // Other/unknown roles: allow by default
    return true;
  };

  // Handle drag end and update task status
  const onDragEnd = async (result) => {
    const { source, destination } = result;
    if (!destination) return;

    const from = source.droppableId;
    const to = destination.droppableId;

    // Check role-based move permissions before applying any optimistic UI changes
    if (!isMoveAllowed(role, from, to)) {
      toast.info("You are not allowed to move this task to the selected column.");
      return;
    }

    // If a manager/admin is performing the move and it's actually moving between columns,
    // prompt for a remark before completing the move so the assigned employee can be notified.
    const r = role ? role.toLowerCase() : "";
    if ((r === "manager" || r === "admin") && from !== to) {
      // capture the moved task and postpone the actual update until remark is added
      const movedTask = columns[from].items[source.index];
      setPendingMove({ movedTask, from, to, sourceIndex: source.index, destIndex: destination.index });
      setRemarkInput("");
      setShowRemarkModal(true);
      return;
    }

    if (from === to) {
      const col = columns[from];
      const items = [...col.items];
      const [moved] = items.splice(source.index, 1);
      items.splice(destination.index, 0, moved);

      setColumns({ ...columns, [from]: { ...col, items } });
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

  // Called when manager confirms remark for a pending move
  const confirmPendingMove = async () => {
    if (!pendingMove) return;
    const { movedTask, from, to, sourceIndex, destIndex } = pendingMove;

    // Apply optimistic UI update
    const sourceCol = columns[from];
    const destCol = columns[to];
    const sourceItems = [...sourceCol.items];
    const destItems = [...destCol.items];

    // Remove the task from source index (ensure it's same task id)
    const [moved] = sourceItems.splice(sourceIndex, 1);
    moved.status = to;
    // attach the manager remark into the task
    moved.remarks = remarkInput;

    destItems.splice(destIndex, 0, moved);

    setColumns({
      ...columns,
      [from]: { ...sourceCol, items: sourceItems },
      [to]: { ...destCol, items: destItems },
    });

    setShowRemarkModal(false);
    setPendingMove(null);

    try {
      // send status and remarks to backend; backend should notify the assigned employee if implemented
      await updateTask(moved.task_id, { status: moved.status, remarks: remarkInput });
      toast.success(`Task moved to ${to} and remark sent to assignee.`);
    } catch (err) {
      toast.error("Backend rejected this move. Reloading.");
      loadTasks();
    }
  };

  const cancelPendingMove = () => {
    setPendingMove(null);
    setRemarkInput("");
    setShowRemarkModal(false);
    // no UI changes performed; the drag is effectively cancelled
  };

  // Handle priority change for a task
  const handlePriorityChange = async (taskId, newPriority) => {
    const updatedColumns = { ...columns };
    let task;

    for (const colId in updatedColumns) {
      task = updatedColumns[colId].items.find((t) => t.task_id === taskId);
      if (task) break;
    }

    if (task) {
      task.priority = newPriority;

      try {
        await updateTask(taskId, { priority: newPriority });
        toast.success("Priority updated!");
      } catch (err) {
        toast.error("Failed to update priority.");
      }

      setColumns(updatedColumns);
    }
  };

  // Handle task click to view task details
  const handleTaskClick = (task) => {
    setSelectedTask(task);
    setTaskTitle(task.title);
    setTaskDescription(task.description || "");
    setTaskPriority(task.priority);
    setTaskRemarks(task.remarks || ""); // Set the remarks when task is clicked
    // load attachments for that task
    loadAttachments(task.task_id);
  };

  const loadAttachments = async (taskId) => {
    try {
      const res = await getAttachments();
      const taskAtt = (res || []).filter((a) => Number(a.task_id) === Number(taskId));
      setAttachments(taskAtt);
    } catch (err) {
      // ignore
      setAttachments([]);
    }
  };

  // Handle save task after editing
  const handleSaveTask = async () => {
    const updatedTask = {
      task_id: selectedTask.task_id,
      title: taskTitle,
      description: taskDescription,
      priority: taskPriority,
      remarks: taskRemarks,
    };

    try {
      await updateTask(selectedTask.task_id, updatedTask);
      toast.success("Task updated successfully!");

      const updatedColumns = { ...columns };

      for (const colId in updatedColumns) {
        const taskIndex = updatedColumns[colId].items.findIndex(
          (task) => task.task_id === selectedTask.task_id
        );

        if (taskIndex !== -1) {
          updatedColumns[colId].items[taskIndex] = { ...updatedColumns[colId].items[taskIndex], ...updatedTask };
          break;
        }
      }

      setColumns(updatedColumns);
      setSelectedTask(null);
    } catch (err) {
      toast.error("Failed to update task.");
    }
  };

  // Employee uploads a file (metadata saved via attachments API)
  const handleFilePick = (e) => {
    const f = e.target.files?.[0] || null;
    setNewFile(f);
  };

  const uploadFile = async () => {
    if (!newFile || !selectedTask) {
      toast.error('Select a file first');
      return;
    }

    try {
      // perform multipart upload to backend which stores file and metadata
      const form = new FormData();
      form.append('task_id', Number(selectedTask.task_id));
      form.append('uploaded_by', Number(localStorage.getItem('emp_id')));
      form.append('file', newFile);

      await uploadAttachment(form);
      toast.success('Attachment uploaded successfully.');
      setNewFile(null);
      loadAttachments(selectedTask.task_id);

      // notify other parts of the app that attachments changed so badges refresh
      try { window.dispatchEvent(new Event('attachments:changed')); } catch(e) { /* ignore */ }
    } catch (err) {
      console.error(err);
      toast.error('Failed to upload attachment.');
    }
  };

  const downloadAttachment = async (id, fileName) => {
    try {
      const res = await api.get(`/attachments/${id}/download`, { responseType: 'blob' });
      const url = window.URL.createObjectURL(new Blob([res.data]));
      const link = document.createElement('a');
      link.href = url;
      link.setAttribute('download', fileName || 'file');
      document.body.appendChild(link);
      link.click();
      link.remove();
      window.URL.revokeObjectURL(url);
    } catch (err) {
      console.error(err);
      toast.error('Failed to download file');
    }
  };

  const removeAttachment = async (id) => {
    try {
      await deleteAttachment(id);
      toast.success('Attachment removed');
      if (selectedTask) loadAttachments(selectedTask.task_id);
      // notify other parts of the app that attachments changed so badges refresh
      try { window.dispatchEvent(new Event('attachments:changed')); } catch(e) { /* ignore */ }
    } catch (err) {
      toast.error('Failed to delete attachment');
    }
  };

  // Employee can send a remark back to manager; we'll append to existing remarks
  const sendEmployeeRemark = async () => {
    if (!selectedTask) return;
    if (!employeeRemark) {
      toast.error('Please enter a remark');
      return;
    }

    try {
      const existing = selectedTask.remarks ? String(selectedTask.remarks) + '\n' : '';
      const appended = `${existing}Employee(${localStorage.getItem('user_name') || localStorage.getItem('emp_id')}): ${employeeRemark}`;
      await updateTask(selectedTask.task_id, { remarks: appended, updated_by: Number(localStorage.getItem('emp_id')) });
      toast.success('Remark sent to manager');
      // refresh task and UI
      loadTasks();
      setSelectedTask(null);
      setEmployeeRemark('');
    } catch (err) {
      toast.error('Failed to send remark');
    }
  };

  // Handle Create Task form submission
  const handleCreate = async (e) => {
    e?.preventDefault?.();
    if (!form.title || !form.assigned_to) {
      toast.error("Title and employee are required.");
      return;
    }

    try {
      await createTask(form);
      toast.success("Task created successfully!");
      // reset form and reload
      setForm({ ...form, title: "", description: "", assigned_to: "" });
      loadTasks();
      setShowForm(false);
    } catch (error) {
      toast.error("Failed to create task.");
    }
  };

  // Load employees for assignment (used in the Create Task form)
  useEffect(() => {
    const loadEmployees = async () => {
      try {
        const res = await getEmployees();
        const data = Array.isArray(res) ? res : (res?.data || []);
        setEmployees(data);
      } catch (err) {
        // silently ignore - no employees to show
      }
    };

    loadEmployees();
  }, [managerId]);

  // when the Create Task modal opens, focus the title input for faster entry
  useEffect(() => {
    if (showForm && titleInputRef.current) {
      setTimeout(() => titleInputRef.current.focus(), 80);
    }
  }, [showForm]);

  // Helper to resolve an employee id to a display name (fallback to id)
  const getEmployeeName = (id) => {
    if (!id) return "—";
    const e = employees.find((emp) => String(emp.id) === String(id));
    return e ? e.name : id;
  };

  // Avatar images (reuse same images as sidebars)
  const managerAvatar = "https://img.freepik.com/premium-photo/3d-avatar-cartoon-character_113255-95871.jpg";
  const employeeAvatar = "https://img.freepik.com/premium-photo/3d-cartoon-avatar_113255-5627.jpg";

  // Fallback avatar pool provided by user (do not modify sidebar images)
  const fallbackAvatars = [
    "https://img.freepik.com/premium-photo/cartoon-vector-profile-avatar_1183071-2894.jpg",
    "https://static.vecteezy.com/system/resources/previews/024/183/502/original/male-avatar-portrait-of-a-young-man-with-a-beard-illustration-of-male-character-in-modern-color-style-vector.jpg",
    "https://static.vecteezy.com/system/resources/previews/024/183/525/original/avatar-of-a-man-portrait-of-a-young-guy-illustration-of-male-character-in-modern-color-style-vector.jpg",
    "https://mir-s3-cdn-cf.behance.net/project_modules/max_1200/01f9e3124033301.60fb358c954c1.jpg",
  ];

  // deterministic chooser: prefer employee.image, otherwise pick one from fallbackAvatars based on id
  const chooseAvatarForId = (id) => {
    try {
      const n = Number(id);
      if (!Number.isNaN(n)) {
        return fallbackAvatars[Math.abs(n) % fallbackAvatars.length];
      }
      // fallback: hash string
      let h = 0;
      for (let i = 0; i < String(id).length; i++) h = (h << 5) - h + String(id).charCodeAt(i);
      return fallbackAvatars[Math.abs(h) % fallbackAvatars.length];
    } catch (e) {
      return fallbackAvatars[0];
    }
  };

  const getEmployeeImage = (emp) => {
    if (!emp) return employeeAvatar;
    if (emp.image) return emp.image;
    return chooseAvatarForId(emp.id || emp);
  };

  // filter tasks by searchTerm (title or description) and priority
  const getFilteredColumns = () => {
    const q = String(searchTerm || "").trim().toLowerCase();
    const pf = (priorityFilter || 'All').toLowerCase();

    const out = {};
    Object.entries(columns).forEach(([colId, col]) => {
      const items = (col.items || []).filter((task) => {
        const taskPriority = String(task.priority || '').toLowerCase();
        if (pf !== 'all' && taskPriority !== pf) return false;
        if (!q) return true;
        const inTitle = String(task.title || "").toLowerCase().includes(q);
        const inDesc = String(task.description || "").toLowerCase().includes(q);
        return inTitle || inDesc;
      });
      out[colId] = { ...col, items };
    });
    return out;
  };

  const displayColumns = getFilteredColumns();

  return (
    <div className="flex flex-col gap-4 p-6 w-full font-sans">
      <div className="w-full flex justify-end items-center gap-3">
        <input
          value={searchTerm}
          onChange={(e) => setSearchTerm(e.target.value)}
          placeholder="Search by title or description..."
          className="px-3 py-2 border rounded w-80"
        />

        {/* Priority filter dropdown */}
        <div className="relative">
          <button
            onClick={() => setShowPriorityDropdown((s) => !s)}
            title="Filter by priority"
            className="ml-2 px-3 py-2 bg-gray-100 text-gray-800 rounded hover:bg-gray-200 flex items-center gap-2"
          >
            <FiFilter />
            <span className="hidden sm:inline">{priorityFilter === 'All' ? 'Filter' : priorityFilter}</span>
          </button>

          {showPriorityDropdown && (
            <div className="absolute mt-2 left-0 bg-white rounded shadow-md z-50 w-40">
              {["All", "Low", "Medium", "High", "Critical"].map((p) => (
                <div
                  key={p}
                  onClick={() => { setPriorityFilter(p); setShowPriorityDropdown(false); }}
                  className={`px-3 py-2 cursor-pointer hover:bg-gray-100 ${priorityFilter === p ? 'font-semibold bg-gray-50' : ''}`}
                >
                  {p}
                </div>
              ))}
            </div>
          )}
        </div>
        <button
          onClick={() => {
            // collect tasks assigned to current user
            const empId = String(localStorage.getItem('emp_id'));
            const all = [];
            Object.values(columns).forEach(col => (col.items || []).forEach(t => all.push(t)));
            const assigned = all.filter(t => String(t.assigned_to) === empId);
            setMyTasks(assigned);
            setShowMyTasks(true);
          }}
          title="My tasks"
          className="ml-2 px-3 py-2 bg-gray-100 text-gray-800 rounded hover:bg-gray-200 flex items-center gap-2"
        >
          <FiList />
          <span className="hidden sm:inline">My Tasks</span>
        </button>
        <button
          onClick={() => {
            // collect tasks assigned by current user (manager)
            const me = String(localStorage.getItem('emp_id'));
            const all = [];
            Object.values(columns).forEach(col => (col.items || []).forEach(t => all.push(t)));
            const assignedByMe = all.filter(t => String(t.assigned_by) === me);
            // ensure deterministic dummy due dates for items missing expected_closure
            const withDue = assignedByMe.map((t, idx) => {
              if (t.expected_closure) return t;
              const days = (idx % 7) + 3; // 3-9 days
              const d = new Date();
              d.setDate(d.getDate() + days);
              // format YYYY-MM-DD to match date inputs/back-end expectations
              const iso = d.toISOString().slice(0, 10);
              return { ...t, expected_closure: iso };
            });
            setAssignedTasks(withDue);
            setShowAssignedTasks(true);
          }}
          title="Assigned by me"
          className="ml-2 px-3 py-2 bg-gray-100 text-gray-800 rounded hover:bg-gray-200 flex items-center gap-2"
        >
          <FiUser />
          <span className="hidden sm:inline">Assigned</span>
        </button>
        <button
          onClick={() => {
            // build employee summary
            const all = [];
            Object.values(columns).forEach(col => (col.items || []).forEach(t => all.push(t)));

            const summary = employees.map((emp) => {
              const assigned = all.filter(t => String(t.assigned_to) === String(emp.id));
              const completed = assigned.filter(t => t.status === 'COMPLETED').length;
              return {
                id: emp.id,
                name: emp.name,
                image: emp.image,
                assignedTasks: assigned,
                completedCount: completed,
              };
            });

            setEmployeesSummary(summary);
            setShowEmployeesModal(true);
          }}
          title="Employees"
          className="ml-2 px-3 py-2 bg-gray-100 text-gray-800 rounded hover:bg-gray-200 flex items-center gap-2"
        >
          <FiUser />
          <span className="hidden sm:inline">Employees</span>
        </button>
        <button
          onClick={() => setShowForm(true)}
          title="Create task"
          className="ml-2 px-3 py-2 bg-indigo-600 text-white rounded hover:bg-indigo-700 flex items-center gap-2"
        >
          <FiPlus />
          <span className="hidden sm:inline">Create</span>
        </button>
      </div>

      <div className="flex gap-6 w-full">
      <DragDropContext onDragEnd={onDragEnd}>
        {Object.entries(displayColumns).map(([colId, col]) => (
          <div key={colId} className="w-1/4 relative kanban-column">
            <h2
              className="flex items-center justify-between text-lg font-semibold mb-4 p-4 rounded-lg kanban-header"
              style={{ backgroundColor: hexToRgba(statusColors[colId], 0.12), color: statusColors[colId], borderBottom: `2px solid ${hexToRgba(statusColors[colId], 0.18)}` }}
            >
              <div className="flex items-center gap-3">
                <span className="uppercase tracking-wider text-sm">{col.name.replace(/_/g, ' ')}</span>
                <span className="text-xs bg-white/20 px-2 py-0.5 rounded-full">{col.items.length}</span>
              </div>

              {/* Header actions intentionally removed for a cleaner Jira-like header (no Add button) */}
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
                            className={`kanban-card relative bg-white pl-6 pr-4 py-4 rounded-lg mb-4 shadow-md transition-all min-h-[120px] flex flex-col justify-between`}
                          >
                            {/* left accent bar */}
                            <div style={{ backgroundColor: priorityHex[task.priority] || 'transparent' }} className="absolute left-0 top-0 bottom-0 w-1.5 rounded-l-md" />
                            {/* Accessibility: screen-reader label for critical tasks */}
                            {task.priority === 'Critical' && (
                              <span className="sr-only">Critical priority</span>
                            )}
                            <div className="mb-2 relative">
                            <div className="flex justify-between items-start">
                              <div className="flex items-center gap-2">
                                {/* Drag handle: three horizontal lines — only this element is the drag handle */}
                                <button
                                  {...provided.dragHandleProps}
                                  onClick={(e) => e.stopPropagation()}
                                  aria-label="Drag task"
                                  className="drag-handle cursor-grab p-1 text-gray-400 hover:text-gray-600"
                                >
                                  <svg xmlns="http://www.w3.org/2000/svg" className="w-4 h-4" viewBox="0 0 20 20" fill="currentColor">
                                    <path d="M3 5h14a1 1 0 110 2H3a1 1 0 110-2zm0 4h14a1 1 0 110 2H3a1 1 0 110-2zm0 4h14a1 1 0 110 2H3a1 1 0 110-2z" />
                                  </svg>
                                </button>

                                {/* Title (larger, truncated like Jira cards) */}
                                <h3 className="font-semibold text-black cursor-pointer mt-1 title text-lg truncate max-w-[70%]" onClick={(e) => { e.stopPropagation(); handleTaskClick(task); }}>{task.title}</h3>
                              </div>

                              <div className="flex items-center gap-2">
                                <button
                                  title="Notifications"
                                  onClick={(e) => {
                                    e.stopPropagation();
                                    // compute current total for this task and mark it as seen (baseline)
                                    const remarksCount = task.remarks ? String(task.remarks).split('\n').filter(Boolean).length : 0;
                                    const attachCount = attachmentCounts[Number(task.task_id)] || 0;
                                    const total = remarksCount + attachCount;
                                    setPrevNotifCounts((p) => ({ ...p, [task.task_id]: total }));
                                    setSeenNotifications((s) => Array.from(new Set([...s, Number(task.task_id)])));
                                    setNotificationsTarget(task);
                                  }}
                                  className={`relative p-1 rounded hover:bg-gray-100 icon-btn ${ringingTasks.includes(Number(task.task_id)) ? 'ringing' : ''}`}
                                >
                                  <FiBell className="text-lg" />
                                  {(() => {
                                    const remarksCount = task.remarks ? String(task.remarks).split('\n').filter(Boolean).length : 0;
                                    const attachCount = attachmentCounts[Number(task.task_id)] || 0;
                                    const total = remarksCount + attachCount;
                                    const prev = prevNotifCounts[task.task_id] || 0;
                                    const isSeen = seenNotifications.includes(Number(task.task_id));
                                    // hide badge when the user has opened notifications and there are no new items since
                                    if (isSeen && total <= prev) return null;
                                    return total > 0 ? (
                                      <span className="absolute -top-2 -right-2 notif-badge">{total}</span>
                                    ) : null;
                                  })()}
                                </button>
                                {/* attachment icon will open attachments modal */}
                                {/* removed duplicate attachment icon from the top-right */}
                              </div>
                            </div>
                          </div>

                          {task.description && (
                            <p className="text-gray-700 dark:text-gray-300 text-sm mt-2">{task.description}</p>
                          )}

                          {/* Due days (use provided expected_closure if present, otherwise assign deterministic dummy days) */}
                          {(() => {
                            const today = new Date();
                            let diff = null;
                            let isOverdue = false;
                            if (task.expected_closure) {
                              const due = new Date(task.expected_closure);
                              const msPerDay = 24 * 60 * 60 * 1000;
                              diff = Math.ceil((due - new Date(today.getFullYear(), today.getMonth(), today.getDate())) / msPerDay);
                              if (diff < 0) { isOverdue = true; }
                            } else {
                              diff = (index % 7) + 3; // deterministic dummy between 3-9 days
                            }
                            const formatDays = (n) => {
                              if (n === 0) return 'Today';
                              const absn = Math.abs(n);
                              return `${absn} ${absn === 1 ? 'Day' : 'Days'}`;
                            };

                            return (
                              <div className="flex items-center gap-2 text-sm text-gray-600 mt-2">
                                <FiClock className="text-xs text-gray-500" />
                                <span>{diff !== null ? (isOverdue ? `Overdue ${formatDays(diff)}` : formatDays(diff)) : '—'}</span>
                              </div>
                            );
                          })()}

                          {/* reviewer & assignee shown in detail modal / popovers; removed from card surface for visual clarity */}

                          {/* Assigned/By removed from card surface — shown via employee icon modal */}

                          {/* Bottom action icons: eye (view), edit, delete */}
                          <div className="card-footer">
                            <div className="flex items-center gap-4">
                              <button
                                onClick={(e) => { e.stopPropagation(); handleTaskClick(task); }}
                                className="flex items-center gap-2 text-sm text-gray-600 hover:text-gray-800"
                                title="View details"
                              >
                                <FiEye className="text-lg" />
                              </button>

                              <button
                                onClick={(e) => { e.stopPropagation(); loadAttachments(task.task_id); setAttachmentsTarget(task); }}
                                className="flex items-center gap-2 text-sm text-gray-600 hover:text-gray-800"
                                aria-label="attachments"
                              >
                                <FiPaperclip className="text-lg" />
                              </button>
                            </div>

                            <div className="flex items-center gap-4">
                              <div
                                className="relative"
                                onMouseEnter={(e) => {
                                  const r = e.currentTarget.getBoundingClientRect();
                                  setHoverUserTaskId(task.task_id);
                                  setHoverPos({ top: r.top, left: r.left, right: r.right, bottom: r.bottom, width: r.width, height: r.height });
                                }}
                                onMouseLeave={() => { setHoverUserTaskId(null); setHoverPos(null); }}
                              >
                                <button
                                  onClick={(e) => { e.stopPropagation(); setAssigneeTarget(task); }}
                                  className="flex items-center gap-2 text-sm text-gray-600 hover:text-gray-800"
                                  title="People"
                                  aria-haspopup="true"
                                  aria-expanded={hoverUserTaskId === task.task_id}
                                >
                                  <FiUser className="text-lg" />
                                </button>

                                {hoverUserTaskId === task.task_id && hoverPos && createPortal(
                                  (() => {
                                    const assignedEmp = employees.find((e) => String(e.id) === String(task.assigned_to));
                                    const assignedBy = employees.find((e) => String(e.id) === String(task.assigned_by));
                                    const popWidth = 300;
                                    const spaceRight = window.innerWidth - hoverPos.right;
                                    const left = spaceRight > popWidth + 16 ? (hoverPos.right + 8) : Math.max(8, hoverPos.left - popWidth - 8);
                                    const top = Math.min(window.innerHeight - 120 - 16, Math.max(8, hoverPos.bottom + 8));

                                    return (
                                      <div style={{ position: 'fixed', top: `${top}px`, left: `${left}px`, width: `${popWidth}px`, zIndex: 9999 }}>
                                        <div className="p-3 bg-white rounded shadow-lg text-sm">
                  <div className="flex items-start gap-3 mb-3">
                    <img src={getEmployeeImage(assignedEmp)} alt="Assignee" className="w-12 h-12 rounded-full object-cover" />
                                            <div className="flex-1">
                                              <div className="text-xs text-gray-500">Assigned to</div>
                                              <div className="font-medium text-gray-800">{getEmployeeName(task.assigned_to)}</div>
                                              {assignedEmp && assignedEmp.email ? (
                                                <a href={`mailto:${assignedEmp.email}`} className="text-xs text-blue-600 underline">{assignedEmp.email}</a>
                                              ) : (
                                                <div className="text-xs text-gray-400">ID: {task.assigned_to}</div>
                                              )}
                                            </div>
                                          </div>

                                          <div className="flex items-start gap-3">
                                            <img src={getEmployeeImage(assignedBy) || managerAvatar} alt="Reviewer" className="w-12 h-12 rounded-full object-cover" />
                                            <div className="flex-1">
                                              <div className="text-xs text-gray-500">Reviewer</div>
                                              <div className="font-medium text-gray-800">{getEmployeeName(task.assigned_by)}</div>
                                              {assignedBy && assignedBy.email ? (
                                                <a href={`mailto:${assignedBy.email}`} className="text-xs text-blue-600 underline">{assignedBy.email}</a>
                                              ) : (
                                                <div className="text-xs text-gray-400">ID: {task.assigned_by}</div>
                                              )}
                                            </div>
                                          </div>
                                        </div>
                                      </div>
                                    );
                                  })(), document.body
                                )}
                              </div>

                              <button
                                onClick={(e) => { e.stopPropagation(); setSelectedTask(task); setTaskTitle(task.title); setTaskDescription(task.description || ''); setTaskPriority(task.priority || ''); setTaskRemarks(task.remarks || ''); setIsEditMode(true); loadAttachments(task.task_id); }}
                                className="flex items-center gap-2 text-sm text-gray-600 hover:text-gray-800"
                                title="Edit task"
                              >
                                <FiEdit3 className="text-lg" />
                              </button>

                              <button
                                onClick={(e) => { e.stopPropagation(); setDeleteTarget(task); setShowDeleteConfirm(true); }}
                                className="flex items-center gap-2 text-sm text-red-600 hover:text-red-800"
                                title="Delete task"
                              >
                                <FiTrash2 className="text-lg" />
                              </button>
                            </div>
                          </div>
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

  </DragDropContext>
  </div>

      {/* Create Task Form Modal (DashboardManager style) */}
      {showForm && (
        <div className="fixed inset-0 bg-gray-500 bg-opacity-50 flex justify-center items-center z-50">
          <div className="bg-white p-6 rounded-lg shadow-lg w-1/3 animate-scale-up">
            <h2 className="text-2xl font-semibold mb-4">Create Task</h2>

            <form onSubmit={handleCreate} className="space-y-4">
              <div>
                <label className="block text-sm font-medium">Title</label>
                <input
                  ref={titleInputRef}
                  placeholder="Title"
                  className="mt-2 w-full p-2 border rounded"
                  value={form.title}
                  onChange={(e) => setForm({ ...form, title: e.target.value })}
                />
              </div>

              <div>
                <label className="block text-sm font-medium">Description</label>
                <textarea
                  rows={3}
                  className="mt-2 w-full p-2 border rounded"
                  value={form.description}
                  onChange={(e) => setForm({ ...form, description: e.target.value })}
                />
              </div>

              <div>
                <label className="block text-sm font-medium">Assign To</label>
                <select
                  className="mt-2 w-full p-2 border rounded"
                  value={form.assigned_to}
                  onChange={(e) => setForm({ ...form, assigned_to: e.target.value })}
                >
                  <option value="">Assign To</option>
                  {employees.map((e) => (
                    <option key={e.id} value={e.id}>
                      {e.name}
                    </option>
                  ))}
                </select>
              </div>

              <div>
                <label className="block text-sm font-medium">Priority</label>
                <select
                  className="mt-2 w-full p-2 border rounded"
                  value={form.priority}
                  onChange={(e) => setForm({ ...form, priority: e.target.value })}
                >
                  <option value="Low">Low</option>
                  <option value="Medium">Medium</option>
                  <option value="High">High</option>
                  <option value="Critical">Critical</option>
                </select>
              </div>

              <div>
                <label className="block text-sm font-medium">Reviewer</label>
                <select
                  className="mt-2 w-full p-2 border rounded"
                  value={form.reviewer}
                  onChange={(e) => setForm({ ...form, reviewer: e.target.value })}
                >
                  <option value="">Select reviewer</option>
                  {employees.map((emp) => (
                    <option key={emp.id} value={emp.id}>{emp.name}</option>
                  ))}
                </select>
              </div>

              <div>
                <label className="block text-sm font-medium">Expected Closure</label>
                <input
                  type="date"
                  className="mt-2 w-full p-2 border rounded"
                  value={form.expected_closure}
                  onChange={(e) => setForm({ ...form, expected_closure: e.target.value })}
                />
              </div>

              <div className="flex justify-between">
                <button
                  type="button"
                  onClick={() => setShowForm(false)} // Close form
                  className="bg-gray-300 text-white py-2 px-4 rounded-md"
                >
                  Cancel
                </button>
                <button
                  type="submit"
                  className="bg-blue-500 text-white py-2 px-4 rounded-md"
                >
                  Create Task
                </button>
              </div>
            </form>
          </div>
        </div>
      )}

      {/* My Tasks modal */}
      {showMyTasks && (
        <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50 p-4">
          <div className="bg-white rounded-lg shadow-xl w-full max-w-2xl overflow-auto">
            <div className="flex items-center justify-between p-4 border-b">
              <h3 className="text-lg font-semibold">My Tasks</h3>
              <button onClick={() => setShowMyTasks(false)} className="text-gray-500 hover:bg-gray-100 p-2 rounded">Close</button>
            </div>

            <div className="p-4 space-y-3">
              {myTasks.length === 0 && <div className="text-sm text-gray-500">No tasks assigned to you.</div>}
              {myTasks.map((t) => (
                <div key={t.task_id} className={`p-3 rounded-lg border ${priorityColors[t.priority] || 'border-gray-200'} flex justify-between items-start bg-white`}>
                  <div>
                    <div className="flex items-center gap-3">
                      <div className="font-medium text-gray-800">{t.title}</div>
                      <div className="text-xs px-2 py-1 rounded text-white" style={{ backgroundColor: statusColors[t.status] }}>{t.status}</div>
                    </div>
                    <div className="text-sm text-gray-600 mt-1">{t.description || 'No description'}</div>
                    <div className="text-xs text-gray-500 mt-2">Assigned by: {getEmployeeName(t.assigned_by)}</div>
                  </div>

                  <div className="text-right">
                    <div className="text-sm text-gray-600">Priority: <strong>{t.priority}</strong></div>
                    <div className="text-sm text-gray-600 mt-2">{t.expected_closure ? new Date(t.expected_closure).toLocaleDateString() : 'No due date'}</div>
                    <div className="flex gap-2 mt-3">
                      <button onClick={() => { setShowMyTasks(false); handleTaskClick(t); }} className="px-3 py-1 bg-indigo-600 text-white rounded">Open</button>
                    </div>
                  </div>
                </div>
              ))}
            </div>
          </div>
        </div>
      )}

      {/* Assigned-by-me side panel (smaller, scrollable) */}
      {showAssignedTasks && (
        <div className="fixed inset-0 bg-black bg-opacity-40 flex items-center justify-center z-50 p-4">
          <div className="w-full max-w-3xl max-h-[80vh] bg-white rounded-lg shadow-xl overflow-auto">
            <div className="flex items-center justify-between p-4 border-b sticky top-0 bg-white z-10">
              <h3 className="text-lg font-semibold">Assigned Tasks</h3>
              <button onClick={() => setShowAssignedTasks(false)} className="text-gray-500 hover:bg-gray-100 p-2 rounded">Close</button>
            </div>

            <div className="p-4 grid grid-cols-1 gap-3">
              {assignedTasks.length === 0 && <div className="text-sm text-gray-500">You haven't assigned any tasks yet.</div>}
              {assignedTasks.map((t, i) => {
                const assignee = employees.find((e) => String(e.id) === String(t.assigned_to));
                // compute due label
                const today = new Date();
                let dueLabel = 'No due date';
                if (t.expected_closure) {
                  const due = new Date(t.expected_closure);
                  const msPerDay = 24 * 60 * 60 * 1000;
                  const diff = Math.ceil((due - new Date(today.getFullYear(), today.getMonth(), today.getDate())) / msPerDay);
                  if (diff === 0) dueLabel = 'Due Today';
                  else if (diff < 0) dueLabel = `Overdue ${Math.abs(diff)} ${Math.abs(diff) === 1 ? 'Day' : 'Days'}`;
                  else dueLabel = `${diff} ${diff === 1 ? 'Day' : 'Days'}`;
                }

                return (
                  <div key={t.task_id} className={`p-3 rounded-lg border ${priorityColors[t.priority] || 'border-gray-200'} flex justify-between items-start bg-white`}>
                    <div className="flex items-start gap-3">
                      <img src={getEmployeeImage(assignee)} alt="Assignee avatar" className="w-12 h-12 rounded-full object-cover" />
                      <div>
                        <div className="text-sm font-medium text-gray-800">{t.title}</div>
                        <div className="text-xs text-gray-500">To: <strong className="text-gray-800">{assignee ? assignee.name : getEmployeeName(t.assigned_to)}</strong></div>
                        <div className="text-xs text-gray-500 mt-1">{t.description ? t.description : 'No description'}</div>
                      </div>
                    </div>

                    <div className="text-right flex flex-col items-end gap-2">
                      <div className="text-xs px-2 py-1 rounded text-white" style={{ backgroundColor: statusColors[t.status] }}>{t.status}</div>
                      <div className="text-sm text-gray-600">Priority: <strong>{t.priority}</strong></div>
                      <div className="text-sm text-gray-600">{dueLabel}</div>
                      <div className="flex gap-2 mt-3">
                        <button onClick={() => { setShowAssignedTasks(false); handleTaskClick(t); }} className="px-3 py-1 bg-indigo-600 text-white rounded">Open</button>
                      </div>
                    </div>
                  </div>
                );
              })}
            </div>
          </div>
        </div>
      )}

      {/* Employees modal (centered, same style as Assigned) */}
      {showEmployeesModal && (
        <div className="fixed inset-0 bg-black bg-opacity-40 flex items-center justify-center z-50 p-4">
          <div className="w-full max-w-3xl max-h-[80vh] bg-white rounded-lg shadow-xl overflow-auto">
            <div className="flex items-center justify-between p-4 border-b sticky top-0 bg-white z-10">
              <h3 className="text-lg font-semibold">Employees</h3>
              <button onClick={() => setShowEmployeesModal(false)} className="text-gray-500 hover:bg-gray-100 p-2 rounded">Close</button>
            </div>

            <div className="p-4 grid grid-cols-1 gap-3">
              {employeesSummary.length === 0 && <div className="text-sm text-gray-500">No employees available.</div>}
              {employeesSummary.map((emp) => (
                <div key={emp.id} className={`p-3 rounded-lg border ${emp.assignedTasks && emp.assignedTasks.length ? 'border-gray-200' : 'border-dashed border-gray-300'} flex justify-between items-start bg-white`}>
                  <div className="flex items-start gap-3">
                    <img src={getEmployeeImage(emp)} alt="Employee avatar" className="w-12 h-12 rounded-full object-cover" />
                    <div>
                      <div className="text-sm font-medium text-gray-800">{emp.name} <span className="text-xs text-gray-500">(ID: {emp.id})</span></div>
                      <div className="text-xs text-gray-500 mt-1">Tasks assigned: {emp.assignedTasks.length}</div>
                      <div className="text-xs text-gray-500 mt-1">Completed: {emp.completedCount}</div>
                      {emp.assignedTasks.length > 0 && (
                        <div className="text-xs text-gray-600 mt-2 space-y-1 max-w-xl">
                          {emp.assignedTasks.slice(0,3).map((t) => (
                            <div key={t.task_id} className="flex items-center justify-between gap-2">
                              <div className="truncate">• {t.title}</div>
                              <div className="text-xs text-gray-400">{t.status}</div>
                            </div>
                          ))}
                          {emp.assignedTasks.length > 3 && <div className="text-xs text-gray-400">and {emp.assignedTasks.length - 3} more...</div>}
                        </div>
                      )}
                    </div>
                  </div>

                  <div className="text-right flex flex-col items-end gap-2">
                    <div className="text-sm text-gray-600">Total: <strong>{emp.assignedTasks.length}</strong></div>
                    <div className="text-sm text-gray-600">Completed: <strong>{emp.completedCount}</strong></div>
                    <div className="flex gap-2 mt-3">
                      <button onClick={() => { setShowEmployeesModal(false); setMyTasks(emp.assignedTasks); setShowMyTasks(true); }} className="px-3 py-1 bg-indigo-600 text-white rounded">View tasks</button>
                    </div>
                  </div>
                </div>
              ))}
            </div>
          </div>
        </div>
      )}

      {/* Task Details modal (for employees to view remarks, attachments, and reply) */}
      {selectedTask && (
        <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50 p-4">
          <div className="bg-white rounded-lg shadow-xl w-full max-w-4xl overflow-hidden">
            <div className="flex items-center justify-between p-4 border-b">
              <div className="flex items-center gap-4">
                <div className="w-12 h-12 rounded-full bg-indigo-100 flex items-center justify-center text-indigo-700 font-bold">{(selectedTask.title || 'T').charAt(0)}</div>
                <div className="flex-1">
                  {isEditMode ? (
                    <input className="w-full text-lg font-semibold border-b pb-1" value={taskTitle} onChange={(e) => setTaskTitle(e.target.value)} />
                  ) : (
                    <h3 className="text-lg font-semibold">{selectedTask.title}</h3>
                  )}

                  <div className="flex gap-2 items-center text-sm text-gray-600 mt-1">
                    <span className="px-2 py-1 rounded-full text-xs font-medium" style={{ backgroundColor: statusColors[selectedTask.status], color: '#fff' }}>{selectedTask.status}</span>
                    {isEditMode ? (
                      <select value={taskPriority} onChange={(e) => setTaskPriority(e.target.value)} className="text-sm p-1 border rounded">
                        <option value="Low">Low</option>
                        <option value="Medium">Medium</option>
                        <option value="High">High</option>
                        <option value="Critical">Critical</option>
                      </select>
                    ) : (
                      <span className="text-xs">Priority: <strong className="ml-1">{selectedTask.priority}</strong></span>
                    )}
                    <span className="text-xs">Assigned to: <strong className="ml-1">{getEmployeeName(selectedTask.assigned_to)}</strong></span>
                    <span className="text-xs">Assigned by: <strong className="ml-1">{getEmployeeName(selectedTask.assigned_by)}</strong></span>
                  </div>
                </div>
              </div>
              <div className="flex items-center gap-3">
                <div className="text-sm text-gray-500">{selectedTask.created_at ? new Date(selectedTask.created_at).toLocaleString() : ''}</div>
                <button onClick={() => setSelectedTask(null)} className="text-gray-500 hover:bg-gray-100 p-2 rounded">
                  <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5" viewBox="0 0 20 20" fill="currentColor"><path fillRule="evenodd" d="M10 9l-3-3a1 1 0 10-1.414 1.414L8.586 10l-3 3A1 1 0 106.586 14L10 11.586 13.414 15A1 1 0 1014.828 13.586L11.414 10l3-3A1 1 0 0013.414 6L10 9z" clipRule="evenodd"/></svg>
                </button>
              </div>
            </div>

            <div className="p-6 grid grid-cols-1 md:grid-cols-3 gap-6">
              <div className="md:col-span-2 space-y-4">
                <div>
                  <h4 className="font-semibold text-sm text-gray-700">Description</h4>
                  {isEditMode ? (
                    <textarea className="text-sm text-gray-800 mt-2 w-full p-2 border rounded" value={taskDescription} onChange={(e) => setTaskDescription(e.target.value)} />
                  ) : (
                    <p className="text-sm text-gray-800 mt-2">{selectedTask.description || 'No description provided.'}</p>
                  )}
                </div>

                <div>
                  <h4 className="font-semibold text-sm text-gray-700">Conversation / Remarks</h4>
                  <div className="mt-3 space-y-2 max-h-64 overflow-auto pr-2">
                    {selectedTask.remarks ? (
                      String(selectedTask.remarks).split('\n').map((line, idx) => (
                        <div key={idx} className={`p-3 rounded-lg ${line.startsWith('Employee(') ? 'bg-blue-50 self-end' : 'bg-gray-100'}`}>
                          <div className="text-sm text-gray-800 whitespace-pre-wrap">{line}</div>
                        </div>
                      ))
                    ) : (
                      <div className="text-sm text-gray-500">No remarks yet.</div>
                    )}
                  </div>
                </div>

                {/* Employee reply area (visible to employees) */}
                {role && role.toLowerCase() === 'employee' && (
                  <div className="mt-4">
                    <h4 className="font-semibold text-sm text-gray-700">Your reply to manager</h4>
                    <textarea value={employeeRemark} onChange={(e) => setEmployeeRemark(e.target.value)} rows={3} className="mt-2 w-full border rounded p-2" placeholder="Write a brief remark to the manager..." />
                    <div className="flex items-center justify-end gap-2 mt-2">
                      <button onClick={() => setEmployeeRemark('')} className="px-3 py-1 bg-gray-100 rounded">Clear</button>
                      <button onClick={sendEmployeeRemark} className="px-3 py-1 bg-blue-600 text-white rounded">Send</button>
                    </div>
                  </div>
                )}
              </div>

              <aside className="md:col-span-1">
                <div className="bg-gray-50 p-4 rounded">
                  <h5 className="font-semibold text-sm text-gray-700">Attachments</h5>
                  <div className="mt-3 space-y-2">
                    {attachments.length === 0 && <div className="text-sm text-gray-500">No attachments</div>}
                    {attachments.map((a) => (
                      <div key={a.id} className="flex items-center justify-between gap-3 bg-white p-2 rounded border">
                        <div className="flex items-center gap-3">
                          <div className="w-8 h-8 bg-gray-100 rounded flex items-center justify-center text-sm">{a.file_name.split('.').pop().toUpperCase()}</div>
                                <div className="text-sm">
                                  <button onClick={(e) => { e.stopPropagation(); downloadAttachment(a.id, a.file_name); }} className="text-blue-600 underline bg-transparent border-0 p-0 m-0 cursor-pointer">{a.file_name}</button>
                                  <div className="text-xs text-gray-500">{(a.file_size/1024).toFixed(1)} KB</div>
                                </div>
                        </div>
                        <div className="flex items-center gap-2">
                          <button className="text-xs text-red-500" onClick={() => removeAttachment(a.id)}>Delete</button>
                        </div>
                      </div>
                    ))}
                  </div>

                  <div className="mt-4">
                    <label className="block text-xs text-gray-600">Add file</label>
                    <input type="file" onChange={handleFilePick} className="mt-2" accept=".pdf,.doc,.docx,.xls,.xlsx,.png,.jpg,.jpeg,.gif,.txt,.csv,.zip" />
                    <div className="flex justify-end mt-2">
                      <button onClick={uploadFile} className="px-3 py-1 bg-green-600 text-white rounded">Upload</button>
                    </div>
                  </div>
                </div>
              </aside>
            </div>

            {/* Edit footer actions when in edit mode */}
            {isEditMode ? (
              <div className="p-4 border-t flex justify-end gap-2">
                <button className="px-3 py-1 rounded border" onClick={() => { setIsEditMode(false); setSelectedTask(null); }}>Cancel</button>
                <button className="px-3 py-1 rounded bg-indigo-600 text-white" onClick={handleSaveTask}>Save</button>
              </div>
            ) : null}
          </div>
        </div>
      )}

      {/* Notifications modal (basic, derived from remarks/metadata) */}
      {notificationsTarget && (
        <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
          <div className="bg-white p-6 rounded-lg shadow-lg w-96">
            <h3 className="text-lg font-semibold mb-2">Notifications for: {notificationsTarget.title}</h3>
            <div className="text-sm text-gray-600 mb-4">Recent activity and remarks</div>
            <div className="max-h-64 overflow-auto space-y-2">
              <div className="p-2 bg-gray-100 rounded">Created: {notificationsTarget.created_at ? new Date(notificationsTarget.created_at).toLocaleString() : '—'}</div>
              <div className="p-2 bg-gray-100 rounded">Updated: {notificationsTarget.updated_at ? new Date(notificationsTarget.updated_at).toLocaleString() : '—'}</div>
              {notificationsTarget.remarks ? String(notificationsTarget.remarks).split('\n').map((r, i) => (
                <div key={i} className="p-2 bg-white border rounded">{r}</div>
              )) : <div className="p-2 text-gray-500">No remarks</div>}
            </div>
            <div className="flex justify-end mt-4">
              <button onClick={() => setNotificationsTarget(null)} className="px-3 py-1 rounded border">Close</button>
            </div>
          </div>
        </div>
      )}

      {/* Delete confirmation modal */}
      {showDeleteConfirm && deleteTarget && (
        <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
          <div className="bg-white p-6 rounded-lg shadow-lg w-96">
            <h3 className="text-lg font-semibold mb-2 text-red-600">Delete task</h3>
            <p className="text-sm text-gray-700 mb-4">Do you want to delete permanently?</p>
            <div className="flex justify-end gap-2">
              <button onClick={() => { setShowDeleteConfirm(false); setDeleteTarget(null); }} className="px-3 py-1 rounded border">Cancel</button>
              <button onClick={async () => {
                try {
                  await deleteTask(deleteTarget.task_id);
                  toast.success('Task deleted permanently');
                  setShowDeleteConfirm(false);
                  setDeleteTarget(null);
                  loadTasks();
                } catch (err) {
                  toast.error('Failed to delete task');
                }
              }} className="px-3 py-1 rounded bg-red-600 text-white">Delete</button>
            </div>
          </div>
        </div>
      )}

      {/* Assignee / Assigner modal (opened by clicking the user icon on a card) */}
      {assigneeTarget && (
        <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
          <div className="bg-white p-6 rounded-lg shadow-lg w-96">
            <h3 className="text-lg font-semibold mb-2">Task assignment</h3>
            <div className="text-sm text-gray-700 mb-4">Task: <strong>{assigneeTarget.title}</strong></div>
            <div className="space-y-3">
              <div className="flex items-center gap-3 p-2 bg-gray-100 rounded">
                <img src={getEmployeeImage({ id: assigneeTarget?.assigned_to })} alt="Assignee avatar" className="w-12 h-12 rounded-full object-cover" />
                <div>
                  <div className="text-xs text-gray-500">Assigned to</div>
                  <div className="font-medium text-gray-800">{getEmployeeName(assigneeTarget.assigned_to)}</div>
                </div>
              </div>

              <div className="flex items-center gap-3 p-2 bg-gray-100 rounded">
                <img src={getEmployeeImage({ id: assigneeTarget?.assigned_by }) || managerAvatar} alt="Reviewer avatar" className="w-12 h-12 rounded-full object-cover" />
                <div>
                  <div className="text-xs text-gray-500">Reviewer</div>
                  <div className="font-medium text-gray-800">{getEmployeeName(assigneeTarget.assigned_by)}</div>
                </div>
              </div>
            </div>
            <div className="flex justify-end mt-4">
              <button onClick={() => setAssigneeTarget(null)} className="px-3 py-1 rounded border">Close</button>
            </div>
          </div>
        </div>
      )}

      {/* Attachments modal (opened by clicking the paperclip on a card) */}
      {attachmentsTarget && (
        <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
          <div className="bg-white p-6 rounded-lg shadow-lg w-96">
            <h3 className="text-lg font-semibold mb-2">Attachments for: {attachmentsTarget.title}</h3>
            <div className="mt-3 space-y-2 max-h-64 overflow-auto">
              {attachments.length === 0 && <div className="text-sm text-gray-500">No attachments</div>}
              {attachments.map((a) => (
                <div key={a.id} className="flex items-center justify-between gap-3 bg-white p-2 rounded border">
                  <div className="flex items-center gap-3">
                    <div className="w-8 h-8 bg-gray-100 rounded flex items-center justify-center text-sm">{a.file_name.split('.').pop().toUpperCase()}</div>
                    <div className="text-sm">
                      <button onClick={(e) => { e.stopPropagation(); downloadAttachment(a.id, a.file_name); }} className="text-blue-600 underline bg-transparent border-0 p-0 m-0 cursor-pointer">{a.file_name}</button>
                      <div className="text-xs text-gray-500">{(a.file_size/1024).toFixed(1)} KB</div>
                    </div>
                  </div>
                  <div className="flex items-center gap-2">
                    <button className="text-xs text-red-500" onClick={() => removeAttachment(a.id)}>Delete</button>
                  </div>
                </div>
              ))}
            </div>
            <div className="flex justify-end mt-4">
              <button onClick={() => setAttachmentsTarget(null)} className="px-3 py-1 rounded border">Close</button>
            </div>
          </div>
        </div>
      )}

      {/* Remark modal shown when manager/admin drags a task */}
      {showRemarkModal && pendingMove && (
        <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
          <div className="bg-white p-6 rounded-lg shadow-lg w-96">
            <h3 className="text-lg font-semibold mb-2">Add remark for move</h3>
            <p className="text-sm opacity-70 mb-3">Task: {pendingMove.movedTask?.title}</p>

            <textarea
              rows={4}
              className="w-full p-2 border rounded mb-4"
              placeholder="Write a remark that will be sent to the assigned employee..."
              value={remarkInput}
              onChange={(e) => setRemarkInput(e.target.value)}
            />

            <div className="flex justify-end gap-2">
              <button
                className="px-3 py-1 rounded bg-gray-200"
                onClick={cancelPendingMove}
              >
                Cancel
              </button>
              <button
                className="px-3 py-1 rounded bg-blue-600 text-white"
                onClick={confirmPendingMove}
              >
                Confirm & Notify
              </button>
            </div>
          </div>
        </div>
      )}

      {/* Toast Container for showing notifications */}
      <ToastContainer position="top-right" autoClose={3000} hideProgressBar newestOnTop closeOnClick rtl={false} pauseOnFocusLoss draggable pauseOnHover />
    </div>
  );
};

export default KanbanBoard;
