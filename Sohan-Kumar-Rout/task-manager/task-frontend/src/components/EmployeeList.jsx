import React, { useEffect, useState } from "react";
import { getEmployees, deleteEmployee } from "../services/employeeService";

const EmployeeList = ({ onEdit }) => {
  const [employees, setEmployees] = useState([]);

  const loadEmployees = async () => {
    try {
      const data = await getEmployees();
      console.log("API returned:", data);
      setEmployees(Array.isArray(data) ? data : []);
    } catch (err) {
      console.error("Error loading employees:", err);
      setEmployees([]);
    }
  };

  useEffect(() => {
    loadEmployees();
  }, []);

  return (
    <div className="bg-[#112240] p-6 rounded-lg text-white mt-6">
      <h2 className="text-2xl font-semibold mb-4">Employee List</h2>

      <table className="w-full border-collapse">
        <thead>
          <tr className="bg-[#1F2A40]">
            <th className="p-3">Name</th>
            <th className="p-3">Email</th>
            <th className="p-3">Designation</th>
            <th className="p-3">Actions</th>
          </tr>
        </thead>

        <tbody>
          {employees.map((emp) => (
            <tr key={emp.id} className="border-b border-[#1F2A40]">
              <td className="p-3">{emp.name}</td>
              <td className="p-3">{emp.email}</td>
              <td className="p-3">{emp.designation}</td>
              <td className="p-3 flex gap-3">
                <button
                  onClick={() => onEdit(emp)}
                  className="bg-blue-600 px-3 py-1 rounded"
                >
                  Edit
                </button>

                <button
                  onClick={async () => {
                    await deleteEmployee(emp.id);
                    loadEmployees();
                  }}
                  className="bg-red-600 px-3 py-1 rounded"
                >
                  Delete
                </button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default EmployeeList;
