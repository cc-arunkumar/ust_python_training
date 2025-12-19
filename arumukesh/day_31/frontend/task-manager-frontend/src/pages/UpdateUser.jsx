// src/pages/UpdateUser.js
import React, { useEffect, useState } from "react";
import axios from "axios";

const UpdateUser = () => {
  const [users, setUsers] = useState([]);
  const [selectedUser, setSelectedUser] = useState(null);
  const [formData, setFormData] = useState({ password: "", role: "" });
  const [error, setError] = useState("");
  const [success, setSuccess] = useState("");

  useEffect(() => {
    const fetchUsers = async () => {
      try {
        const response = await axios.get("/api/v1/users");
        setUsers(response.data);
      } catch (err) {
        console.error(err);
        setError("Failed to fetch users");
      }
    };
    fetchUsers();
  }, []);

  const handleSelect = (user) => {
    setSelectedUser(user);
    setFormData({ password: "", role: user.role });
  };

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await axios.put(`/api/v1/users/${selectedUser.emp_id}`, formData);
      setSuccess("User updated successfully");
    } catch (err) {
      console.error(err);
      setError("Failed to update user");
    }
  };

  return (
    <div>
      <h2 className="text-xl font-bold mb-4">Update User</h2>
      {error && <p className="text-red-500">{error}</p>}
      {success && <p className="text-green-500">{success}</p>}
      <div className="mb-4">
        <h3>Select User</h3>
        <ul>
          {users.map((user) => (
            <li key={user.emp_id}>
              <button
                onClick={() => handleSelect(user)}
                className="text-blue-500"
              >
                {user.emp_id} - {user.role}
              </button>
            </li>
          ))}
        </ul>
      </div>
      {selectedUser && (
        <form onSubmit={handleSubmit} className="space-y-4">
          <div>
            <label>New Password (optional)</label>
            <input
              type="password"
              name="password"
              value={formData.password}
              onChange={handleChange}
              className="w-full p-2 border"
            />
          </div>
          <div>
            <label>Role</label>
            <select
              name="role"
              value={formData.role}
              onChange={handleChange}
              className="w-full p-2 border"
            >
              <option value="admin">Admin</option>
              <option value="manager">Manager</option>
              <option value="developer">Developer</option>
            </select>
          </div>
          <button type="submit" className="bg-blue-500 text-white p-2 rounded">
            Update
          </button>
        </form>
      )}
    </div>
  );
};

export default UpdateUser;
