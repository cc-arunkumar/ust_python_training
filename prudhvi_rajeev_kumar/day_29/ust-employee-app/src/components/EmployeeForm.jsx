import React, { useState, useEffect } from "react";
import {
  getEmployees,
  addEmployee,
  deleteEmployee,
} from "../api/api"; // adjust path if your api.js is directly under src
import "../App.css"; // import the CSS we created

function EmployeeForm() {
  const [employees, setEmployees] = useState([]);
  const [formData, setFormData] = useState({
    name: "",
    designation: "",
    location: "",
    project: "",
  });

  // Load employees on mount
  useEffect(() => {
    fetchEmployees();
  }, []);

  const fetchEmployees = async () => {
    try {
      const res = await getEmployees();
      setEmployees(res.data);
    } catch (err) {
      console.error("Error fetching employees:", err);
    }
  };

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await addEmployee(formData);
      fetchEmployees();
      setFormData({ name: "", designation: "", location: "", project: "" });
    } catch (err) {
      console.error("Error adding employee:", err);
    }
  };

  const handleDelete = async (name) => {
    try {
      await deleteEmployee(name);
      fetchEmployees();
    } catch (err) {
      console.error("Error deleting employee:", err);
    }
  };

  return (
    <div className="App">
      <div className="form-container">
        <h2>Add Employee</h2>
        <form onSubmit={handleSubmit}>
          <input
            name="name"
            placeholder="Name"
            value={formData.name}
            onChange={handleChange}
          />
          <input
            name="designation"
            placeholder="Designation"
            value={formData.designation}
            onChange={handleChange}
          />
          <input
            name="location"
            placeholder="Location"
            value={formData.location}
            onChange={handleChange}
          />
          <input
            name="project"
            placeholder="Project"
            value={formData.project}
            onChange={handleChange}
          />
          <button type="submit">Add</button>
        </form>
      </div>

      <div className="employee-list">
        <h2>Employee List</h2>
        <ul>
          {employees.map((emp, idx) => (
            <li key={idx}>
              <span>
                {emp.name} - {emp.designation} - {emp.location} - {emp.project}
              </span>
              <button onClick={() => handleDelete(emp.name)}>Delete</button>
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
}

export default EmployeeForm;
