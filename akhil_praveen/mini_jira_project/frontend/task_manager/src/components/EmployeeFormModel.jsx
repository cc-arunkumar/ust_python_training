import React, { useState, useEffect } from "react";
import { X, User, Mail, Briefcase, UserCheck } from "lucide-react";

function EmployeeFormModal({ employee, employees, onClose, onSave, role }) {
  const [formData, setFormData] = useState({
    emp_name: "",
    email: "",
    designation: "",
    manager_id: null,
  });

  useEffect(() => {
    if (employee) {
      setFormData({
        emp_name: employee.emp_name || "",
        email: employee.email || "",
        designation: employee.designation || "",
        manager_id: employee.manager_id || null,
      });
    }
  }, [employee]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    await onSave(formData);
  };

  return (
    <div className="fixed inset-0 bg-black/50 backdrop-blur-sm flex items-center justify-center z-50 p-4">
      <div className="bg-white rounded-2xl p-8 w-full max-w-lg shadow-2xl">
        {/* Header */}
        <div className="flex items-center justify-between mb-6">
          <div className="flex items-center gap-3">
            <div className="p-3 bg-gradient-to-br from-indigo-500 to-purple-600 rounded-xl shadow-md">
              <User className="text-white" size={24} />
            </div>
            <div>
              <h2 className="text-2xl font-bold text-gray-800">
                {employee ? "Edit Employee" : "Add New Employee"}
              </h2>
              <p className="text-sm text-gray-600">
                {employee
                  ? "Update employee details"
                  : "Enter employee information"}
              </p>
            </div>
          </div>
          <button
            onClick={onClose}
            className="p-2 rounded-xl hover:bg-gray-100 transition-all"
          >
            <X size={24} className="text-gray-600" />
          </button>
        </div>

        <form onSubmit={handleSubmit} className="space-y-5">
          {/* Name */}
          <div>
            <label className="block text-sm font-bold text-gray-700 mb-2 flex items-center gap-2">
              <User size={16} />
              Full Name
              <span className="text-red-500">*</span>
            </label>
            <input
              type="text"
              value={formData.emp_name}
              onChange={(e) =>
                setFormData({ ...formData, emp_name: e.target.value })
              }
              className="w-full px-4 py-3 border-2 border-gray-200 rounded-xl focus:ring-2 focus:ring-indigo-500 focus:outline-none transition-all"
              placeholder="Enter employee name"
              required
            />
          </div>

          {/* Email */}
          <div>
            <label className="block text-sm font-bold text-gray-700 mb-2 flex items-center gap-2">
              <Mail size={16} />
              Email Address
              <span className="text-red-500">*</span>
            </label>
            <input
              type="email"
              value={formData.email}
              onChange={(e) =>
                setFormData({ ...formData, email: e.target.value })
              }
              className="w-full px-4 py-3 border-2 border-gray-200 rounded-xl focus:ring-2 focus:ring-indigo-500 focus:outline-none transition-all"
              placeholder="employee@company.com"
              required
            />
          </div>

          {/* Designation */}
          <div>
            <label className="block text-sm font-bold text-gray-700 mb-2 flex items-center gap-2">
              <Briefcase size={16} />
              Designation
            </label>
            <input
              type="text"
              value={formData.designation}
              onChange={(e) =>
                setFormData({ ...formData, designation: e.target.value })
              }
              className="w-full px-4 py-3 border-2 border-gray-200 rounded-xl focus:ring-2 focus:ring-indigo-500 focus:outline-none transition-all"
              placeholder="e.g., Software Engineer, Manager"
            />
          </div>

          {/* Manager */}
          <div>
            <label className="block text-sm font-bold text-gray-700 mb-2 flex items-center gap-2">
              <UserCheck size={16} />
              Reports To
            </label>
            {/* If current role is MANAGER and we're editing an employee, disallow changing reports-to */}
            {role && role.includes("MANAGER") && employee ? (
              <input
                type="text"
                readOnly
                value={
                  employees.find((e) => e.emp_id === formData.manager_id)
                    ?.emp_name || "No Manager"
                }
                className="w-full px-4 py-3 border-2 border-gray-200 rounded-xl bg-gray-50 text-gray-700 focus:outline-none"
              />
            ) : (
              <select
                value={formData.manager_id || ""}
                onChange={(e) =>
                  setFormData({
                    ...formData,
                    manager_id: e.target.value
                      ? parseInt(e.target.value)
                      : null,
                  })
                }
                className="w-full px-4 py-3 border-2 border-gray-200 rounded-xl focus:ring-2 focus:ring-indigo-500 focus:outline-none bg-white cursor-pointer appearance-none transition-all"
              >
                <option value="">No Manager</option>
                {employees
                  .filter((emp) => !employee || emp.emp_id !== employee.emp_id)
                  .map((emp) => (
                    <option key={emp.emp_id} value={emp.emp_id}>
                      {emp.emp_name}
                    </option>
                  ))}
              </select>
            )}
          </div>

          {/* Action Buttons */}
          <div className="flex gap-3 justify-end pt-6 border-t-2 border-gray-100">
            <button
              type="button"
              onClick={onClose}
              className="px-6 py-3 bg-gray-100 text-gray-700 rounded-xl hover:bg-gray-200 font-semibold transition-all"
            >
              Cancel
            </button>
            <button
              type="submit"
              className="px-6 py-3 bg-gradient-to-r from-indigo-600 to-purple-600 text-white rounded-xl hover:shadow-lg font-semibold transition-all hover:scale-105 active:scale-95"
            >
              {employee ? "Update Employee" : "Create Employee"}
            </button>
          </div>
        </form>
      </div>
    </div>
  );
}

export default EmployeeFormModal;
