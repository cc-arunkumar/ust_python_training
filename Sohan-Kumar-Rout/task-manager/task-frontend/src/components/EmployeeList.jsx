import React, { useEffect, useState } from "react";
import { getEmployees, deleteEmployee } from "../services/employeeService";

const EmployeeList = () => {
  const [employees, setEmployees] = useState([]);

  const role = localStorage.getItem("role");

  const loadEmployees = async () => {
    const res = await getEmployees();
    setEmployees(res);
  };

  useEffect(() => {
    loadEmployees();
  }, []);

  const handleDelete = async (id) => {
    if (!window.confirm("Delete this employee")) return;
    await deleteEmployee(id);
    loadEmployees();
  };

  return (
    <div className="bg-gray-800 p-6 rounded-xl shadow-lg text-white w-full">
      <h2 className="text-2xl font-bold mb-4 text-blue-400">Employees</h2>

      <table className="w-full text-left border-collapse">
        <thead>
          <tr className="border-b border-gray-600 text-gray-300">
            <th className="p-3">ID</th>
            <th className="p-3">Name</th>
            <th className="p-3">Email</th>
            <th className="p-3">Designation</th>
            {role !== "Employee" && <th className="p-3">Actions</th>}
          </tr>
        </thead>

        <tbody>
          {employees.map((emp) => (
            <tr key={emp.id} className="border-b border-gray-700">
              <td className="p-3">{emp.id}</td>
              <td className="p-3">{emp.name}</td>
              <td className="p-3">{emp.email}</td>
              <td className="p-3">{emp.designation}</td>

              {role !== "Employee" && (
                <td className="p-3 space-x-2">
                  <button
                    onClick={() =>
                      (window.location.href = `/admin/employees/create?id=${emp.id}`)
                    }
                    className="bg-blue-600 px-3 py-1 rounded hover:bg-blue-700"
                  >
                    Edit
                  </button>

                  <button
                    onClick={() => handleDelete(emp.id)}
                    className="bg-red-600 px-3 py-1 rounded hover:bg-red-700"
                  >
                    Delete
                  </button>
                </td>
              )}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default EmployeeList;
