import React, { useEffect, useState } from "react";
import { getEmployees, deleteEmployee } from "../services/employeeService";
import 'animate.css';

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
    if (!window.confirm("Are you sure you want to delete this employee?")) return;
    await deleteEmployee(id);
    loadEmployees();
  };

  return (
    <div className="bg-gradient-to-r from-blue-800 to-purple-700 p-8 rounded-lg shadow-lg text-white w-full min-h-screen animate__animated animate__fadeIn">
      <h2 className="text-3xl font-bold mb-6 text-center text-blue-200">
        Employee Directory
      </h2>

      <div className="overflow-x-auto shadow-lg rounded-lg">
        <table className="w-full text-left border-separate table-auto">
          <thead>
            <tr className="bg-gray-700 text-white">
              <th className="p-4">ID</th>
              <th className="p-4">Name</th>
              <th className="p-4">Email</th>
              <th className="p-4">Designation</th>
              {role !== "Employee" && <th className="p-4">Actions</th>}
            </tr>
          </thead>

          <tbody>
            {employees.map((emp) => (
              <tr
                key={emp.id}
                className="border-b border-gray-600 hover:bg-gray-800 transform transition duration-200"
              >
                <td className="p-4">{emp.id}</td>
                <td className="p-4">{emp.name}</td>
                <td className="p-4">{emp.email}</td>
                <td className="p-4">{emp.designation}</td>

                {role !== "Employee" && (
                  <td className="p-4 space-x-4 flex items-center justify-center">
                    <button
                      onClick={() =>
                        (window.location.href = `/admin/employees/create?id=${emp.id}`)
                      }
                      className="bg-blue-500 text-white px-4 py-2 rounded-lg hover:bg-blue-600 transition duration-300"
                    >
                      Edit
                    </button>

                    <button
                      onClick={() => handleDelete(emp.id)}
                      className="bg-red-500 text-white px-4 py-2 rounded-lg hover:bg-red-600 transition duration-300"
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
    </div>
  );
};

export default EmployeeList;
