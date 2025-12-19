// src/pages/DeleteUser.js
import React, { useEffect, useState } from "react";
import axios from "axios";

const DeleteUser = () => {
  const [users, setUsers] = useState([]);
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

  const handleDelete = async (emp_id) => {
    if (window.confirm("Are you sure?")) {
      try {
        await axios.delete(`/api/v1/users/${emp_id}`);
        setSuccess("User deleted");
        setUsers(users.filter((u) => u.emp_id !== emp_id));
      } catch (err) {
        console.error(err);
        setError("Failed to delete user");
      }
    }
  };

  return (
    <div>
      <h2 className="text-xl font-bold mb-4">Delete User</h2>
      {error && <p className="text-red-500">{error}</p>}
      {success && <p className="text-green-500">{success}</p>}
      <ul>
        {users.map((user) => (
          <li key={user.emp_id} className="flex justify-between">
            {user.emp_id} - {user.role}
            <button
              onClick={() => handleDelete(user.emp_id)}
              className="text-red-500"
            >
              Delete
            </button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default DeleteUser;
