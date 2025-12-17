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
        const role = userData.role.find(r => ['admin', 'manager'].includes(r));
        setUserRole(role);
      }
    } catch (error) {
      console.error('Error fetching user role:', error);
    }
  };

  const loadEmployees = async () => {
    try {
      setLoading(true);
      const data = await api.getEmployees(token, user.emp_id);
      setEmployees(Array.isArray(data) ? data : []);
    } catch (error) {
      console.error('Error loading employees:', error);
      setEmployees([]);
    } finally {
      setLoading(false);
    }
  };

  const handleEditEmployee = (employee) => {
    setSelectedEmployee(employee);
    setShowEditModal(true);
  };

  const handleChangeRole = (employee) => {
    setSelectedEmployee(employee);
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

  const filteredEmployees = employees.filter(emp =>
    emp.name?.toLowerCase().includes(searchTerm.toLowerCase()) ||
    emp.email?.toLowerCase().includes(searchTerm.toLowerCase()) ||
    emp.emp_id?.toString().includes(searchTerm)
  );

  if (loading) {
    return (
      <div className="min-h-screen bg-gray-50 flex items-center justify-center">
        <div className="text-center">
          <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-600 mx-auto mb-4"></div>
          <p className="text-gray-600">Loading employees...</p>
        </div>
      </div>
    );
  }

  if (!userRole || !['admin', 'manager'].includes(userRole)) {
    return (
      <div className="min-h-screen bg-gray-50 flex items-center justify-center">
        <div className="text-center">
          <p className="text-red-600 text-lg">Access Denied</p>
          <p className="text-gray-600 mt-2">You don't have permission to view this page.</p>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-gray-50 to-gray-100">
      <Header onNavigate={navigate} />
      <div className="max-w-7xl mx-auto p-6">
        {/* Header */}
        <div className="bg-white rounded-lg shadow-md p-6 mb-6">
          <div className="flex items-center justify-between mb-4">
            <div className="flex items-center gap-3">
              <Users className="text-blue-600" size={32} />
              <div>
                <h1 className="text-2xl font-bold text-gray-800">Employee Management</h1>
                <p className="text-gray-600 text-sm">
                  {userRole === 'admin' ? 'Manage all employees' : 'View and update your team'}
                </p>
              </div>
            </div>
            {userRole === 'admin' && (
              <button
                onClick={() => setShowCreateModal(true)}
                className="flex items-center gap-2 px-6 py-3 bg-gradient-to-r from-blue-600 to-purple-600 text-white rounded-lg hover:shadow-lg transform hover:-translate-y-0.5 transition-all font-semibold"
              >
                <Plus size={20} />
                Add Employee
              </button>
            )}
          </div>

          {/* Search Bar */}
          <div className="relative">
            <Search
              className="absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-400"
              size={20}
            />
            <input
              type="text"
              placeholder="Search by name, email, or ID..."
              value={searchTerm}
              onChange={(e) => setSearchTerm(e.target.value)}
              className="w-full pl-10 pr-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
            />
          </div>
        </div>

        {/* Employee Count */}
        <div className="bg-white rounded-lg shadow-md p-4 mb-6">
          <p className="text-gray-600">
            Total Employees: <span className="font-semibold text-gray-800">{filteredEmployees.length}</span>
          </p>
        </div>

        {/* Employees Table */}
        <div className="bg-white rounded-lg shadow-md overflow-hidden">
          <div className="overflow-x-auto">
            <table className="w-full">
              <thead className="bg-gradient-to-r from-blue-50 to-purple-50">
                <tr>
                  <th className="px-6 py-4 text-left text-xs font-semibold text-gray-700 uppercase tracking-wider">
                    Employee ID
                  </th>
                  <th className="px-6 py-4 text-left text-xs font-semibold text-gray-700 uppercase tracking-wider">
                    Name
                  </th>
                  <th className="px-6 py-4 text-left text-xs font-semibold text-gray-700 uppercase tracking-wider">
                    Email
                  </th>
                  <th className="px-6 py-4 text-left text-xs font-semibold text-gray-700 uppercase tracking-wider">
                    Position
                  </th>
                  <th className="px-6 py-4 text-left text-xs font-semibold text-gray-700 uppercase tracking-wider">
                    Department
                  </th>
                  <th className="px-6 py-4 text-left text-xs font-semibold text-gray-700 uppercase tracking-wider">
                    Status
                  </th>
                  <th className="px-6 py-4 text-right text-xs font-semibold text-gray-700 uppercase tracking-wider">
                    Actions
                  </th>
                </tr>
              </thead>
              <tbody className="divide-y divide-gray-200">
                {filteredEmployees.length === 0 ? (
                  <tr>
                    <td colSpan="7" className="px-6 py-8 text-center text-gray-500">
                      No employees found
                    </td>
                  </tr>
                ) : (
                  filteredEmployees.map((emp) => (
                    <tr key={emp.emp_id} className="hover:bg-gray-50 transition-colors">
                      <td className="px-6 py-4 whitespace-nowrap">
                        <span className="text-sm font-medium text-gray-900">{emp.emp_id}</span>
                      </td>
                      <td className="px-6 py-4 whitespace-nowrap">
                        <span className="text-sm text-gray-900">{emp.name}</span>
                      </td>
                      <td className="px-6 py-4 whitespace-nowrap">
                        <span className="text-sm text-gray-600">{emp.email}</span>
                      </td>
                      <td className="px-6 py-4 whitespace-nowrap">
                        <span className="text-sm text-gray-900">{emp.position || 'N/A'}</span>
                      </td>
                      <td className="px-6 py-4 whitespace-nowrap">
                        <span className="text-sm text-gray-900">{emp.department || 'N/A'}</span>
                      </td>
                      <td className="px-6 py-4 whitespace-nowrap">
                        <span
                          className={`px-3 py-1 inline-flex text-xs leading-5 font-semibold rounded-full ${
                            emp.status === 'active'
                              ? 'bg-green-100 text-green-800'
                              : 'bg-red-100 text-red-800'
                          }`}
                        >
                          {emp.status || 'active'}
                        </span>
                      </td>
                      <td className="px-6 py-4 whitespace-nowrap text-right text-sm font-medium">
                        <div className="flex items-center justify-end gap-2">
                          {userRole === 'admin' && (
                            <button
                              onClick={() => handleChangeRole(emp)}
                              className="p-2 text-purple-600 hover:bg-purple-50 rounded-lg transition-colors"
                              title="Change Role"
                            >
                              <UserCog size={18} />
                            </button>
                          )}
                          <button
                            onClick={() => handleEditEmployee(emp)}
                            className="p-2 text-blue-600 hover:bg-blue-50 rounded-lg transition-colors"
                            title="Edit Employee"
                          >
                            <Edit size={18} />
                          </button>
                          {userRole === 'admin' && (
                            <button
                              onClick={() => handleDeleteEmployee(emp.emp_id)}
                              className="p-2 text-red-600 hover:bg-red-50 rounded-lg transition-colors"
                              title="Delete Employee"
                            >
                              <Trash2 size={18} />
                            </button>
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
      </div>
    

      {/* Modals */}
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
          managerId={user.emp_id}
          employee={selectedEmployee}
          userRole={userRole}
          onClose={() => {
            setShowEditModal(false);
            setSelectedEmployee(null);
          }}
          onSuccess={() => {
            setShowEditModal(false);
            setSelectedEmployee(null);
            loadEmployees();
          }}
        />
      )}

      {showRoleModal && selectedEmployee && (
        <ChangeRoleModal
          token={token}
          employee={selectedEmployee}
          onClose={() => {
            setShowRoleModal(false);
            setSelectedEmployee(null);
          }}
          onSuccess={() => {
            setShowRoleModal(false);
            setSelectedEmployee(null);
            loadEmployees();
          }}
        />
      )}
    </div>
  );
};

export default EmployeeManagement;