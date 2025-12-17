import React, { useState } from 'react';
import { X, Upload, AlertCircle, CheckCircle } from 'lucide-react';
import ApiService from '../../services/api';
import { TASK_STATUSES } from '../../utils/constants';

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
      await ApiService.updateTaskStatus(task.task_id, status, review.trim() || null);
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

  const formatDate = (dateString) => (dateString ? new Date(dateString).toLocaleDateString() : '-');

  return (
    <div className="fixed inset-0 bg-white bg-opacity-30 backdrop-blur-sm flex items-center justify-center p-4 z-50 overflow-auto backdrop-blur-sm bg-white/30">
      <div className="bg-white rounded-2xl shadow-2xl w-full max-w-4xl max-h-[90vh] overflow-y-auto flex flex-col sm:flex-row p-6 border border-gray-200">
        
        {/* Left: Task Info */}
        <div className="flex-1 pr-4 border-b sm:border-b-0 sm:border-r border-gray-200 sm:pr-6 sm:mr-6 space-y-4">
          <div className="flex justify-between items-center mb-4">
            <h2 className="text-2xl font-bold text-gray-800">Task Overview</h2>
            <button onClick={onClose} className="text-gray-400 hover:text-gray-600 transition">
              <X size={24} />
            </button>
          </div>

          {error && (
            <div className="bg-red-100 border border-red-300 text-red-700 px-4 py-3 rounded flex items-center gap-2">
              <AlertCircle size={20} />
              <span className="text-sm">{error}</span>
            </div>
          )}
          {uploadSuccess && (
            <div className="bg-green-100 border border-green-300 text-green-700 px-4 py-3 rounded flex items-center gap-2">
              <CheckCircle size={20} />
              <span className="text-sm">File uploaded successfully!</span>
            </div>
          )}

          <div className="space-y-3">
            <div>
              <h3 className="text-xs font-semibold text-gray-500 uppercase mb-1">Task Number</h3>
              <p className="text-gray-800 font-medium">{task.task_id}</p>
            </div>

            <div>
              <h3 className="text-xs font-semibold text-gray-500 uppercase mb-1">Task Name</h3>
              <p className="text-gray-900 font-semibold text-lg">{task.title}</p>
            </div>

            <div>
              <h3 className="text-xs font-semibold text-gray-500 uppercase mb-1">Details</h3>
              <p className="text-gray-700">{task.description || 'No additional details provided.'}</p>
            </div>

            <div className="grid grid-cols-2 gap-4">
              <div>
                <h3 className="text-xs font-semibold text-gray-500 uppercase mb-1">Assigned To</h3>
                <p className="text-gray-800">{task.assigned_to ? `Employee ID: ${task.assigned_to}` : 'Not assigned yet'}</p>
              </div>
              <div>
                <h3 className="text-xs font-semibold text-gray-500 uppercase mb-1">Reviewed By</h3>
                <p className="text-gray-800">{task.reviewer ? `Employee ID: ${task.reviewer}` : 'Pending assignment'}</p>
              </div>
              <div>
                <h3 className="text-xs font-semibold text-gray-500 uppercase mb-1">Created By</h3>
                <p className="text-gray-800">{task.creator_name ? `${task.creator_name} (#${task.created_by})` : `Employee ID: `}</p>
              </div>
              <div>
                <h3 className="text-xs font-semibold text-gray-500 uppercase mb-1">Due Date</h3>
                <p className="text-gray-800">{formatDate(task.expected_closure)}</p>
              </div>
            </div>
          </div>
        </div>

        {/* Right: Actions */}
        <div className="flex-1 mt-6 sm:mt-0 space-y-5">
          <div>
            <h3 className="text-sm font-semibold text-gray-600 uppercase mb-2">Change Task Status</h3>
            <div className="flex flex-col gap-3">
              <select
                value={status}
                onChange={(e) => setStatus(e.target.value)}
                className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:outline-none"
              >
                {Object.values(TASK_STATUSES).map((st) => (
                  <option key={st} value={st}>
                    {st.replace('_', ' ')}
                  </option>
                ))}
              </select>

              <textarea
                value={review}
                onChange={(e) => setReview(e.target.value)}
                placeholder="Add comments or feedback (optional)..."
                className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:outline-none"
                rows="4"
              />
            </div>
          </div>

          <div>
            <h3 className="text-sm font-semibold text-gray-600 uppercase mb-2">Attach Supporting File</h3>
            <div className="flex flex-col sm:flex-row gap-2">
              <input
                type="file"
                onChange={(e) => setFile(e.target.files?.[0] || null)}
                className="flex-1 text-gray-700 file:mr-4 file:py-2 file:px-4 file:rounded-lg file:border-0 file:bg-blue-500 file:text-white hover:file:bg-blue-600 file:cursor-pointer"
              />
              <button
                onClick={handleFileUpload}
                disabled={!file || loading}
                className="flex-1 bg-green-500 text-white px-4 py-2 rounded-lg hover:bg-green-600 disabled:bg-green-300 disabled:cursor-not-allowed flex items-center justify-center gap-2 transition"
              >
                <Upload size={18} />
                Upload
              </button>
            </div>
          </div>

          <div className="flex flex-col sm:flex-row gap-3">
            <button
              onClick={onClose}
              className="flex-1 px-4 py-2 border border-gray-300 text-gray-700 rounded-lg hover:bg-gray-100 transition font-medium"
            >
              Close
            </button>
            <button
              onClick={handleStatusUpdate}
              disabled={loading}
              className="flex-1 bg-blue-500 text-white px-4 py-2 rounded-lg hover:bg-blue-600 disabled:bg-blue-300 disabled:cursor-not-allowed transition font-medium"
            >
              {loading ? 'Updating...' : 'Save Changes'}
            </button>
          </div>
        </div>
      </div>
    </div>
  );
};

export default TaskDetailsModal;
