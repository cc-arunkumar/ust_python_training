import React, { useState } from 'react';
import { X, Upload, AlertCircle, CheckCircle } from 'lucide-react';
import ApiService from '../../services/api';
import { TASK_STATUSES } from '../../utils/constants';

const PRIORITY_COLORS = {
  high: 'bg-red-600 text-red-100',
  medium: 'bg-yellow-600 text-yellow-100',
  low: 'bg-green-600 text-green-100'
};

const TaskDetailsModal = ({ task, onClose, onUpdate }) => {
  const [status, setStatus] = useState(task.status);
  const [review, setReview] = useState('');
  const [file, setFile] = useState(null);
  const [loading, setLoading] = useState(false);
  const [uploadSuccess, setUploadSuccess] = useState(false);
  const [error, setError] = useState('');

  const handleStatusUpdate = async () => {
    setLoading(true);
    setError('');

    try {
      await ApiService.updateTaskStatus(
        task.task_id, 
        status, 
        review.trim() || null
      );
      onUpdate();
      onClose();
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  const handleFileUpload = async () => {
    if (!file) return;
    
    setLoading(true);
    setError('');
    setUploadSuccess(false);

    try {
      await ApiService.uploadFile(task.task_id, file);
      setUploadSuccess(true);
      setFile(null);
      
      setTimeout(() => setUploadSuccess(false), 3000);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  const formatDate = (dateString) => {
    if (!dateString) return '-';
    return new Date(dateString).toLocaleDateString();
  };

  return (
    <div className="fixed inset-0 bg-black/50 transition-opacity z-50 flex items-center justify-center p-4">
      <div className="bg-gray-800 rounded-lg shadow-2xl p-6 w-full max-w-2xl max-h-[90vh] overflow-y-auto border border-gray-700">
        <div className="flex justify-between items-center mb-6">
          <h2 className="text-2xl font-bold text-white">Task Details</h2>
          <button
            onClick={onClose}
            className="text-gray-400 hover:text-gray-200 transition"
          >
            <X size={24} />
          </button>
        </div>

        {error && (
          <div className="bg-red-900 bg-opacity-50 border border-red-700 text-red-200 px-4 py-3 rounded mb-4 flex items-center gap-2">
            <AlertCircle size={20} />
            <span className="text-sm">{error}</span>
          </div>
        )}

        {uploadSuccess && (
          <div className="bg-green-900 bg-opacity-50 border border-green-700 text-green-200 px-4 py-3 rounded mb-4 flex items-center gap-2">
            <CheckCircle size={20} />
            <span className="text-sm">File uploaded successfully!</span>
          </div>
        )}

        <div className="space-y-6">
          {/* Task Information */}
          <div className="grid gap-4">
            <div>
              <h3 className="text-sm font-semibold text-gray-400 uppercase mb-1">
                Task ID
              </h3>
              <p className="text-white">#{task.task_id}</p>
            </div>

            <div>
              <h3 className="text-sm font-semibold text-gray-400 uppercase mb-1">
                Title
              </h3>
              <p className="text-white text-lg font-medium">{task.title}</p>
            </div>

            <div>
              <h3 className="text-sm font-semibold text-gray-400 uppercase mb-1">
                Description
              </h3>
              <p className="text-gray-300">
                {task.description || 'No description provided'}
              </p>
            </div>
          </div>

          {/* Assignment Details */}
          <div className="grid grid-cols-2 gap-4 pt-4 border-t border-gray-700">
            <div>
              <h3 className="text-sm font-semibold text-gray-400 uppercase mb-1">
                Assigned To
              </h3>
              <p className="text-white">
                {task.assigned_to ? `Employee #${task.assigned_to}` : 'Unassigned'}
              </p>
            </div>

            <div>
              <h3 className="text-sm font-semibold text-gray-400 uppercase mb-1">
                Reviewer
              </h3>
              <p className="text-white">
                {task.reviewer ? `Employee #${task.reviewer}` : 'No reviewer'}
              </p>
            </div>

            <div>
              <h3 className="text-sm font-semibold text-gray-400 uppercase mb-1">
                Created By
              </h3>
              <p className="text-white">Employee #{task.created_by}</p>
            </div>

            <div>
              <h3 className="text-sm font-semibold text-gray-400 uppercase mb-1">
                Expected Closure
              </h3>
              <p className="text-white">{formatDate(task.expected_closure)}</p>
            </div>

            <div>
              <h3 className="text-sm font-semibold text-gray-400 uppercase mb-1">
                Priority
              </h3>
              <span className={`inline-block text-xs font-semibold px-2 py-1 rounded ${PRIORITY_COLORS[task.priority || 'medium']}`}>
                {(task.priority || 'medium').toUpperCase()}
              </span>
            </div>
          </div>

          {/* Status Update Section */}
          <div className="pt-4 border-t border-gray-700">
            <h3 className="text-sm font-semibold text-gray-400 uppercase mb-3">
              Update Status
            </h3>
            <div className="space-y-4">
              <div>
                <label className="block text-sm font-medium text-gray-300 mb-2">
                  Status
                </label>
                <select
                  value={status}
                  onChange={(e) => setStatus(e.target.value)}
                  className="w-full px-3 py-2 bg-gray-700 border border-gray-600 text-white rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent outline-none"
                >
                  {Object.values(TASK_STATUSES).map((st) => (
                    <option key={st} value={st}>
                      {st.replace('_', ' ')}
                    </option>
                  ))}
                </select>
              </div>

              <div>
                <label className="block text-sm font-medium text-gray-300 mb-2">
                  Review Notes (Optional)
                </label>
                <textarea
                  value={review}
                  onChange={(e) => setReview(e.target.value)}
                  placeholder="Add review comments or feedback..."
                  className="w-full px-3 py-2 bg-gray-700 border border-gray-600 text-white rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent outline-none"
                  rows="3"
                />
              </div>
            </div>
          </div>

          {/* File Upload Section */}
          <div className="pt-4 border-t border-gray-700">
            <h3 className="text-sm font-semibold text-gray-400 uppercase mb-3">
              Upload File
            </h3>
            <div className="flex gap-2">
              <input
                type="file"
                onChange={(e) => setFile(e.target.files?.[0] || null)}
                className="flex-1 text-sm text-gray-300 file:mr-4 file:py-2 file:px-4 file:rounded-lg file:border-0 file:text-sm file:font-medium file:bg-blue-600 file:text-white hover:file:bg-blue-700 file:cursor-pointer"
              />
              <button
                onClick={handleFileUpload}
                disabled={!file || loading}
                className="bg-green-600 text-white px-4 py-2 rounded-lg hover:bg-green-700 disabled:bg-green-800 disabled:cursor-not-allowed transition flex items-center gap-2"
              >
                <Upload size={18} />
                Upload
              </button>
            </div>
          </div>

          {/* Action Buttons */}
          <div className="flex gap-3 pt-6 border-t border-gray-700">
            <button
              onClick={onClose}
              className="flex-1 px-4 py-2 border border-gray-600 text-gray-300 rounded-lg hover:bg-gray-700 transition font-medium"
            >
              Close
            </button>
            <button
              onClick={handleStatusUpdate}
              disabled={loading}
              className="flex-1 bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700 disabled:bg-blue-800 disabled:cursor-not-allowed transition font-medium"
            >
              {loading ? 'Updating...' : 'Update Status'}
            </button>
          </div>
        </div>
      </div>
    </div>
  );
};

export default TaskDetailsModal;