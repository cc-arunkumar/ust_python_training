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
    if (!window.confirm('Are you sure you want to delete this employee? This action cannot be undone.')) {
      return;
    }

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
      <div className="p-8 text-center">
        <div className="inline-block animate-spin rounded-full h-8 w-8 border-b-2 border-blue-500"></div>
        <p className="mt-2 text-gray-400">Loading employees...</p>
      </div>
    );
  }

  return (
    <div className="p-8">
      <div className="flex justify-between items-center mb-6">
        <div>
          <h1 className="text-3xl font-bold text-white">Employees</h1>
          <p className="text-gray-400 mt-1">Manage your team members</p>
        </div>
        {isAdmin && (
          <button
            onClick={handleAdd}
            className="bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700 transition flex items-center gap-2 shadow-lg"
          >
            <Plus size={20} />
            Add Employee
          </button>
        )}
      </div>

      {error && (
        <div className="bg-red-900 bg-opacity-50 border border-red-700 text-red-200 px-4 py-3 rounded mb-4 flex items-center gap-2">
          <AlertCircle size={20} />
          <span>{error}</span>
        </div>
      )}

      {employees.length === 0 ? (
        <div className="bg-gray-800 rounded-lg shadow-xl border border-gray-700 p-8 text-center">
          <p className="text-gray-400">No employees found</p>
        </div>
      ) : (
        <div className="bg-gray-800 rounded-lg shadow-xl overflow-hidden border border-gray-700">
          <div className="overflow-x-auto">
            <table className="w-full">
              <thead className="bg-gray-900 border-b border-gray-700">
                <tr>
                  <th className="px-6 py-3 text-left text-xs font-medium text-gray-400 uppercase tracking-wider">
                    ID
                  </th>
                  <th className="px-6 py-3 text-left text-xs font-medium text-gray-400 uppercase tracking-wider">
                    Name
                  </th>
                  <th className="px-6 py-3 text-left text-xs font-medium text-gray-400 uppercase tracking-wider">
                    Email
                  </th>
                  <th className="px-6 py-3 text-left text-xs font-medium text-gray-400 uppercase tracking-wider">
                    Designation
                  </th>
                  <th className="px-6 py-3 text-left text-xs font-medium text-gray-400 uppercase tracking-wider">
                    Manager ID
                  </th>
                  {isAdmin && (
                    <th className="px-6 py-3 text-left text-xs font-medium text-gray-400 uppercase tracking-wider">
                      Actions
                    </th>
                  )}
                </tr>
              </thead>
              <tbody className="divide-y divide-gray-700">
                {employees.map((emp) => (
                  <tr key={emp.emp_id} className="hover:bg-gray-750 transition">
                    <td className="px-6 py-4 whitespace-nowrap text-sm font-medium text-white">
                      {emp.emp_id}
                    </td>
                    <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-300">
                      {emp.emp_name}
                    </td>
                    <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-400">
                      {emp.email}
                    </td>
                    <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-400">
                      {emp.designation}
                    </td>
                    <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-400">
                      {emp.manager_id || '-'}
                    </td>
                    {isAdmin && (
                      <td className="px-6 py-4 whitespace-nowrap text-sm">
                        <div className="flex gap-2">
                          <button
                            onClick={() => handleEdit(emp)}
                            className="text-blue-400 hover:text-blue-300 transition p-1"
                            title="Edit employee"
                          >
                            <Edit2 size={18} />
                          </button>
                          <button
                            onClick={() => handleDelete(emp.emp_id)}
                            className="text-red-400 hover:text-red-300 transition p-1"
                            title="Delete employee"
                          >
                            <Trash2 size={18} />
                          </button>
                        </div>
                      </td>
                    )}
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>
      )}

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