export const API_BASE = 'http://localhost:8000';

export const STATUS_CONFIG = {
  TO_DO: { 
    color: 'bg-gray-500', 
    label: 'To Do',
    textColor: 'text-gray-700'
  },
  IN_PROGRESS: { 
    color: 'bg-blue-500', 
    label: 'In Progress',
    textColor: 'text-blue-700'
  },
  REVIEW: { 
    color: 'bg-yellow-500', 
    label: 'In Review',
    textColor: 'text-yellow-700'
  },
  DONE: { 
    color: 'bg-green-500', 
    label: 'Done',
    textColor: 'text-green-700'
  },
};

export const PRIORITY_COLORS = {
  LOW: 'bg-gray-100 text-gray-700',
  MEDIUM: 'bg-yellow-100 text-yellow-700',
  HIGH: 'bg-orange-100 text-orange-700',
  CRITICAL: 'bg-red-100 text-red-700',
};

export const STATUSES = ['TO_DO', 'IN_PROGRESS', 'REVIEW', 'DONE'];
export const PRIORITIES = ['LOW', 'MEDIUM', 'HIGH', 'CRITICAL'];