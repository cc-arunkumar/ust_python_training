import React, { useState, useCallback, useRef, useEffect } from 'react';
import { User, Calendar, MessageSquare, ChevronDown, ChevronUp, UserPlus, Send, Upload, Download, File, Loader2, Eye } from 'lucide-react';
import { PRIORITY_COLORS } from '../../utils/constants';
import { api } from '../../services/api';

const TaskCard = ({ task, onStatusChange, onAddRemark, canEdit, onAssign, employees = [], token }) => {
  const [showDetails, setShowDetails] = useState(false);
  const [remark, setRemark] = useState('');
  const [addingRemark, setAddingRemark] = useState(false);
  const [assignee, setAssignee] = useState(task.assigned_to || '');
  
  // 🔴 FILE STATES - FIXED
  const [taskFiles, setTaskFiles] = useState(task.files || []);
  const [uploading, setUploading] = useState(false);
  const [selectedFileName, setSelectedFileName] = useState('');
  const [fileInputKey, setFileInputKey] = useState(0);
  const fileInputRef = useRef(null);

  // 🔴 FILE HANDLERS - FIXED
  const loadTaskFiles = useCallback(async () => {
    if (!token || !task._id) return;
    try {
      const response = await api.getTaskFiles(token, task._id);
      setTaskFiles(response.files || []);
    } catch (error) {
      console.error('Failed to load files:', error);
    }
  }, [token, task._id]);

  const handleFileUpload = useCallback(async (event) => {
    const file = event.target.files[0];
    if (!file || !token) return;

    setUploading(true);
    setSelectedFileName(file.name);
    try {
      await api.uploadFileToTask(token, task._id, file);
      await loadTaskFiles(); // Refresh file list
      
      // 🔴 PROPER RESET - BUTTON BECOMES EMPTY
      setSelectedFileName('');
      setFileInputKey(prev => prev + 1); // Force input re-render
      if (fileInputRef.current) {
        fileInputRef.current.value = ''; // Clear file input
      }
      
      alert(`✅ "${file.name}" uploaded successfully!`);
    } catch (error) {
      alert(`❌ Upload failed: ${error.message}`);
      setSelectedFileName('');
    } finally {
      setUploading(false);
    }
  }, [token, task._id, loadTaskFiles]);

  const handleDownloadFile = useCallback(async (fileId, fileName) => {
    try {
      await api.downloadFileBlob(token, fileId, fileName);
    } catch (error) {
      alert(`❌ Download failed: ${error.message}`);
    }
  }, [token]);

  const handlePreviewFile = useCallback(async (fileId) => {
    try {
      const fileData = await api.downloadFile(token, fileId);
      if (fileData.file_type.startsWith('image/')) {
        const imgWindow = window.open('', '_blank');
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
  }, [token]);

  // Load files when details expand
  useEffect(() => {
    if (showDetails) {
      loadTaskFiles();
    }
  }, [showDetails, loadTaskFiles]);

  const handleAddRemark = async () => {
    if (!remark.trim()) return;
    setAddingRemark(true);
    await onAddRemark(task._id, remark);
    setRemark('');
    setAddingRemark(false);
  };

  const handleAssign = async () => {
    if (!assignee) {
      alert('Please select an employee to assign.');
      return;
    }
    if (!onAssign) return;
    await onAssign(task._id, parseInt(assignee, 10));
  };

  const canAddRemarkNow = task.status === 'In Progress' || task.status === 'Review';
  const canManageFiles = canEdit; // Manager/Developer can upload/download

  const priorityConfig = {
    High: {
      gradient: 'from-red-500 to-pink-500',
      bg: 'bg-red-50',
      border: 'border-red-200',
      text: 'text-red-700'
    },
    Medium: {
      gradient: 'from-yellow-500 to-orange-500',
      bg: 'bg-yellow-50',
      border: 'border-yellow-200',
      text: 'text-yellow-700'
    },
    Low: {
      gradient: 'from-green-500 to-emerald-500',
      bg: 'bg-green-50',
      border: 'border-green-200',
      text: 'text-green-700'
    }
  };

  const config = priorityConfig[task.priority] || priorityConfig.Low;
  const assignedEmployee = employees.find((e) => (e.emp_id ?? e.id) === task.assigned_to);

  return (
    <div className="bg-white rounded-2xl shadow-lg border-2 border-gray-100 hover:shadow-2xl hover:scale-[1.02] transition-all duration-300 overflow-hidden group">
      {/* Priority accent bar */}
      <div className={`h-2 bg-gradient-to-r ${config.gradient}`}></div>
      
      <div className="p-5">
        {/* Summary view */}
        <div onClick={() => setShowDetails(!showDetails)} className="cursor-pointer">
          <div className="flex items-start justify-between mb-4">
            <h3 className="font-bold text-gray-900 text-base flex-1 pr-2 leading-tight group-hover:text-blue-600 transition-colors">
              {task.title}
            </h3>
            <span
              className={`${config.bg} ${config.border} ${config.text} text-xs px-3 py-1.5 rounded-xl font-bold border-2 shadow-sm whitespace-nowrap`}
            >
              {task.priority}
            </span>
          </div>

          <p className="text-sm text-gray-600 mb-4 line-clamp-2 whitespace-pre-wrap leading-relaxed">
            {task.description}
          </p>

          <div className="flex flex-col gap-3 text-xs">
            {/* Assigned to */}
            <div className="flex items-center gap-2 bg-gradient-to-r from-blue-50 to-cyan-50 px-3 py-2 rounded-xl border border-blue-100">
              <div className="w-6 h-6 rounded-lg bg-gradient-to-br from-blue-500 to-cyan-500 flex items-center justify-center text-white shadow-sm">
                <User size={14} />
              </div>
              <div className="flex-1 min-w-0">
                <span className="text-gray-500 font-medium block">Assigned to</span>
                <span className="font-bold text-gray-800 truncate block">
                  {assignedEmployee ? assignedEmployee.name : task.assigned_to || 'Not assigned'}
                </span>
              </div>
            </div>

            {/* Due date */}
            <div className="flex items-center gap-2 bg-gradient-to-r from-purple-50 to-pink-50 px-3 py-2 rounded-xl border border-purple-100">
              <div className="w-6 h-6 rounded-lg bg-gradient-to-br from-purple-500 to-pink-500 flex items-center justify-center text-white shadow-sm">
                <Calendar size={14} />
              </div>
              <div className="flex-1">
                <span className="text-gray-500 font-medium block">Due date</span>
                <span className="font-bold text-gray-800 block">
                  {task.expected_completion_date
                    ? new Date(task.expected_completion_date).toLocaleDateString()
                    : 'Not set'}
                </span>
              </div>
            </div>
          </div>

          {/* Expand/Collapse button */}
          <button className="w-full mt-4 py-2 rounded-xl bg-gray-50 hover:bg-gray-100 text-gray-600 font-semibold text-xs flex items-center justify-center gap-2 transition-all border border-gray-200">
            {showDetails ? (
              <>
                <ChevronUp size={16} />
                Hide Details
              </>
            ) : (
              <>
                <ChevronDown size={16} />
                Show Details
              </>
            )}
          </button>
        </div>

        {/* Expanded details */}
        {showDetails && (
          <div className="mt-5 pt-5 border-t-2 border-gray-100 space-y-5 animate-in fade-in slide-in-from-top-2 duration-300">
            {/* Assign to (only in To Do) */}
            {canEdit && onAssign && task.status === 'To Do' && (
              <div className="bg-gradient-to-br from-indigo-50 to-blue-50 rounded-2xl p-4 border-2 border-indigo-100">
                <label className="text-xs font-bold text-indigo-700 mb-3 flex items-center gap-2">
                  <UserPlus size={16} />
                  Assign Task
                </label>
                <div className="space-y-3">
                  <select
                    value={assignee}
                    onChange={(e) => setAssignee(e.target.value)}
                    className="w-full px-4 py-3 border-2 border-indigo-200 rounded-xl text-sm focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 bg-white font-medium transition-all"
                  >
                    <option value="">Select employee</option>
                    {employees.map((emp) => (
                      <option key={emp.id || emp.emp_id} value={emp.emp_id ?? emp.id}>
                        {emp.name} (ID: {emp.emp_id ?? emp.id})
                      </option>
                    ))}
                  </select>
                  <button
                    type="button"
                    onClick={handleAssign}
                    className="w-full px-5 py-3 bg-gradient-to-r from-indigo-600 to-blue-600 text-white text-sm rounded-xl hover:from-indigo-700 hover:to-blue-700 font-bold shadow-lg hover:shadow-xl transition-all transform hover:scale-105"
                  >
                    Assign
                  </button>
                </div>
              </div>
            )}

            {/* Status change */}
            <div className="bg-gradient-to-br from-purple-50 to-pink-50 rounded-2xl p-4 border-2 border-purple-100">
              <label className="text-xs font-bold text-purple-700 mb-3 block">
                Task Status
              </label>
              {task.status === 'To Do' && !task.assigned_to && (
                <div className="mb-2 text-xs text-orange-600 bg-orange-50 px-3 py-2 rounded-lg border border-orange-200 font-medium">
                  ⚠️ Please assign this task before changing status
                </div>
              )}
              <select
                value={task.status}
                onChange={(e) => onStatusChange(task, e.target.value)}
                disabled={!canEdit || (task.status === 'To Do' && !task.assigned_to)}
                className="w-full px-4 py-3 border-2 border-purple-200 rounded-xl text-sm focus:ring-2 focus:ring-purple-500 focus:border-purple-500 disabled:bg-gray-100 disabled:cursor-not-allowed bg-white font-semibold transition-all"
              >
                <option value="To Do">📋 To Do</option>
                <option value="In Progress">⚡ In Progress</option>
                <option value="Review">👁️ Review</option>
                <option value="Done">✅ Done</option>
              </select>
            </div>

            {/* Remarks list */}
            {task.remarks && task.remarks.length > 0 && (
              <div className="bg-gradient-to-br from-gray-50 to-blue-50 rounded-2xl p-4 border-2 border-gray-200">
                <label className="text-xs font-bold text-gray-700 mb-3 flex items-center gap-2">
                  <MessageSquare size={16} />
                  Remarks ({task.remarks.length})
                </label>
                <div className="space-y-2 max-h-40 overflow-y-auto custom-scrollbar">
                  {task.remarks.map((r, i) => (
                    <div
                      key={i}
                      className="text-sm bg-white p-3 rounded-xl border-2 border-gray-200 shadow-sm hover:shadow-md transition-shadow"
                    >
                      <div className="flex items-start gap-2">
                        <div className="w-6 h-6 rounded-lg bg-gradient-to-br from-gray-400 to-gray-500 flex items-center justify-center text-white text-xs font-bold flex-shrink-0">
                          {i + 1}
                        </div>
                        <p className="text-gray-700 flex-1 leading-relaxed">
                          {typeof r === 'object'
                            ? Object.entries(r)
                                .map(([k, v]) => `${k}: ${v}`)
                                .join(', ')
                            : r}
                        </p>
                      </div>
                    </div>
                  ))}
                </div>
              </div>
            )}

            {/* 🔴 FILE UPLOAD/ DOWNLOAD SECTION - FIXED */}
            {canManageFiles && (
              <div className="bg-gradient-to-br from-emerald-50 to-teal-50 rounded-2xl p-4 border-2 border-emerald-200">
                <label className="text-xs font-bold text-emerald-700 mb-4 flex items-center gap-2">
                  <File size={16} />
                  Files ({taskFiles.length})
                </label>

                {/* File Upload - FIXED */}
                <div className="mb-4 p-4 bg-white rounded-xl border-2 border-dashed border-emerald-300 hover:border-emerald-400 transition-all">
                  <input
                    key={fileInputKey}
                    ref={fileInputRef}
                    type="file"
                    onChange={handleFileUpload}
                    className="hidden"
                    accept=".pdf,.doc,.docx,.jpg,.jpeg,.png,.gif"
                  />
                  <button
                    type="button"
                    onClick={() => fileInputRef.current?.click()}
                    disabled={uploading}
                    className="w-full flex items-center justify-center gap-2 px-4 py-3 text-sm font-bold bg-gradient-to-r from-emerald-500 to-teal-500 text-white rounded-xl hover:from-emerald-600 hover:to-teal-600 disabled:opacity-50 disabled:cursor-not-allowed transition-all shadow-lg hover:shadow-xl transform hover:scale-[1.02]"
                  >
                    {uploading ? (
                      <>
                        <Loader2 className="w-4 h-4 animate-spin" />
                        Uploading...
                      </>
                    ) : (
                      <>
                        <Upload size={16} />
                        {selectedFileName || 'Upload File'}
                      </>
                    )}
                  </button>
                  <p className="text-xs text-emerald-600 mt-2 text-center">
                    Supports PDF, DOC, Images (Max 10MB)
                  </p>
                </div>

                {/* File List */}
                {taskFiles.length > 0 && (
                  <div className="space-y-2 max-h-32 overflow-y-auto custom-scrollbar">
                    {taskFiles.map((file) => (
                      <div key={file.file_id} className="flex items-center justify-between p-3 bg-white rounded-lg border border-gray-200 hover:shadow-md transition-all group/file">
                        <div className="flex items-center gap-3 flex-1 min-w-0">
                          <div className="w-8 h-8 bg-gradient-to-br from-gray-400 to-gray-500 rounded-lg flex items-center justify-center text-white text-xs font-bold flex-shrink-0">
                            {file.file_name.split('.').pop()?.toUpperCase() || 'F'}
                          </div>
                          <div className="min-w-0 flex-1">
                            <p className="font-medium text-sm text-gray-900 truncate">{file.file_name}</p>
                            <p className="text-xs text-gray-500">
                              {(file.file_size / 1024).toFixed(1)} KB
                            </p>
                          </div>
                        </div>
                        <div className="flex items-center gap-1">
                          <button
                            onClick={() => handlePreviewFile(file.file_id)}
                            className="p-1.5 text-gray-500 hover:text-emerald-600 hover:bg-emerald-50 rounded-lg transition-all group-hover/file:bg-emerald-50"
                            title="Preview"
                          >
                            <Eye size={14} />
                          </button>
                          <button
                            onClick={() => handleDownloadFile(file.file_id, file.file_name)}
                            className="p-2 text-gray-500 hover:text-blue-600 hover:bg-blue-50 rounded-lg transition-all group-hover/file:bg-blue-50"
                            title="Download"
                          >
                            <Download size={16} />
                          </button>
                        </div>
                      </div>
                    ))}
                  </div>
                )}
              </div>
            )}

            {/* Add remark (In Progress / Review) */}
            {canAddRemarkNow && (
              <div className="bg-gradient-to-br from-blue-50 to-cyan-50 rounded-2xl p-4 border-2 border-blue-100">
                <label className="text-xs font-bold text-blue-700 mb-3 flex items-center gap-2">
                  <MessageSquare size={16} />
                  Add New Remark
                </label>
                <div className="space-y-3">
                  <input
                    type="text"
                    value={remark}
                    onChange={(e) => setRemark(e.target.value)}
                    placeholder="Enter your remark here..."
                    className="w-full px-4 py-3 border-2 border-blue-200 rounded-xl text-sm focus:ring-2 focus:ring-blue-500 focus:border-blue-500 bg-white font-medium transition-all"
                    onKeyDown={(e) => {
                      if (e.key === 'Enter' && !addingRemark && remark.trim()) {
                        handleAddRemark();
                      }
                    }}
                  />
                  <button
                    onClick={handleAddRemark}
                    disabled={addingRemark || !remark.trim()}
                    className="w-full px-4 py-3 bg-gradient-to-r from-blue-600 to-cyan-600 text-white rounded-xl text-sm font-bold hover:from-blue-700 hover:to-cyan-700 disabled:opacity-50 disabled:cursor-not-allowed transition-all shadow-lg hover:shadow-xl transform hover:scale-[1.02] flex items-center justify-center gap-2"
                  >
                    {addingRemark ? (
                      <>
                        <div className="w-4 h-4 border-2 border-white border-t-transparent rounded-full animate-spin"></div>
                        Adding...
                      </>
                    ) : (
                      <>
                        <Send size={16} />
                        Add Remark
                      </>
                    )}
                  </button>
                </div>
              </div>
            )}
          </div>
        )}
      </div>
    </div>
  );
};

export default TaskCard;
