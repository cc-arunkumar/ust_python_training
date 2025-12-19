import React, { useState, useEffect } from "react";
import {
  Users,
  Plus,
  Edit,
  Trash2,
  Search,
  UserCog,
  Mail,
  Briefcase,
  Shield,
} from "lucide-react";
import { useAuth } from "../../contexts/AuthContext";
import { api } from "../../services/api";
import { useNavigate } from "react-router-dom";
import Header from "../layout/Header";
import CreateEmployeeModal from "../modals/CreateEmployeeModal";
import EditEmployeeModal from "../modals/EditEmployeeModal";
import ChangeRoleModal from "../modals/ChangeRoleModal";

const EmployeeManagement = () => {
  const { user, token } = useAuth();
  const navigate = useNavigate();

  const [employees, setEmployees] = useState([]);
  const [loading, setLoading] = useState(true);
  const [searchTerm, setSearchTerm] = useState("");
  const [showCreateModal, setShowCreateModal] = useState(false);
  const [showEditModal, setShowEditModal] = useState(false);
  const [showRoleModal, setShowRoleModal] = useState(false);
  const [selectedEmployee, setSelectedEmployee] = useState(null);
  const [userName, setUserName] = useState("User");

  // roles and current view for this page
  const [userRoles, setUserRoles] = useState([]);
  const [currentView, setCurrentView] = useState(null); // 'admin' or 'manager'

  // Callback to receive user name from Header
  const handleUserNameFetched = (name) => {
    setUserName(name);
  };

  useEffect(() => {
    fetchUserRoles();
  }, []);

  useEffect(() => {
    if (currentView) {
      loadEmployees();
    }
  }, [currentView]);

  const fetchUserRoles = async () => {
    try {
      const userData = await api.getUserById(token, user.emp_id);
      if (userData && Array.isArray(userData.role)) {
        const roles = userData.role.filter((r) =>
          ["admin", "manager"].includes(r)
        );
        setUserRoles(roles);
        setCurrentView(roles[0] || null);
      } else {
        setUserRoles([]);
        setCurrentView(null);
      }
    } catch (error) {
      console.error("Error fetching user role:", error);
      setUserRoles([]);
      setCurrentView(null);
    }
  };

  const loadEmployees = async () => {
    try {
      setLoading(true);

      let data;
      if (currentView === "admin") {
        // admin: see all employees
        data = await api.getEmployeesForAdmin(token);
      } else if (currentView === "manager") {
        // manager: see own team
        data = await api.getEmployees(token, user.emp_id);
      } else {
        data = [];
      }

      setEmployees(Array.isArray(data) ? data : []);
    } catch (error) {
      console.error("Error loading employees:", error);
      setEmployees([]);
    } finally {
      setLoading(false);
    }
  };

  const handleEditEmployee = (employee) => {
    setSelectedEmployee({
      ...employee,
      emp_id: employee.emp_id ?? employee.id,
    });
    setShowEditModal(true);
  };

  const handleChangeRole = (employee) => {
    setSelectedEmployee({
      ...employee,
      emp_id: employee.emp_id ?? employee.id,
    });
    setShowRoleModal(true);
  };

  const handleDeleteEmployee = async (empId) => {
    if (!window.confirm("Are you sure you want to delete this employee?")) {
      return;
    }
    try {
      await api.deleteEmployee(token, user.emp_id, empId);
      loadEmployees();
    } catch (error) {
      console.error("Error deleting employee:", error);
      alert("Failed to delete employee");
    }
  };

  const filteredEmployees = employees.filter(
    (emp) =>
      emp.name?.toLowerCase().includes(searchTerm.toLowerCase()) ||
      emp.email?.toLowerCase().includes(searchTerm.toLowerCase()) ||
      emp.emp_id?.toString().includes(searchTerm)
  );

  if (loading && !currentView) {
    return (
      <div className="min-h-screen bg-blue-50 flex items-center justify-center">
        <div className="text-center">
          <div className="relative">
            <div className="animate-spin rounded-full h-16 w-16 border-4 border-gray-200 mx-auto mb-4"></div>
            <div className="animate-spin rounded-full h-16 w-16 border-4 border-blue-600 border-t-transparent absolute top-0 left-1/2 transform -translate-x-1/2"></div>
          </div>
          <p className="text-gray-700 font-semibold text-lg">
            Loading employees...
          </p>
          <p className="text-gray-500 text-sm mt-2">Just a moment</p>
        </div>
      </div>
    );
  }

  if (!currentView) {
    return (
      <div className="min-h-screen bg-blue-50 flex flex-col items-center justify-center">
        <div className="bg-white rounded-3xl shadow-2xl p-12 max-w-md text-center border-2 border-gray-100">
          <div className="w-20 h-20 bg-blue-500 rounded-full mx-auto mb-6 flex items-center justify-center">
            <Shield className="text-white" size={40} />
          </div>
          <p className="text-2xl font-bold mb-3 text-blue-800">Access Denied</p>
          <p className="text-gray-600 mb-6">
            You don't have permission to view this page.
          </p>
          <button
            onClick={() => navigate("/dashboard")}
            className="px-6 py-3 bg-blue-600 text-white rounded-xl hover:bg-blue-700 transition-all transform hover:scale-105 font-semibold"
          >
            Go to Dashboard
          </button>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-blue-50">
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
            <div className="w-12 h-12 bg-blue-600 rounded-2xl flex items-center justify-center shadow-lg">
              <Users className="text-white" size={24} />
            </div>
            <div>
              <h1 className="text-3xl font-bold text-blue-800">
                Employee Management
              </h1>
              <p className="text-gray-600 text-sm mt-1">
                {currentView === "admin"
                  ? "Manage all employees across the organization"
                  : "View and manage your team members"}
              </p>
            </div>
          </div>
        </div>

        {/* Stats Cards */}
        <div className="grid grid-cols-1 sm:grid-cols-3 gap-4 mb-8">
          <div className="bg-blue-600 rounded-2xl p-6 text-white shadow-lg hover:shadow-xl transition-all transform hover:scale-105">
            <div className="flex items-center justify-between">
              <div>
                <p className="text-blue-100 text-sm font-medium mb-1">
                  Total Employees
                </p>
                <p className="text-3xl font-bold">{filteredEmployees.length}</p>
              </div>
              <div className="w-14 h-14 bg-white/20 rounded-xl flex items-center justify-center backdrop-blur-sm">
                <Users size={28} />
              </div>
            </div>
          </div>

          <div className="bg-blue-600 rounded-2xl p-6 text-white shadow-lg hover:shadow-xl transition-all transform hover:scale-105">
            <div className="flex items-center justify-between">
              <div>
                <p className="text-green-100 text-sm font-medium mb-1">
                  Active
                </p>
                <p className="text-3xl font-bold">
                  {
                    filteredEmployees.filter((e) => e.status !== "inactive")
                      .length
                  }
                </p>
              </div>
              <div className="w-14 h-14 bg-white/20 rounded-xl flex items-center justify-center backdrop-blur-sm">
                <Shield size={28} />
              </div>
            </div>
          </div>

          <div className="bg-blue-600 rounded-2xl p-6 text-white shadow-lg hover:shadow-xl transition-all transform hover:scale-105">
            <div className="flex items-center justify-between">
              <div>
                <p className="text-purple-100 text-sm font-medium mb-1">
                  Your Role
                </p>
                <p className="text-2xl font-bold capitalize">{currentView}</p>
              </div>
              <div className="w-14 h-14 bg-white/20 rounded-xl flex items-center justify-center backdrop-blur-sm">
                <UserCog size={28} />
              </div>
            </div>
          </div>
        </div>

        {/* Search and Actions */}
        <div className="bg-white rounded-3xl shadow-2xl p-6 border-2 border-white backdrop-blur-sm mb-8 relative overflow-hidden">
          {/* Decorative elements */}
          <div className="absolute top-0 right-0 w-64 h-64 bg-blue-100 rounded-full blur-3xl"></div>
          <div className="absolute bottom-0 left-0 w-64 h-64 bg-blue-100 rounded-full blur-3xl"></div>

          <div className="relative z-10 flex flex-col sm:flex-row gap-4 items-start sm:items-center justify-between">
            <div className="relative flex-1 max-w-md group">
              <div className="absolute inset-0 bg-blue-100 rounded-2xl opacity-0 group-focus-within:opacity-100 blur transition-opacity duration-300"></div>
              <div className="relative">
                <Search
                  className="absolute left-4 top-1/2 transform -translate-y-1/2 text-gray-400 group-focus-within:text-blue-600 transition-all duration-300 group-focus-within:scale-110"
                  size={20}
                />
                <input
                  type="text"
                  placeholder="Search by name, email, or ID..."
                  value={searchTerm}
                  onChange={(e) => setSearchTerm(e.target.value)}
                  className="w-full pl-12 pr-4 py-4 border-2 border-gray-200 rounded-2xl focus:ring-4 focus:ring-blue-500/20 focus:border-blue-500 transition-all outline-none bg-white shadow-lg hover:shadow-xl font-medium text-gray-700 placeholder:text-gray-400"
                />
              </div>
            </div>

            {currentView === "admin" && (
              <button
                onClick={() => setShowCreateModal(true)}
                className="flex items-center gap-2 px-5 py-2.5 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition-colors font-semibold shadow-md"
              >
                <Plus size={20} />
                <span>Add Employee</span>
              </button>
            )}
          </div>
        </div>

        {/* Employee Table */}
        <div className="bg-white rounded-3xl shadow-2xl border-2 border-gray-100 overflow-hidden">
          <div className="overflow-x-auto">
            <table className="min-w-full divide-y divide-gray-200">
              <thead className="bg-gray-50">
                <tr>
                  <th className="px-6 py-4 text-left text-xs font-bold text-gray-700 uppercase tracking-wider">
                    Employee ID
                  </th>
                  <th className="px-6 py-4 text-left text-xs font-bold text-gray-700 uppercase tracking-wider">
                    Name
                  </th>
                  <th className="px-6 py-4 text-left text-xs font-bold text-gray-700 uppercase tracking-wider">
                    Email
                  </th>
                  <th className="px-6 py-4 text-left text-xs font-bold text-gray-700 uppercase tracking-wider">
                    Designation
                  </th>
                  <th className="px-6 py-4 text-left text-xs font-bold text-gray-700 uppercase tracking-wider">
                    Status
                  </th>
                  <th className="px-6 py-4 text-right text-xs font-bold text-gray-700 uppercase tracking-wider">
                    Actions
                  </th>
                </tr>
              </thead>
              <tbody className="bg-white divide-y divide-gray-100">
                {filteredEmployees.length === 0 ? (
                  <tr>
                    <td colSpan={6} className="px-6 py-12 text-center">
                      <div className="flex flex-col items-center gap-3">
                        <div className="w-16 h-16 bg-gray-100 rounded-full flex items-center justify-center">
                          <Users className="text-gray-400" size={32} />
                        </div>
                        <p className="text-gray-500 font-medium">
                          No employees found
                        </p>
                        <p className="text-gray-400 text-sm">
                          Try adjusting your search criteria
                        </p>
                      </div>
                    </td>
                  </tr>
                ) : (
                  filteredEmployees.map((emp, index) => (
                    <tr
                      key={emp.id || emp.emp_id}
                      className="hover:bg-blue-50 transition-all duration-150"
                    >
                      <td className="px-6 py-4">
                        <div className="flex items-center gap-2">
                          <div className="w-8 h-8 bg-blue-600 rounded-lg flex items-center justify-center text-white text-xs font-bold">
                            {(emp.emp_id ?? emp.id).toString().slice(-2)}
                          </div>
                          <span className="text-gray-800 font-semibold">
                            {emp.emp_id ?? emp.id}
                          </span>
                        </div>
                      </td>
                      <td className="px-6 py-4">
                        <div className="flex items-center gap-3">
                          <div className="w-10 h-10 bg-blue-500 rounded-xl flex items-center justify-center text-white font-bold shadow-lg">
                            {emp.name?.charAt(0).toUpperCase()}
                          </div>
                          <span className="text-gray-800 font-semibold">
                            {emp.name}
                          </span>
                        </div>
                      </td>
                      <td className="px-6 py-4">
                        <div className="flex items-center gap-2 text-gray-600">
                          <Mail size={14} className="text-gray-400" />
                          <span>{emp.email}</span>
                        </div>
                      </td>
                      <td className="px-6 py-4">
                        <div className="flex items-center gap-2 text-gray-600">
                          <Briefcase size={14} className="text-gray-400" />
                          <span>
                            {emp.designation || emp.position || "N/A"}
                          </span>
                        </div>
                      </td>
                      <td className="px-6 py-4">
                        <span className="inline-flex items-center px-3 py-1.5 rounded-xl text-xs font-bold shadow-sm bg-blue-500 text-white">
                          {emp.status || "active"}
                        </span>
                      </td>
                      <td className="px-6 py-4 text-right">
                        <div className="inline-flex items-center gap-2">
                          <button
                            onClick={() => handleEditEmployee(emp)}
                            className="p-2 rounded-xl hover:bg-blue-100 text-blue-600 transition-all hover:scale-110 shadow-sm hover:shadow-md"
                            title="Edit"
                          >
                            <Edit size={18} />
                          </button>
                          {currentView === "admin" && (
                            <>
                              <button
                                onClick={() => handleChangeRole(emp)}
                                className="p-2 rounded-xl hover:bg-blue-100 text-blue-600 transition-all hover:scale-110 shadow-sm hover:shadow-md"
                                title="Change Role"
                              >
                                <UserCog size={18} />
                              </button>
                              <button
                                onClick={() =>
                                  handleDeleteEmployee(emp.emp_id ?? emp.id)
                                }
                                className="p-2 rounded-xl hover:bg-blue-100 text-blue-600 transition-all hover:scale-110 shadow-sm hover:shadow-md"
                                title="Delete"
                              >
                                <Trash2 size={18} />
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
