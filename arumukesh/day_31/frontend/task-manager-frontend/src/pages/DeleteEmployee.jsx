// src/pages/DeleteEmployee.js
import React, { useEffect, useState } from "react";
import axios from "axios";

const DeleteEmployee = () => {
  const [employees, setEmployees] = useState([]);
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

  const handleDelete = async (emp_id) => {
    if (window.confirm("Are you sure?")) {
      try {
        await axios.delete(`/api/v1/employees/${emp_id}`);
        setSuccess("Employee deleted");
        setEmployees(employees.filter((e) => e.emp_id !== emp_id));
      } catch (err) {
        console.error(err);
        setError("Failed to delete");
      }
    }
  };

  return (
    <div>
      <h2 className="text-xl font-bold mb-4">Delete Employee</h2>
      {error && <p className="text-red-500">{error}</p>}
      {success && <p className="text-green-500">{success}</p>}
      <ul>
        {employees.map((emp) => (
          <li key={emp.emp_id} className="flex justify-between">
            {emp.emp_id} - {emp.name}
            <button
              onClick={() => handleDelete(emp.emp_id)}
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

export default DeleteEmployee;
