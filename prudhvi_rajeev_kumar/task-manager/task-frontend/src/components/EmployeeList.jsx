import React, { useEffect, useState } from "react";
import { getEmployees, deleteEmployee } from "../services/employeeService";
import 'animate.css';
import { toast, ToastContainer } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';

const EmployeeList = () => {
  const [employees, setEmployees] = useState([]);
  const [loading, setLoading] = useState(false);
  const [err, setErr] = useState('');
  const role = localStorage.getItem("role");

  const loadEmployees = async () => {
    setLoading(true);
    setErr('');
    try {
      const res = await getEmployees();
      // getEmployees usually returns an array; handle if service returns { data }
      const data = Array.isArray(res) ? res : (res?.data || []);
      setEmployees(data);
    } catch (error) {
      console.error('Failed to load employees', error);
      setErr('Failed to load employees. Make sure you are logged in and have permission.');
      setEmployees([]);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    loadEmployees();
  }, []);

  const handleDelete = async (id) => {
    if (!window.confirm("Are you sure you want to delete this employee?")) return;
    try {
      await deleteEmployee(id);
      toast.success('Employee deleted');
      loadEmployees();
    } catch (err) {
      toast.error('Failed to delete employee');
    }
  };

  return (
    <div className="bg-gradient-to-r from-green-50 via-blue-50 to-purple-50 p-8 rounded-xl shadow-lg text-gray-800 w-full min-h-screen animate__animated animate__fadeIn">
      <h2 className="text-4xl font-semibold mb-6 text-center text-indigo-600 animate__animated animate__zoomIn">
        Employee Directory
      </h2>

      <div className="overflow-x-auto shadow-2xl rounded-lg">
        {loading && <div className="p-4 text-sm text-gray-500">Loading employees...</div>}
        {err && <div className="p-4 text-sm text-red-500">{err}</div>}
        <table className="w-full text-left border-separate table-auto">
          <thead>
            <tr className="bg-gradient-to-r from-teal-100 to-teal-300 text-gray-800">
              <th className="p-4 text-lg font-medium">ID</th>
              <th className="p-4 text-lg font-medium">Name</th>
              <th className="p-4 text-lg font-medium">Email</th>
              <th className="p-4 text-lg font-medium">Designation</th>
              {role === "Admin" && <th className="p-4 text-lg font-medium">Actions</th>}
            </tr>
          </thead>

          <tbody>
            {employees.length === 0 && !loading && !err && (
              <tr>
                <td colSpan={role === 'Admin' ? 5 : 4} className="p-6 text-center text-gray-500">No employees found.</td>
              </tr>
            )}

            {employees.map((emp) => (
              <tr
                key={emp.id}
                className="border-b border-gray-300 hover:bg-gradient-to-r from-gray-100 to-gray-200 transform transition duration-200 ease-in-out"
              >
                <td className="p-4">{emp.id}</td>
                <td className="p-4">{emp.name}</td>
                <td className="p-4">{emp.email}</td>
                <td className="p-4">{emp.designation}</td>

                {role === "Admin" && (
                  <td className="p-4 space-x-4 flex items-center justify-center">
                    <button
                      onClick={() =>
                        (window.location.href = `/admin/employees/create?id=${emp.id}`)
                      }
                      className="bg-gradient-to-r from-indigo-400 to-indigo-600 text-white px-6 py-2 rounded-lg hover:scale-105 transition duration-300"
                    >
                      Edit
                    </button>

                    <button
                      onClick={() => handleDelete(emp.id)}
                      className="bg-gradient-to-r from-red-400 to-red-600 text-white px-6 py-2 rounded-lg hover:scale-105 transition duration-300"
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
      <ToastContainer position="top-right" autoClose={3000} hideProgressBar newestOnTop closeOnClick rtl={false} pauseOnFocusLoss draggable pauseOnHover />
    </div>
  );
};

export default EmployeeList;
