import React, { useState } from 'react';
import { User, CheckCircle, Clock, PlayCircle, Pause, Edit2, ChevronDown } from 'lucide-react';
import { STATUS_CONFIG, PRIORITY_COLORS } from '../utils/constants';

function TaskCard({ task, employees, userRole, onUpdateStatus, onEdit }) {
  const [showStatusMenu, setShowStatusMenu] = useState(false);
  const [review, setReview] = useState('');
  const [showReviewInput, setShowReviewInput] = useState(false);
  const [pendingStatus, setPendingStatus] = useState(null);

  const statusIcons = {
    TO_DO: Clock,
    IN_PROGRESS: PlayCircle,
    REVIEW: Pause,
    DONE: CheckCircle,
  };

  const config = STATUS_CONFIG[task.status] || STATUS_CONFIG.TO_DO;
  const StatusIcon = statusIcons[task.status];

  const assignee = employees.find((e) => e.emp_id === task.assigned_to);
  const reviewer = employees.find((e) => e.emp_id === task.reviewer);

  // Check if user can mark task as DONE
  const canMarkDone = userRole.includes('ADMIN') || userRole.includes('MANAGER');

  // Filter available statuses based on permissions
  const getAvailableStatuses = () => {
    const allStatuses = Object.entries(STATUS_CONFIG);
    
    // If not admin or manager, filter out DONE
    if (!canMarkDone) {
      return allStatuses.filter(([status]) => status !== 'DONE');
    }
    
    return allStatuses;
  };

  const handleStatusChange = async (newStatus) => {
    // Double-check permission
    if (newStatus === 'DONE' && !canMarkDone) {
      alert('Only Managers and Admins can mark tasks as Done');
      return;
    }

    if (newStatus === 'REVIEW' || newStatus === 'DONE') {
      setPendingStatus(newStatus);
      setShowReviewInput(true);
      setShowStatusMenu(false);
    } else {
      await onUpdateStatus(task.task_id, newStatus, null);
      setShowStatusMenu(false);
    }
  };

  const submitWithReview = async () => {
    await onUpdateStatus(task.task_id, pendingStatus, review);
    setShowReviewInput(false);
    setReview('');
    setPendingStatus(null);
  };

  const cancelReview = () => {
    setShowReviewInput(false);
    setReview('');
    setPendingStatus(null);
  };

  return (
    <div className="bg-white rounded-lg shadow p-4 hover:shadow-md transition">
      <div className="flex justify-between items-start mb-3">
        <div className="flex-1">
          <h4 className="font-semibold text-gray-800 mb-1">{task.title}</h4>
          <p className="text-sm text-gray-600">
            {task.description || 'No description'}
          </p>
        </div>
        <button
          onClick={onEdit}
          className="text-gray-400 hover:text-gray-600 ml-2"
        >
          <Edit2 size={16} />
        </button>
      </div>

      <div className="space-y-2 mb-3">
        {task.dept_name && (
          <div className="text-xs text-gray-500">
            Dept: {task.dept_name}
          </div>
        )}

        {assignee && (
          <div className="flex items-center gap-2 text-sm text-gray-600">
            <User size={14} />
            {assignee.emp_name}
          </div>
        )}

        {reviewer && (
          <div className="text-xs text-gray-500">
            Reviewer: {reviewer.emp_name}
          </div>
        )}

        <div className="flex items-center justify-between">
          <div className="relative">
            <button
              onClick={() => setShowStatusMenu(!showStatusMenu)}
              className={`${config.color} text-white px-3 py-1 rounded-full text-xs font-medium flex items-center gap-1`}
            >
              {StatusIcon && <StatusIcon size={12} />}
              {config.label}
              <ChevronDown size={12} />
            </button>

            {showStatusMenu && (
              <div className="absolute top-full left-0 mt-1 bg-white rounded-lg shadow-lg border z-10 min-w-[150px]">
                {getAvailableStatuses().map(([status, cfg]) => {
                  const Icon = statusIcons[status];
                  const isDisabled = status === 'DONE' && !canMarkDone;
                  
                  return (
                    <button
                      key={status}
                      onClick={() => handleStatusChange(status)}
                      disabled={isDisabled}
                      className={`w-full px-4 py-2 text-left text-sm hover:bg-gray-50 flex items-center gap-2 ${
                        isDisabled ? 'opacity-50 cursor-not-allowed' : ''
                      }`}
                      title={isDisabled ? 'Only Managers and Admins can mark as Done' : ''}
                    >
                      {Icon && <Icon size={14} />}
                      {cfg.label}
                      {isDisabled && <span className="ml-auto text-xs text-gray-400">🔒</span>}
                    </button>
                  );
                })}
              </div>
            )}
          </div>

          {task.priority && (
            <span className={`${PRIORITY_COLORS[task.priority]} px-2 py-1 rounded text-xs font-medium`}>
              {task.priority}
            </span>
          )}
        </div>
      </div>

      {showReviewInput && (
        <div className="mt-3 pt-3 border-t">
          <p className="text-sm text-gray-600 mb-2">
            Changing status to: <strong>{STATUS_CONFIG[pendingStatus]?.label}</strong>
          </p>
          <textarea
            value={review}
            onChange={(e) => setReview(e.target.value)}
            placeholder="Add review comments..."
            className="w-full px-3 py-2 border rounded text-sm mb-2"
            rows="2"
          />
          <div className="flex gap-2">
            <button
              onClick={submitWithReview}
              className="flex-1 bg-blue-600 text-white py-1 rounded text-sm hover:bg-blue-700"
            >
              Submit
            </button>
            <button
              onClick={cancelReview}
              className="flex-1 bg-gray-200 text-gray-700 py-1 rounded text-sm hover:bg-gray-300"
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