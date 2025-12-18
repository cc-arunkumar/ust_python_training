export interface User {
  e_id: number;
  password?: string;
  role: string[];
  status: string;
}

export interface Employee {
  e_id?: number;
  name: string;
  email: string;
  designation: string;
  mgr_id: number;
}

export interface Task {
  t_id?: number;
  title: string;
  description: string;
  assigned_to?: number;
  assigned_by?: number;
  assigned_at?: string;
  updated_by?: number;
  updated_at?: string;
  priority: 'high' | 'medium' | 'low';
  status?: string;
  reviewer?: number;
  created_by?: number;
  expected_closure: string;
  actual_closure?: string;
}

export interface Remark {
  _id?: string;
  task_id: number;
  comment: string;
  e_id: number;
  created_at?: string;
  file_url?: string;
}

export interface LoginCredentials {
  e_id: number;
  password: string;
}

export interface AuthResponse {
  access_token: string;
  token_type: string;
  user?: User;
}

