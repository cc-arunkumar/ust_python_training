export const API_BASE = "http://localhost:8000";

export const STATUS_CONFIG = {
  TO_DO: {
    color: "bg-slate-500",
    label: "To Do",
    textColor: "text-slate-700",
    columnBg: "bg-slate-50",
    cardBg: "bg-slate-50",
  },
  IN_PROGRESS: {
    color: "bg-blue-500",
    label: "In Progress",
    textColor: "text-blue-700",
    columnBg: "bg-blue-50",
    cardBg: "bg-blue-50",
  },
  REVIEW: {
    color: "bg-amber-500",
    label: "In Review",
    textColor: "text-amber-700",
    columnBg: "bg-orange-100",
    cardBg: "bg-orange-100",
  },
  DONE: {
    color: "bg-emerald-500",
    label: "Done",
    textColor: "text-emerald-700",
    columnBg: "bg-emerald-50",
    cardBg: "bg-emerald-50",
  },
};

export const PRIORITY_COLORS = {
  LOW: "bg-gray-200 text-gray-700 border border-gray-300",
  MEDIUM: "bg-amber-200 text-amber-800 border border-amber-300",
  HIGH: "bg-red-200 text-red-800 border border-red-300",
};

export const STATUSES = ["TO_DO", "IN_PROGRESS", "REVIEW", "DONE"];
export const PRIORITIES = ["LOW", "MEDIUM", "HIGH"];