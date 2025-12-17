// API Configuration
export const API_BASE_URL = 'http://localhost:8000';

// Task Status Options
export const TASK_STATUSES = {
  TODO: 'TODO',
  IN_PROGRESS: 'IN_PROGRESS',
  IN_REVIEW: 'IN_REVIEW',
  DONE: 'DONE'
};

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