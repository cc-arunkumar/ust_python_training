import React, { useState, useEffect } from 'react';
import { Plus, Edit2, Trash2, AlertCircle } from 'lucide-react';
import { useAuth } from '../../context/AuthContext';
import ApiService from '../../services/api';
import EmployeeModal from './EmployeeModal';

const EmployeesPage = () => {
  const [employees, setEmployees] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const [showModal, setShowModal] = useState(false);
  const [editingEmployee, setEditingEmployee] = useState(null);
  const { hasRole } = useAuth();

  const isAdmin = hasRole('ADMIN');

  useEffect(() => {
    fetchEmployees();
  }, []);

  const fetchEmployees = async () => {
    try {
      setError('');
      const data = await ApiService.getEmployees();
      setEmployees(data);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  const handleDelete = async (id) => {
    if (!window.confirm('Are you sure you want to delete this employee?')) return;
    try {
      await ApiService.deleteEmployee(id);
      await fetchEmployees();
    } catch (err) {
      alert(`Failed to delete employee: ${err.message}`);
    }
  };

  const handleEdit = (employee) => {
    setEditingEmployee(employee);
    setShowModal(true);
  };

  const handleAdd = () => {
    setEditingEmployee(null);
    setShowModal(true);
  };

  if (loading) {
    return (
      <div className="flex justify-center items-center h-64">
        <div className="animate-spin h-10 w-10 border-b-2 border-blue-500 rounded-full"></div>
      </div>
    );
  }

  return (
    <div className="p-6 bg-gray-50 min-h-screen">
      {/* Header */}
      <div className="flex flex-col md:flex-row justify-between items-start md:items-center gap-4 mb-6">
        <div>
          <h1 className="text-3xl font-bold text-gray-900">Team Members</h1>
          <p className="text-gray-500 mt-1">Overview of all employees</p>
        </div>
        {isAdmin && (
          <button
            onClick={handleAdd}
            className="bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700 transition flex items-center gap-2 shadow"
          >
            <Plus size={20} />
            Add Employee
          </button>
        )}
      </div>

      {/* Error */}
      {error && (
        <div className="bg-red-100 border border-red-300 text-red-700 px-4 py-3 rounded mb-4 flex items-center gap-2">
          <AlertCircle size={20} />
          <span>{error}</span>
        </div>
      )}

      {/* Employees Grid */}
      {employees.length === 0 ? (
        <div className="text-center py-12 bg-white rounded-lg shadow">
          <p className="text-gray-500">No employees found</p>
        </div>
      ) : (
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
          {employees.map((emp) => (
            <div
              key={emp.emp_id}
              className="bg-white rounded-lg shadow p-4 flex flex-col justify-between hover:shadow-lg transition"
            >
              <div>
                <h2 className="text-lg font-semibold text-gray-900">{emp.emp_name}</h2>
                <p className="text-gray-500 text-sm">{emp.designation}</p>
                <p className="text-gray-400 text-sm mt-1">{emp.email}</p>
                <p className="text-gray-400 text-sm mt-1">Manager ID: {emp.manager_id || '-'}</p>
                <p className="text-gray-400 text-sm mt-1">Employee ID: {emp.emp_id}</p>
              </div>

              {isAdmin && (
                <div className="flex justify-end gap-2 mt-4">
                  <button
                    onClick={() => handleEdit(emp)}
                    className="text-blue-500 hover:text-blue-700 transition"
                  >
                    <Edit2 size={18} />
                  </button>
                  <button
                    onClick={() => handleDelete(emp.emp_id)}
                    className="text-red-500 hover:text-red-700 transition"
                  >
                    <Trash2 size={18} />
                  </button>
                </div>
              )}
            </div>
          ))}
        </div>
      )}

      {/* Employee Modal */}
      {showModal && (
        <EmployeeModal
          employee={editingEmployee}
          onClose={() => setShowModal(false)}
          onSuccess={() => {
            setShowModal(false);
            fetchEmployees();
          }}
        />
      )}
    </div>
  );
};

export default EmployeesPage;
