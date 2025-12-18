import React from 'react';
import { Draggable } from '@hello-pangea/dnd';
import { Eye, Trash, Edit, User } from 'lucide-react';
import { STATUS_COLORS, PRIORITY_COLORS } from '../../utils/constants';
import toast from 'react-hot-toast';

const TaskCard = ({ task, index, onView, onEdit, onDelete }) => {

  const handleDelete = () => {
    if (!onDelete) return;
    const confirm = window.confirm('Are you sure you want to delete this task?');
    if (!confirm) return;
    onDelete(task.task_id);
  };

  return (
    <Draggable draggableId={task.task_id.toString()} index={index}>
      {(provided) => (
        <div
          ref={provided.innerRef}
          {...provided.draggableProps}
          {...provided.dragHandleProps}
          className="bg-white rounded-lg shadow-sm p-4 flex flex-col hover:shadow-md transition"
        >
          {/* Header */}
          <div className="flex justify-between items-start mb-2">
            <h4 className="text-sm font-semibold text-gray-800 line-clamp-1">{task.title}</h4>
            <span
              className={`px-2 py-1 rounded-full text-xs font-medium ${STATUS_COLORS[task.status]}`}
            >
              {task.status.replace('_', ' ')}
            </span>
          </div>

          {/* Description */}
          {task.description && (
            <p className="text-gray-500 text-sm line-clamp-2 mb-2">
              {task.description}
            </p>
          )}
          
          {/* Assigned, Reviewer & Priority */}
          <div className="flex flex-col gap-1 mb-2 text-xs text-gray-500">
            <p className="flex items-center gap-1">
              <User size={12} /> Assigned To: {task.assigned_to || 'Unassigned'}
            </p>
            {task.reviewer && (
              <p className="flex items-center gap-1">
                <User size={12} /> Reviewer: {task.reviewer}
              </p>
            )}
            {task.priority && (
              <span
                className={`inline-block px-2 py-1 rounded-full text-xs font-medium ${PRIORITY_COLORS[task.priority.toLowerCase()]}`}
              >
                {task.priority}
              </span>
            )}
          </div>

          {/* Actions */}
          <div className="mt-2 flex gap-2">
            {onView && (
              <button
                onClick={() => onView(task)}
                className="flex-1 flex items-center justify-center gap-1 text-blue-600 text-xs font-medium rounded-lg py-1 hover:bg-blue-50 transition"
              >
                <Eye size={14} /> View
              </button>
            )}
            {onEdit && (
              <button
                onClick={() => onEdit(task)}
                className="flex-1 flex items-center justify-center gap-1 text-green-600 text-xs font-medium rounded-lg py-1 hover:bg-green-50 transition"
              >
                <Edit size={14} /> Edit
              </button>
            )}
            {onDelete && (
              <button
                onClick={handleDelete}
                className="flex-1 flex items-center justify-center gap-1 text-red-600 text-xs font-medium rounded-lg py-1 hover:bg-red-50 transition"
              >
                <Trash size={14} /> Delete
              </button>
            )}
          </div>
        </div>
      )}
    </Draggable>
  );
};

export default TaskCard;
