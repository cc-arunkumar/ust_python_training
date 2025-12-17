import { useState } from "react";
import api from "../api/axios";

export default function AdminPage() {
  const [userId, setUserId] = useState("");
  const [password, setPassword] = useState("");
  const [role, setRole] = useState("employee");
  const [status, setStatus] = useState("active");
  const [employeeId, setEmployeeId] = useState("");

  const createUser = async (e) => {
    e.preventDefault();
    try {
      await api.post("/users", {
        user_id: userId,
        password,
        role,
        status,
        employee_id: employeeId ? Number(employeeId) : null,
      });
      alert("User created successfully");
    } catch (err) {
      alert(err.response?.data?.detail || "Error creating user");
    }
  };

  return (
    <div className="container">
      <h2>Admin Panel</h2>
      <form className="form" onSubmit={createUser}>
        <input placeholder="User ID" value={userId} onChange={(e) => setUserId(e.target.value)} />
        <input type="password" placeholder="Password" value={password} onChange={(e) => setPassword(e.target.value)} />
        <select value={role} onChange={(e) => setRole(e.target.value)}>
          <option value="employee">Employee</option>
          <option value="manager">Manager</option>
          <option value="admin">Admin</option>
        </select>
        <select value={status} onChange={(e) => setStatus(e.target.value)}>
          <option value="active">Active</option>
          <option value="inactive">Inactive</option>
        </select>
        <input placeholder="Employee ID" value={employeeId} onChange={(e) => setEmployeeId(e.target.value)} />
        <button type="submit">Create User</button>
      </form>
    </div>
  );
}
