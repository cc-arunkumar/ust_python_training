// src/pages/CreateEmployee.js
import React, { useState } from "react";
import axios from "axios";

const CreateEmployee = () => {
  const [formData, setFormData] = useState({
    emp_id: "",
    name: "",
    email: "",
    designation: "",
    mgr_id: "",
  });
  const [userData, setUserData] = useState({
    password: "",
    role: "",
  });
  const [error, setError] = useState("");
  const [success, setSuccess] = useState("");

  const handleEmployeeChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleUserChange = (e) => {
    setUserData({ ...userData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      // Create employee
      await axios.post("/api/v1/employees", formData);
      // Automatically create user
      await axios.post("/api/v1/users", {
        emp_id: formData.emp_id,
        password: userData.password,
        role: userData.role,
      });
      setSuccess("Employee and User created successfully");
    } catch (err) {
      console.error(err);
      setError("Failed to create");
    }
  };

  return (
    <div>
      <h2 className="text-xl font-bold mb-4">Create Employee</h2>
      {error && <p className="text-red-500">{error}</p>}
      {success && <p className="text-green-500">{success}</p>}
      <form onSubmit={handleSubmit} className="space-y-4">
        <div>
          <label>Employee ID</label>
          <input
            name="emp_id"
            value={formData.emp_id}
            onChange={handleEmployeeChange}
            className="w-full p-2 border"
            required
          />
        </div>
        <div>
          <label>Name</label>
          <input
            name="name"
            value={formData.name}
            onChange={handleEmployeeChange}
            className="w-full p-2 border"
            required
          />
        </div>
        <div>
          <label>Email</label>
          <input
            type="email"
            name="email"
            value={formData.email}
            onChange={handleEmployeeChange}
            className="w-full p-2 border"
            required
          />
        </div>
        <div>
          <label>Designation</label>
          <input
            name="designation"
            value={formData.designation}
            onChange={handleEmployeeChange}
            className="w-full p-2 border"
            required
          />
        </div>
        <div>
          <label>Manager ID (optional)</label>
          <input
            name="mgr_id"
            value={formData.mgr_id}
            onChange={handleEmployeeChange}
            className="w-full p-2 border"
          />
        </div>
        <hr />
        <h3>User Details (Automatic Creation)</h3>
        <div>
          <label>Password</label>
          <input
            type="password"
            name="password"
            value={userData.password}
            onChange={handleUserChange}
            className="w-full p-2 border"
            required
          />
        </div>
        <div>
          <label>Role</label>
          <select
            name="role"
            value={userData.role}
            onChange={handleUserChange}
            className="w-full p-2 border"
            required
          >
            <option value="">Select</option>
            <option value="admin">Admin</option>
            <option value="manager">Manager</option>
            <option value="developer">Developer</option>
          </select>
        </div>
        <button type="submit" className="bg-blue-500 text-white p-2 rounded">
          Create
        </button>
      </form>
    </div>
  );
};

export default CreateEmployee;
