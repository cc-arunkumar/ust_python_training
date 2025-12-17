export const API_BASE_URL = 'http://localhost:8000/api/v1';

export const USER_ROLES = {
  ADMIN: 'admin',
  MANAGER: 'manager',
  DEVELOPER: 'developer'
};

export const TASK_STATUS = {
  TODO: 'To Do',
  IN_PROGRESS: 'In Progress',
  REVIEW: 'Review',
  DONE: 'Done'
};

export const TASK_PRIORITY = {
  LOW: 'Low',
  MEDIUM: 'Medium',
  HIGH: 'High'
};

export const PRIORITY_COLORS = {
  Low: 'bg-green-100 text-green-700 border-green-200',
  Medium: 'bg-yellow-100 text-yellow-700 border-yellow-200',
  High: 'bg-red-100 text-red-700 border-red-200'
};

export const STATUS_COLORS = {
  'To Do': 'bg-gray-100 border-gray-300',
  'In Progress': 'bg-blue-50 border-blue-300',
  'Review': 'bg-purple-50 border-purple-300',
  'Done': 'bg-green-50 border-green-300'
};