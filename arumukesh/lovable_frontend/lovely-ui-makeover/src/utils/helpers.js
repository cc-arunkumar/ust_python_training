import { format, formatDistanceToNow, differenceInDays, parseISO } from 'date-fns'

// Format date to readable string
export const formatDate = (date) => {
  if (!date) return 'N/A'
  try {
    const parsedDate = typeof date === 'string' ? parseISO(date) : date
    return format(parsedDate, 'MMM dd, yyyy')
  } catch (error) {
    return 'Invalid date'
  }
}

// Format date with time
export const formatDateTime = (date) => {
  if (!date) return 'N/A'
  try {
    const parsedDate = typeof date === 'string' ? parseISO(date) : date
    return format(parsedDate, 'MMM dd, yyyy hh:mm a')
  } catch (error) {
    return 'Invalid date'
  }
}

// Get relative time (e.g., "2 days ago")
export const getRelativeTime = (date) => {
  if (!date) return 'N/A'
  try {
    const parsedDate = typeof date === 'string' ? parseISO(date) : date
    return formatDistanceToNow(parsedDate, { addSuffix: true })
  } catch (error) {
    return 'Invalid date'
  }
}

// Calculate days remaining
export const getDaysRemaining = (dueDate) => {
  if (!dueDate) return null
  try {
    const parsedDate = typeof dueDate === 'string' ? parseISO(dueDate) : dueDate
    const days = differenceInDays(parsedDate, new Date())
    
    if (days < 0) return { text: `Overdue by ${Math.abs(days)}d`, isOverdue: true }
    if (days === 0) return { text: 'Due today', isDueToday: true }
    return { text: `${days}d left`, daysLeft: days }
  } catch (error) {
    return { text: 'Invalid date', isError: true }
  }
}

// Truncate text
export const truncateText = (text, maxLength = 100) => {
  if (!text) return ''
  if (text.length <= maxLength) return text
  return text.substring(0, maxLength) + '...'
}

// Get initials from name
export const getInitials = (name) => {
  if (!name) return '?'
  const parts = name.trim().split(' ')
  if (parts.length === 1) return parts[0].charAt(0).toUpperCase()
  return (parts[0].charAt(0) + parts[parts.length - 1].charAt(0)).toUpperCase()
}

// Validate email
export const isValidEmail = (email) => {
  const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/
  return re.test(email)
}

// Sort tasks by priority
export const sortByPriority = (tasks) => {
  const priorityOrder = { high: 1, medium: 2, low: 3 }
  return [...tasks].sort((a, b) => {
    return priorityOrder[a.priority] - priorityOrder[b.priority]
  })
}

// Group tasks by status
export const groupTasksByStatus = (tasks) => {
  return tasks.reduce((acc, task) => {
    const status = task.status
    if (!acc[status]) {
      acc[status] = []
    }
    acc[status].push(task)
    return acc
  }, {})
}

// Check if user can drag task
export const canDragTask = (task, user) => {
  if (task.status === 'completed') return false
  
  const userEmpId = String(user.emp_id)
  const isReviewer = String(task.reviewer) === userEmpId
  const isAssignee = String(task.assigned_to) === userEmpId
  
  if (isReviewer) {
    return task.status === 'in_review'
  }
  
  if (isAssignee) {
    return task.status === 'pending' || task.status === 'in_progress'
  }
  
  return false
}

// Validate task status transition
export const isValidStatusTransition = (currentStatus, newStatus, userRole, isReviewer, isAssignee) => {
  // Completed tasks cannot be moved
  if (currentStatus === 'completed') return false
  
  // Cannot move directly to completed unless from in_review
  if (newStatus === 'completed' && currentStatus !== 'in_review') return false
  
  // Developer (assignee) transitions
  if (isAssignee && !isReviewer) {
    const allowedTransitions = {
      pending: ['in_progress'],
      in_progress: ['in_review'],
      in_review: [], // Developer cannot move from in_review
    }
    return allowedTransitions[currentStatus]?.includes(newStatus) || false
  }
  
  // Reviewer transitions
  if (isReviewer) {
    if (currentStatus === 'in_review') {
      return newStatus === 'completed' || newStatus === 'in_progress'
    }
  }
  
  return false
}