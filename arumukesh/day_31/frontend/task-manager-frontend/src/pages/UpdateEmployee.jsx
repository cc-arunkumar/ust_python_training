// src/pages/UpdateEmployee.js
import React, { useEffect, useState } from "react";
import axios from "axios";

const UpdateEmployee = () => {
  const [employees, setEmployees] = useState([]);
  const [selectedEmp, setSelectedEmp] = useState(null);
  const [formData, setFormData] = useState({
    name: "",
    email: "",
    designation: "",
    mgr_id: "",
  });
  const [error, setError] = useState("");
  const [success, setSuccess] = useState("");

  useEffect(() => {
    const fetchEmployees = async () => {
      try {
        const response = await axios.get("/api/v1/employees");
        setEmployees(response.data);
      } catch (err) {
        console.error(err);
        setError("Failed to fetch employees");
      }
    };
    fetchEmployees();
  }, []);

  const handleSelect = (emp) => {
    setSelectedEmp(emp);
    setFormData({
      name: emp.name,
      email: emp.email,
      designation: emp.designation,
      mgr_id: emp.mgr_id || "",
    });
  };

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await axios.put(`/api/v1/employees/${selectedEmp.emp_id}`, formData);
      setSuccess("Employee updated");
    } catch (err) {
      console.error(err);
      setError("Failed to update");
    }
  };

  return (
    <div>
      <h2 className="text-xl font-bold mb-4">Update Employee</h2>
      {error && <p className="text-red-500">{error}</p>}
      {success && <p className="text-green-500">{success}</p>}
      <div className="mb-4">
        <h3>Select Employee</h3>
        <ul>
          {employees.map((emp) => (
            <li key={emp.emp_id}>
              <button
                onClick={() => handleSelect(emp)}
                className="text-blue-500"
              >
                {emp.emp_id} - {emp.name}
              </button>
            </li>
          ))}
        </ul>
      </div>
      {selectedEmp && (
        <form onSubmit={handleSubmit} className="space-y-4">
          <div>
            <label>Name</label>
            <input
              name="name"
              value={formData.name}
              onChange={handleChange}
              className="w-full p-2 border"
            />
          </div>
          <div>
            <label>Email</label>
            <input
              type="email"
              name="email"
              value={formData.email}
              onChange={handleChange}
              className="w-full p-2 border"
            />
          </div>
          <div>
            <label>Designation</label>
            <input
              name="designation"
              value={formData.designation}
              onChange={handleChange}
              className="w-full p-2 border"
            />
          </div>
          <div>
            <label>Manager ID</label>
            <input
              name="mgr_id"
              value={formData.mgr_id}
              onChange={handleChange}
              className="w-full p-2 border"
            />
          </div>
          <button type="submit" className="bg-blue-500 text-white p-2 rounded">
            Update
          </button>
        </form>
      )}
    </div>
  );
};

export default UpdateEmployee;
