import React from 'react'
import Modal from '../common/Modal'
import Badge from '../common/Badge'
import { formatDate, formatDateTime } from '../../utils/helpers'
import { STATUS_LABELS, PRIORITY_LABELS } from '../../utils/constants'

const TaskDetailModal = ({ task, isOpen, onClose, onUpdate }) => {
  if (!task) return null

  const getPriorityVariant = (priority) => {
    switch (priority) {
      case 'high': return 'danger'
      case 'medium': return 'warning'
      case 'low': return 'success'
      default: return 'default'
    }
  }

  const getStatusVariant = (status) => {
    switch (status) {
      case 'completed': return 'success'
      case 'in_progress': return 'info'
      case 'in_review': return 'warning'
      case 'pending': return 'default'
      default: return 'default'
    }
  }

  return (
    <Modal
      isOpen={isOpen}
      onClose={onClose}
      title="Task Details"
      size="large"
    >
      <div className="space-y-4">
        <div>
          <h3 className="text-lg font-semibold text-gray-900 mb-2">{task.title}</h3>
          <p className="text-gray-600">{task.description}</p>
        </div>

        <div className="grid grid-cols-2 gap-4">
          <div>
            <p className="text-sm text-gray-500 mb-1">Status</p>
            <Badge variant={getStatusVariant(task.status)}>
              {STATUS_LABELS[task.status]}
            </Badge>
          </div>
          <div>
            <p className="text-sm text-gray-500 mb-1">Priority</p>
            <Badge variant={getPriorityVariant(task.priority)}>
              {PRIORITY_LABELS[task.priority]}
            </Badge>
          </div>
        </div>

        <div className="grid grid-cols-2 gap-4">
          <div>
            <p className="text-sm text-gray-500">Created By</p>
            <p className="font-medium">{task.created_by}</p>
          </div>
          <div>
            <p className="text-sm text-gray-500">Assigned To</p>
            <p className="font-medium">{task.assigned_to}</p>
          </div>
          <div>
            <p className="text-sm text-gray-500">Assigned By</p>
            <p className="font-medium">{task.assigned_by}</p>
          </div>
          <div>
            <p className="text-sm text-gray-500">Reviewer</p>
            <p className="font-medium">{task.reviewer}</p>
          </div>
        </div>

        <div className="grid grid-cols-2 gap-4">
          <div>
            <p className="text-sm text-gray-500">Assigned At</p>
            <p className="font-medium">{formatDateTime(task.assigned_at)}</p>
          </div>
          <div>
            <p className="text-sm text-gray-500">Expected Closure</p>
            <p className="font-medium">{formatDate(task.expected_closure)}</p>
          </div>
          {task.updated_at && (
            <div>
              <p className="text-sm text-gray-500">Last Updated</p>
              <p className="font-medium">{formatDateTime(task.updated_at)}</p>
            </div>
          )}
          {task.actual_closure && (
            <div>
              <p className="text-sm text-gray-500">Actual Closure</p>
              <p className="font-medium">{formatDateTime(task.actual_closure)}</p>
            </div>
          )}
        </div>

        {task.remarks && (
          <div>
            <p className="text-sm text-gray-500 mb-1">Remarks</p>
            <p className="text-gray-700 bg-gray-50 p-3 rounded">{task.remarks}</p>
          </div>
        )}
      </div>
    </Modal>
  )
}

export default TaskDetailModal