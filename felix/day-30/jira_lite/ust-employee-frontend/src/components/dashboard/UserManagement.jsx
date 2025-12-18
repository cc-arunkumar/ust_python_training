import React, { useState, useEffect } from 'react';
import { Shield, Plus, Edit, Trash2, Search, Key, UserCheck, AlertCircle } from 'lucide-react';
import { useAuth } from '../../contexts/AuthContext';
import { api } from '../../services/api';
import { useNavigate } from 'react-router-dom';
import Header from '../layout/Header';
import CreateUserModal from '../modals/CreateUserModal';
import EditUserModal from '../modals/EditUserModal';

const UserManagement = () => {
  const { user, token } = useAuth();
  const navigate = useNavigate();

  const [users, setUsers] = useState([]);
  const [loading, setLoading] = useState(true);
  const [searchTerm, setSearchTerm] = useState('');
  const [showCreateModal, setShowCreateModal] = useState(false);
  const [showEditModal, setShowEditModal] = useState(false);
  const [selectedUser, setSelectedUser] = useState(null);
  const [userName, setUserName] = useState('User');
  const [userRoles, setUserRoles] = useState([]);
  const [currentView, setCurrentView] = useState(null);

  const handleUserNameFetched = (name) => {
    setUserName(name);
  };

  useEffect(() => {
    fetchUserRoles();
  }, []);

  useEffect(() => {
    if (currentView === 'admin') {
      loadUsers();
    } else if (currentView !== null) {
      // User role has been fetched but they're not admin
      setLoading(false);
    }
  }, [currentView]);

  const fetchUserRoles = async () => {
    try {
      const userData = await api.getUserById(token, user.emp_id);
      if (userData && Array.isArray(userData.role)) {
        const roles = userData.role.filter((r) => ['admin', 'manager', 'employee'].includes(r));
        setUserRoles(roles);
        // Only set admin view if user is admin
        const adminView = roles.includes('admin') ? 'admin' : (roles[0] || null);
        setCurrentView(adminView);
      } else {
        setUserRoles([]);
        setCurrentView(null);
        setLoading(false);
      }
    } catch (error) {
      console.error('Error fetching user role:', error);
      setUserRoles([]);
      setCurrentView(null);
      setLoading(false);
    }
  };

  const loadUsers = async () => {
    try {
      setLoading(true);
      const data = await api.getAllUsers(token);
      setUsers(Array.isArray(data) ? data : []);
    } catch (error) {
      console.error('Error loading users:', error);
      setUsers([]);
    } finally {
      setLoading(false);
    }
  };

  const handleEditUser = (userItem) => {
    setSelectedUser(userItem);
    setShowEditModal(true);
  };

  const handleDeleteUser = async (empId) => {
    if (!window.confirm('Are you sure you want to delete this user? This will remove their login access.')) {
      return;
    }
    try {
      await api.deleteUser(token, empId);
      loadUsers();
    } catch (error) {
      console.error('Error deleting user:', error);
      alert('Failed to delete user');
    }
  };

  const getRoleBadgeColor = (roles) => {
    if (roles.includes('admin')) return 'from-red-500 to-pink-500';
    if (roles.includes('manager')) return 'from-blue-500 to-purple-500';
    if (roles.includes('employee')) return 'from-green-500 to-emerald-500';
    return 'from-gray-500 to-gray-600';
  };

  const filteredUsers = users.filter(
    (u) =>
      u.emp_id?.toString().includes(searchTerm) ||
      u.role?.some(r => r.toLowerCase().includes(searchTerm.toLowerCase()))
  );

  if (loading) {
    return (
      <div className="min-h-screen bg-gradient-to-br from-blue-50 via-purple-50 to-pink-50">
        <Header
          currentView={currentView}
          userRoles={userRoles}
          onChangeView={setCurrentView}
          onNavigate={navigate}
          onUserNameFetched={handleUserNameFetched}
        />
        <div className="flex items-center justify-center" style={{ minHeight: 'calc(100vh - 64px)' }}>
          <div className="text-center">
            <div className="relative">
              <div className="animate-spin rounded-full h-16 w-16 border-4 border-gray-200 mx-auto mb-4"></div>
              <div className="animate-spin rounded-full h-16 w-16 border-4 border-blue-600 border-t-transparent absolute top-0 left-1/2 transform -translate-x-1/2"></div>
            </div>
            <p className="text-gray-700 font-semibold text-lg">Loading users...</p>
          </div>
        </div>
      </div>
    );
  }

  if (currentView !== 'admin') {
    return (
      <div className="min-h-screen bg-gradient-to-br from-blue-50 via-purple-50 to-pink-50">
        <Header
          currentView={currentView}
          userRoles={userRoles}
          onChangeView={setCurrentView}
          onNavigate={navigate}
          onUserNameFetched={handleUserNameFetched}
        />
        <div className="flex flex-col items-center justify-center" style={{ minHeight: 'calc(100vh - 64px)' }}>
          <div className="bg-white rounded-3xl shadow-2xl p-12 max-w-md text-center border-2 border-gray-100">
            <div className="w-20 h-20 bg-gradient-to-br from-red-500 to-pink-500 rounded-full mx-auto mb-6 flex items-center justify-center">
              <Shield className="text-white" size={40} />
            </div>
            <p className="text-2xl font-bold mb-3 bg-gradient-to-r from-gray-800 to-gray-600 bg-clip-text text-transparent">
              Admin Access Required
            </p>
            <p className="text-gray-600 mb-6">
              You need admin privileges to access user management.
            </p>
            <button
              onClick={() => navigate('/dashboard')}
              className="px-6 py-3 bg-gradient-to-r from-blue-600 to-purple-600 text-white rounded-xl hover:shadow-xl transition-all transform hover:scale-105 font-semibold"
            >
              Go to Dashboard
            </button>
          </div>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 via-purple-50 to-pink-50">
      <Header
        currentView={currentView}
        userRoles={userRoles}
        onChangeView={setCurrentView}
        onNavigate={navigate}
        onUserNameFetched={handleUserNameFetched}
      />

      <main className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        {/* Page Header */}
        <div className="mb-8">
          <div className="flex items-center gap-3 mb-3">
            <div className="w-12 h-12 bg-gradient-to-br from-red-500 to-pink-600 rounded-2xl flex items-center justify-center shadow-lg">
              <Shield className="text-white" size={24} />
            </div>
            <div>
              <h1 className="text-3xl font-bold bg-gradient-to-r from-red-600 via-pink-600 to-purple-600 bg-clip-text text-transparent">
                User Management
              </h1>
              <p className="text-gray-600 text-sm mt-1">
                Manage user accounts, roles, and access permissions
              </p>
            </div>
          </div>
        </div>

        {/* Stats Cards */}
        <div className="grid grid-cols-1 sm:grid-cols-4 gap-4 mb-8">
          <div className="bg-gradient-to-br from-blue-500 to-blue-600 rounded-2xl p-6 text-white shadow-lg hover:shadow-xl transition-all transform hover:scale-105">
            <div className="flex items-center justify-between">
              <div>
                <p className="text-blue-100 text-sm font-medium mb-1">Total Users</p>
                <p className="text-3xl font-bold">{users.length}</p>
              </div>
              <div className="w-14 h-14 bg-white/20 rounded-xl flex items-center justify-center backdrop-blur-sm">
                <Shield size={28} />
              </div>
            </div>
          </div>

          <div className="bg-gradient-to-br from-red-500 to-pink-600 rounded-2xl p-6 text-white shadow-lg hover:shadow-xl transition-all transform hover:scale-105">
            <div className="flex items-center justify-between">
              <div>
                <p className="text-red-100 text-sm font-medium mb-1">Admins</p>
                <p className="text-3xl font-bold">
                  {users.filter(u => u.role?.includes('admin')).length}
                </p>
              </div>
              <div className="w-14 h-14 bg-white/20 rounded-xl flex items-center justify-center backdrop-blur-sm">
                <Key size={28} />
              </div>
            </div>
          </div>

          <div className="bg-gradient-to-br from-purple-500 to-purple-600 rounded-2xl p-6 text-white shadow-lg hover:shadow-xl transition-all transform hover:scale-105">
            <div className="flex items-center justify-between">
              <div>
                <p className="text-purple-100 text-sm font-medium mb-1">Managers</p>
                <p className="text-3xl font-bold">
                  {users.filter(u => u.role?.includes('manager')).length}
                </p>
              </div>
              <div className="w-14 h-14 bg-white/20 rounded-xl flex items-center justify-center backdrop-blur-sm">
                <UserCheck size={28} />
              </div>
            </div>
          </div>

          <div className="bg-gradient-to-br from-green-500 to-emerald-600 rounded-2xl p-6 text-white shadow-lg hover:shadow-xl transition-all transform hover:scale-105">
            <div className="flex items-center justify-between">
              <div>
                <p className="text-green-100 text-sm font-medium mb-1">Active</p>
                <p className="text-3xl font-bold">
                  {users.filter(u => u.status === 'active').length}
                </p>
              </div>
              <div className="w-14 h-14 bg-white/20 rounded-xl flex items-center justify-center backdrop-blur-sm">
                <UserCheck size={28} />
              </div>
            </div>
          </div>
        </div>

        {/* Search and Actions */}
        <div className="bg-gradient-to-br from-white via-blue-50/30 to-purple-50/30 rounded-3xl shadow-2xl p-6 border-2 border-white backdrop-blur-sm mb-8 relative overflow-hidden">
          <div className="absolute top-0 right-0 w-64 h-64 bg-gradient-to-br from-blue-400/10 to-purple-400/10 rounded-full blur-3xl"></div>
          <div className="absolute bottom-0 left-0 w-64 h-64 bg-gradient-to-tr from-pink-400/10 to-blue-400/10 rounded-full blur-3xl"></div>

          <div className="relative z-10 flex flex-col sm:flex-row gap-4 items-start sm:items-center justify-between">
            <div className="relative flex-1 max-w-md group">
              <div className="absolute inset-0 bg-gradient-to-r from-blue-500 to-purple-500 rounded-2xl opacity-0 group-focus-within:opacity-100 blur transition-opacity duration-300"></div>
              <div className="relative">
                <Search
                  className="absolute left-4 top-1/2 transform -translate-y-1/2 text-gray-400 group-focus-within:text-blue-600 transition-all duration-300 group-focus-within:scale-110"
                  size={20}
                />
                <input
                  type="text"
                  placeholder="Search by user ID or role..."
                  value={searchTerm}
                  onChange={(e) => setSearchTerm(e.target.value)}
                  className="w-full pl-12 pr-4 py-4 border-2 border-gray-200 rounded-2xl focus:ring-4 focus:ring-blue-500/20 focus:border-blue-500 transition-all outline-none bg-white shadow-lg hover:shadow-xl font-medium text-gray-700 placeholder:text-gray-400"
                />
              </div>
            </div>

            <button
              onClick={() => setShowCreateModal(true)}
              className="flex items-center gap-2 px-8 py-4 bg-gradient-to-r from-red-600 via-pink-600 to-purple-600 text-white rounded-2xl hover:shadow-2xl hover:shadow-pink-500/50 transform hover:scale-105 transition-all font-bold relative overflow-hidden group shadow-xl"
            >
              <div className="absolute inset-0 bg-gradient-to-r from-purple-600 via-pink-600 to-red-600 opacity-0 group-hover:opacity-100 transition-opacity duration-300"></div>
              <Plus size={22} className="relative z-10 group-hover:rotate-90 transition-transform duration-300" />
              <span className="relative z-10">Create User</span>
            </button>
          </div>
        </div>

        {/* Alert Box */}
        <div className="bg-gradient-to-r from-amber-50 to-orange-50 border-2 border-amber-200 rounded-2xl p-4 mb-8 flex items-start gap-3">
          <AlertCircle className="text-amber-600 flex-shrink-0 mt-0.5" size={20} />
          <div>
            <p className="text-amber-900 font-semibold text-sm">User vs Employee</p>
            <p className="text-amber-700 text-sm mt-1">
              Users have login credentials and system roles. Employees are organizational records. 
              Create users for staff who need system access.
            </p>
          </div>
        </div>

        {/* Users Table */}
        <div className="bg-white rounded-3xl shadow-2xl border-2 border-gray-100 overflow-hidden">
          <div className="overflow-x-auto">
            <table className="min-w-full divide-y divide-gray-200">
              <thead className="bg-gradient-to-r from-gray-50 to-blue-50/50">
                <tr>
                  <th className="px-6 py-4 text-left text-xs font-bold text-gray-700 uppercase tracking-wider">
                    User ID
                  </th>
                  <th className="px-6 py-4 text-left text-xs font-bold text-gray-700 uppercase tracking-wider">
                    Roles
                  </th>
                  <th className="px-6 py-4 text-left text-xs font-bold text-gray-700 uppercase tracking-wider">
                    Status
                  </th>
                  <th className="px-6 py-4 text-left text-xs font-bold text-gray-700 uppercase tracking-wider">
                    Created
                  </th>
                  <th className="px-6 py-4 text-right text-xs font-bold text-gray-700 uppercase tracking-wider">
                    Actions
                  </th>
                </tr>
              </thead>
              <tbody className="bg-white divide-y divide-gray-100">
                {filteredUsers.length === 0 ? (
                  <tr>
                    <td colSpan={5} className="px-6 py-12 text-center">
                      <div className="flex flex-col items-center gap-3">
                        <div className="w-16 h-16 bg-gray-100 rounded-full flex items-center justify-center">
                          <Shield className="text-gray-400" size={32} />
                        </div>
                        <p className="text-gray-500 font-medium">No users found</p>
                        <p className="text-gray-400 text-sm">Try adjusting your search criteria</p>
                      </div>
                    </td>
                  </tr>
                ) : (
                  filteredUsers.map((userItem) => (
                    <tr
                      key={userItem.emp_id}
                      className="hover:bg-gradient-to-r hover:from-blue-50/50 hover:to-purple-50/50 transition-all duration-150"
                    >
                      <td className="px-6 py-4">
                        <div className="flex items-center gap-2">
                          <div className="w-10 h-10 bg-gradient-to-br from-red-500 to-pink-600 rounded-xl flex items-center justify-center text-white font-bold shadow-lg">
                            <Key size={18} />
                          </div>
                          <span className="text-gray-800 font-bold text-lg">
                            {userItem.emp_id}
                          </span>
                        </div>
                      </td>
                      <td className="px-6 py-4">
                        <div className="flex flex-wrap gap-2">
                          {userItem.role?.map((role, idx) => (
                            <span
                              key={idx}
                              className={`inline-flex items-center px-3 py-1.5 rounded-xl text-xs font-bold shadow-md bg-gradient-to-r ${getRoleBadgeColor([role])} text-white`}
                            >
                              {role}
                            </span>
                          ))}
                        </div>
                      </td>
                      <td className="px-6 py-4">
                        <span
                          className={`inline-flex items-center px-3 py-1.5 rounded-xl text-xs font-bold shadow-sm ${
                            userItem.status === 'inactive'
                              ? 'bg-gradient-to-r from-gray-500 to-gray-600 text-white'
                              : 'bg-gradient-to-r from-green-500 to-emerald-500 text-white'
                          }`}
                        >
                          {userItem.status || 'active'}
                        </span>
                      </td>
                      <td className="px-6 py-4 text-gray-600 text-sm">
                        {userItem.created_at ? new Date(userItem.created_at).toLocaleDateString() : 'N/A'}
                      </td>
                      <td className="px-6 py-4 text-right">
                        <div className="inline-flex items-center gap-2">
                          <button
                            onClick={() => handleEditUser(userItem)}
                            className="p-2 rounded-xl hover:bg-blue-100 text-blue-600 transition-all hover:scale-110 shadow-sm hover:shadow-md"
                            title="Edit User"
                          >
                            <Edit size={18} />
                          </button>
                          <button
                            onClick={() => handleDeleteUser(userItem.emp_id)}
                            className="p-2 rounded-xl hover:bg-red-100 text-red-600 transition-all hover:scale-110 shadow-sm hover:shadow-md"
                            title="Delete User"
                          >
                            <Trash2 size={18} />
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
      </main>

      {showCreateModal && (
        <CreateUserModal
          token={token}
          onClose={() => setShowCreateModal(false)}
          onSuccess={() => {
            setShowCreateModal(false);
            loadUsers();
          }}
        />
      )}

      {showEditModal && selectedUser && (
        <EditUserModal
          token={token}
          user={selectedUser}
          onClose={() => setShowEditModal(false)}
          onSuccess={() => {
            setShowEditModal(false);
            loadUsers();
          }}
        />
      )}
    </div>
  );
};

export default UserManagement;