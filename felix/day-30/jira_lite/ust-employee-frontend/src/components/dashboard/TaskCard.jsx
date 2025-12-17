import React, { useState } from 'react';
import { User, Calendar } from 'lucide-react';
import { PRIORITY_COLORS } from '../../utils/constants';

const TaskCard = ({ task, onStatusChange, onAddRemark, canEdit }) => {
  const [showDetails, setShowDetails] = useState(false);
  const [remark, setRemark] = useState('');
  const [addingRemark, setAddingRemark] = useState(false);

  const handleAddRemark = async () => {
    if (!remark.trim()) return;
    setAddingRemark(true);
    await onAddRemark(task._id, remark);
    setRemark('');
    setAddingRemark(false);
  };

  return (
    <div className="bg-white rounded-xl shadow-sm border border-gray-200 p-4 hover:shadow-md transition-all cursor-pointer">
      <div onClick={() => setShowDetails(!showDetails)}>
        <div className="flex items-start justify-between mb-3">
          <h3 className="font-semibold text-gray-900 flex-1">{task.title}</h3>
          <span className={`text-xs px-2 py-1 rounded-full border ${PRIORITY_COLORS[task.priority]}`}>
            {task.priority}
          </span>
        </div>
        
        <p className="text-sm text-gray-600 mb-3 line-clamp-2">{task.description}</p>
        
        <div className="flex items-center justify-between text-xs text-gray-500">
          <div className="flex items-center gap-1">
            <User size={14} />
            <span>ID: {task.assigned_to}</span>
          </div>
          <div className="flex items-center gap-1">
            <Calendar size={14} />
            <span>{new Date(task.expected_completion_date).toLocaleDateString()}</span>
          </div>
        </div>
      </div>
      
      {showDetails && (
        <div className="mt-4 pt-4 border-t border-gray-100 space-y-3">
          <div>
            <label className="text-xs font-semibold text-gray-700 mb-1 block">
              Change Status
            </label>
            <select
              value={task.status}
              onChange={(e) => onStatusChange(task._id, e.target.value)}
              disabled={!canEdit}
              className="w-full px-3 py-2 border border-gray-300 rounded-lg text-sm focus:ring-2 focus:ring-blue-500 focus:border-transparent disabled:bg-gray-100"
            >
              <option value="To Do">To Do</option>
              <option value="In Progress">In Progress</option>
              <option value="Review">Review</option>
              <option value="Done">Done</option>
            </select>
          </div>
          
          {task.remarks && task.remarks.length > 0 && (
            <div>
              <label className="text-xs font-semibold text-gray-700 mb-1 block">
                Remarks
              </label>
              <div className="space-y-1 max-h-32 overflow-y-auto">
                {task.remarks.map((r, i) => (
                  <div key={i} className="text-xs bg-gray-50 p-2 rounded">
                    {typeof r === 'object' 
                      ? Object.entries(r).map(([k, v]) => `${k}: ${v}`).join(', ') 
                      : r}
                  </div>
                ))}
              </div>
            </div>
          )}
          
          <div>
            <label className="text-xs font-semibold text-gray-700 mb-1 block">
              Add Remark
            </label>
            <div className="flex gap-2">
              <input
                type="text"
                value={remark}
                onChange={(e) => setRemark(e.target.value)}
                placeholder="Enter remark..."
                className="flex-1 px-3 py-2 border border-gray-300 rounded-lg text-sm focus:ring-2 focus:ring-blue-500 focus:border-transparent"
              />
              <button
                onClick={handleAddRemark}
                disabled={addingRemark || !remark.trim()}
                className="px-4 py-2 bg-blue-600 text-white rounded-lg text-sm hover:bg-blue-700 disabled:opacity-50 transition-colors"
              >
                Add
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};

export default TaskCard;