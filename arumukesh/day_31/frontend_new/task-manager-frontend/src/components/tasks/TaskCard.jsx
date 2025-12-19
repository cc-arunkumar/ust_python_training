import React from 'react'
import { Calendar, User, Clock } from 'lucide-react'
import { formatDate, getDaysRemaining, truncateText } from '../../utils/helpers'
import { PRIORITY_COLORS } from '../../utils/constants'
import Badge from '../common/Badge'

const TaskCard = ({ task, onClick }) => {
  const daysInfo = getDaysRemaining(task.expected_closure)
  
  const getPriorityBadgeVariant = (priority) => {
    switch (priority) {
      case 'high': return 'danger'
      case 'medium': return 'warning'
      case 'low': return 'success'
      default: return 'default'
    }
  }

  return (
    <div
      onClick={onClick}
      className={`
        bg-white p-4 rounded-lg shadow-sm border border-gray-200
        hover:shadow-md transition-shadow cursor-pointer
        ${PRIORITY_COLORS[task.priority]}
      `}
    >
      <div className="flex items-start justify-between mb-2">
        <h4 className="font-semibold text-gray-900 flex-1 pr-2">
          {task.title}
        </h4>
        <Badge variant={getPriorityBadgeVariant(task.priority)} size="small">
          {task.priority.toUpperCase()}
        </Badge>
      </div>

      <p className="text-sm text-gray-600 mb-3">
        {truncateText(task.description, 80)}
      </p>

      <div className="space-y-2 text-xs text-gray-500">
        <div className="flex items-center gap-2">
          <Calendar className="w-3 h-3" />
          <span>Due: {formatDate(task.expected_closure)}</span>
        </div>

        {daysInfo && (
          <div className="flex items-center gap-2">
            <Clock className="w-3 h-3" />
            <span className={`
              ${daysInfo.isOverdue ? 'text-red-600 font-medium' : ''}
              ${daysInfo.isDueToday ? 'text-yellow-600 font-medium' : ''}
            `}>
              {daysInfo.text}
            </span>
          </div>
        )}

        <div className="flex items-center gap-2">
          <User className="w-3 h-3" />
          <span>Assignee: {task.assigned_to}</span>
        </div>

        <div className="flex items-center gap-2">
          <User className="w-3 h-3" />
          <span>Reviewer: {task.reviewer}</span>
        </div>
      </div>
    </div>
  )
}

export default TaskCard