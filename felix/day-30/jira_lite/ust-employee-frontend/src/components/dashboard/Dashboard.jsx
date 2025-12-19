import React, { useState, useEffect } from "react";
import {
  Plus,
  Search,
  Filter,
  X,
  Send,
  Download,
  Eye,
  File,
  MessageSquare,
  UserPlus,
  Calendar,
} from "lucide-react";
import { useAuth } from "../../contexts/AuthContext";
import { useNavigate } from "react-router-dom";
import { api } from "../../services/api";
import Header from "../layout/Header";
import TaskBoard from "./TaskBoard";
import CreateTaskModal from "../modals/CreateTaskModal";

const Dashboard = () => {
  const { user, token } = useAuth();
  const navigate = useNavigate();

  const [tasks, setTasks] = useState([]);
  const [loading, setLoading] = useState(true);
  const [showCreateModal, setShowCreateModal] = useState(false);
  const [searchTerm, setSearchTerm] = useState("");
  const [filterPriority, setFilterPriority] = useState("All");
  const [userRoles, setUserRoles] = useState([]);
  const [userName, setUserName] = useState("User");
  const [currentView, setCurrentView] = useState(null);

  const [managerEmployees, setManagerEmployees] = useState([]);
  const [managers, setManagers] = useState([]);

  // Panel state
  const [panel, setPanel] = useState(null);
  const [panelFiles, setPanelFiles] = useState([]);
  const [panelLoading, setPanelLoading] = useState(false);
  const [panelRemark, setPanelRemark] = useState("");
  const [panelAssignTo, setPanelAssignTo] = useState("");
  const [panelStatus, setPanelStatus] = useState("");

  const [panelTitle, setPanelTitle] = useState("");
  const [panelDescription, setPanelDescription] = useState("");
  const [panelPriority, setPanelPriority] = useState("");
  const [panelReviewer, setPanelReviewer] = useState("");
  const [panelExpectedCompletion, setPanelExpectedCompletion] = useState("");


  const handleUserNameFetched = (name) => setUserName(name);

  useEffect(() => {
    const fetchUserRoles = async () => {
      try {
        const userData = await api.getUserById(token, user.emp_id);
        if (userData && Array.isArray(userData.role)) {
          setUserRoles(userData.role);
          setCurrentView(userData.role[0] || "developer");
        } else {
          setUserRoles(["developer"]);
          setCurrentView("developer");
        }
      } catch (err) {
        console.error("Failed to fetch roles:", err);
        setUserRoles(["developer"]);
        setCurrentView("developer");
      }
    };
    fetchUserRoles();
  }, [token, user.emp_id]);

  useEffect(() => {
    if (currentView) {
      loadTasks();
      loadHelperLists();
    }
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [currentView]);

  const loadTasks = async () => {
    try {
      setLoading(true);
      const data = await api.getTasks(token, currentView, user.emp_id);
      setTasks(Array.isArray(data) ? data : []);
    } catch (err) {
      console.error("Error loading tasks:", err);
      setTasks([]);
    } finally {
      setLoading(false);
    }
  };

  const loadHelperLists = async () => {
    if (currentView === "manager") {
      try {
        const data = await api.getEmployees(token, user.emp_id);
        setManagerEmployees(Array.isArray(data) ? data : []);
      } catch (err) {
        console.error("Error loading employees for manager:", err);
        setManagerEmployees([]);
      }
    } else {
      setManagerEmployees([]);
    }

    if (currentView === "admin") {
      try {
        const mgrs = await api.getManagers(token);
        setManagers(Array.isArray(mgrs) ? mgrs : []);
      } catch (err) {
        console.error("Error loading managers for admin:", err);
        setManagers([]);
      }
    } else {
      setManagers([]);
    }
  };

  const handleStatusChange = async (task, newStatus) => {
    try {
      if (
        currentView === "manager" &&
        task.status === "To Do" &&
        newStatus === "In Progress" &&
        !task.assigned_to
      ) {
        alert(
          "Please assign this task to a developer before moving it to In Progress."
        );
        return;
      }
      await api.updateTaskStatus(token, task._id, newStatus);
      loadTasks();
    } catch (err) {
      console.error("Error updating task:", err);
      alert("Failed to update task status");
    }
  };

  const handleAddRemark = async (taskId, remark) => {
    try {
      await api.addRemark(token, user.emp_id, taskId, remark);
      try {
        const updatedTask = await api.getTaskById(token, taskId);
        const recipientId =
          currentView === "manager"
            ? updatedTask.assigned_to
            : updatedTask.assigned_by;
        setTasks((prev) =>
          prev.map((t) => {
            if (t._id !== taskId) return t;
            const prevNotifications = t.notifications || {};
            const nextNotifications = { ...prevNotifications };
            if (recipientId) {
              const prevCount =
                parseInt(nextNotifications[recipientId] || 0, 10) || 0;
              nextNotifications[recipientId] = prevCount + 1;
            }
            const nextRemarks = Array.isArray(t.remarks)
              ? [...t.remarks, { [user.emp_id]: remark }]
              : [{ [user.emp_id]: remark }];
            return {
              ...t,
              notifications: nextNotifications,
              remarks: nextRemarks,
            };
          })
        );
      } catch (e) {
        console.warn(
          "Optimistic notification update failed, reloading tasks",
          e
        );
        loadTasks();
      }
    } catch (err) {
      console.error("Error adding remark:", err);
    }
  };

  const handleAssign = async (taskId, empId) => {
    try {
      await api.updateTask(token, taskId, {
        assigned_to: empId,
        assigned_by: user.emp_id,
        assigned_at: new Date().toISOString(),
        updated_by: user.emp_id,
      });
      loadTasks();
    } catch (err) {
      console.error("Error assigning task:", err);
      alert("Failed to assign task");
    }
  };

  const handlePanelEditTask = async () => {
  if (!panel || !panel.task) return;
  
  if (!panelTitle.trim()) {
    alert("Title is required");
    return;
  }
  
  if (!panelDescription.trim()) {
    alert("Description is required");
    return;
  }
  
  try {
    const updateData = {
      title: panelTitle,
      description: panelDescription,
      priority: panelPriority,
      reviewer: parseInt(panelReviewer, 10),
      expected_completion_date: panelExpectedCompletion,
      updated_by: user.emp_id,
      assigned_to:parseInt(panelAssignTo,10),
    };
    
    await api.updateTask(token, panel.task._id, updateData);
    await loadTasks();
    closePanel();
    alert("✅ Task updated successfully!");
  } catch (err) {
    console.error("Failed to update task", err);
    alert("❌ Failed to update task: " + (err.message || err));
  }
};

  // Panel helpers
  const openPanel = async (action, task) => {
    setPanel({ action, task });
    setPanelRemark("");
    setPanelAssignTo(task.assigned_to || "");
    setPanelStatus(task.status || "");

    if (action === "edit") {
    setPanelTitle(task.title || "");
    setPanelDescription(task.description || "");
    setPanelPriority(task.priority || "Low");
    setPanelReviewer(task.reviewer || "");
    const dueDate = task.expected_completion_date 
      ? new Date(task.expected_completion_date).toISOString().slice(0, 10)
      : "";
    setPanelExpectedCompletion(dueDate);
  }

    if (action === "remarks") {
      try {
        await api.clearTaskNotifications(token, task._id);
        setTasks((prev) =>
          prev.map((t) => {
            if (t._id !== task._id) return t;
            const nextNotifications = { ...(t.notifications || {}) };
            nextNotifications[user.emp_id] = 0;
            return { ...t, notifications: nextNotifications };
          })
        );
      } catch (err) {
        console.warn("Failed to clear notifications when opening remarks", err);
      }
    }

    if (action === "files") {
      setPanelLoading(true);
      try {
        const res = await api.getTaskFiles(token, task._id);
        setPanelFiles(res.files || []);
      } catch (err) {
        console.error("Failed to load files for panel", err);
        setPanelFiles([]);
      } finally {
        setPanelLoading(false);
      }
    }
  };

  const closePanel = () => {
    setPanel(null);
    setPanelFiles([]);
  };

  const handlePanelAssign = async () => {
    if (!panel || !panel.task) return;
    try {
      const employeeId = parseInt(panelAssignTo, 10);
      await api.updateTask(token, panel.task._id, {
        assigned_to: employeeId,
        assigned_by: user.emp_id,
        assigned_at: new Date().toISOString(),
        updated_by: user.emp_id,
      });
      if (panel.task.status === "To Do") {
      try {
        await api.updateTaskStatus(token, panel.task._id, "In Progress");
        alert(`✅ Task assigned to employee ID ${employeeId} and moved to In Progress!`);
      } catch (statusError) {
        console.warn("Auto status update failed:", statusError);
        alert(`✅ Task assigned to employee ID ${employeeId}!`);
      }
    } else {
      alert(`✅ Task assigned to employee ID ${employeeId}!`);
    }
      await loadTasks();
      closePanel();
    } catch (err) {
      console.error("Assign from panel failed", err);
      alert("Failed to assign task");
    }
  };

  const handlePanelStatusChange = async () => {
    if (!panel || !panel.task) return;
    try {
      await api.updateTaskStatus(token, panel.task._id, panelStatus);
      await loadTasks();
      closePanel();
    } catch (err) {
      console.error("Panel status change failed", err);
      alert("Failed to change status");
    }
  };

  const handlePanelAddRemark = async () => {
    if (!panel || !panel.task || !panelRemark.trim()) return;
    try {
      await api.addRemark(token, user.emp_id, panel.task._id, panelRemark);
      setTasks((prev) =>
        prev.map((t) => {
          if (t._id !== panel.task._id) return t;
          const nextRemarks = Array.isArray(t.remarks)
            ? [...t.remarks, { [user.emp_id]: panelRemark }]
            : [{ [user.emp_id]: panelRemark }];
          return { ...t, remarks: nextRemarks };
        })
      );
      setPanelRemark("");
    } catch (err) {
      console.error("Failed to add remark from panel", err);
      alert("Failed to add remark");
    }
  };

  const handlePanelUpload = async (e) => {
    if (!panel || !panel.task) return;
    const file = e.target.files[0];
    if (!file) return;
    setPanelLoading(true);
    try {
      await api.uploadFileToTask(token, panel.task._id, file);
      const res = await api.getTaskFiles(token, panel.task._id);
      setPanelFiles(res.files || []);
      alert(`Uploaded ${file.name}`);
    } catch (err) {
      console.error("Upload failed", err);
      alert("Upload failed");
    } finally {
      setPanelLoading(false);
    }
  };

  const filteredTasks = tasks.filter((task) => {
    const matchesSearch =
      task.title.toLowerCase().includes(searchTerm.toLowerCase()) ||
      task.description.toLowerCase().includes(searchTerm.toLowerCase());
    const matchesPriority =
      filterPriority === "All" || task.priority === filterPriority;
    return matchesSearch && matchesPriority;
  });

  if (loading || !currentView) {
    return (
      <div className="min-h-screen bg-gradient-to-br from-blue-50 via-purple-50 to-pink-50 flex items-center justify-center">
        <div className="text-center">
          <div className="relative">
            <div className="animate-spin rounded-full h-16 w-16 border-4 border-gray-200 mx-auto mb-4"></div>
            <div className="animate-spin rounded-full h-16 w-16 border-4 border-blue-600 border-t-transparent absolute top-0 left-1/2 transform -translate-x-1/2"></div>
          </div>
          <p className="text-gray-700 font-semibold text-lg">
            Loading your workspace...
          </p>
          <p className="text-gray-500 text-sm mt-2">Just a moment</p>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 via-purple-50 to-pink-50">
      <Header
        currentView={currentView}
        userRoles={userRoles}
        onChangeView={setCurrentView}
        onNavigate={navigate}
        onUserNameFetched={handleUserNameFetched}
      />

      <main className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        <div className="mb-8">
          <h2 className="text-3xl font-bold bg-gradient-to-r from-blue-600 via-purple-600 to-pink-600 bg-clip-text text-transparent mb-2">
            Welcome back, {userName}!
          </h2>
          <p className="text-gray-600">
            You have{" "}
            <span className="font-semibold text-purple-600">
              {filteredTasks.length}
            </span>{" "}
            tasks to manage
          </p>
        </div>

        <div className="mb-8 bg-gradient-to-br from-white via-blue-50/30 to-purple-50/30 rounded-3xl shadow-2xl p-8 border-2 border-white backdrop-blur-sm relative overflow-hidden">
          <div className="absolute top-0 right-0 w-64 h-64 bg-gradient-to-br from-blue-400/10 to-purple-400/10 rounded-full blur-3xl"></div>
          <div className="absolute bottom-0 left-0 w-64 h-64 bg-gradient-to-tr from-pink-400/10 to-blue-400/10 rounded-full blur-3xl"></div>

          <div className="relative z-10 flex flex-col sm:flex-row gap-4 items-start sm:items-center justify-between">
            <div className="flex flex-col sm:flex-row gap-4 flex-1 w-full sm:w-auto">
              <div className="relative flex-1 max-w-md group">
                <div className="absolute inset-0 bg-gradient-to-r from-blue-500 to-purple-500 rounded-2xl opacity-0 group-focus-within:opacity-100 blur transition-opacity duration-300"></div>
                <div className="relative">
                  <Search
                    className="absolute left-4 top-1/2 transform -translate-y-1/2 text-gray-400 group-focus-within:text-blue-600 transition-all duration-300 group-focus-within:scale-110"
                    size={20}
                  />
                  <input
                    type="text"
                    placeholder="Search tasks..."
                    value={searchTerm}
                    onChange={(e) => setSearchTerm(e.target.value)}
                    className="w-full pl-12 pr-4 py-4 border-2 border-gray-200 rounded-2xl focus:ring-4 focus:ring-blue-500/20 focus:border-blue-500 transition-all outline-none bg-white shadow-lg hover:shadow-xl font-medium text-gray-700 placeholder:text-gray-400"
                  />
                </div>
              </div>

              <div className="relative group min-w-[200px]">
                <div className="absolute inset-0 bg-gradient-to-r from-purple-500 to-pink-500 rounded-2xl opacity-0 group-focus-within:opacity-100 blur transition-opacity duration-300"></div>
                <div className="relative">
                  <Filter
                    className="absolute left-4 top-1/2 transform -translate-y-1/2 text-gray-400 group-focus-within:text-purple-600 transition-all duration-300 pointer-events-none group-focus-within:scale-110"
                    size={20}
                  />
                  <select
                    value={filterPriority}
                    onChange={(e) => setFilterPriority(e.target.value)}
                    className="w-full pl-12 pr-12 py-4 border-2 border-gray-200 rounded-2xl focus:ring-4 focus:ring-purple-500/20 focus:border-purple-500 bg-white transition-all outline-none appearance-none cursor-pointer font-semibold text-gray-700 shadow-lg hover:shadow-xl"
                  >
                    <option value="All">All Priorities</option>
                    <option value="Low"> Low Priority</option>
                    <option value="Medium"> Medium Priority</option>
                    <option value="High"> High Priority</option>
                  </select>
                  <div className="absolute right-4 top-1/2 transform -translate-y-1/2 pointer-events-none">
                    <svg
                      className="w-5 h-5 text-gray-400 group-focus-within:text-purple-600 transition-colors"
                      fill="none"
                      stroke="currentColor"
                      viewBox="0 0 24 24"
                    >
                      <path
                        strokeLinecap="round"
                        strokeLinejoin="round"
                        strokeWidth={2.5}
                        d="M19 9l-7 7-7-7"
                      />
                    </svg>
                  </div>
                </div>
              </div>
            </div>

            {currentView !== "developer" && (
              <button
                onClick={() => setShowCreateModal(true)}
                className="flex items-center gap-2 px-8 py-4 bg-blue-600 text-white rounded-2xl hover:bg-blue-700 hover:shadow-lg transition-all font-bold shadow-md"
              >
                <Plus size={22} />
                <span>Create Task</span>
              </button>
            )}
          </div>
        </div>

        <TaskBoard
          tasks={filteredTasks}
          onStatusChange={handleStatusChange}
          onAddRemark={handleAddRemark}
          onAssign={handleAssign}
          onOpenPanel={openPanel}
          userRole={currentView}
          employees={managerEmployees}
          token={token}
          currentUserId={user.emp_id}
        />

        {panel && (
          <aside className="fixed right-6 top-24 w-96 max-h-[70vh] overflow-y-auto bg-white rounded-3xl shadow-2xl border-2 border-gray-100 z-50">
            <div className="p-4 flex items-start justify-between border-b border-gray-200">
              <div>
                <h3 className="font-bold text-lg">{panel.task.title}</h3>
                <p className="text-xs text-gray-500">{panel.action}</p>
              </div>
              <button
                onClick={closePanel}
                className="p-2 hover:bg-gray-100 rounded-lg"
              >
                <X size={18} />
              </button>
            </div>
            <div className="p-4 space-y-4">
              {panel.action === "assign" && (
  <div className="space-y-3">
    <label className="text-sm font-semibold block">Assign To</label>
    
    {/* ✅ Debug info - remove after fixing */}
    {managerEmployees.length === 0 && (
      <p className="text-xs text-amber-600 bg-amber-50 p-2 rounded">
        ⚠️ No employees found. Make sure employees are added under this manager.
      </p>
    )}
    
    <select
      value={panelAssignTo}
      onChange={(e) => {
        console.log("Selected employee ID:", e.target.value); // ✅ Debug
        setPanelAssignTo(e.target.value);
      }}
      className="w-full px-3 py-2 border rounded-md"
    >
      <option value="">Select developer...</option>
      {managerEmployees.map((emp) => {
        // ✅ Handle both emp_id and id fields
        const empId = emp.emp_id || emp.id;
        const empName = emp.name || `Employee ${empId}`;
        
        console.log("Rendering employee:", empId, empName); // ✅ Debug
        
        return (
          <option key={empId} value={empId}>
            {empName} (ID: {empId})
          </option>
        );
      })}
    </select>
    
    {/* ✅ Show current selection */}
    {panelAssignTo && (
      <p className="text-xs text-green-600 bg-green-50 p-2 rounded">
        Selected: Employee ID {panelAssignTo}
      </p>
    )}
    
    <div className="flex justify-end gap-2">
      <button
        onClick={closePanel}
        className="px-3 py-1.5 bg-gray-100 text-gray-700 rounded-md text-sm hover:bg-gray-200"
      >
        Cancel
      </button>
      <button
        onClick={handlePanelAssign}
        disabled={!panelAssignTo}
        className={`px-3 py-1.5 rounded-md text-sm font-semibold ${
          panelAssignTo 
            ? 'bg-blue-600 text-white hover:bg-blue-700' 
            : 'bg-gray-300 text-gray-500 cursor-not-allowed'
        }`}
      >
        Assign Task
      </button>
    </div>
  </div>
)}

              {panel.action === "status" && (
                <div className="space-y-3">
                  <label className="text-sm font-semibold">Change Status</label>
                  <select
                    value={panelStatus}
                    onChange={(e) => setPanelStatus(e.target.value)}
                    className="w-full px-3 py-2 border rounded-md"
                  >
                    <option value="To Do">To Do</option>
                    <option value="In Progress">In Progress</option>
                    <option value="Review">Review</option>
                    <option value="Done">Done</option>
                  </select>
                  <div className="flex justify-end">
                    <button
                      onClick={handlePanelStatusChange}
                      className="px-3 py-1.5 bg-blue-600 text-white rounded-md text-sm"
                    >
                      Update
                    </button>
                  </div>
                </div>
              )}

              {(panel.action === "remarks" || panel.action === "addRemark") && (
                <div className="space-y-3">
                  <div className="space-y-2">
                    {(panel.task.remarks || []).length === 0 ? (
                      <p className="text-sm text-gray-500">No remarks yet</p>
                    ) : (
                      (panel.task.remarks || []).map((r, i) => (
                        <div key={i} className="p-3 bg-gray-50 rounded-md">
                          <p className="text-sm">
                            {typeof r === "object"
                              ? Object.entries(r)
                                  .map(([k, v]) => `${k}: ${v}`)
                                  .join(", ")
                              : r}
                          </p>
                        </div>
                      ))
                    )}
                  </div>
                  <div>
                    <label className="text-sm font-semibold">Add Remark</label>
                    <div className="flex gap-2 mt-2">
                      <input
                        value={panelRemark}
                        onChange={(e) => setPanelRemark(e.target.value)}
                        className="flex-1 px-3 py-2 border rounded-md"
                        placeholder="Write a remark..."
                      />
                      <button
                        onClick={handlePanelAddRemark}
                        className="px-3 py-1.5 bg-emerald-600 text-white rounded-md text-sm"
                      >
                        <Send size={16} />
                      </button>
                    </div>
                  </div>
                </div>
              )}

              {panel.action === "files" && (
                <div className="space-y-3">
                  <div>
                    <label className="text-sm font-semibold">Files</label>
                    <div className="space-y-2 mt-2">
                      {panelLoading ? (
                        <p className="text-sm text-gray-500">Loading...</p>
                      ) : panelFiles.length === 0 ? (
                        <p className="text-sm text-gray-500">
                          No files attached
                        </p>
                      ) : (
                        panelFiles.map((f) => (
                          <div
                            key={f.file_id}
                            className="flex items-center justify-between p-2 bg-gray-50 rounded-md"
                          >
                            <div className="min-w-0">
                              <p className="text-sm font-medium truncate">
                                {f.file_name}
                              </p>
                              <p className="text-xs text-gray-400">
                                {(f.file_size / 1024).toFixed(1)} KB
                              </p>
                            </div>
                            <div className="flex items-center gap-2">
                              <button
                                onClick={async () => {
                                  try {
                                    const fileData = await api.downloadFile(
                                      token,
                                      f.file_id
                                    );
                                    if (
                                      fileData.file_type.startsWith("image/")
                                    ) {
                                      const imgWindow = window.open(
                                        "",
                                        "_blank"
                                      );
                                      imgWindow.document.write(
                                        `<html><body style=\"margin:0;padding:20px;background:#f8fafc;\"><img src=\"data:${fileData.file_type};base64,${fileData.file_data}\" style=\"max-width:90vw;max-height:90vh;border-radius:12px;\"><p style=\"text-align:center;\">${fileData.file_name}</p></body></html>`
                                      );
                                    } else {
                                      await api.downloadFileBlob(
                                        token,
                                        f.file_id,
                                        f.file_name
                                      );
                                    }
                                  } catch (err) {
                                    console.error("Preview failed", err);
                                    alert("Preview failed");
                                  }
                                }}
                                className="p-2 rounded-md hover:bg-gray-100"
                              >
                                <Eye size={16} />
                              </button>
                              <button
                                onClick={async () => {
                                  try {
                                    await api.downloadFileBlob(
                                      token,
                                      f.file_id,
                                      f.file_name
                                    );
                                  } catch (err) {
                                    console.error("Download failed", err);
                                    alert("Download failed");
                                  }
                                }}
                                className="p-2 rounded-md hover:bg-gray-100"
                              >
                                <Download size={16} />
                              </button>
                            </div>
                          </div>
                        ))
                      )}
                    </div>
                  </div>
                  <div>
                    <label className="text-sm font-semibold">Upload File</label>
                    <input
                      type="file"
                      onChange={handlePanelUpload}
                      className="mt-2"
                    />
                  </div>
                </div>
              )}

              {panel.action === "edit" && (
  <div className="space-y-4">
    <div>
      <label className="text-sm font-semibold block mb-2">Title</label>
      <input
        type="text"
        value={panelTitle}
        onChange={(e) => setPanelTitle(e.target.value)}
        className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 outline-none"
        placeholder="Task title..."
      />
    </div>

    <div>
      <label className="text-sm font-semibold block mb-2">Description</label>
      <textarea
        value={panelDescription}
        onChange={(e) => setPanelDescription(e.target.value)}
        className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 outline-none min-h-[100px]"
        placeholder="Task description..."
      />
    </div>

    <div>
      <label className="text-sm font-semibold block mb-2">Priority</label>
      <select
        value={panelPriority}
        onChange={(e) => setPanelPriority(e.target.value)}
        className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 outline-none"
      >
        <option value="Low">Low</option>
        <option value="Medium">Medium</option>
        <option value="High">High</option>
      </select>
    </div>

    <div>
      {currentView === "manager" && 
      (<label className="text-sm font-semibold block mb-2">Developer</label>)
      }
      {currentView === "admin" && 
      (<label className="text-sm font-semibold block mb-2">Reviewer</label>)
      }
      <select
        value={currentView === "manager" ? panelAssignTo : panelReviewer}
        onChange={(e) => 
          currentView === "manager" 
            ? setPanelAssignTo(e.target.value) 
            : currentView === "admin" 
            ? setPanelReviewer(e.target.value)
            : null
        }
        className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 outline-none"
      >
        {currentView === "manager" &&
        (<option value="">Select developer...</option>)
        }
        {currentView === "admin" &&
        (<option value="">Select reviewer...</option>)
        }
        {currentView === "manager" && managerEmployees.map((emp) => {
          const empId = emp.emp_id || emp.id;
        const empName = emp.name || `Employee ${empId}`;
        
        console.log("Rendering employee:", empId, empName); // ✅ Debug
        
        return (
          <option key={empId} value={empId}>
            {empName} (ID: {empId})
          </option>
        );
})}
        {currentView === "admin" && managers.map((mgr) => {
          const empId = mgr.emp_id || mgr.id;
        const empName = mgr.name || `Employee ${empId}`;
        
        console.log("Rendering employee:", empId, empName); // ✅ Debug
        
        return (
          <option key={empId} value={empId}>
            {empName} (ID: {empId})
          </option>
        );
        })}
      </select>
    </div>

    <div>
      <label className="text-sm font-semibold block mb-2">Expected Completion Date</label>
      <input
        type="date"
        value={panelExpectedCompletion}
        onChange={(e) => setPanelExpectedCompletion(e.target.value)}
        className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 outline-none"
      />
    </div>

    <div className="flex justify-end gap-2 pt-2">
      <button
        onClick={closePanel}
        className="px-4 py-2 bg-gray-100 text-gray-700 rounded-lg hover:bg-gray-200 transition-colors"
      >
        Cancel
      </button>
      <button
        onClick={handlePanelEditTask}
        className="px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition-colors font-semibold"
      >
        Update Task
      </button>
    </div>
  </div>
)}
            </div>
          </aside>
        )}

        {showCreateModal && (
          <CreateTaskModal
            token={token}
            empId={user.emp_id}
            currentRole={currentView}
            employees={managerEmployees}
            managers={managers}
            onClose={() => setShowCreateModal(false)}
            onSuccess={() => {
              setShowCreateModal(false);
              loadTasks();
            }}
          />
        )}
      </main>
    </div>
  );
};

export default Dashboard;
