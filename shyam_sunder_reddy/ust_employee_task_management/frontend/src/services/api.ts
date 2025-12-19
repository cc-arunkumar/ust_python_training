import axios, { AxiosError } from "axios";
import type {
  User,
  Employee,
  Task,
  Remark,
  LoginCredentials,
  AuthResponse,
} from "../types";

export const API_BASE_URL = "http://localhost:8000";

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    "Content-Type": "application/json",
  },
});

// Normalize role input from various formats coming from the backend or localStorage.
// The DB sometimes stores roles as JSON strings (e.g. '["Developer","Manager"]')
// or comma-separated strings (e.g. 'Developer,Manager'). This helper returns
// a single role string to send to backend endpoints (the first role by preference)
// and ensures we don't send the raw, malformed value.
export const normalizeRoleForApi = (
  role?: string | string[] | null
): string => {
  if (!role) return "";

  // If already an array-like string (serialized JSON), try to parse it
  if (typeof role === "string") {
    const trimmed = role.trim();

    // JSON array like '["Developer","Manager"]'
    if (trimmed.startsWith("[") && trimmed.endsWith("]")) {
      try {
        const parsed = JSON.parse(trimmed);
        if (Array.isArray(parsed) && parsed.length > 0)
          return String(parsed[0]);
      } catch (_e) {
        // fallthrough to other parsing strategies
      }
    }

    // Comma separated like 'Developer,Manager,Admin' or '"Developer,Manager"'
    if (trimmed.includes(",")) {
      // remove surrounding quotes if present
      const unquoted = trimmed.replace(/^\"|\"$/g, "").replace(/^\'|\'$/g, "");
      const parts = unquoted
        .split(",")
        .map((p) => p.trim())
        .filter(Boolean);
      if (parts.length > 0) return parts[0];
    }

    // Quoted single value like '"Developer"' or '\"Developer\"'
    const unquoted = trimmed.replace(/^\"|\"$/g, "").replace(/^\'|\'$/g, "");
    if (unquoted) return unquoted;
  }

  // If role is already an array (shouldn't happen here, but be defensive)
  if (Array.isArray(role) && role.length > 0) return String(role[0]);

  return "";
};

// Add token to requests
api.interceptors.request.use((config) => {
  const token = localStorage.getItem("token");
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  // Log requests in development
  if (import.meta.env.DEV) {
    console.log(
      `📤 API Request: ${config.method?.toUpperCase()} ${config.url}`,
      {
        params: config.params,
        data: config.data,
        headers: config.headers,
      }
    );
  }
  return config;
});

// Handle errors and add logging
api.interceptors.response.use(
  (response) => {
    // Log successful responses in development
    if (import.meta.env.DEV) {
      console.log(
        `✅ API Success: ${response.config.method?.toUpperCase()} ${
          response.config.url
        }`,
        response.data
      );
    }
    return response;
  },
  (error: AxiosError) => {
    // Log errors in development
    if (import.meta.env.DEV) {
      console.error(
        `❌ API Error: ${error.config?.method?.toUpperCase()} ${
          error.config?.url
        }`,
        {
          status: error.response?.status,
          statusText: error.response?.statusText,
          data: error.response?.data,
          message: error.message,
        }
      );
    }

    if (error.response?.status === 401) {
      localStorage.removeItem("token");
      // Only redirect if we're not already on the login page
      if (window.location.pathname !== "/login") {
        window.location.href = "/login";
      }
    }
    return Promise.reject(error);
  }
);

// Auth API
export const authAPI = {
  login: async (credentials: LoginCredentials): Promise<AuthResponse> => {
    const response = await api.post<AuthResponse>("/auth/login", credentials);
    return response.data;
  },
  getMe: async (): Promise<User> => {
    const response = await api.get<User>("/auth/me");
    return response.data;
  },
};

// Employee API
export const employeeAPI = {
  getAll: async (role: string): Promise<Employee[]> => {
    try {
      const r = normalizeRoleForApi(role);
      const response = await api.get<Employee[]>(
        `/Employee/getall?role=${encodeURIComponent(r)}`
      );
      return response.data || [];
    } catch (error: any) {
      // Handle 404 as empty array instead of error
      if (error.response?.status === 404) {
        return [];
      }
      throw error;
    }
  },
  getById: async (id: number, role: string): Promise<Employee> => {
    const r = normalizeRoleForApi(role);
    const response = await api.get<Employee>(
      `/Employee/get?id=${id}&role=${encodeURIComponent(r)}`
    );
    return response.data;
  },
  create: async (
    role: string,
    employee: { employee: Employee; assigning_role: string[] }
  ): Promise<any> => {
    const r = normalizeRoleForApi(role);
    const response = await api.post(
      `/Employee/create?role=${encodeURIComponent(r)}`,
      employee
    );
    return response.data;
  },
  update: async (
    id: number,
    role: string,
    employee: Employee
  ): Promise<any> => {
    const r = normalizeRoleForApi(role);
    const response = await api.put(
      `/Employee/update?id=${id}&role=${encodeURIComponent(r)}`,
      employee
    );
    return response.data;
  },
  delete: async (id: number, role: string): Promise<any> => {
    const r = normalizeRoleForApi(role);
    const response = await api.delete(
      `/Employee/delete?id=${id}&role=${encodeURIComponent(r)}`
    );
    return response.data;
  },
};

// Task API
export const taskAPI = {
  getAll: async (role: string): Promise<Task[]> => {
    try {
      const r = normalizeRoleForApi(role);
      const response = await api.get<Task[]>(
        `/Task/getall?role=${encodeURIComponent(r)}`
      );
      return response.data || [];
    } catch (error: any) {
      // Handle 404 as empty array instead of error
      if (error.response?.status === 404) {
        return [];
      }
      throw error;
    }
  },
  getById: async (id: number, role: string): Promise<Task> => {
    const r = normalizeRoleForApi(role);
    const response = await api.get<Task>(
      `/Task/get?id=${id}&role=${encodeURIComponent(r)}`
    );
    return response.data;
  },
  getByStatus: async (status: string, role: string): Promise<Task[]> => {
    const r = normalizeRoleForApi(role);
    const response = await api.get<Task[]>(
      `/Task/getbystatus?status=${encodeURIComponent(
        status
      )}&role=${encodeURIComponent(r)}`
    );
    return response.data;
  },
  create: async (role: string, task: Task): Promise<any> => {
    const r = normalizeRoleForApi(role);
    const response = await api.post(
      `/Task/create?role=${encodeURIComponent(r)}`,
      task
    );
    return response.data;
  },
  update: async (
    t_id: number,
    role: string,
    updates: Partial<Task>
  ): Promise<any> => {
    // Backend expects query parameters, not a JSON body
    const params = new URLSearchParams();
    params.append("t_id", t_id.toString());
    params.append("role", normalizeRoleForApi(role));

    if (updates.title !== undefined) params.append("title", updates.title);
    if (updates.description !== undefined)
      params.append("description", updates.description);
    if (updates.assigned_to !== undefined)
      params.append("assigned_to", updates.assigned_to.toString());
    if (updates.priority !== undefined)
      params.append("priority", updates.priority);
    if (updates.status !== undefined) params.append("status", updates.status);
    if (updates.reviewer !== undefined)
      params.append("reviewer", updates.reviewer.toString());
    if (updates.expected_closure !== undefined) {
      params.append(
        "expected_closure",
        new Date(updates.expected_closure).toISOString()
      );
    }

    const response = await api.put(`/Task/update?${params.toString()}`);
    return response.data;
  },
  patchStatus: async (
    id: number,
    status: string,
    role: string
  ): Promise<any> => {
    const r = normalizeRoleForApi(role);
    const response = await api.patch(
      `/Task/patch?id=${id}&status=${encodeURIComponent(
        status
      )}&role=${encodeURIComponent(r)}`
    );
    return response.data;
  },
  patchPriority: async (
    t_id: number,
    priority: string,
    role: string
  ): Promise<any> => {
    const r = normalizeRoleForApi(role);
    const response = await api.patch(
      `/Task/tasks/${t_id}/priority?priority=${encodeURIComponent(
        priority
      )}&role=${encodeURIComponent(r)}`
    );
    return response.data;
  },
  delete: async (id: number, role: string): Promise<any> => {
    const r = normalizeRoleForApi(role);
    const response = await api.delete(
      `/Task/delete?id=${id}&role=${encodeURIComponent(r)}`
    );
    return response.data;
  },
};

// User API
export const userAPI = {
  getAll: async (role: string): Promise<User[]> => {
    const r = normalizeRoleForApi(role);
    const response = await api.get<User[]>(
      `/Users/getall?role=${encodeURIComponent(r)}`
    );
    return response.data;
  },
  getById: async (id: number, role: string): Promise<User> => {
    const r = normalizeRoleForApi(role);
    const response = await api.get<User>(
      `/Users/get?id=${id}&role=${encodeURIComponent(r)}`
    );
    return response.data;
  },
  getByRole: async (role: string): Promise<User[]> => {
    const r = normalizeRoleForApi(role);
    const response = await api.get<User[]>(
      `/Users/getbyrole?role=${encodeURIComponent(r)}`
    );
    return response.data;
  },
  create: async (role: string, user: User): Promise<any> => {
    const r = normalizeRoleForApi(role);
    const response = await api.post(
      `/Users/create?role=${encodeURIComponent(r)}`,
      user
    );
    return response.data;
  },
  update: async (
    id: number,
    role: string,
    user: Partial<User>
  ): Promise<any> => {
    const r = normalizeRoleForApi(role);
    const response = await api.put(
      `/Users/update?id=${id}&role=${encodeURIComponent(r)}`,
      user
    );
    return response.data;
  },
  delete: async (id: number, role: string): Promise<any> => {
    const r = normalizeRoleForApi(role);
    const response = await api.delete(
      `/Users/delete?id=${id}&role=${encodeURIComponent(r)}`
    );
    return response.data;
  },
};

// Remark API
export const remarkAPI = {
  getByTask: async (task_id: number, role: string): Promise<Remark[]> => {
    try {
      const r = normalizeRoleForApi(role);
      const response = await api.get<Remark[]>(
        `/Remark/getbytask?task_id=${task_id}&role=${encodeURIComponent(r)}`
      );
      return response.data || [];
    } catch (error: any) {
      // Handle 404 as empty array instead of error
      if (error.response?.status === 404) {
        return [];
      }
      throw error;
    }
  },
  create: async (
    task_id: number,
    comment: string,
    role: string,
    file?: File
  ): Promise<any> => {
    const formData = new FormData();
    formData.append("task_id", task_id.toString());
    formData.append("comment", comment);
    formData.append("role", normalizeRoleForApi(role));
    if (file) {
      formData.append("file", file);
    }
    const response = await api.post("/Remark/create", formData, {
      headers: {
        "Content-Type": "multipart/form-data",
      },
    });
    return response.data;
  },
  update: async (
    remark_id: string,
    role: string,
    comment?: string,
    file?: File
  ): Promise<any> => {
    const formData = new FormData();
    formData.append("remark_id", remark_id);
    formData.append("role", normalizeRoleForApi(role));
    if (comment) {
      formData.append("comment", comment);
    }
    if (file) {
      formData.append("file", file);
    }
    const response = await api.put("/Remark/update", formData, {
      headers: {
        "Content-Type": "multipart/form-data",
      },
    });
    return response.data;
  },
  delete: async (id: string, role: string): Promise<any> => {
    const r = normalizeRoleForApi(role);
    const response = await api.delete(
      `/Remark/delete?id=${id}&role=${encodeURIComponent(r)}`
    );
    return response.data;
  },
};

export default api;
