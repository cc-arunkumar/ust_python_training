import React, { useEffect, useState } from "react";
import {
  createEmployee,
  updateEmployee,
  getEmployees,
} from "../services/employeeService";
import { toast } from "react-toastify";

const EmployeeForm = () => {
  const params = new URLSearchParams(window.location.search);
  const editId = params.get("id");

  const [form, setForm] = useState({
    name: "",
    email: "",
    designation: "",
    manager_id: "",
  });

  const [managers, setManagers] = useState([]);

  // Load managers (filter employees with designation "Manager")
  const loadManagers = async () => {
    try {
      const emps = await getEmployees();
      const mgrs = emps.filter((e) =>
        e.designation?.toLowerCase().includes("manager")
      );
      setManagers(mgrs);
    } catch (err) {
      console.error("Failed to load managers", err);
      toast.error("Failed to load managers!");
    }
  };

  useEffect(() => {
    loadManagers();
  }, []);

  const handleSubmit = async (e) => {
    e.preventDefault();

    const payload = {
      ...form,
      manager_id:
        form.designation.toLowerCase() === "employee"
          ? form.manager_id
          : null, // only send manager_id if designation is Employee
    };

    try {
      if (editId) {
        await updateEmployee(editId, payload);
        toast.success("Employee updated successfully!");
      } else {
        await createEmployee(payload);
        toast.success("Employee created successfully!");
      }
      window.location.href = "/admin/employees";
    } catch (err) {
      console.error("Error saving employee", err);
      toast.error("Failed to save employee!");
    }
  };

  return (
    <div className="bg-gray-200 p-6 rounded-xl text-black w-full">
      <h2 className="text-2xl font-bold mb-4 text-blue-600">
        {editId ? "Edit Employee" : "Create Employee"}
      </h2>

      <form onSubmit={handleSubmit} className="space-y-4 max-w-lg">
        <input
          className="w-full p-3 bg-white rounded border shadow-sm transition-all duration-300 hover:shadow-md"
          placeholder="Name"
          value={form.name}
          onChange={(e) => setForm({ ...form, name: e.target.value })}
          required
        />

        <input
          className="w-full p-3 bg-white rounded border shadow-sm transition-all duration-300 hover:shadow-md"
          placeholder="Email"
          type="email"
          value={form.email}
          onChange={(e) => setForm({ ...form, email: e.target.value })}
          required
        />

        <select
          className="w-full p-3 bg-white rounded border shadow-sm transition-all duration-300 hover:shadow-md"
          value={form.designation}
          onChange={(e) => setForm({ ...form, designation: e.target.value })}
          required
        >
          <option value="">Select Designation</option>
          <option value="Manager">Manager</option>
          <option value="Employee">Employee</option>
        </select>

        {/* Manager dropdown - enabled only if designation is Employee */}
        <select
          className={`w-full p-3 rounded border shadow-sm transition-all duration-300 ${
            form.designation.toLowerCase() === "employee"
              ? "bg-white"
              : "bg-gray-300 cursor-not-allowed"
          }`}
          value={form.manager_id}
          onChange={(e) => setForm({ ...form, manager_id: e.target.value })}
          disabled={form.designation.toLowerCase() !== "employee"}
        >
          <option value="">Assign Manager</option>
          {managers.map((mgr) => (
            <option key={mgr.id} value={mgr.id}>
              {mgr.name}
            </option>
          ))}
        </select>

        <button
          type="submit"
          className="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600 shadow-md transition-all duration-300"
        >
          {editId ? "Update" : "Create"}
        </button>
      </form>
    </div>
  );
};

export default EmployeeForm;
