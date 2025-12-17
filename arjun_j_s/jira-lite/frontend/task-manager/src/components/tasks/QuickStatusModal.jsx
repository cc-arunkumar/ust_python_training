import React, { useState } from 'react';
import { X, AlertCircle, CheckCircle } from 'lucide-react';
import ApiService from '../../services/api';
import { TASK_STATUSES } from '../../utils/constants';

const QuickStatusModal = ({ task, onClose, onUpdate }) => {
  const [status, setStatus] = useState(task.status);
  const [review, setReview] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const [success, setSuccess] = useState(false);

  const handleUpdate = async () => {
    setLoading(true);
    setError('');
    setSuccess(false);

    try {
      await ApiService.updateTaskStatus(
        task.task_id,
        status,
        review.trim() || null
      );
      setSuccess(true);
      setTimeout(() => {
        onUpdate();
        onClose();
      }, 1000);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="fixed inset-0 bg-black/50 transition-opacity z-50 flex items-center justify-center p-4">
      <div className="bg-gray-800 rounded-lg shadow-2xl p-5 w-full max-w-md border border-gray-700">
        <div className="flex justify-between items-center mb-4">
          <div>
            <h3 className="text-lg font-bold text-white">Update Status</h3>
            <p className="text-xs text-gray-400 mt-1">#{task.task_id} - {task.title}</p>
          </div>
          <button
            onClick={onClose}
            className="text-gray-400 hover:text-gray-200 transition"
          >
            <X size={20} />
          </button>
        </div>

        {error && (
          <div className="bg-red-900 bg-opacity-50 border border-red-700 text-red-200 px-3 py-2 rounded mb-4 flex items-center gap-2 text-sm">
            <AlertCircle size={16} />
            <span>{error}</span>
          </div>
        )}

        {success && (
          <div className="bg-green-900 bg-opacity-50 border border-green-700 text-green-200 px-3 py-2 rounded mb-4 flex items-center gap-2 text-sm">
            <CheckCircle size={16} />
            <span>Status updated successfully!</span>
          </div>
        )}

        <div className="space-y-4">
          <div>
            <label className="block text-sm font-medium text-gray-300 mb-2">
              Status
            </label>
            <select
              value={status}
              onChange={(e) => setStatus(e.target.value)}
              className="w-full px-3 py-2 bg-gray-700 border border-gray-600 text-white text-sm rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent outline-none"
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
              Review Notes
              <span className="text-gray-500 font-normal ml-1">(Optional)</span>
            </label>
            <textarea
              value={review}
              onChange={(e) => setReview(e.target.value)}
              placeholder="Add comments or feedback..."
              className="w-full px-3 py-2 bg-gray-700 border border-gray-600 text-white text-sm rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent outline-none resize-none"
              rows="3"
            />
          </div>

          <div className="flex gap-2 pt-2">
            <button
              onClick={onClose}
              disabled={loading}
              className="flex-1 px-4 py-2 border border-gray-600 text-gray-300 rounded-lg hover:bg-gray-700 disabled:opacity-50 transition text-sm font-medium"
            >
              Cancel
            </button>
            <button
              onClick={handleUpdate}
              disabled={loading || success}
              className="flex-1 bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700 disabled:bg-blue-800 disabled:cursor-not-allowed transition text-sm font-medium"
            >
              {loading ? 'Updating...' : success ? 'Updated!' : 'Update'}
            </button>
          </div>
        </div>
      </div>
    </div>
  );
};

export default QuickStatusModal;