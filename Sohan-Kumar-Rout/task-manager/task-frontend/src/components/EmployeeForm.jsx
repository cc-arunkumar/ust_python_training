import React, { useEffect, useState } from "react";
import { createEmployee, updateEmployee, getEmployees } from "../services/employeeService";

const EmployeeForm = ({ selectedEmployee, onSuccess }) => {
  const [employee, setEmployee] = useState({
    name: "",
    email: "",
    designation: "",
    managerId: "",
  });

  const [managers, setManagers] = useState([]);

  useEffect(() => {
    loadManagers();

    if (selectedEmployee) {
      setEmployee({
        name: selectedEmployee.name || "",
        email: selectedEmployee.email || "",
        designation: selectedEmployee.designation || "",
        managerId: selectedEmployee.managerId ?? "",
      });
    }
  }, [selectedEmployee]);

  const loadManagers = async () => {
    const res = await getEmployees();
    setManagers(res); // FIXED
  };

  const handleChange = (e) => {
    setEmployee({ ...employee, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (selectedEmployee) {
      await updateEmployee(selectedEmployee.id, employee);
      alert("Employee updated successfully");
    } else {
      await createEmployee(employee);
      alert("Employee created successfully");
    }

    onSuccess();

    setEmployee({
      name: "",
      email: "",
      designation: "",
      managerId: "",
    });
  };

  return (
    <div className="bg-[#1F2635] p-6 rounded-xl shadow-lg text-white max-w-2xl mb-6">
      <h2 className="text-2xl font-bold mb-6 text-blue-400">
        {selectedEmployee ? "Update Employee" : "Create Employee"}
      </h2>

      <form onSubmit={handleSubmit} className="space-y-4">

        {/* Name */}
        <div>
          <label className="block mb-1 text-sm font-medium">Name</label>
          <input
            type="text"
            name="name"
            value={employee.name}
            onChange={handleChange}
            className="w-full p-3 bg-[#1A2230] border border-[#2F3A4D] rounded outline-none"
          />
        </div>

        {/* Email */}
        <div>
          <label className="block mb-1 text-sm font-medium">Email</label>
          <input
            type="email"
            name="email"
            value={employee.email}
            onChange={handleChange}
            className="w-full p-3 bg-[#1A2230] border border-[#2F3A4D] rounded outline-none"
          />
        </div>

        {/* Designation */}
        <div>
          <label className="block mb-1 text-sm font-medium">Designation</label>
          <input
            type="text"
            name="designation"
            value={employee.designation}
            onChange={handleChange}
            className="w-full p-3 bg-[#1A2230] border border-[#2F3A4D] rounded outline-none"
          />
        </div>

        {/* Manager */}
        <div>
          <label className="block mb-1 text-sm font-medium">Manager</label>
          <select
            name="managerId"
            value={employee.managerId}
            onChange={handleChange}
            className="w-full p-3 bg-[#1A2230] border border-[#2F3A4D] rounded outline-none"
          >
            <option value="">Select Manager</option>

            {managers.map((m) => (
              <option key={m.id} value={m.id}>
                {m.id} — {m.name}
              </option>
            ))}
          </select>
        </div>

        <button
          type="submit"
          className="w-full bg-blue-600 py-3 rounded-lg font-semibold hover:bg-blue-700"
        >
          {selectedEmployee ? "Update Employee" : "Create Employee"}
        </button>
      </form>
    </div>
  );
};

export default EmployeeForm;
