// API Configuration
export const API_BASE_URL = 'http://localhost:8000';

export const TASK_STATUSES = {
  TODO: 'TODO',
  ON_PROCESS: 'ON_PROCESS',
  REVIEW: 'REVIEW',
  DONE: 'DONE'
};

export const STATUS_LABELS = {
  TODO: 'Todo',
  ON_PROCESS: 'On Process',
  REVIEW: 'Review',
  DONE: 'Done'
};

export const STATUS_ORDER = ['TODO', 'ON_PROCESS', 'REVIEW', 'DONE'];

// Status Colors for UI (Dark Theme)
export const STATUS_COLORS = {
  TODO: 'bg-gray-700 text-gray-200',
  IN_PROGRESS: 'bg-blue-700 text-blue-100',
  IN_REVIEW: 'bg-yellow-700 text-yellow-100',
  DONE: 'bg-green-700 text-green-100',
  BLOCKED: 'bg-red-700 text-red-100'
};

// User Roles
export const USER_ROLES = {
  ADMIN: 'ADMIN',
  MANAGER: 'MANAGER',
  DEVELOPER: 'DEVELOPER'
};

// Role Descriptions
export const ROLE_DESCRIPTIONS = {
  ADMIN: 'Full access to all features',
  MANAGER: 'Manage team and tasks',
  DEVELOPER: 'View and update assigned tasks'
};

// Local Storage Keys
export const STORAGE_KEYS = {
  TOKEN: 'token',
  USER: 'user',
  ACTIVE_ROLE: 'active_role'
}; 

export const PRIORITY_COLORS = {
  high: 'bg-red-500 text-white',
  medium: 'bg-yellow-400 text-black',
  low: 'bg-green-500 text-white',
};