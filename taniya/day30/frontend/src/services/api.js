const API_BASE = "http://localhost:8000/api";

const STORAGE_KEY = "tf_token";

const readToken = () => {
  return (
    localStorage.getItem(STORAGE_KEY) ||
    sessionStorage.getItem(STORAGE_KEY) ||
    null
  );
};

const saveToken = (token, remember) => {
  if (remember) localStorage.setItem(STORAGE_KEY, token);
  else sessionStorage.setItem(STORAGE_KEY, token);
};

const clearToken = () => {
  localStorage.removeItem(STORAGE_KEY);
  sessionStorage.removeItem(STORAGE_KEY);
};

export const apiService = {
  setToken: (token, remember = true) => saveToken(token, remember),
  getToken: () => readToken(),
  clearToken,
  login: async (empId, password) => {
    // FastAPI endpoints expect simple params (query/form) for these handlers.
    // Use query params so the backend receives emp_id and password as expected.
    const url = new URL(`${API_BASE}/users/login/by-emp`);
    url.searchParams.append("emp_id", empId);
    url.searchParams.append("password", password);
    const response = await fetch(url.toString(), { method: "POST" });

    if (!response.ok) throw new Error("Login failed");
    return response.json();
  },

  getUserById: async (empId, token) => {
    // This endpoint expects a user_id path param. If caller only has empId,
    // prefer using the utils endpoint that returns employee+user info.
    const auth = token || readToken();
    const response = await fetch(`${API_BASE}/users/${empId}`, {
      headers: auth ? { Authorization: `Bearer ${auth}` } : {},
    });
    if (!response.ok) throw new Error("Failed to fetch user");
    return response.json();
  },

  // Get employee and nested user info using employee id (protected)
  getEmployeeWithUser: async (empId, token) => {
    const auth = token || readToken();
    const response = await fetch(`${API_BASE}/utils/employee/${empId}`, {
      headers: auth ? { Authorization: `Bearer ${auth}` } : {},
    });
    if (!response.ok) throw new Error("Failed to fetch employee/user");
    return response.json();
  },

  getTasks: async (token) => {
    const auth = token || readToken();
    const response = await fetch(`${API_BASE}/tasks`, {
      headers: auth ? { Authorization: `Bearer ${auth}` } : {},
    });
    if (!response.ok) throw new Error("Failed to fetch tasks");
    return response.json();
  },

  createTask: async (taskData, token) => {
    const auth = token || readToken();
    const response = await fetch(`${API_BASE}/tasks`, {
      method: "POST",
      headers: {
        ...(auth ? { Authorization: `Bearer ${auth}` } : {}),
        "Content-Type": "application/json",
      },
      body: JSON.stringify(taskData),
    });
    if (!response.ok) throw new Error("Failed to create task");
    return response.json();
  },

  updateTaskStatus: async (taskId, status, token) => {
    const auth = token || readToken();
    const url = `${API_BASE}/tasks/${taskId}/status`;
    const response = await fetch(url, {
      method: "PUT",
      headers: {
        ...(auth ? { Authorization: `Bearer ${auth}` } : {}),
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ status }),
    });
    if (!response.ok) {
      const text = await response.text();
      throw new Error(`Failed to update status: ${text}`);
    }
    return response.json();
  },

  updateTaskPriority: async (taskId, priority, token) => {
    const auth = token || readToken();
    const url = `${API_BASE}/tasks/${taskId}/priority`;
    const response = await fetch(url, {
      method: "PUT",
      headers: {
        ...(auth ? { Authorization: `Bearer ${auth}` } : {}),
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ priority }),
    });
    if (!response.ok) throw new Error("Failed to update priority");
    return response.json();
  },

  getEmployees: async (searchQuery, token) => {
    const auth = token || readToken();
    // build URL without empty ?q= to avoid backend edge-cases
    const url = new URL(`${API_BASE}/employees`);
    if (searchQuery && String(searchQuery).trim() !== "") {
      url.searchParams.append("q", String(searchQuery));
    }

    // debug: log request
    console.log(
      "apiService.getEmployees request:",
      url.toString(),
      "token?",
      !!auth
    );

    const response = await fetch(url.toString(), {
      headers: auth ? { Authorization: `Bearer ${auth}` } : {},
    });

    if (!response.ok) {
      const text = await response.text().catch(() => "<no body>");
      console.error(`getEmployees failed (${response.status}):`, text);
      throw new Error(`Failed to fetch employees: ${response.status} ${text}`);
    }

    return response.json();
  },

  updateEmployee: async (empId, updateData, token) => {
    // Backend expects query params for optional fields on PATCH
    const url = new URL(`${API_BASE}/employees/${empId}`);
    Object.entries(updateData || {}).forEach(([k, v]) => {
      if (v !== undefined && v !== null) url.searchParams.append(k, v);
    });

    const auth = token || readToken();
    const response = await fetch(url.toString(), {
      method: "PATCH",
      headers: auth ? { Authorization: `Bearer ${auth}` } : {},
    });

    if (!response.ok) {
      const text = await response.text();
      throw new Error(`Failed to update employee: ${text}`);
    }
    return response.json();
  },
  createEmployee: async (employeeData, token) => {
    // employeeData: { name, email, department?, title? }
    const url = new URL(`${API_BASE}/employees`);
    Object.entries(employeeData || {}).forEach(([k, v]) => {
      if (v !== undefined && v !== null) url.searchParams.append(k, v);
    });
    const auth = token || readToken();
    const response = await fetch(url.toString(), {
      method: "POST",
      headers: auth ? { Authorization: `Bearer ${auth}` } : {},
    });
    if (!response.ok) {
      const text = await response.text();
      throw new Error(`Failed to create employee: ${text}`);
    }
    return response.json();
  },
};
