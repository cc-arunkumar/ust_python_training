import React, { useState } from 'react';
import { User, Calendar, MessageSquare, ChevronDown, ChevronUp, UserPlus, Send } from 'lucide-react';
import { PRIORITY_COLORS } from '../../utils/constants';

const TaskCard = ({ task, onStatusChange, onAddRemark, canEdit, onAssign, employees = [] }) => {
  const [showDetails, setShowDetails] = useState(false);
  const [remark, setRemark] = useState('');
  const [addingRemark, setAddingRemark] = useState(false);
  const [assignee, setAssignee] = useState(task.assigned_to || '');

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

  const canAddRemarkNow =
    task.status === 'In Progress' || task.status === 'Review';

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

      <style jsx>{`
        .custom-scrollbar::-webkit-scrollbar {
          width: 6px;
        }
        .custom-scrollbar::-webkit-scrollbar-track {
          background: #f1f1f1;
          border-radius: 10px;
        }
        .custom-scrollbar::-webkit-scrollbar-thumb {
          background: #cbd5e1;
          border-radius: 10px;
        }
        .custom-scrollbar::-webkit-scrollbar-thumb:hover {
          background: #94a3b8;
        }
      `}</style>
    </div>
  );
};

export default TaskCard;