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
    if (!window.confirm("Delete this employee?")) return;
    await deleteEmployee(id);
    loadEmployees();
  };

  return (
    <div className="space-y-8 bg-[#F7F6F3] p-6 rounded-xl text-black font-poppins">
      <h2 className="text-3xl font-semibold text-[#5D6A75] mb-6">Employee List</h2>

      <table className="w-full text-left border-collapse shadow-lg">
        <thead>
          <tr className="border-b border-[#E3E9EC]">
            <th className="p-4 text-lg text-[#616F77] font-medium">ID</th>
            <th className="p-4 text-lg text-[#616F77] font-medium">Name</th>
            <th className="p-4 text-lg text-[#616F77] font-medium">Email</th>
            <th className="p-4 text-lg text-[#616F77] font-medium">Designation</th>
            {role !== "Employee" && <th className="p-4 text-lg text-[#616F77] font-medium">Actions</th>}
          </tr>
        </thead>

        <tbody>
          {employees.map((emp) => (
            <tr
              key={emp.id}
              className="border-b border-[#E3E9EC] hover:bg-[#F0F5F1] transition-all duration-300"
            >
              <td className="p-4 text-sm text-[#3C4C56]">{emp.id}</td>
              <td className="p-4 text-sm text-[#3C4C56]">{emp.name}</td>
              <td className="p-4 text-sm text-[#3C4C56]">{emp.email}</td>
              <td className="p-4 text-sm text-[#3C4C56]">{emp.designation}</td>

              {role !== "Employee" && (
                <td className="p-4 space-x-2">
                  <button
                    onClick={() =>
                      (window.location.href = `/admin/employees/create?id=${emp.id}`)
                    }
                    className="bg-[#76C7C0] text-white px-4 py-2 rounded-full hover:bg-[#5BAF9F] transition-all duration-200"
                  >
                    Edit
                  </button>
                  <button
                    onClick={() => handleDelete(emp.id)}
                    className="bg-[#FF6F61] text-white px-4 py-2 rounded-full hover:bg-[#FF4B40] transition-all duration-200"
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
