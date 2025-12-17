export const API_BASE_URL = "http://localhost:8000";

export const TASK_STATUS = {
  TODO: "to-do",
  IN_PROGRESS: "in-progress",
  REVIEW: "review",
  COMPLETED: "completed",
};

export const PRIORITY_LEVELS = {
  LOW: "low",
  MEDIUM: "medium",
  HIGH: "high",
};

export const USER_ROLES = {
  ADMIN: "admin",
  MANAGER: "manager",
  DEVELOPER: "developer",
};

export const PRIORITY_COLORS = {
  low: "bg-green-100 text-green-800",
  medium: "bg-yellow-100 text-yellow-800",
  high: "bg-red-100 text-red-800",
};

export const STATUS_FLOW = ["to-do", "in-progress", "review", "completed"];
