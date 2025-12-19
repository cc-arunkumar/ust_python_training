import React, { useEffect, useState } from "react";
import {
  createEmployee,
  updateEmployee,
  getEmployees,
} from "../services/employeeService";
import 'animate.css';

const EmployeeForm = () => {
  const params = new URLSearchParams(window.location.search);
  const editId = params.get("id");

  const [form, setForm] = useState({
    name: "",
    email: "",
    designation: "",
    manager_id: null,
  });

  const [managers, setManagers] = useState([]); // To store list of managers

  // Load managers when designation is Employee
  const loadManagers = async () => {
    const employees = await getEmployees();
    const managersList = employees.filter((e) => e.designation === "Manager");
    setManagers(managersList);
  };

  // Load employee data for editing
  const loadEmployee = async () => {
    if (!editId) return;
    const employees = await getEmployees();
    const emp = employees.find((e) => e.id == editId);
    if (emp) setForm(emp);
  };

  useEffect(() => {
    loadEmployee();
    if (form.designation === "Employee") {
      loadManagers(); // Load managers if designation is Employee
    }
  }, [form.designation]);

  // Handle form submission
  const handleSubmit = async (e) => {
    e.preventDefault();

    if (editId) {
      await updateEmployee(editId, form);
    } else {
      await createEmployee(form);
    }

    window.location.href = "/admin/employees";
  };

  return (
    <div className="bg-gradient-to-r from-green-50 via-blue-50 to-purple-50 p-8 rounded-lg shadow-xl text-gray-800 w-full min-h-screen animate__animated animate__fadeIn">
      <h2 className="text-3xl font-bold mb-6 text-center text-indigo-600 animate__animated animate__zoomIn">
        {editId ? "Edit Employee" : "Create Employee"}
      </h2>

      <form onSubmit={handleSubmit} className="space-y-6 max-w-xl mx-auto">
        {/* Name field */}
        <input
          className="w-full p-4 bg-gray-200 rounded-lg focus:outline-none focus:ring-2 focus:ring-indigo-400 transition-all duration-300"
          placeholder="Name"
          value={form.name}
          onChange={(e) => setForm({ ...form, name: e.target.value })}
        />

        {/* Email field */}
        <input
          className="w-full p-4 bg-gray-200 rounded-lg focus:outline-none focus:ring-2 focus:ring-indigo-400 transition-all duration-300"
          placeholder="Email"
          value={form.email}
          onChange={(e) => setForm({ ...form, email: e.target.value })}
        />

        {/* Designation field */}
        <select
          className="w-full p-4 bg-gray-200 rounded-lg focus:outline-none focus:ring-2 focus:ring-indigo-400 transition-all duration-300"
          value={form.designation}
          onChange={(e) => setForm({ ...form, designation: e.target.value })}
        >
          <option value="">Select Designation</option>
          <option value="Employee">Employee</option>
          <option value="Manager">Manager</option>
        </select>

        {/* Manager field: Conditional rendering based on the designation */}
        {form.designation === "Employee" && (
          <select
            className="w-full p-4 bg-gray-200 rounded-lg focus:outline-none focus:ring-2 focus:ring-indigo-400 transition-all duration-300"
            value={form.manager_id}
            onChange={(e) => setForm({ ...form, manager_id: e.target.value })}
          >
            <option value="">Select Manager</option>
            {managers.map((manager) => (
              <option key={manager.id} value={manager.id}>
                {manager.name}
              </option>
            ))}
          </select>
        )}

        {/* If designation is not Employee, fade out the manager field */}
        {form.designation !== "Employee" && (
          <div className="w-full p-4 bg-gray-200 rounded-lg opacity-50 cursor-not-allowed">
            <span>Select Manager</span>
          </div>
        )}

        {/* Submit button */}
        <button
          className="w-full bg-gradient-to-r from-indigo-400 to-indigo-600 px-4 py-3 rounded-lg hover:scale-105 transition-all duration-300 text-white"
        >
          {editId ? "Update Employee" : "Create Employee"}
        </button>
      </form>
    </div>
  );
};

export default EmployeeForm;
