import { useState } from 'react';
import { Settings, LogOut, Plus, Edit2, Trash2 } from 'lucide-react';

const AdminDashboard = ({
  user,
  employees,
  tasks,
  token,
  onLogout,
  onError,
  onSwitchRole,
  onCreateEmployee,
  onUpdateEmployee,
  onDeleteEmployee,
  onUpdateTasks,
  onCreateTask,
}) => {
  const [activeTab, setActiveTab] = useState('employees');
  const [showCreateEmployee, setShowCreateEmployee] = useState(false);
  const [showEditEmployee, setShowEditEmployee] = useState(false);
  const [selectedEmployee, setSelectedEmployee] = useState(null);
  const [employeeForm, setEmployeeForm] = useState({
    emp_id: '',
    name: '',
    email: '',
    designation: '',
    mgr_id: '',
  });
  const [loading, setLoading] = useState(false);  // Local loading for actions

  const handleCreateEmployee = async (e) => {
    e.preventDefault();
    setLoading(true);
    try {
      // Assuming api.createEmployee is imported or passed; use it here
      const created = await api.createEmployee(employeeForm, token);  // Import api if needed
      onCreateEmployee(created);
      setShowCreateEmployee(false);
      setEmployeeForm({ emp_id: '', name: '', email: '', designation: '', mgr_id: '' });
    } catch (err) {
      onError(err.message);
    } finally {
      setLoading(false);
    }
  };

  const handleEditEmployee = async (e) => {
    e.preventDefault();
    setLoading(true);
    try {
      const updated = await api.updateEmployee(employeeForm.emp_id, employeeForm, token);
      onUpdateEmployee(updated);
      setShowEditEmployee(false);
      setSelectedEmployee(null);
    } catch (err) {
      onError(err.message);
    } finally {
      setLoading(false);
    }
  };

  const handleDeleteEmployee = async (empId) => {
    if (window.confirm('Are you sure you want to delete this employee?')) {
      setLoading(true);
      try {
        await api.deleteEmployee(empId, token);
        onDeleteEmployee(empId);
      } catch (err) {
        onError(err.message);
      } finally {
        setLoading(false);
      }
    }
  };

  const openEditModal = (employee) => {
    setSelectedEmployee(employee);
    setEmployeeForm({ ...employee, mgr_id: employee.mgr_id || '' });
    setShowEditEmployee(true);
  };

  if (loading) {
    return (
      <div className="min-h-screen bg-gray-50 flex items-center justify-center">
        <div className="text-lg">Loading...</div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-gray-50">
      <header className="bg-white border-b border-gray-200 sticky top-0 z-10">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-4">
          <div className="flex items-center justify-between">
            <div className="flex items-center space-x-3">
              <Settings className="w-8 h-8 text-indigo-600" />
              <div>
                <h1 className="text-2xl font-bold text-gray-900">Admin Dashboard</h1>
                <p className="text-sm text-gray-600">{user?.name}</p>
              </div>
            </div>
            <div className="flex items-center space-x-4">
              <button
                onClick={onSwitchRole}
                className="text-gray-600 hover:text-gray-900"
              >
                Switch Role
              </button>
              <button
                onClick={onLogout}
                className="flex items-center space-x-2 text-gray-600 hover:text-gray-900"
              >
                <LogOut className="w-5 h-5" />
                <span>Logout</span>
              </button>
            </div>
          </div>
        </div>
      </header>
      <main className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        {onError && (  // Use prop for error display
          <div className="bg-red-50 text-red-600 px-4 py-3 rounded-lg text-sm mb-4">{onError}</div>
        )}
        <div className="mb-6 flex items-center justify-between">
          <div className="flex space-x-4">
            <button
              onClick={() => setActiveTab('employees')}
              className={`px-4 py-2 rounded-lg font-medium ${
                activeTab === 'employees'
                  ? 'bg-indigo-600 text-white'
                  : 'bg-white text-gray-700 hover:bg-gray-50'
              }`}
            >
              Employees
            </button>
            <button
              onClick={() => setActiveTab('assign')}
              className={`px-4 py-2 rounded-lg font-medium ${
                activeTab === 'assign'
                  ? 'bg-indigo-600 text-white'
                  : 'bg-white text-gray-700 hover:bg-gray-50'
              }`}
            >
              Assign Employees
            </button>
          </div>
          {activeTab === 'employees' && (
            <button
              onClick={() => setShowCreateEmployee(true)}
              disabled={loading}
              className="bg-indigo-600 text-white px-4 py-2 rounded-lg hover:bg-indigo-700 flex items-center space-x-2 disabled:opacity-50"
            >
              <Plus className="w-5 h-5" />
              <span>Create Employee</span>
            </button>
          )}
        </div>

        {/* Create Employee Modal */}
        {showCreateEmployee && (
          <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center p-4 z-50">
            <div className="bg-white rounded-lg max-w-2xl w-full p-6">
              <h3 className="text-xl font-bold mb-4">Create New Employee</h3>
              <form onSubmit={handleCreateEmployee} className="space-y-4">
                <div className="grid grid-cols-2 gap-4">
                  <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">Employee ID</label>
                    <input
                      type="text"
                      value={employeeForm.emp_id}
                      onChange={(e) => setEmployeeForm({ ...employeeForm, emp_id: e.target.value })}
                      className="w-full px-3 py-2 border border-gray-300 rounded-lg"
                      required
                      disabled={loading}
                    />
                  </div>
                  <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">Name</label>
                    <input
                      type="text"
                      value={employeeForm.name}
                      onChange={(e) => setEmployeeForm({ ...employeeForm, name: e.target.value })}
                      className="w-full px-3 py-2 border border-gray-300 rounded-lg"
                      required
                      disabled={loading}
                    />
                  </div>
                </div>
                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-1">Email</label>
                  <input
                    type="email"
                    value={employeeForm.email}
                    onChange={(e) => setEmployeeForm({ ...employeeForm, email: e.target.value })}
                    className="w-full px-3 py-2 border border-gray-300 rounded-lg"
                    required
                    disabled={loading}
                  />
                </div>
                <div className="grid grid-cols-2 gap-4">
                  <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">Designation</label>
                    <input
                      type="text"
                      value={employeeForm.designation}
                      onChange={(e) => setEmployeeForm({ ...employeeForm, designation: e.target.value })}
                      className="w-full px-3 py-2 border border-gray-300 rounded-lg"
                      required
                      disabled={loading}
                    />
                  </div>
                  <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">Manager ID (Optional)</label>
                    <input
                      type="text"
                      value={employeeForm.mgr_id}
                      onChange={(e) => setEmployeeForm({ ...employeeForm, mgr_id: e.target.value })}
                      className="w-full px-3 py-2 border border-gray-300 rounded-lg"
                      disabled={loading}
                    />
                  </div>
                </div>
                <div className="flex justify-end space-x-3 pt-4">
                  <button
                    type="button"
                    onClick={() => setShowCreateEmployee(false)}
                    className="px-4 py-2 border border-gray-300 rounded-lg hover:bg-gray-50 disabled:opacity-50"
                    disabled={loading}
                  >
                    Cancel
                  </button>
                  <button
                    type="submit"
                    disabled={loading}
                    className="px-4 py-2 bg-indigo-600 text-white rounded-lg hover:bg-indigo-700 disabled:opacity-50"
                  >
                    {loading ? 'Creating...' : 'Create Employee'}
                  </button>
                </div>
              </form>
            </div>
          </div>
        )}

        {/* Edit Employee Modal */}
        {showEditEmployee && (
          <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center p-4 z-50">
            <div className="bg-white rounded-lg max-w-2xl w-full p-6">
              <h3 className="text-xl font-bold mb-4">Edit Employee</h3>
              <form onSubmit={handleEditEmployee} className="space-y-4">
                <div className="grid grid-cols-2 gap-4">
                  <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">Employee ID</label>
                    <input
                      type="text"
                      value={employeeForm.emp_id}
                      className="w-full px-3 py-2 border border-gray-300 rounded-lg bg-gray-100"
                      disabled
                    />
                  </div>
                  <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">Name</label>
                    <input
                      type="text"
                      value={employeeForm.name}
                      onChange={(e) => setEmployeeForm({ ...employeeForm, name: e.target.value })}
                      className="w-full px-3 py-2 border border-gray-300 rounded-lg"
                      required
                      disabled={loading}
                    />
                  </div>
                </div>
                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-1">Email</label>
                  <input
                    type="email"
                    value={employeeForm.email}
                    onChange={(e) => setEmployeeForm({ ...employeeForm, email: e.target.value })}
                    className="w-full px-3 py-2 border border-gray-300 rounded-lg"
                    required
                    disabled={loading}
                  />
                </div>
                <div className="grid grid-cols-2 gap-4">
                  <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">Designation</label>
                    <input
                      type="text"
                      value={employeeForm.designation}
                      onChange={(e) => setEmployeeForm({ ...employeeForm, designation: e.target.value })}
                      className="w-full px-3 py-2 border border-gray-300 rounded-lg"
                      required
                      disabled={loading}
                    />
                  </div>
                  <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">Manager ID</label>
                    <input
                      type="text"
                      value={employeeForm.mgr_id}
                      onChange={(e) => setEmployeeForm({ ...employeeForm, mgr_id: e.target.value })}
                      className="w-full px-3 py-2 border border-gray-300 rounded-lg"
                      disabled={loading}
                    />
                  </div>
                </div>
                <div className="flex justify-end space-x-3 pt-4">
                  <button
                    type="button"
                    onClick={() => {
                      setShowEditEmployee(false);
                      setSelectedEmployee(null);
                    }}
                    className="px-4 py-2 border border-gray-300 rounded-lg hover:bg-gray-50 disabled:opacity-50"
                    disabled={loading}
                  >
                    Cancel
                  </button>
                  <button
                    type="submit"
                    disabled={loading}
                    className="px-4 py-2 bg-indigo-600 text-white rounded-lg hover:bg-indigo-700 disabled:opacity-50"
                  >
                    {loading ? 'Updating...' : 'Update Employee'}
                  </button>
                </div>
              </form>
            </div>
          </div>
        )}

        {/* Employees Tab */}
        {activeTab === 'employees' && (
          <div className="bg-white rounded-lg shadow overflow-hidden">
            <div className="overflow-x-auto">
              <table className="w-full">
                <thead className="bg-gray-50 border-b border-gray-200">
                  <tr>
                    <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Employee ID</th>
                    <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Name</th>
                    <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Email</th>
                    <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Designation</th>
                    <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Manager</th>
                    <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Actions</th>
                  </tr>
                </thead>
                <tbody className="divide-y divide-gray-200">
                  {employees.length === 0 ? (
                    <tr>
                      <td colSpan="6" className="px-6 py-8 text-center text-gray-500">
                        No employees found. Create your first employee to get started.
                      </td>
                    </tr>
                  ) : (
                    employees.map((emp) => (
                      <tr key={emp.emp_id} className="hover:bg-gray-50">
                        <td className="px-6 py-4 text-sm font-medium text-gray-900">{emp.emp_id}</td>
                        <td className="px-6 py-4 text-sm text-gray-900">{emp.name}</td>
                        <td className="px-6 py-4 text-sm text-gray-900">{emp.email}</td>
                        <td className="px-6 py-4 text-sm text-gray-900">{emp.designation}</td>
                        <td className="px-6 py-4 text-sm text-gray-900">{emp.mgr_id || '-'}</td>
                        <td className="px-6 py-4">
                          <div className="flex items-center space-x-2">
                            <button
                              onClick={() => openEditModal(emp)}
                              className="text-indigo-600 hover:text-indigo-900 disabled:opacity-50"
                              disabled={loading}
                            >
                              <Edit2 className="w-4 h-4" />
                            </button>
                            <button
                              onClick={() => handleDeleteEmployee(emp.emp_id)}
                              className="text-red-600 hover:text-red-900 disabled:opacity-50"
                              disabled={loading}
                            >
                              <Trash2 className="w-4 h-4" />
                            </button>
                          </div>
                        </td>
                      </tr>
                    ))
                  )}
                </tbody>
              </table>
            </div>
          </div>
        )}

        {/* Assign Tab (Placeholder) */}
        {activeTab === 'assign' && (
          <div className="bg-white rounded-lg shadow p-6">
            <h3 className="text-lg font-semibold mb-4">Assign Employee to Manager</h3>
            <p className="text-gray-600 mb-4">Select an employee and assign them to a manager</p>
            <div className="text-center text-gray-500 py-8">
              Feature coming soon - Use the employee edit form to update manager assignments
            </div>
          </div>
        )}
      </main>
    </div>
  );
};

// Import api at top if not passed as prop
import { api } from '../../services/api';

export default AdminDashboard;