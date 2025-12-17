import React, { useState, useEffect } from 'react';
import { Users, Plus, Edit, Trash2, Search, UserCog } from 'lucide-react';
import { useAuth } from '../../contexts/AuthContext';
import { api } from '../../services/api';
import { useNavigate } from 'react-router-dom';
import Header from '../layout/Header';
import CreateEmployeeModal from '../modals/CreateEmployeeModal';
import EditEmployeeModal from '../modals/EditEmployeeModal';
import ChangeRoleModal from '../modals/ChangeRoleModal';

const EmployeeManagement = () => {
  const { user, token } = useAuth();
  const navigate = useNavigate();

  const [employees, setEmployees] = useState([]);
  const [loading, setLoading] = useState(true);
  const [searchTerm, setSearchTerm] = useState('');
  const [showCreateModal, setShowCreateModal] = useState(false);
  const [showEditModal, setShowEditModal] = useState(false);
  const [showRoleModal, setShowRoleModal] = useState(false);
  const [selectedEmployee, setSelectedEmployee] = useState(null);
  const [userRole, setUserRole] = useState(null);

  useEffect(() => {
    fetchUserRole();
  }, []);

  useEffect(() => {
    if (userRole) {
      loadEmployees();
    }
  }, [userRole]);

  const fetchUserRole = async () => {
    try {
      const userData = await api.getUserById(token, user.emp_id);
      if (userData && Array.isArray(userData.role)) {
        // Check if user has admin or manager role
        const role = userData.role.find((r) => ['admin', 'manager'].includes(r));
        setUserRole(role || null);
      }
    } catch (error) {
      console.error('Error fetching user role:', error);
    }
  };

  const loadEmployees = async () => {
  try {
    setLoading(true);

    let data;
    if (userRole === 'admin') {
      // ✅ admin: call /employees/admin
      data = await api.getEmployeesForAdmin(token);
    } else {
      // ✅ manager: existing behavior
      data = await api.getEmployees(token, user.emp_id);
    }

    setEmployees(Array.isArray(data) ? data : []);
  } catch (error) {
    console.error('Error loading employees:', error);
    setEmployees([]);
  } finally {
    setLoading(false);
  }
};


  const handleEditEmployee = (employee) => {
    // Ensure emp_id is present for EditEmployeeModal
    setSelectedEmployee({
      ...employee,
      emp_id: employee.emp_id ?? employee.id,
    });
    setShowEditModal(true);
  };

  const handleChangeRole = (employee) => {
    // Ensure emp_id is present for ChangeRoleModal
    setSelectedEmployee({
      ...employee,
      emp_id: employee.emp_id ?? employee.id,
    });
    setShowRoleModal(true);
  };

  const handleDeleteEmployee = async (empId) => {
    if (!window.confirm('Are you sure you want to delete this employee?')) {
      return;
    }
    try {
      await api.deleteEmployee(token, user.emp_id, empId);
      loadEmployees();
    } catch (error) {
      console.error('Error deleting employee:', error);
      alert('Failed to delete employee');
    }
  };

  const filteredEmployees = employees.filter(
    (emp) =>
      emp.name?.toLowerCase().includes(searchTerm.toLowerCase()) ||
      emp.email?.toLowerCase().includes(searchTerm.toLowerCase()) ||
      emp.emp_id?.toString().includes(searchTerm)
  );

  if (loading) {
    return (
      <div className="min-h-screen flex items-center justify-center">
        <p>Loading employees...</p>
      </div>
    );
  }

  if (!userRole) {
    return (
      <div className="min-h-screen flex flex-col items-center justify-center">
        <p className="text-xl font-semibold mb-2">Access Denied</p>
        <p className="text-gray-600">
          You don't have permission to view this page.
        </p>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-gray-50 to-gray-100">
      <Header onNavigate={navigate} />

      <main className="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        <div className="mb-6 flex flex-col sm:flex-row justify-between items-start sm:items-center gap-4">
          <div>
            <h1 className="text-2xl font-bold text-gray-800 flex items-center gap-2">
              <Users className="text-blue-600" />
              Employee Management
            </h1>
            <p className="text-gray-600 text-sm mt-1">
              {userRole === 'admin'
                ? 'Manage all employees'
                : 'View and update your team'}
            </p>
          </div>

          <div className="flex gap-3">
            <div className="relative">
              <Search className="absolute left-3 top-2.5 text-gray-400" size={18} />
              <input
                type="text"
                placeholder="Search employees..."
                value={searchTerm}
                onChange={(e) => setSearchTerm(e.target.value)}
                className="pl-9 pr-4 py-2 border border-gray-300 rounded-lg text-sm focus:ring-2 focus:ring-blue-500 focus:border-transparent"
              />
            </div>

            {userRole === 'admin' && (
              <button
                onClick={() => setShowCreateModal(true)}
                className="flex items-center gap-2 px-4 py-2 bg-gradient-to-r from-blue-600 to-purple-600 text-white text-sm rounded-lg hover:shadow-lg transition-all"
              >
                <Plus size={18} />
                Add Employee
              </button>
            )}
          </div>
        </div>

        <div className="bg-white rounded-lg shadow-sm border border-gray-200 overflow-hidden">
          <div className="overflow-x-auto">
            <table className="min-w-full divide-y divide-gray-200 text-sm">
              <thead className="bg-gray-50">
                <tr>
                  <th className="px-4 py-3 text-left font-medium text-gray-600">
                    Employee ID
                  </th>
                  <th className="px-4 py-3 text-left font-medium text-gray-600">
                    Name
                  </th>
                  <th className="px-4 py-3 text-left font-medium text-gray-600">
                    Email
                  </th>
                  <th className="px-4 py-3 text-left font-medium text-gray-600">
                    Designation
                  </th>
                  <th className="px-4 py-3 text-left font-medium text-gray-600">
                    Status
                  </th>
                  <th className="px-4 py-3 text-right font-medium text-gray-600">
                    Actions
                  </th>
                </tr>
              </thead>
              <tbody className="bg-white divide-y divide-gray-100">
                {filteredEmployees.length === 0 ? (
                  <tr>
                    <td
                      colSpan={6}
                      className="px-4 py-6 text-center text-gray-500 text-sm"
                    >
                      No employees found
                    </td>
                  </tr>
                ) : (
                  filteredEmployees.map((emp) => (
                    <tr key={emp.id || emp.emp_id}>
                      <td className="px-4 py-3 text-gray-800">
                        {emp.emp_id ?? emp.id}
                      </td>
                      <td className="px-4 py-3 text-gray-800">{emp.name}</td>
                      <td className="px-4 py-3 text-gray-600">{emp.email}</td>
                      <td className="px-4 py-3 text-gray-600">
                        {emp.designation || emp.position || 'N/A'}
                      </td>
                      <td className="px-4 py-3">
                        <span
                          className={`px-2 py-1 rounded-full text-xs font-medium ${
                            emp.status === 'inactive'
                              ? 'bg-red-50 text-red-700'
                              : 'bg-green-50 text-green-700'
                          }`}
                        >
                          {emp.status || 'active'}
                        </span>
                      </td>
                      <td className="px-4 py-3 text-right">
                        <div className="inline-flex items-center gap-2">
                          <button
                            onClick={() => handleEditEmployee(emp)}
                            className="p-1.5 rounded hover:bg-gray-100 text-gray-600"
                            title="Edit"
                          >
                            <Edit size={16} />
                          </button>
                          {userRole === 'admin' && (
                            <>
                              <button
                                onClick={() => handleChangeRole(emp)}
                                className="p-1.5 rounded hover:bg-gray-100 text-purple-600"
                                title="Change Role"
                              >
                                <UserCog size={16} />
                              </button>
                              <button
                                onClick={() => handleDeleteEmployee(emp.emp_id ?? emp.id)}
                                className="p-1.5 rounded hover:bg-red-50 text-red-600"
                                title="Delete"
                              >
                                <Trash2 size={16} />
                              </button>
                            </>
                          )}
                        </div>
                      </td>
                    </tr>
                  ))
                )}
              </tbody>
            </table>
          </div>
        </div>
      </main>

      {showCreateModal && (
        <CreateEmployeeModal
          token={token}
          managerId={user.emp_id}
          onClose={() => setShowCreateModal(false)}
          onSuccess={() => {
            setShowCreateModal(false);
            loadEmployees();
          }}
        />
      )}

      {showEditModal && selectedEmployee && (
        <EditEmployeeModal
          token={token}
          employee={selectedEmployee}
          onClose={() => setShowEditModal(false)}
          onSuccess={() => {
            setShowEditModal(false);
            loadEmployees();
          }}
        />
      )}

      {showRoleModal && selectedEmployee && (
        <ChangeRoleModal
          token={token}
          employee={selectedEmployee}
          onClose={() => setShowRoleModal(false)}
          onSuccess={() => {
            setShowRoleModal(false);
            loadEmployees();
          }}
        />
      )}
    </div>
  );
};

export default EmployeeManagement;
