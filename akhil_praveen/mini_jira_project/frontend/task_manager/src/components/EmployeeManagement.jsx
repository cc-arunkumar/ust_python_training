import React, { useState, useMemo } from "react";
import {
  Plus,
  Edit2,
  Trash2,
  Users,
  Mail,
  Briefcase,
  UserCheck,
} from "lucide-react";
import EmployeeFormModal from "./EmployeeFormModel";
import api from "../api/api";
import { publish } from "../utils/events";

function EmployeeManagement({ employees, onRefresh, role, currentEmpId }) {
  const [showForm, setShowForm] = useState(false);
  const [editingEmployee, setEditingEmployee] = useState(null);

  // For admins show all employees. For managers show only direct reports.
  const visibleEmployees = useMemo(() => {
    if (!role) return employees;
    if (role.includes("ADMIN")) return employees;
    if (role.includes("MANAGER")) {
      return employees.filter((e) => e.manager_id === currentEmpId);
    }
    return employees;
  }, [employees, role, currentEmpId]);

  const handleEdit = (emp) => {
    setEditingEmployee(emp);
    setShowForm(true);
  };

  const handleStatusChange = async (empId, newStatus) => {
    try {
      await api.updateEmployee(empId, { status: newStatus });
      onRefresh();
      // notify other in-app components that employees changed
      try {
        publish("app:updated", { resource: "employees", id: empId });
      } catch (e) {}
    } catch (err) {
      alert(err.message);
    }
  };

  const handleSave = async (formData) => {
    try {
      if (editingEmployee) {
        await api.updateEmployee(editingEmployee.emp_id, formData);
      } else {
        await api.createEmployee(formData);
      }
      setShowForm(false);
      setEditingEmployee(null);
      onRefresh();
      try {
        publish("app:updated", { resource: "employees" });
      } catch (e) {}
    } catch (err) {
      alert(err.message);
    }
  };

  const handleCloseForm = () => {
    setShowForm(false);
    setEditingEmployee(null);
  };

  return (
    <div className="p-6">
      {/* Header */}
      <div className="flex justify-between items-center mb-6 bg-white rounded-2xl p-5 shadow-sm border border-gray-100">
        <div className="flex items-center gap-3">
          <div className="p-3 bg-gradient-to-br from-indigo-500 to-purple-600 rounded-xl shadow-md">
            <Users className="text-white" size={24} />
          </div>
          <div>
            <h2 className="text-2xl font-bold text-gray-800">
              Employee Management
            </h2>
            <p className="text-sm text-gray-600">Manage your team members</p>
          </div>
        </div>
        {role && role.includes("ADMIN") ? (
          <button
            onClick={() => setShowForm(true)}
            className="bg-gradient-to-r from-indigo-600 to-purple-600 text-white px-5 py-3 rounded-xl flex items-center gap-2 hover:shadow-lg hover:scale-105 active:scale-95 transition-all font-semibold"
          >
            <Plus size={20} />
            Add Employee
          </button>
        ) : (
          <div className="text-sm text-gray-600">Showing your team</div>
        )}
      </div>

      {/* Employee Grid */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-5">
        {visibleEmployees.map((emp) => {
          const manager = employees.find((e) => e.emp_id === emp.manager_id);

          return (
            <div
              key={emp.emp_id}
              className="bg-white rounded-2xl p-6 shadow-md hover:shadow-xl transition-all border border-gray-100 group hover:scale-105"
            >
              {/* Employee Avatar & ID */}
              <div className="flex items-start justify-between mb-4">
                <div className="flex items-center gap-3">
                  <div className="w-12 h-12 bg-gradient-to-br from-indigo-500 to-purple-600 rounded-full flex items-center justify-center text-white font-bold text-lg shadow-md">
                    {emp.emp_name.charAt(0).toUpperCase()}
                  </div>
                  <div>
                    <h3 className="font-bold text-gray-800 text-lg">
                      {emp.emp_name}
                    </h3>
                    <span className="text-xs text-gray-500 font-medium">
                      ID: {emp.emp_id}
                    </span>
                  </div>
                </div>

                {/* Action Buttons */}
                <div className="flex gap-1 opacity-0 group-hover:opacity-100 transition-opacity items-center">
                  <button
                    onClick={() => handleEdit(emp)}
                    className="p-2 rounded-lg text-blue-600 hover:bg-blue-50 transition-colors"
                    title="Edit"
                  >
                    <Edit2 size={18} />
                  </button>
                  {/* Admins can change status via dropdown instead of deleting */}
                  {role && role.includes("ADMIN") && (
                    <select
                      value={emp.status || "ACTIVE"}
                      onChange={(e) =>
                        handleStatusChange(emp.emp_id, e.target.value)
                      }
                      className="p-2 rounded-lg border-gray-200 bg-white text-sm"
                      title="Change status"
                    >
                      <option value="ACTIVE">Active</option>
                      <option value="INACTIVE">InActive</option>
                    </select>
                  )}
                </div>
              </div>

              {/* Employee Details */}
              <div className="space-y-3">
                <div className="flex items-center gap-2 text-sm">
                  <Mail size={16} className="text-gray-400" />
                  <span className="text-gray-700">{emp.email}</span>
                </div>

                {emp.designation && (
                  <div className="flex items-center gap-2 text-sm">
                    <Briefcase size={16} className="text-gray-400" />
                    <span className="text-gray-700 font-medium">
                      {emp.designation}
                    </span>
                  </div>
                )}

                {/* Status badge */}
                <div className="mt-2">
                  <span
                    className={`inline-block px-2 py-1 text-xs rounded-full font-medium ${
                      (emp.status || "ACTIVE") === "ACTIVE"
                        ? "bg-green-100 text-green-800"
                        : "bg-red-100 text-red-600"
                    }`}
                  >
                    {(emp.status || "ACTIVE").toUpperCase()}
                  </span>
                </div>

                {manager && (
                  <div className="flex items-center gap-2 text-sm">
                    <UserCheck size={16} className="text-gray-400" />
                    <span className="text-gray-600">
                      Reports to:{" "}
                      <span className="font-medium text-gray-800">
                        {manager.emp_name}
                      </span>
                    </span>
                  </div>
                )}

                {!manager && (
                  <div className="flex items-center gap-2 text-sm text-gray-400">
                    <UserCheck size={16} />
                    <span>No manager assigned</span>
                  </div>
                )}
              </div>
            </div>
          );
        })}
      </div>

      {/* Empty State */}
      {visibleEmployees.length === 0 && (
        <div className="text-center py-16 bg-white rounded-2xl border-2 border-dashed border-gray-200">
          <Users size={48} className="mx-auto text-gray-300 mb-4" />
          <h3 className="text-xl font-bold text-gray-600 mb-2">
            No Employees Yet
          </h3>
          <p className="text-gray-500 mb-4">
            Start by adding your first team member
          </p>
          {role && role.includes("ADMIN") ? (
            <button
              onClick={() => setShowForm(true)}
              className="bg-gradient-to-r from-indigo-600 to-purple-600 text-white px-5 py-2 rounded-lg inline-flex items-center gap-2 hover:shadow-lg transition-all"
            >
              <Plus size={18} />
              Add First Employee
            </button>
          ) : (
            <div className="text-sm text-gray-500">No team members to show</div>
          )}
        </div>
      )}

      {showForm && (
        <EmployeeFormModal
          employee={editingEmployee}
          employees={employees}
          onClose={handleCloseForm}
          onSave={handleSave}
          role={role}
          currentEmpId={currentEmpId}
        />
      )}
    </div>
  );
}

export default EmployeeManagement;
