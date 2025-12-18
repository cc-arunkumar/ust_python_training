export type Role = "admin" | "manager" | "employee";
export type TaskStatus = "TO_DO" | "IN_PROGRESS" | "REVIEW" | "DONE";
export type Priority = "high" | "medium" | "low";
export type UserStatus = "active" | "inactive";

export interface Employee {
  e_id: string;
  name: string;
  email: string;
  designation: string;
  mgr_id?: string;
}

export interface User {
  e_id: string;
  password: string;
  role: Role[];
  status: UserStatus;
  employee: Employee;
}

export interface Task {
  t_id: string;
  title: string;
  description: string;
  created_by: string;
  assigned_to?: string;
  assigned_by?: string;
  assigned_at?: string;
  updated_by?: string;
  updated_at?: string;
  priority: Priority;
  status: TaskStatus;
  reviewer?: string;
  expected_closure: string;
  actual_closure?: string;
}

export interface Remark {
  id: string;
  task_id: string;
  comment: string;
  created_by: string;
  created_at: string;
}

export interface AuthContextType {
  user: User | null;
  // login by employee id (e_id) and password
  login: (e_id: string, password: string) => Promise<boolean>;
  loading: boolean;
  logout: () => void;
  isAdmin: boolean;
  isManager: boolean;
  isEmployee: boolean;
  highestRole: Role;
}

export interface PaginatedResponse<T> {
  data: T[];
  total: number;
  page: number;
  limit: number;
}
export type CreateTaskInput = {
  title: string;
  description: string;
  priority: Priority;
  expected_closure: string; // YYYY-MM-DD from input
};
