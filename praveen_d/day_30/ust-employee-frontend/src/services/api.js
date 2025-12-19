const API_BASE_URL = "http://127.0.0.1:8000";

// ================= JWT Decode =================
export const decodeToken = (token) => {
  try {
    const base64Url = token.split(".")[1];
    const base64 = base64Url.replace(/-/g, "+").replace(/_/g, "/");
    return JSON.parse(atob(base64));
  } catch {
    return null;
  }
};

// ================= API SERVICE =================
export const api = {
  // ---------- AUTH ----------
  login: async (emp_id, password) => {
    const res = await fetch(
      `${API_BASE_URL}/auth/login?emp_id=${emp_id}&password=${password}`,
      { method: "POST" }
    );

    if (!res.ok) throw new Error("Login failed");
    return res.json();
  },

  // ---------- TASKS ----------
  getTasks: async (token) => {
    const res = await fetch(`${API_BASE_URL}/tasks/`, {
      headers: { Authorization: `Bearer ${token}` },
    });

    if (!res.ok) throw new Error("Failed to fetch tasks");
    return res.json();
  },

  // ---------- ADD TASK REMARK (with optional file) ----------
  addTaskRemark: async (taskId, remark, file, token) => {
    const formData = new FormData();
    if (remark) formData.append("remark", remark);
    if (file) formData.append("file", file);

    const res = await fetch(`${API_BASE_URL}/tasks/${taskId}/remarks`, {
      method: "POST",
      headers: {
        Authorization: `Bearer ${token}`,
      },
      body: formData,
    });

    if (!res.ok) {
      const text = await res.text();
      throw new Error(text || "Failed to add remark");
    }

    return res.json();
  },

  updateTaskStatus: async (taskId, status, remarks, token) => {
    const res = await fetch(`${API_BASE_URL}/tasks/${taskId}`, {
      method: "PATCH",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${token}`,
      },
      body: JSON.stringify({
        status_: status,
        remarks,
      }),
    });

    if (!res.ok) throw new Error("Failed to update task");
    return res.json();
  },

  // ---------- SAVE REMARKS (SQL) ----------
  saveTaskRemarks: async (taskId, remarks, token) => {
    const res = await fetch(`${API_BASE_URL}/tasks/${taskId}/remarks`, {
      method: "PATCH",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${token}`,
      },
      body: JSON.stringify({ remarks }),
    });

    if (!res.ok) throw new Error("Saving remarks failed");
    return res.json();
  },

  // ---------- FILE UPLOAD (Mongo + Disk) ----------
  uploadTaskFile: async (taskId, file, token) => {
    const formData = new FormData();
    formData.append("file", file);

    const res = await fetch(`${API_BASE_URL}/files/upload`, {
      method: "POST",
      headers: {
        Authorization: `Bearer ${token}`,
      },
      body: formData,
    });

    if (!res.ok) throw new Error("File upload failed");
    return res.json();
  },

  // ---------- EMPLOYEES ----------
  getEmployees: async (token) => {
    const res = await fetch(`${API_BASE_URL}/employees/`, {
      headers: { Authorization: `Bearer ${token}` },
    });

    if (!res.ok) throw new Error("Failed to fetch employees");
    return res.json();
  },

  getEmployee: async (empId, token) => {
    const res = await fetch(`${API_BASE_URL}/employees/${empId}`, {
      headers: { Authorization: `Bearer ${token}` },
    });

    if (!res.ok) throw new Error("Employee not found");
    return res.json();
  },
};
