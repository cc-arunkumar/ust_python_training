export const TASK_STATUS = {
  PENDING: 'pending',
  IN_PROGRESS: 'in_progress',
  IN_REVIEW: 'in_review',
  COMPLETED: 'completed',
  ON_HOLD: 'on_hold',
  CANCELLED: 'cancelled',
}

export const TASK_PRIORITY = {
  HIGH: 'high',
  MEDIUM: 'medium',
  LOW: 'low',
}

export const USER_ROLES = {
  ADMIN: 'admin',
  MANAGER: 'manager',
  DEVELOPER: 'developer',
}

export const STATUS_COLORS = {
  pending: 'bg-gray-100 text-gray-800 border-gray-300',
  in_progress: 'bg-blue-100 text-blue-800 border-blue-300',
  in_review: 'bg-yellow-100 text-yellow-800 border-yellow-300',
  completed: 'bg-green-100 text-green-800 border-green-300',
  on_hold: 'bg-orange-100 text-orange-800 border-orange-300',
  cancelled: 'bg-red-100 text-red-800 border-red-300',
}

export const PRIORITY_COLORS = {
  high: 'border-l-4 border-l-red-500',
  medium: 'border-l-4 border-l-yellow-500',
  low: 'border-l-4 border-l-green-500',
}

export const STATUS_LABELS = {
  pending: 'Pending',
  in_progress: 'In Progress',
  in_review: 'In Review',
  completed: 'Completed',
  on_hold: 'On Hold',
  cancelled: 'Cancelled',
}

export const PRIORITY_LABELS = {
  high: 'High',
  medium: 'Medium',
  low: 'Low',
}