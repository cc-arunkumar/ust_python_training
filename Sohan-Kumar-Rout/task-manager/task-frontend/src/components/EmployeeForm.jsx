import React, { useEffect, useState } from "react";
import {
  createEmployee,
  updateEmployee,
  getEmployees,
} from "../services/employeeService";

const EmployeeForm = () => {
  const params = new URLSearchParams(window.location.search);
  const editId = params.get("id");

  const [form, setForm] = useState({
    name: "",
    email: "",
    designation: "",
    manager_id: null,
  });

  const loadEmployee = async () => {
    if (!editId) return;
    const employees = await getEmployees();
    const emp = employees.find((e) => e.id == editId);
    if (emp) setForm(emp);
  };

  useEffect(() => {
    loadEmployee();
  }, []);

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
    <div className="bg-gray-800 p-6 rounded-xl text-white w-full">
      <h2 className="text-2xl font-bold mb-4 text-blue-400">
        {editId ? "Edit Employee" : "Create Employee"}
      </h2>

      <form onSubmit={handleSubmit} className="space-y-4">
        <input
          className="w-full p-3 bg-gray-700 rounded"
          placeholder="Name"
          value={form.name}
          onChange={(e) => setForm({ ...form, name: e.target.value })}
        />

        <input
          className="w-full p-3 bg-gray-700 rounded"
          placeholder="Email"
          value={form.email}
          onChange={(e) => setForm({ ...form, email: e.target.value })}
        />

        <input
          className="w-full p-3 bg-gray-700 rounded"
          placeholder="Designation"
          value={form.designation}
          onChange={(e) => setForm({ ...form, designation: e.target.value })}
        />

        <button className="bg-blue-600 px-4 py-2 rounded hover:bg-blue-700">
          {editId ? "Update" : "Create"}
        </button>
      </form>
    </div>
  );
};

export default EmployeeForm;
