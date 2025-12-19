import { useState, useMemo } from "react";
import {
  Settings,
  LogOut,
  Plus,
  Edit2,
  Trash2,
  Users,
  AlertCircle,
  UserCheck,
} from "lucide-react";
import { api } from "../../services/api";
import TaskCard from "../ui/TaskCard";
import {
  PerformancePieChart,
  EmployeePerformanceBarChart,
} from "../ui/PerformanceChart";

const STATUS_ORDER = ["TO_DO", "IN_PROGRESS", "REVIEW", "DONE"];

const STATUS_META = {
  TO_DO: { label: "To Do", bg: "bg-blue-50", ring: "ring-blue-300" },
  IN_PROGRESS: {
    label: "In Progress",
    bg: "bg-amber-50",
    ring: "ring-amber-300",
  },
  REVIEW: { label: "Review", bg: "bg-purple-50", ring: "ring-purple-300" },
  DONE: { label: "Done", bg: "bg-emerald-50", ring: "ring-emerald-300" },
};

// View-only column (no droppable)
const TaskColumn = ({ status, count, children }) => {
  const meta = STATUS_META[status];

  return (
    <div className="flex flex-col">
      <div className="flex justify-between mb-2 px-1">
        <h3 className="font-semibold text-gray-700">{meta.label}</h3>
        <span className="text-xs bg-white px-2 py-0.5 rounded-full shadow">
          {count}
        </span>
      </div>
      <div
        className={`min-h-[420px] p-4 rounded-2xl border transition
          ${meta.bg}`}
      >
        <div className="space-y-3">{children}</div>
      </div>
    </div>
  );
};

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
  error,
}) => {
  const [activeTab, setActiveTab] = useState("employees");
  const [viewMode, setViewMode] = useState("KANBAN"); // For tasks tab
  const [showCreateEmployee, setShowCreateEmployee] = useState(false);
  const [showEditEmployee, setShowEditEmployee] = useState(false);
  const [showCreateTask, setShowCreateTask] = useState(false);
  const [showAssignEmployee, setShowAssignEmployee] = useState(false);
  const [selectedEmployee, setSelectedEmployee] = useState(null);
  const [employeeForm, setEmployeeForm] = useState({
    emp_id: "",
    name: "",
    email: "",
    designation: "",
    mgr_id: "",
  });
  const [taskForm, setTaskForm] = useState({
    task_id: "",
    name: "",
    description: "",
    assigned_to: "",
    priority: "MEDIUM",
    expected_closure: "",
  });
  const [assignForm, setAssignForm] = useState({
    employee_id: "",
    manager_id: "",
  });
  const [loading, setLoading] = useState(false);

  // Admin's tasks: Show ALL tasks for full oversight (updated to populate views)
  const adminTasks = tasks;

  const tasksByStatus = {
    TO_DO: adminTasks.filter((t) => t.status === "TO_DO"),
    IN_PROGRESS: adminTasks.filter((t) => t.status === "IN_PROGRESS"),
    REVIEW: adminTasks.filter((t) => t.status === "REVIEW"),
    DONE: adminTasks.filter((t) => t.status === "DONE"),
  };

  const sortedTasksByDate = useMemo(() => {
    return [...adminTasks].sort((a, b) => {
      const aDate = new Date(a.expected_closure || a.created_at || 0);
      const bDate = new Date(b.expected_closure || b.created_at || 0);
      return aDate - bDate;
    });
  }, [adminTasks]);

  // Filter potential managers (assuming all employees can be managers; adjust if role field exists)
  const managers = employees.filter(emp => emp.emp_id !== user?.emp_id); // Exclude self if needed

  const handleCreateEmployee = async (e) => {
    e.preventDefault();
    setLoading(true);
    try {
      const created = await api.createEmployee(employeeForm, token);
      onCreateEmployee(created);
      setShowCreateEmployee(false);
      setEmployeeForm({
        emp_id: "",
        name: "",
        email: "",
        designation: "",
        mgr_id: "",
      });
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
      const updated = await api.updateEmployee(
        employeeForm.emp_id,
        employeeForm,
        token
      );
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
    if (window.confirm("Are you sure you want to delete this employee?")) {
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
    setEmployeeForm({ ...employee, mgr_id: employee.mgr_id || "" });
    setShowEditEmployee(true);
  };

  const handleCreateTask = async (e) => {
    e.preventDefault();
    setLoading(true);
    try {
      const newTask = {
        ...taskForm,
        status: "TO_DO",
        assigned_by: user?.emp_id,
        created_by: user?.emp_id,
      };
      const created = await api.createTask(newTask, token);
      onCreateTask(created);
      setShowCreateTask(false);
      setTaskForm({
        task_id: "",
        name: "",
        description: "",
        assigned_to: "",
        priority: "MEDIUM",
        expected_closure: "",
      });
    } catch (err) {
      onError(err.message);
    } finally {
      setLoading(false);
    }
  };

  const handleAssignEmployee = async (e) => {
    e.preventDefault();
    if (!assignForm.employee_id || !assignForm.manager_id) {
      onError("Please select both employee and manager.");
      return;
    }
    setLoading(true);
    try {
      // Update the employee's mgr_id
      const updateData = { mgr_id: assignForm.manager_id };
      const updated = await api.updateEmployee(assignForm.employee_id, updateData, token);
      onUpdateEmployee(updated);
      setShowAssignEmployee(false);
      setAssignForm({ employee_id: "", manager_id: "" });
      alert("Employee assigned successfully!");
    } catch (err) {
      onError(err.message || "Failed to assign employee.");
    } finally {
      setLoading(false);
    }
  };

  if (loading) {
    return (
      <div className="min-h-screen bg-gradient-to-br from-slate-100 to-gray-200 flex items-center justify-center">
        <div className="text-lg">Loading...</div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-100 to-gray-200">
      <header className="bg-white shadow-sm border-b">
        <div className="max-w-7xl mx-auto px-6 py-4 flex justify-between">
          <div className="flex items-center gap-3">
            <Settings className="text-emerald-600" />
            <div>
              <h1 className="font-bold">Admin Dashboard</h1>
              <p className="text-sm text-gray-600">{user?.emp_id}</p>
            </div>
          </div>
          <div className="flex items-center gap-4">
            {user?.role === "ADMIN" && (
              <button
                onClick={onSwitchRole}
                className="text-gray-600 hover:text-gray-900"
              >
                Switch Role
              </button>
            )}
            <button
              onClick={onLogout}
              className="flex items-center gap-2 bg-red-500 hover:bg-red-600 text-white px-4 py-2 rounded-lg"
            >
              <LogOut size={16} /> Logout
            </button>
          </div>
        </div>
      </header>

      <main className="max-w-7xl mx-auto px-6 py-6">
        {error && (
          <div className="mb-4 bg-red-50 border border-red-300 text-red-700 p-3 rounded-lg flex items-center gap-2">
            <AlertCircle size={16} />
            {error}
          </div>
        )}

        <div className="mb-6 flex items-center justify-between">
          <div className="flex space-x-4">
            <button
              onClick={() => setActiveTab("employees")}
              className={`px-4 py-2 rounded-lg font-medium ${
                activeTab === "employees"
                  ? "bg-emerald-600 text-white"
                  : "bg-white border"
              }`}
            >
              Employees
            </button>
            <button
              onClick={() => setActiveTab("tasks")}
              className={`px-4 py-2 rounded-lg font-medium ${
                activeTab === "tasks"
                  ? "bg-emerald-600 text-white"
                  : "bg-white border"
              }`}
            >
              Tasks
            </button>
            <button
              onClick={() => setActiveTab("assign")}
              className={`px-4 py-2 rounded-lg font-medium ${
                activeTab === "assign"
                  ? "bg-emerald-600 text-white"
                  : "bg-white border"
              }`}
            >
              Assign Employees
            </button>
          </div>
          {activeTab === "employees" && (
            <button
              onClick={() => setShowCreateEmployee(true)}
              disabled={loading}
              className="bg-green-600 text-white px-4 py-2 rounded-lg hover:bg-green-700 flex items-center gap-2 disabled:opacity-50"
            >
              <Plus className="w-5 h-5" />
              <span>Create Employee</span>
            </button>
          )}
          {activeTab === "tasks" && (
            <button
              onClick={() => setShowCreateTask(true)}
              className="bg-green-600 text-white px-4 py-2 rounded-lg hover:bg-green-700 flex items-center gap-2"
            >
              <Plus className="w-5 h-5" />
              <span>Create New Task</span>
            </button>
          )}
          {activeTab === "assign" && (
            <button
              onClick={() => setShowAssignEmployee(true)}
              disabled={loading}
              className="bg-green-600 text-white px-4 py-2 rounded-lg hover:bg-green-700 flex items-center gap-2 disabled:opacity-50"
            >
              <UserCheck className="w-5 h-5" />
              <span>Assign Employee</span>
            </button>
          )}
        </div>

        {/* Employees Tab */}
        {activeTab === "employees" && (
          <div className="bg-white rounded-xl shadow border overflow-x-auto">
            <table className="w-full text-sm">
              <thead className="bg-gray-100">
                <tr>
                  <th className="px-4 py-3 text-left">Employee ID</th>
                  <th className="px-4 py-3 text-left">Name</th>
                  <th className="px-4 py-3 text-left">Email</th>
                  <th className="px-4 py-3 text-left">Designation</th>
                  <th className="px-4 py-3 text-left">Manager</th>
                  <th className="px-4 py-3 text-left">Actions</th>
                </tr>
              </thead>
              <tbody>
                {employees.length === 0 ? (
                  <tr>
                    <td
                      colSpan="6"
                      className="px-4 py-8 text-center text-gray-500"
                    >
                      No employees found. Create your first employee to get
                      started.
                    </td>
                  </tr>
                ) : (
                  employees.map((emp) => (
                    <tr key={emp.emp_id} className="border-t hover:bg-gray-50">
                      <td className="px-4 py-3 text-sm font-medium text-gray-900">
                        {emp.emp_id}
                      </td>
                      <td className="px-4 py-3 text-sm text-gray-900">
                        {emp.name}
                      </td>
                      <td className="px-4 py-3 text-sm text-gray-900">
                        {emp.email}
                      </td>
                      <td className="px-4 py-3 text-sm text-gray-900">
                        {emp.designation}
                      </td>
                      <td className="px-4 py-3 text-sm text-gray-900">
                        {emp.mgr_id || "-"}
                      </td>
                      <td className="px-4 py-3">
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
        )}

        {/* Tasks Tab */}
        {activeTab === "tasks" && (
          <>
            {/* View Toggle */}
            <div className="flex justify-end mb-4 gap-2">
              <button
                onClick={() => setViewMode("KANBAN")}
                className={`px-4 py-2 rounded-lg text-sm font-medium ${
                  viewMode === "KANBAN"
                    ? "bg-emerald-600 text-white"
                    : "bg-white border"
                }`}
              >
                Kanban
              </button>
              <button
                onClick={() => setViewMode("LIST")}
                className={`px-4 py-2 rounded-lg text-sm font-medium ${
                  viewMode === "LIST"
                    ? "bg-indigo-600 text-white"
                    : "bg-white border"
                }`}
              >
                List
              </button>
              <button
                onClick={() => setViewMode("PERFORMANCE")}
                className={`px-4 py-2 rounded-lg text-sm font-medium ${
                  viewMode === "PERFORMANCE"
                    ? "bg-orange-600 text-white"
                    : "bg-white border"
                }`}
              >
                Performance
              </button>
            </div>

            {/* KANBAN View (Read-only) */}
            {viewMode === "KANBAN" && (
              <div className="grid grid-cols-4 gap-6">
                {STATUS_ORDER.map((status) => (
                  <TaskColumn
                    key={status}
                    status={status}
                    count={tasksByStatus[status].length}
                  >
                    {tasksByStatus[status].map((task) => (
                      <TaskCard
                        key={task.task_id}
                        task={task}
                        token={token}
                        draggable={false} // Admin cannot drag/change status
                        // No onUpdateTask for admin - read-only
                      />
                    ))}
                  </TaskColumn>
                ))}
              </div>
            )}

            {/* LIST View */}
            {viewMode === "LIST" && (
              <div className="bg-white rounded-xl shadow border overflow-x-auto">
                <table className="w-full text-sm">
                  <thead className="bg-gray-100">
                    <tr>
                      <th className="px-4 py-3 text-left">Task</th>
                      <th className="px-4 py-3 text-left">Assigned To</th>
                      <th className="px-4 py-3 text-left">Status</th>
                      <th className="px-4 py-3 text-left">Priority</th>
                      <th className="px-4 py-3 text-left">Created</th>
                      <th className="px-4 py-3 text-left">Deadline</th>
                    </tr>
                  </thead>
                  <tbody>
                    {sortedTasksByDate.map((task) => (
                      <tr key={task.task_id} className="border-t">
                        <td className="px-4 py-3">{task.name}</td>
                        <td className="px-4 py-3">{task.assigned_to}</td>
                        <td className="px-4 py-3">{task.status}</td>
                        <td className="px-4 py-3">{task.priority}</td>
                        <td className="px-4 py-3">
                          {task.created_at
                            ? new Date(task.created_at).toLocaleDateString()
                            : "—"}
                        </td>
                        <td className="px-4 py-3">
                          {task.expected_closure
                            ? new Date(
                                task.expected_closure
                              ).toLocaleDateString()
                            : "—"}
                        </td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            )}

            {/* PERFORMANCE View */}
            {viewMode === "PERFORMANCE" && (
              <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
                <PerformancePieChart
                  tasksByStatus={tasksByStatus}
                  title="Team Task Status"
                />
                <EmployeePerformanceBarChart
                  tasks={adminTasks}
                  title="Employee Completion Rates"
                />
              </div>
            )}
          </>
        )}

        {/* Assign Employees Tab */}
        {activeTab === "assign" && (
          <div className="bg-white rounded-xl shadow border p-6">
            <div className="flex items-center gap-2 mb-4">
              <UserCheck size={20} className="text-emerald-600" />
              <h3 className="text-lg font-semibold">Assign Employee to Manager</h3>
            </div>
            <p className="text-gray-600 mb-6">
              Select an employee and assign them to a manager below.
            </p>
            {employees.length === 0 ? (
              <div className="text-center text-gray-500 py-8">
                No employees available. Create employees first in the Employees tab.
              </div>
            ) : (
              <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                {/* Current Assignments Table */}
                <div className="space-y-4">
                  <h4 className="font-medium text-gray-700">Current Assignments</h4>
                  {employees.filter(emp => emp.mgr_id).length === 0 ? (
                    <p className="text-gray-500 text-sm">No assignments yet.</p>
                  ) : (
                    <div className="overflow-x-auto">
                      <table className="w-full text-xs">
                        <thead className="bg-gray-50">
                          <tr>
                            <th className="px-3 py-2 text-left">Employee</th>
                            <th className="px-3 py-2 text-left">Manager</th>
                          </tr>
                        </thead>
                        <tbody>
                          {employees
                            .filter(emp => emp.mgr_id)
                            .map((emp) => (
                              <tr key={emp.emp_id} className="border-t">
                                <td className="px-3 py-2">{emp.name} ({emp.emp_id})</td>
                                <td className="px-3 py-2">
                                  {employees.find(m => m.emp_id === emp.mgr_id)?.name || emp.mgr_id}
                                </td>
                              </tr>
                            ))}
                        </tbody>
                      </table>
                    </div>
                  )}
                </div>

                {/* Quick Assignment Form */}
                <div className="space-y-4">
                  <h4 className="font-medium text-gray-700">Quick Assign</h4>
                  <form onSubmit={handleAssignEmployee} className="space-y-3">
                    <div>
                      <label className="block text-sm font-medium text-gray-700 mb-1">
                        Select Employee
                      </label>
                      <select
                        value={assignForm.employee_id}
                        onChange={(e) =>
                          setAssignForm({ ...assignForm, employee_id: e.target.value })
                        }
                        className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-emerald-500"
                        required
                        disabled={loading}
                      >
                        <option value="">Choose an employee...</option>
                        {employees.map((emp) => (
                          <option key={emp.emp_id} value={emp.emp_id}>
                            {emp.name} ({emp.emp_id})
                          </option>
                        ))}
                      </select>
                    </div>
                    <div>
                      <label className="block text-sm font-medium text-gray-700 mb-1">
                        Select Manager
                      </label>
                      <select
                        value={assignForm.manager_id}
                        onChange={(e) =>
                          setAssignForm({ ...assignForm, manager_id: e.target.value })
                        }
                        className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-emerald-500"
                        required
                        disabled={loading}
                      >
                        <option value="">Choose a manager...</option>
                        {managers.map((mgr) => (
                          <option key={mgr.emp_id} value={mgr.emp_id}>
                            {mgr.name} ({mgr.emp_id})
                          </option>
                        ))}
                      </select>
                    </div>
                    <button
                      type="submit"
                      disabled={loading || !assignForm.employee_id || !assignForm.manager_id}
                      className="w-full bg-emerald-600 text-white py-2 rounded-lg hover:bg-emerald-700 disabled:opacity-50 font-medium transition"
                    >
                      {loading ? "Assigning..." : "Assign Employee"}
                    </button>
                  </form>
                </div>
              </div>
            )}
          </div>
        )}

        {/* Create Employee Modal */}
        {showCreateEmployee && (
          <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center p-4 z-50">
            <div className="bg-white rounded-lg max-w-2xl w-full p-6">
              <h3 className="text-xl font-bold mb-4">Create New Employee</h3>
              <form onSubmit={handleCreateEmployee} className="space-y-4">
                <div className="grid grid-cols-2 gap-4">
                  <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">
                      Employee ID
                    </label>
                    <input
                      type="text"
                      value={employeeForm.emp_id}
                      onChange={(e) =>
                        setEmployeeForm({
                          ...employeeForm,
                          emp_id: e.target.value,
                        })
                      }
                      className="w-full px-3 py-2 border border-gray-300 rounded-lg"
                      required
                      disabled={loading}
                    />
                  </div>
                  <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">
                      Name
                    </label>
                    <input
                      type="text"
                      value={employeeForm.name}
                      onChange={(e) =>
                        setEmployeeForm({
                          ...employeeForm,
                          name: e.target.value,
                        })
                      }
                      className="w-full px-3 py-2 border border-gray-300 rounded-lg"
                      required
                      disabled={loading}
                    />
                  </div>
                </div>
                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-1">
                    Email
                  </label>
                  <input
                    type="email"
                    value={employeeForm.email}
                    onChange={(e) =>
                      setEmployeeForm({
                        ...employeeForm,
                        email: e.target.value,
                      })
                    }
                    className="w-full px-3 py-2 border border-gray-300 rounded-lg"
                    required
                    disabled={loading}
                  />
                </div>
                <div className="grid grid-cols-2 gap-4">
                  <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">
                      Designation
                    </label>
                    <input
                      type="text"
                      value={employeeForm.designation}
                      onChange={(e) =>
                        setEmployeeForm({
                          ...employeeForm,
                          designation: e.target.value,
                        })
                      }
                      className="w-full px-3 py-2 border border-gray-300 rounded-lg"
                      required
                      disabled={loading}
                    />
                  </div>
                  <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">
                      Manager ID (Optional)
                    </label>
                    <input
                      type="text"
                      value={employeeForm.mgr_id}
                      onChange={(e) =>
                        setEmployeeForm({
                          ...employeeForm,
                          mgr_id: e.target.value,
                        })
                      }
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
                    className="px-4 py-2 bg-green-600 text-white rounded-lg hover:bg-green-700 disabled:opacity-50"
                  >
                    {loading ? "Creating..." : "Create Employee"}
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
                    <label className="block text-sm font-medium text-gray-700 mb-1">
                      Employee ID
                    </label>
                    <input
                      type="text"
                      value={employeeForm.emp_id}
                      className="w-full px-3 py-2 border border-gray-300 rounded-lg bg-gray-100"
                      disabled
                    />
                  </div>
                  <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">
                      Name
                    </label>
                    <input
                      type="text"
                      value={employeeForm.name}
                      onChange={(e) =>
                        setEmployeeForm({
                          ...employeeForm,
                          name: e.target.value,
                        })
                      }
                      className="w-full px-3 py-2 border border-gray-300 rounded-lg"
                      required
                      disabled={loading}
                    />
                  </div>
                </div>
                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-1">
                    Email
                  </label>
                  <input
                    type="email"
                    value={employeeForm.email}
                    onChange={(e) =>
                      setEmployeeForm({
                        ...employeeForm,
                        email: e.target.value,
                      })
                    }
                    className="w-full px-3 py-2 border border-gray-300 rounded-lg"
                    required
                    disabled={loading}
                  />
                </div>
                <div className="grid grid-cols-2 gap-4">
                  <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">
                      Designation
                    </label>
                    <input
                      type="text"
                      value={employeeForm.designation}
                      onChange={(e) =>
                        setEmployeeForm({
                          ...employeeForm,
                          designation: e.target.value,
                        })
                      }
                      className="w-full px-3 py-2 border border-gray-300 rounded-lg"
                      required
                      disabled={loading}
                    />
                  </div>
                  <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">
                      Manager ID
                    </label>
                    <input
                      type="text"
                      value={employeeForm.mgr_id}
                      onChange={(e) =>
                        setEmployeeForm({
                          ...employeeForm,
                          mgr_id: e.target.value,
                        })
                      }
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
                    className="px-4 py-2 bg-green-600 text-white rounded-lg hover:bg-green-700 disabled:opacity-50"
                  >
                    {loading ? "Updating..." : "Update Employee"}
                  </button>
                </div>
              </form>
            </div>
          </div>
        )}

        {/* Create Task Modal */}
        {showCreateTask && (
          <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center p-4 z-50">
            <div className="bg-white rounded-lg max-w-2xl w-full p-6">
              <h3 className="text-xl font-bold mb-4">Create New Task</h3>
              <form onSubmit={handleCreateTask} className="space-y-4">
                <div className="grid grid-cols-2 gap-4">
                  <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">
                      Task ID
                    </label>
                    <input
                      type="text"
                      value={taskForm.task_id}
                      onChange={(e) =>
                        setTaskForm({ ...taskForm, task_id: e.target.value })
                      }
                      className="w-full px-3 py-2 border border-gray-300 rounded-lg"
                      required
                    />
                  </div>
                  <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">
                      Priority
                    </label>
                    <select
                      value={taskForm.priority}
                      onChange={(e) =>
                        setTaskForm({ ...taskForm, priority: e.target.value })
                      }
                      className="w-full px-3 py-2 border border-gray-300 rounded-lg"
                    >
                      <option value="HIGH">High</option>
                      <option value="MEDIUM">Medium</option>
                      <option value="LOW">Low</option>
                    </select>
                  </div>
                </div>
                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-1">
                    Task Name
                  </label>
                  <input
                    type="text"
                    value={taskForm.name}
                    onChange={(e) =>
                      setTaskForm({ ...taskForm, name: e.target.value })
                    }
                    className="w-full px-3 py-2 border border-gray-300 rounded-lg"
                    required
                  />
                </div>
                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-1">
                    Description
                  </label>
                  <textarea
                    value={taskForm.description}
                    onChange={(e) =>
                      setTaskForm({ ...taskForm, description: e.target.value })
                    }
                    className="w-full px-3 py-2 border border-gray-300 rounded-lg"
                    rows="3"
                    required
                  />
                </div>
                <div className="grid grid-cols-2 gap-4">
                  <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">
                      Assign To (Employee ID)
                    </label>
                    <input
                      type="text"
                      value={taskForm.assigned_to}
                      onChange={(e) =>
                        setTaskForm({
                          ...taskForm,
                          assigned_to: e.target.value,
                        })
                      }
                      className="w-full px-3 py-2 border border-gray-300 rounded-lg"
                      required
                    />
                  </div>
                  <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">
                      Expected Closure
                    </label>
                    <input
                      type="date"
                      value={taskForm.expected_closure}
                      onChange={(e) =>
                        setTaskForm({
                          ...taskForm,
                          expected_closure: e.target.value,
                        })
                      }
                      className="w-full px-3 py-2 border border-gray-300 rounded-lg"
                      required
                    />
                  </div>
                </div>
                <div className="flex justify-end space-x-3 pt-4">
                  <button
                    type="button"
                    onClick={() => setShowCreateTask(false)}
                    className="px-4 py-2 border border-gray-300 rounded-lg hover:bg-gray-50"
                  >
                    Cancel
                  </button>
                  <button
                    type="submit"
                    disabled={loading}
                    className="px-4 py-2 bg-green-600 text-white rounded-lg hover:bg-green-700 disabled:opacity-50"
                  >
                    {loading ? "Creating..." : "Create Task"}
                  </button>
                </div>
              </form>
            </div>
          </div>
        )}

        {/* Assign Employee Modal (Fallback if needed, but inline form used) */}
        {/* Note: Using inline form in tab for better UX; modal not needed here */}
      </main>
    </div>
  );
};

export default AdminDashboard;



// import { useState, useMemo } from "react";
// import {
//   Settings,
//   LogOut,
//   Plus,
//   Edit2,
//   Trash2,
//   Users,
//   AlertCircle,
// } from "lucide-react";
// import { api } from "../../services/api";
// import TaskCard from "../ui/TaskCard";
// import {
//   PerformancePieChart,
//   EmployeePerformanceBarChart,
// } from "../ui/PerformanceChart";

// const STATUS_ORDER = ["TO_DO", "IN_PROGRESS", "REVIEW", "DONE"];

// const STATUS_META = {
//   TO_DO: { label: "To Do", bg: "bg-blue-50", ring: "ring-blue-300" },
//   IN_PROGRESS: {
//     label: "In Progress",
//     bg: "bg-amber-50",
//     ring: "ring-amber-300",
//   },
//   REVIEW: { label: "Review", bg: "bg-purple-50", ring: "ring-purple-300" },
//   DONE: { label: "Done", bg: "bg-emerald-50", ring: "ring-emerald-300" },
// };

// // View-only column (no droppable)
// const TaskColumn = ({ status, count, children }) => {
//   const meta = STATUS_META[status];

//   return (
//     <div className="flex flex-col">
//       <div className="flex justify-between mb-2 px-1">
//         <h3 className="font-semibold text-gray-700">{meta.label}</h3>
//         <span className="text-xs bg-white px-2 py-0.5 rounded-full shadow">
//           {count}
//         </span>
//       </div>
//       <div
//         className={`min-h-[420px] p-4 rounded-2xl border transition
//           ${meta.bg}`}
//       >
//         <div className="space-y-3">{children}</div>
//       </div>
//     </div>
//   );
// };

// const AdminDashboard = ({
//   user,
//   employees,
//   tasks,
//   token,
//   onLogout,
//   onError,
//   onSwitchRole,
//   onCreateEmployee,
//   onUpdateEmployee,
//   onDeleteEmployee,
//   onUpdateTasks,
//   onCreateTask,
//   error,
// }) => {
//   const [activeTab, setActiveTab] = useState("employees");
//   const [viewMode, setViewMode] = useState("KANBAN"); // For tasks tab
//   const [showCreateEmployee, setShowCreateEmployee] = useState(false);
//   const [showEditEmployee, setShowEditEmployee] = useState(false);
//   const [showCreateTask, setShowCreateTask] = useState(false);
//   const [selectedEmployee, setSelectedEmployee] = useState(null);
//   const [employeeForm, setEmployeeForm] = useState({
//     emp_id: "",
//     name: "",
//     email: "",
//     designation: "",
//     mgr_id: "",
//   });
//   const [taskForm, setTaskForm] = useState({
//     task_id: "",
//     name: "",
//     description: "",
//     assigned_to: "",
//     priority: "MEDIUM",
//     expected_closure: "",
//   });
//   const [loading, setLoading] = useState(false);

//   // Admin's tasks: Show ALL tasks for full oversight (updated to populate views)
//   const adminTasks = tasks;

//   const tasksByStatus = {
//     TO_DO: adminTasks.filter((t) => t.status === "TO_DO"),
//     IN_PROGRESS: adminTasks.filter((t) => t.status === "IN_PROGRESS"),
//     REVIEW: adminTasks.filter((t) => t.status === "REVIEW"),
//     DONE: adminTasks.filter((t) => t.status === "DONE"),
//   };

//   const sortedTasksByDate = useMemo(() => {
//     return [...adminTasks].sort((a, b) => {
//       const aDate = new Date(a.expected_closure || a.created_at || 0);
//       const bDate = new Date(b.expected_closure || b.created_at || 0);
//       return aDate - bDate;
//     });
//   }, [adminTasks]);

//   const handleCreateEmployee = async (e) => {
//     e.preventDefault();
//     setLoading(true);
//     try {
//       const created = await api.createEmployee(employeeForm, token);
//       onCreateEmployee(created);
//       setShowCreateEmployee(false);
//       setEmployeeForm({
//         emp_id: "",
//         name: "",
//         email: "",
//         designation: "",
//         mgr_id: "",
//       });
//     } catch (err) {
//       onError(err.message);
//     } finally {
//       setLoading(false);
//     }
//   };

//   const handleEditEmployee = async (e) => {
//     e.preventDefault();
//     setLoading(true);
//     try {
//       const updated = await api.updateEmployee(
//         employeeForm.emp_id,
//         employeeForm,
//         token
//       );
//       onUpdateEmployee(updated);
//       setShowEditEmployee(false);
//       setSelectedEmployee(null);
//     } catch (err) {
//       onError(err.message);
//     } finally {
//       setLoading(false);
//     }
//   };

//   const handleDeleteEmployee = async (empId) => {
//     if (window.confirm("Are you sure you want to delete this employee?")) {
//       setLoading(true);
//       try {
//         await api.deleteEmployee(empId, token);
//         onDeleteEmployee(empId);
//       } catch (err) {
//         onError(err.message);
//       } finally {
//         setLoading(false);
//       }
//     }
//   };

//   const openEditModal = (employee) => {
//     setSelectedEmployee(employee);
//     setEmployeeForm({ ...employee, mgr_id: employee.mgr_id || "" });
//     setShowEditEmployee(true);
//   };

//   const handleCreateTask = async (e) => {
//     e.preventDefault();
//     setLoading(true);
//     try {
//       const newTask = {
//         ...taskForm,
//         status: "TO_DO",
//         assigned_by: user?.emp_id,
//         created_by: user?.emp_id,
//       };
//       const created = await api.createTask(newTask, token);
//       onCreateTask(created);
//       setShowCreateTask(false);
//       setTaskForm({
//         task_id: "",
//         name: "",
//         description: "",
//         assigned_to: "",
//         priority: "MEDIUM",
//         expected_closure: "",
//       });
//     } catch (err) {
//       onError(err.message);
//     } finally {
//       setLoading(false);
//     }
//   };

//   if (loading) {
//     return (
//       <div className="min-h-screen bg-gradient-to-br from-slate-100 to-gray-200 flex items-center justify-center">
//         <div className="text-lg">Loading...</div>
//       </div>
//     );
//   }

//   return (
//     <div className="min-h-screen bg-gradient-to-br from-slate-100 to-gray-200">
//       <header className="bg-white shadow-sm border-b">
//         <div className="max-w-7xl mx-auto px-6 py-4 flex justify-between">
//           <div className="flex items-center gap-3">
//             <Settings className="text-emerald-600" />
//             <div>
//               <h1 className="font-bold">Admin Dashboard</h1>
//               <p className="text-sm text-gray-600">{user?.emp_id}</p>
//             </div>
//           </div>
//           <div className="flex items-center gap-4">
//             {user?.role === "ADMIN" && (
//               <button
//                 onClick={onSwitchRole}
//                 className="text-gray-600 hover:text-gray-900"
//               >
//                 Switch Role
//               </button>
//             )}
//             <button
//               onClick={onLogout}
//               className="flex items-center gap-2 bg-red-500 hover:bg-red-600 text-white px-4 py-2 rounded-lg"
//             >
//               <LogOut size={16} /> Logout
//             </button>
//           </div>
//         </div>
//       </header>

//       <main className="max-w-7xl mx-auto px-6 py-6">
//         {error && (
//           <div className="mb-4 bg-red-50 border border-red-300 text-red-700 p-3 rounded-lg flex items-center gap-2">
//             <AlertCircle size={16} />
//             {error}
//           </div>
//         )}

//         <div className="mb-6 flex items-center justify-between">
//           <div className="flex space-x-4">
//             <button
//               onClick={() => setActiveTab("employees")}
//               className={`px-4 py-2 rounded-lg font-medium ${
//                 activeTab === "employees"
//                   ? "bg-emerald-600 text-white"
//                   : "bg-white border"
//               }`}
//             >
//               Employees
//             </button>
//             <button
//               onClick={() => setActiveTab("tasks")}
//               className={`px-4 py-2 rounded-lg font-medium ${
//                 activeTab === "tasks"
//                   ? "bg-emerald-600 text-white"
//                   : "bg-white border"
//               }`}
//             >
//               Tasks
//             </button>
//             <button
//               onClick={() => setActiveTab("assign")}
//               className={`px-4 py-2 rounded-lg font-medium ${
//                 activeTab === "assign"
//                   ? "bg-emerald-600 text-white"
//                   : "bg-white border"
//               }`}
//             >
//               Assign Employees
//             </button>
//           </div>
//           {activeTab === "employees" && (
//             <button
//               onClick={() => setShowCreateEmployee(true)}
//               disabled={loading}
//               className="bg-green-600 text-white px-4 py-2 rounded-lg hover:bg-green-700 flex items-center gap-2 disabled:opacity-50"
//             >
//               <Plus className="w-5 h-5" />
//               <span>Create Employee</span>
//             </button>
//           )}
//           {activeTab === "tasks" && (
//             <button
//               onClick={() => setShowCreateTask(true)}
//               className="bg-green-600 text-white px-4 py-2 rounded-lg hover:bg-green-700 flex items-center gap-2"
//             >
//               <Plus className="w-5 h-5" />
//               <span>Create New Task</span>
//             </button>
//           )}
//         </div>

//         {/* Employees Tab */}
//         {activeTab === "employees" && (
//           <div className="bg-white rounded-xl shadow border overflow-x-auto">
//             <table className="w-full text-sm">
//               <thead className="bg-gray-100">
//                 <tr>
//                   <th className="px-4 py-3 text-left">Employee ID</th>
//                   <th className="px-4 py-3 text-left">Name</th>
//                   <th className="px-4 py-3 text-left">Email</th>
//                   <th className="px-4 py-3 text-left">Designation</th>
//                   <th className="px-4 py-3 text-left">Manager</th>
//                   <th className="px-4 py-3 text-left">Actions</th>
//                 </tr>
//               </thead>
//               <tbody>
//                 {employees.length === 0 ? (
//                   <tr>
//                     <td
//                       colSpan="6"
//                       className="px-4 py-8 text-center text-gray-500"
//                     >
//                       No employees found. Create your first employee to get
//                       started.
//                     </td>
//                   </tr>
//                 ) : (
//                   employees.map((emp) => (
//                     <tr key={emp.emp_id} className="border-t hover:bg-gray-50">
//                       <td className="px-4 py-3 text-sm font-medium text-gray-900">
//                         {emp.emp_id}
//                       </td>
//                       <td className="px-4 py-3 text-sm text-gray-900">
//                         {emp.name}
//                       </td>
//                       <td className="px-4 py-3 text-sm text-gray-900">
//                         {emp.email}
//                       </td>
//                       <td className="px-4 py-3 text-sm text-gray-900">
//                         {emp.designation}
//                       </td>
//                       <td className="px-4 py-3 text-sm text-gray-900">
//                         {emp.mgr_id || "-"}
//                       </td>
//                       <td className="px-4 py-3">
//                         <div className="flex items-center space-x-2">
//                           <button
//                             onClick={() => openEditModal(emp)}
//                             className="text-indigo-600 hover:text-indigo-900 disabled:opacity-50"
//                             disabled={loading}
//                           >
//                             <Edit2 className="w-4 h-4" />
//                           </button>
//                           <button
//                             onClick={() => handleDeleteEmployee(emp.emp_id)}
//                             className="text-red-600 hover:text-red-900 disabled:opacity-50"
//                             disabled={loading}
//                           >
//                             <Trash2 className="w-4 h-4" />
//                           </button>
//                         </div>
//                       </td>
//                     </tr>
//                   ))
//                 )}
//               </tbody>
//             </table>
//           </div>
//         )}

//         {/* Tasks Tab */}
//         {activeTab === "tasks" && (
//           <>
//             {/* View Toggle */}
//             <div className="flex justify-end mb-4 gap-2">
//               <button
//                 onClick={() => setViewMode("KANBAN")}
//                 className={`px-4 py-2 rounded-lg text-sm font-medium ${
//                   viewMode === "KANBAN"
//                     ? "bg-emerald-600 text-white"
//                     : "bg-white border"
//                 }`}
//               >
//                 Kanban
//               </button>
//               <button
//                 onClick={() => setViewMode("LIST")}
//                 className={`px-4 py-2 rounded-lg text-sm font-medium ${
//                   viewMode === "LIST"
//                     ? "bg-indigo-600 text-white"
//                     : "bg-white border"
//                 }`}
//               >
//                 List
//               </button>
//               <button
//                 onClick={() => setViewMode("PERFORMANCE")}
//                 className={`px-4 py-2 rounded-lg text-sm font-medium ${
//                   viewMode === "PERFORMANCE"
//                     ? "bg-orange-600 text-white"
//                     : "bg-white border"
//                 }`}
//               >
//                 Performance
//               </button>
//             </div>

//             {/* KANBAN View (Read-only) */}
//             {viewMode === "KANBAN" && (
//               <div className="grid grid-cols-4 gap-6">
//                 {STATUS_ORDER.map((status) => (
//                   <TaskColumn
//                     key={status}
//                     status={status}
//                     count={tasksByStatus[status].length}
//                   >
//                     {tasksByStatus[status].map((task) => (
//                       <TaskCard
//                         key={task.task_id}
//                         task={task}
//                         token={token}
//                         draggable={false} // Admin cannot drag/change status
//                         // No onUpdateTask for admin - read-only
//                       />
//                     ))}
//                   </TaskColumn>
//                 ))}
//               </div>
//             )}

//             {/* LIST View */}
//             {viewMode === "LIST" && (
//               <div className="bg-white rounded-xl shadow border overflow-x-auto">
//                 <table className="w-full text-sm">
//                   <thead className="bg-gray-100">
//                     <tr>
//                       <th className="px-4 py-3 text-left">Task</th>
//                       <th className="px-4 py-3 text-left">Assigned To</th>
//                       <th className="px-4 py-3 text-left">Status</th>
//                       <th className="px-4 py-3 text-left">Priority</th>
//                       <th className="px-4 py-3 text-left">Created</th>
//                       <th className="px-4 py-3 text-left">Deadline</th>
//                     </tr>
//                   </thead>
//                   <tbody>
//                     {sortedTasksByDate.map((task) => (
//                       <tr key={task.task_id} className="border-t">
//                         <td className="px-4 py-3">{task.name}</td>
//                         <td className="px-4 py-3">{task.assigned_to}</td>
//                         <td className="px-4 py-3">{task.status}</td>
//                         <td className="px-4 py-3">{task.priority}</td>
//                         <td className="px-4 py-3">
//                           {task.created_at
//                             ? new Date(task.created_at).toLocaleDateString()
//                             : "—"}
//                         </td>
//                         <td className="px-4 py-3">
//                           {task.expected_closure
//                             ? new Date(
//                                 task.expected_closure
//                               ).toLocaleDateString()
//                             : "—"}
//                         </td>
//                       </tr>
//                     ))}
//                   </tbody>
//                 </table>
//               </div>
//             )}

//             {/* PERFORMANCE View */}
//             {viewMode === "PERFORMANCE" && (
//               <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
//                 <PerformancePieChart
//                   tasksByStatus={tasksByStatus}
//                   title="Team Task Status"
//                 />
//                 <EmployeePerformanceBarChart
//                   tasks={adminTasks}
//                   title="Employee Completion Rates"
//                 />
//               </div>
//             )}
//           </>
//         )}

//         {/* Assign Tab (Placeholder) */}
//         {activeTab === "assign" && (
//           <div className="bg-white rounded-xl shadow border p-6">
//             <h3 className="text-lg font-semibold mb-4">
//               Assign Employee to Manager
//             </h3>
//             <p className="text-gray-600 mb-4">
//               Select an employee and assign them to a manager
//             </p>
//             <div className="text-center text-gray-500 py-8">
//               Feature coming soon - Use the employee edit form to update manager
//               assignments
//             </div>
//           </div>
//         )}

//         {/* Create Employee Modal */}
//         {showCreateEmployee && (
//           <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center p-4 z-50">
//             <div className="bg-white rounded-lg max-w-2xl w-full p-6">
//               <h3 className="text-xl font-bold mb-4">Create New Employee</h3>
//               <form onSubmit={handleCreateEmployee} className="space-y-4">
//                 <div className="grid grid-cols-2 gap-4">
//                   <div>
//                     <label className="block text-sm font-medium text-gray-700 mb-1">
//                       Employee ID
//                     </label>
//                     <input
//                       type="text"
//                       value={employeeForm.emp_id}
//                       onChange={(e) =>
//                         setEmployeeForm({
//                           ...employeeForm,
//                           emp_id: e.target.value,
//                         })
//                       }
//                       className="w-full px-3 py-2 border border-gray-300 rounded-lg"
//                       required
//                       disabled={loading}
//                     />
//                   </div>
//                   <div>
//                     <label className="block text-sm font-medium text-gray-700 mb-1">
//                       Name
//                     </label>
//                     <input
//                       type="text"
//                       value={employeeForm.name}
//                       onChange={(e) =>
//                         setEmployeeForm({
//                           ...employeeForm,
//                           name: e.target.value,
//                         })
//                       }
//                       className="w-full px-3 py-2 border border-gray-300 rounded-lg"
//                       required
//                       disabled={loading}
//                     />
//                   </div>
//                 </div>
//                 <div>
//                   <label className="block text-sm font-medium text-gray-700 mb-1">
//                     Email
//                   </label>
//                   <input
//                     type="email"
//                     value={employeeForm.email}
//                     onChange={(e) =>
//                       setEmployeeForm({
//                         ...employeeForm,
//                         email: e.target.value,
//                       })
//                     }
//                     className="w-full px-3 py-2 border border-gray-300 rounded-lg"
//                     required
//                     disabled={loading}
//                   />
//                 </div>
//                 <div className="grid grid-cols-2 gap-4">
//                   <div>
//                     <label className="block text-sm font-medium text-gray-700 mb-1">
//                       Designation
//                     </label>
//                     <input
//                       type="text"
//                       value={employeeForm.designation}
//                       onChange={(e) =>
//                         setEmployeeForm({
//                           ...employeeForm,
//                           designation: e.target.value,
//                         })
//                       }
//                       className="w-full px-3 py-2 border border-gray-300 rounded-lg"
//                       required
//                       disabled={loading}
//                     />
//                   </div>
//                   <div>
//                     <label className="block text-sm font-medium text-gray-700 mb-1">
//                       Manager ID (Optional)
//                     </label>
//                     <input
//                       type="text"
//                       value={employeeForm.mgr_id}
//                       onChange={(e) =>
//                         setEmployeeForm({
//                           ...employeeForm,
//                           mgr_id: e.target.value,
//                         })
//                       }
//                       className="w-full px-3 py-2 border border-gray-300 rounded-lg"
//                       disabled={loading}
//                     />
//                   </div>
//                 </div>
//                 <div className="flex justify-end space-x-3 pt-4">
//                   <button
//                     type="button"
//                     onClick={() => setShowCreateEmployee(false)}
//                     className="px-4 py-2 border border-gray-300 rounded-lg hover:bg-gray-50 disabled:opacity-50"
//                     disabled={loading}
//                   >
//                     Cancel
//                   </button>
//                   <button
//                     type="submit"
//                     disabled={loading}
//                     className="px-4 py-2 bg-green-600 text-white rounded-lg hover:bg-green-700 disabled:opacity-50"
//                   >
//                     {loading ? "Creating..." : "Create Employee"}
//                   </button>
//                 </div>
//               </form>
//             </div>
//           </div>
//         )}

//         {/* Edit Employee Modal */}
//         {showEditEmployee && (
//           <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center p-4 z-50">
//             <div className="bg-white rounded-lg max-w-2xl w-full p-6">
//               <h3 className="text-xl font-bold mb-4">Edit Employee</h3>
//               <form onSubmit={handleEditEmployee} className="space-y-4">
//                 <div className="grid grid-cols-2 gap-4">
//                   <div>
//                     <label className="block text-sm font-medium text-gray-700 mb-1">
//                       Employee ID
//                     </label>
//                     <input
//                       type="text"
//                       value={employeeForm.emp_id}
//                       className="w-full px-3 py-2 border border-gray-300 rounded-lg bg-gray-100"
//                       disabled
//                     />
//                   </div>
//                   <div>
//                     <label className="block text-sm font-medium text-gray-700 mb-1">
//                       Name
//                     </label>
//                     <input
//                       type="text"
//                       value={employeeForm.name}
//                       onChange={(e) =>
//                         setEmployeeForm({
//                           ...employeeForm,
//                           name: e.target.value,
//                         })
//                       }
//                       className="w-full px-3 py-2 border border-gray-300 rounded-lg"
//                       required
//                       disabled={loading}
//                     />
//                   </div>
//                 </div>
//                 <div>
//                   <label className="block text-sm font-medium text-gray-700 mb-1">
//                     Email
//                   </label>
//                   <input
//                     type="email"
//                     value={employeeForm.email}
//                     onChange={(e) =>
//                       setEmployeeForm({
//                         ...employeeForm,
//                         email: e.target.value,
//                       })
//                     }
//                     className="w-full px-3 py-2 border border-gray-300 rounded-lg"
//                     required
//                     disabled={loading}
//                   />
//                 </div>
//                 <div className="grid grid-cols-2 gap-4">
//                   <div>
//                     <label className="block text-sm font-medium text-gray-700 mb-1">
//                       Designation
//                     </label>
//                     <input
//                       type="text"
//                       value={employeeForm.designation}
//                       onChange={(e) =>
//                         setEmployeeForm({
//                           ...employeeForm,
//                           designation: e.target.value,
//                         })
//                       }
//                       className="w-full px-3 py-2 border border-gray-300 rounded-lg"
//                       required
//                       disabled={loading}
//                     />
//                   </div>
//                   <div>
//                     <label className="block text-sm font-medium text-gray-700 mb-1">
//                       Manager ID
//                     </label>
//                     <input
//                       type="text"
//                       value={employeeForm.mgr_id}
//                       onChange={(e) =>
//                         setEmployeeForm({
//                           ...employeeForm,
//                           mgr_id: e.target.value,
//                         })
//                       }
//                       className="w-full px-3 py-2 border border-gray-300 rounded-lg"
//                       disabled={loading}
//                     />
//                   </div>
//                 </div>
//                 <div className="flex justify-end space-x-3 pt-4">
//                   <button
//                     type="button"
//                     onClick={() => {
//                       setShowEditEmployee(false);
//                       setSelectedEmployee(null);
//                     }}
//                     className="px-4 py-2 border border-gray-300 rounded-lg hover:bg-gray-50 disabled:opacity-50"
//                     disabled={loading}
//                   >
//                     Cancel
//                   </button>
//                   <button
//                     type="submit"
//                     disabled={loading}
//                     className="px-4 py-2 bg-green-600 text-white rounded-lg hover:bg-green-700 disabled:opacity-50"
//                   >
//                     {loading ? "Updating..." : "Update Employee"}
//                   </button>
//                 </div>
//               </form>
//             </div>
//           </div>
//         )}

//         {/* Create Task Modal */}
//         {showCreateTask && (
//           <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center p-4 z-50">
//             <div className="bg-white rounded-lg max-w-2xl w-full p-6">
//               <h3 className="text-xl font-bold mb-4">Create New Task</h3>
//               <form onSubmit={handleCreateTask} className="space-y-4">
//                 <div className="grid grid-cols-2 gap-4">
//                   <div>
//                     <label className="block text-sm font-medium text-gray-700 mb-1">
//                       Task ID
//                     </label>
//                     <input
//                       type="text"
//                       value={taskForm.task_id}
//                       onChange={(e) =>
//                         setTaskForm({ ...taskForm, task_id: e.target.value })
//                       }
//                       className="w-full px-3 py-2 border border-gray-300 rounded-lg"
//                       required
//                     />
//                   </div>
//                   <div>
//                     <label className="block text-sm font-medium text-gray-700 mb-1">
//                       Priority
//                     </label>
//                     <select
//                       value={taskForm.priority}
//                       onChange={(e) =>
//                         setTaskForm({ ...taskForm, priority: e.target.value })
//                       }
//                       className="w-full px-3 py-2 border border-gray-300 rounded-lg"
//                     >
//                       <option value="HIGH">High</option>
//                       <option value="MEDIUM">Medium</option>
//                       <option value="LOW">Low</option>
//                     </select>
//                   </div>
//                 </div>
//                 <div>
//                   <label className="block text-sm font-medium text-gray-700 mb-1">
//                     Task Name
//                   </label>
//                   <input
//                     type="text"
//                     value={taskForm.name}
//                     onChange={(e) =>
//                       setTaskForm({ ...taskForm, name: e.target.value })
//                     }
//                     className="w-full px-3 py-2 border border-gray-300 rounded-lg"
//                     required
//                   />
//                 </div>
//                 <div>
//                   <label className="block text-sm font-medium text-gray-700 mb-1">
//                     Description
//                   </label>
//                   <textarea
//                     value={taskForm.description}
//                     onChange={(e) =>
//                       setTaskForm({ ...taskForm, description: e.target.value })
//                     }
//                     className="w-full px-3 py-2 border border-gray-300 rounded-lg"
//                     rows="3"
//                     required
//                   />
//                 </div>
//                 <div className="grid grid-cols-2 gap-4">
//                   <div>
//                     <label className="block text-sm font-medium text-gray-700 mb-1">
//                       Assign To (Employee ID)
//                     </label>
//                     <input
//                       type="text"
//                       value={taskForm.assigned_to}
//                       onChange={(e) =>
//                         setTaskForm({
//                           ...taskForm,
//                           assigned_to: e.target.value,
//                         })
//                       }
//                       className="w-full px-3 py-2 border border-gray-300 rounded-lg"
//                       required
//                     />
//                   </div>
//                   <div>
//                     <label className="block text-sm font-medium text-gray-700 mb-1">
//                       Expected Closure
//                     </label>
//                     <input
//                       type="date"
//                       value={taskForm.expected_closure}
//                       onChange={(e) =>
//                         setTaskForm({
//                           ...taskForm,
//                           expected_closure: e.target.value,
//                         })
//                       }
//                       className="w-full px-3 py-2 border border-gray-300 rounded-lg"
//                       required
//                     />
//                   </div>
//                 </div>
//                 <div className="flex justify-end space-x-3 pt-4">
//                   <button
//                     type="button"
//                     onClick={() => setShowCreateTask(false)}
//                     className="px-4 py-2 border border-gray-300 rounded-lg hover:bg-gray-50"
//                   >
//                     Cancel
//                   </button>
//                   <button
//                     type="submit"
//                     disabled={loading}
//                     className="px-4 py-2 bg-green-600 text-white rounded-lg hover:bg-green-700 disabled:opacity-50"
//                   >
//                     {loading ? "Creating..." : "Create Task"}
//                   </button>
//                 </div>
//               </form>
//             </div>
//           </div>
//         )}
//       </main>
//     </div>
//   );
// };

// export default AdminDashboard;

// import { useState, useMemo } from "react";
// import {
//   Settings,
//   LogOut,
//   Plus,
//   Edit2,
//   Trash2,
//   Users,
//   AlertCircle,
// } from "lucide-react";
// import { api } from "../../services/api";
// import TaskCard from "../ui/TaskCard";
// import {
//   PerformancePieChart,
//   EmployeePerformanceBarChart,
// } from "../ui/PerformanceChart";

// const AdminDashboard = ({
//   user,
//   employees,
//   tasks,
//   token,
//   onLogout,
//   onError,
//   onSwitchRole,
//   onCreateEmployee,
//   onUpdateEmployee,
//   onDeleteEmployee,
//   onUpdateTasks,
//   onCreateTask,
//   error,
// }) => {
//   const [activeTab, setActiveTab] = useState("employees");
//   const [viewMode, setViewMode] = useState("KANBAN"); // For tasks tab
//   const [showCreateEmployee, setShowCreateEmployee] = useState(false);
//   const [showEditEmployee, setShowEditEmployee] = useState(false);
//   const [showCreateTask, setShowCreateTask] = useState(false);
//   const [selectedEmployee, setSelectedEmployee] = useState(null);
//   const [employeeForm, setEmployeeForm] = useState({
//     emp_id: "",
//     name: "",
//     email: "",
//     designation: "",
//     mgr_id: "",
//   });
//   const [taskForm, setTaskForm] = useState({
//     task_id: "",
//     name: "",
//     description: "",
//     assigned_to: "",
//     priority: "MEDIUM",
//     expected_closure: "",
//   });
//   const [loading, setLoading] = useState(false);

//   // Admin's tasks: all tasks assigned by admin
//   const adminTasks = tasks.filter(
//     (t) =>
//       String(t.assigned_by).trim().toUpperCase() ===
//       String(user?.emp_id).trim().toUpperCase()
//   );

//   const tasksByStatus = {
//     TO_DO: adminTasks.filter((t) => t.status === "TO_DO"),
//     IN_PROGRESS: adminTasks.filter((t) => t.status === "IN_PROGRESS"),
//     REVIEW: adminTasks.filter((t) => t.status === "REVIEW"),
//     DONE: adminTasks.filter((t) => t.status === "DONE"),
//   };

//   const sortedTasksByDate = useMemo(() => {
//     return [...adminTasks].sort((a, b) => {
//       const aDate = new Date(a.expected_closure || a.created_at || 0);
//       const bDate = new Date(b.expected_closure || b.created_at || 0);
//       return aDate - bDate;
//     });
//   }, [adminTasks]);

//   const STATUS_ORDER = ["TO_DO", "IN_PROGRESS", "REVIEW", "DONE"];

//   const STATUS_META = {
//     TO_DO: { label: "To Do", bg: "bg-blue-50", ring: "ring-blue-300" },
//     IN_PROGRESS: {
//       label: "In Progress",
//       bg: "bg-amber-50",
//       ring: "ring-amber-300",
//     },
//     REVIEW: { label: "Review", bg: "bg-purple-50", ring: "ring-purple-300" },
//     DONE: { label: "Done", bg: "bg-emerald-50", ring: "ring-emerald-300" },
//   };

//   // View-only column (no droppable)
//   const TaskColumn = ({ status, count, children }) => {
//     const meta = STATUS_META[status];

//     return (
//       <div className="flex flex-col">
//         <div className="flex justify-between mb-2 px-1">
//           <h3 className="font-semibold text-gray-700">{meta.label}</h3>
//           <span className="text-xs bg-white px-2 py-0.5 rounded-full shadow">
//             {count}
//           </span>
//         </div>
//         <div
//           className={`min-h-[420px] p-4 rounded-2xl border
//             ${meta.bg}`}
//         >
//           <div className="space-y-3">{children}</div>
//         </div>
//       </div>
//     );
//   };

//   const handleCreateEmployee = async (e) => {
//     e.preventDefault();
//     setLoading(true);
//     try {
//       const created = await api.createEmployee(employeeForm, token);
//       onCreateEmployee(created);
//       setShowCreateEmployee(false);
//       setEmployeeForm({
//         emp_id: "",
//         name: "",
//         email: "",
//         designation: "",
//         mgr_id: "",
//       });
//     } catch (err) {
//       onError(err.message);
//     } finally {
//       setLoading(false);
//     }
//   };

//   const handleEditEmployee = async (e) => {
//     e.preventDefault();
//     setLoading(true);
//     try {
//       const updated = await api.updateEmployee(
//         employeeForm.emp_id,
//         employeeForm,
//         token
//       );
//       onUpdateEmployee(updated);
//       setShowEditEmployee(false);
//       setSelectedEmployee(null);
//     } catch (err) {
//       onError(err.message);
//     } finally {
//       setLoading(false);
//     }
//   };

//   const handleDeleteEmployee = async (empId) => {
//     if (window.confirm("Are you sure you want to delete this employee?")) {
//       setLoading(true);
//       try {
//         await api.deleteEmployee(empId, token);
//         onDeleteEmployee(empId);
//       } catch (err) {
//         onError(err.message);
//       } finally {
//         setLoading(false);
//       }
//     }
//   };

//   const openEditModal = (employee) => {
//     setSelectedEmployee(employee);
//     setEmployeeForm({ ...employee, mgr_id: employee.mgr_id || "" });
//     setShowEditEmployee(true);
//   };

//   const handleCreateTask = async (e) => {
//     e.preventDefault();
//     setLoading(true);
//     try {
//       const newTask = {
//         ...taskForm,
//         status: "TO_DO",
//         assigned_by: user?.emp_id,
//         created_by: user?.emp_id,
//       };
//       const created = await api.createTask(newTask, token);
//       onCreateTask(created);
//       setShowCreateTask(false);
//       setTaskForm({
//         task_id: "",
//         name: "",
//         description: "",
//         assigned_to: "",
//         priority: "MEDIUM",
//         expected_closure: "",
//       });
//     } catch (err) {
//       onError(err.message);
//     } finally {
//       setLoading(false);
//     }
//   };

//   if (loading) {
//     return (
//       <div className="min-h-screen bg-gray-50 flex items-center justify-center">
//         <div className="text-lg">Loading...</div>
//       </div>
//     );
//   }

//   return (
//     <div className="min-h-screen bg-gray-50">
//       <header className="bg-white border-b border-gray-200 sticky top-0 z-10">
//         <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-4">
//           <div className="flex items-center justify-between">
//             <div className="flex items-center space-x-3">
//               <Settings className="w-8 h-8 text-indigo-600" />
//               <div>
//                 <h1 className="text-2xl font-bold text-gray-900">
//                   Admin Dashboard
//                 </h1>
//                 <p className="text-sm text-gray-600">{user?.name}</p>
//               </div>
//             </div>
//             <div className="flex items-center space-x-4">
//               <button
//                 onClick={onSwitchRole}
//                 className="text-gray-600 hover:text-gray-900"
//               >
//                 Switch Role
//               </button>
//               <button
//                 onClick={onLogout}
//                 className="flex items-center space-x-2 text-gray-600 hover:text-gray-900"
//               >
//                 <LogOut className="w-5 h-5" />
//                 <span>Logout</span>
//               </button>
//             </div>
//           </div>
//         </div>
//       </header>
//       <main className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
//         {error && (
//           <div className="mb-4 bg-red-50 border border-red-300 text-red-700 p-3 rounded-lg flex items-center gap-2">
//             <AlertCircle size={16} />
//             {error}
//           </div>
//         )}
//         <div className="mb-6 flex items-center justify-between">
//           <div className="flex space-x-4">
//             <button
//               onClick={() => setActiveTab("employees")}
//               className={`px-4 py-2 rounded-lg font-medium ${
//                 activeTab === "employees"
//                   ? "bg-indigo-600 text-white"
//                   : "bg-white text-gray-700 hover:bg-gray-50"
//               }`}
//             >
//               Employees
//             </button>
//             <button
//               onClick={() => setActiveTab("tasks")}
//               className={`px-4 py-2 rounded-lg font-medium ${
//                 activeTab === "tasks"
//                   ? "bg-indigo-600 text-white"
//                   : "bg-white text-gray-700 hover:bg-gray-50"
//               }`}
//             >
//               Tasks
//             </button>
//             <button
//               onClick={() => setActiveTab("assign")}
//               className={`px-4 py-2 rounded-lg font-medium ${
//                 activeTab === "assign"
//                   ? "bg-indigo-600 text-white"
//                   : "bg-white text-gray-700 hover:bg-gray-50"
//               }`}
//             >
//               Assign Employees
//             </button>
//           </div>
//           {activeTab === "employees" && (
//             <button
//               onClick={() => setShowCreateEmployee(true)}
//               disabled={loading}
//               className="bg-indigo-600 text-white px-4 py-2 rounded-lg hover:bg-indigo-700 flex items-center space-x-2 disabled:opacity-50"
//             >
//               <Plus className="w-5 h-5" />
//               <span>Create Employee</span>
//             </button>
//           )}
//           {activeTab === "tasks" && (
//             <button
//               onClick={() => setShowCreateTask(true)}
//               className="bg-green-600 text-white px-4 py-2 rounded-lg hover:bg-green-700 flex items-center gap-2"
//             >
//               <Plus className="w-5 h-5" />
//               <span>Create New Task</span>
//             </button>
//           )}
//         </div>

//         {/* Create Employee Modal */}
//         {showCreateEmployee && (
//           <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center p-4 z-50">
//             <div className="bg-white rounded-lg max-w-2xl w-full p-6">
//               <h3 className="text-xl font-bold mb-4">Create New Employee</h3>
//               <form onSubmit={handleCreateEmployee} className="space-y-4">
//                 <div className="grid grid-cols-2 gap-4">
//                   <div>
//                     <label className="block text-sm font-medium text-gray-700 mb-1">
//                       Employee ID
//                     </label>
//                     <input
//                       type="text"
//                       value={employeeForm.emp_id}
//                       onChange={(e) =>
//                         setEmployeeForm({
//                           ...employeeForm,
//                           emp_id: e.target.value,
//                         })
//                       }
//                       className="w-full px-3 py-2 border border-gray-300 rounded-lg"
//                       required
//                       disabled={loading}
//                     />
//                   </div>
//                   <div>
//                     <label className="block text-sm font-medium text-gray-700 mb-1">
//                       Name
//                     </label>
//                     <input
//                       type="text"
//                       value={employeeForm.name}
//                       onChange={(e) =>
//                         setEmployeeForm({
//                           ...employeeForm,
//                           name: e.target.value,
//                         })
//                       }
//                       className="w-full px-3 py-2 border border-gray-300 rounded-lg"
//                       required
//                       disabled={loading}
//                     />
//                   </div>
//                 </div>
//                 <div>
//                   <label className="block text-sm font-medium text-gray-700 mb-1">
//                     Email
//                   </label>
//                   <input
//                     type="email"
//                     value={employeeForm.email}
//                     onChange={(e) =>
//                       setEmployeeForm({
//                         ...employeeForm,
//                         email: e.target.value,
//                       })
//                     }
//                     className="w-full px-3 py-2 border border-gray-300 rounded-lg"
//                     required
//                     disabled={loading}
//                   />
//                 </div>
//                 <div className="grid grid-cols-2 gap-4">
//                   <div>
//                     <label className="block text-sm font-medium text-gray-700 mb-1">
//                       Designation
//                     </label>
//                     <input
//                       type="text"
//                       value={employeeForm.designation}
//                       onChange={(e) =>
//                         setEmployeeForm({
//                           ...employeeForm,
//                           designation: e.target.value,
//                         })
//                       }
//                       className="w-full px-3 py-2 border border-gray-300 rounded-lg"
//                       required
//                       disabled={loading}
//                     />
//                   </div>
//                   <div>
//                     <label className="block text-sm font-medium text-gray-700 mb-1">
//                       Manager ID (Optional)
//                     </label>
//                     <input
//                       type="text"
//                       value={employeeForm.mgr_id}
//                       onChange={(e) =>
//                         setEmployeeForm({
//                           ...employeeForm,
//                           mgr_id: e.target.value,
//                         })
//                       }
//                       className="w-full px-3 py-2 border border-gray-300 rounded-lg"
//                       disabled={loading}
//                     />
//                   </div>
//                 </div>
//                 <div className="flex justify-end space-x-3 pt-4">
//                   <button
//                     type="button"
//                     onClick={() => setShowCreateEmployee(false)}
//                     className="px-4 py-2 border border-gray-300 rounded-lg hover:bg-gray-50 disabled:opacity-50"
//                     disabled={loading}
//                   >
//                     Cancel
//                   </button>
//                   <button
//                     type="submit"
//                     disabled={loading}
//                     className="px-4 py-2 bg-indigo-600 text-white rounded-lg hover:bg-indigo-700 disabled:opacity-50"
//                   >
//                     {loading ? "Creating..." : "Create Employee"}
//                   </button>
//                 </div>
//               </form>
//             </div>
//           </div>
//         )}

//         {/* Edit Employee Modal */}
//         {showEditEmployee && (
//           <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center p-4 z-50">
//             <div className="bg-white rounded-lg max-w-2xl w-full p-6">
//               <h3 className="text-xl font-bold mb-4">Edit Employee</h3>
//               <form onSubmit={handleEditEmployee} className="space-y-4">
//                 <div className="grid grid-cols-2 gap-4">
//                   <div>
//                     <label className="block text-sm font-medium text-gray-700 mb-1">
//                       Employee ID
//                     </label>
//                     <input
//                       type="text"
//                       value={employeeForm.emp_id}
//                       className="w-full px-3 py-2 border border-gray-300 rounded-lg bg-gray-100"
//                       disabled
//                     />
//                   </div>
//                   <div>
//                     <label className="block text-sm font-medium text-gray-700 mb-1">
//                       Name
//                     </label>
//                     <input
//                       type="text"
//                       value={employeeForm.name}
//                       onChange={(e) =>
//                         setEmployeeForm({
//                           ...employeeForm,
//                           name: e.target.value,
//                         })
//                       }
//                       className="w-full px-3 py-2 border border-gray-300 rounded-lg"
//                       required
//                       disabled={loading}
//                     />
//                   </div>
//                 </div>
//                 <div>
//                   <label className="block text-sm font-medium text-gray-700 mb-1">
//                     Email
//                   </label>
//                   <input
//                     type="email"
//                     value={employeeForm.email}
//                     onChange={(e) =>
//                       setEmployeeForm({
//                         ...employeeForm,
//                         email: e.target.value,
//                       })
//                     }
//                     className="w-full px-3 py-2 border border-gray-300 rounded-lg"
//                     required
//                     disabled={loading}
//                   />
//                 </div>
//                 <div className="grid grid-cols-2 gap-4">
//                   <div>
//                     <label className="block text-sm font-medium text-gray-700 mb-1">
//                       Designation
//                     </label>
//                     <input
//                       type="text"
//                       value={employeeForm.designation}
//                       onChange={(e) =>
//                         setEmployeeForm({
//                           ...employeeForm,
//                           designation: e.target.value,
//                         })
//                       }
//                       className="w-full px-3 py-2 border border-gray-300 rounded-lg"
//                       required
//                       disabled={loading}
//                     />
//                   </div>
//                   <div>
//                     <label className="block text-sm font-medium text-gray-700 mb-1">
//                       Manager ID
//                     </label>
//                     <input
//                       type="text"
//                       value={employeeForm.mgr_id}
//                       onChange={(e) =>
//                         setEmployeeForm({
//                           ...employeeForm,
//                           mgr_id: e.target.value,
//                         })
//                       }
//                       className="w-full px-3 py-2 border border-gray-300 rounded-lg"
//                       disabled={loading}
//                     />
//                   </div>
//                 </div>
//                 <div className="flex justify-end space-x-3 pt-4">
//                   <button
//                     type="button"
//                     onClick={() => {
//                       setShowEditEmployee(false);
//                       setSelectedEmployee(null);
//                     }}
//                     className="px-4 py-2 border border-gray-300 rounded-lg hover:bg-gray-50 disabled:opacity-50"
//                     disabled={loading}
//                   >
//                     Cancel
//                   </button>
//                   <button
//                     type="submit"
//                     disabled={loading}
//                     className="px-4 py-2 bg-indigo-600 text-white rounded-lg hover:bg-indigo-700 disabled:opacity-50"
//                   >
//                     {loading ? "Updating..." : "Update Employee"}
//                   </button>
//                 </div>
//               </form>
//             </div>
//           </div>
//         )}

//         {/* Create Task Modal */}
//         {showCreateTask && (
//           <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center p-4 z-50">
//             <div className="bg-white rounded-lg max-w-2xl w-full p-6">
//               <h3 className="text-xl font-bold mb-4">Create New Task</h3>
//               <form onSubmit={handleCreateTask} className="space-y-4">
//                 <div className="grid grid-cols-2 gap-4">
//                   <div>
//                     <label className="block text-sm font-medium text-gray-700 mb-1">
//                       Task ID
//                     </label>
//                     <input
//                       type="text"
//                       value={taskForm.task_id}
//                       onChange={(e) =>
//                         setTaskForm({ ...taskForm, task_id: e.target.value })
//                       }
//                       className="w-full px-3 py-2 border border-gray-300 rounded-lg"
//                       required
//                     />
//                   </div>
//                   <div>
//                     <label className="block text-sm font-medium text-gray-700 mb-1">
//                       Priority
//                     </label>
//                     <select
//                       value={taskForm.priority}
//                       onChange={(e) =>
//                         setTaskForm({ ...taskForm, priority: e.target.value })
//                       }
//                       className="w-full px-3 py-2 border border-gray-300 rounded-lg"
//                     >
//                       <option value="HIGH">High</option>
//                       <option value="MEDIUM">Medium</option>
//                       <option value="LOW">Low</option>
//                     </select>
//                   </div>
//                 </div>
//                 <div>
//                   <label className="block text-sm font-medium text-gray-700 mb-1">
//                     Task Name
//                   </label>
//                   <input
//                     type="text"
//                     value={taskForm.name}
//                     onChange={(e) =>
//                       setTaskForm({ ...taskForm, name: e.target.value })
//                     }
//                     className="w-full px-3 py-2 border border-gray-300 rounded-lg"
//                     required
//                   />
//                 </div>
//                 <div>
//                   <label className="block text-sm font-medium text-gray-700 mb-1">
//                     Description
//                   </label>
//                   <textarea
//                     value={taskForm.description}
//                     onChange={(e) =>
//                       setTaskForm({ ...taskForm, description: e.target.value })
//                     }
//                     className="w-full px-3 py-2 border border-gray-300 rounded-lg"
//                     rows="3"
//                     required
//                   />
//                 </div>
//                 <div className="grid grid-cols-2 gap-4">
//                   <div>
//                     <label className="block text-sm font-medium text-gray-700 mb-1">
//                       Assign To (Employee ID)
//                     </label>
//                     <input
//                       type="text"
//                       value={taskForm.assigned_to}
//                       onChange={(e) =>
//                         setTaskForm({
//                           ...taskForm,
//                           assigned_to: e.target.value,
//                         })
//                       }
//                       className="w-full px-3 py-2 border border-gray-300 rounded-lg"
//                       required
//                     />
//                   </div>
//                   <div>
//                     <label className="block text-sm font-medium text-gray-700 mb-1">
//                       Expected Closure
//                     </label>
//                     <input
//                       type="date"
//                       value={taskForm.expected_closure}
//                       onChange={(e) =>
//                         setTaskForm({
//                           ...taskForm,
//                           expected_closure: e.target.value,
//                         })
//                       }
//                       className="w-full px-3 py-2 border border-gray-300 rounded-lg"
//                       required
//                     />
//                   </div>
//                 </div>
//                 <div className="flex justify-end space-x-3 pt-4">
//                   <button
//                     type="button"
//                     onClick={() => setShowCreateTask(false)}
//                     className="px-4 py-2 border border-gray-300 rounded-lg hover:bg-gray-50"
//                   >
//                     Cancel
//                   </button>
//                   <button
//                     type="submit"
//                     disabled={loading}
//                     className="px-4 py-2 bg-green-600 text-white rounded-lg hover:bg-green-700 disabled:opacity-50"
//                   >
//                     {loading ? "Creating..." : "Create Task"}
//                   </button>
//                 </div>
//               </form>
//             </div>
//           </div>
//         )}

//         {/* Employees Tab */}
//         {activeTab === "employees" && (
//           <div className="bg-white rounded-lg shadow overflow-hidden">
//             <div className="overflow-x-auto">
//               <table className="w-full">
//                 <thead className="bg-gray-50 border-b border-gray-200">
//                   <tr>
//                     <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">
//                       Employee ID
//                     </th>
//                     <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">
//                       Name
//                     </th>
//                     <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">
//                       Email
//                     </th>
//                     <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">
//                       Designation
//                     </th>
//                     <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">
//                       Manager
//                     </th>
//                     <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">
//                       Actions
//                     </th>
//                   </tr>
//                 </thead>
//                 <tbody className="divide-y divide-gray-200">
//                   {employees.length === 0 ? (
//                     <tr>
//                       <td
//                         colSpan="6"
//                         className="px-6 py-8 text-center text-gray-500"
//                       >
//                         No employees found. Create your first employee to get
//                         started.
//                       </td>
//                     </tr>
//                   ) : (
//                     employees.map((emp) => (
//                       <tr key={emp.emp_id} className="hover:bg-gray-50">
//                         <td className="px-6 py-4 text-sm font-medium text-gray-900">
//                           {emp.emp_id}
//                         </td>
//                         <td className="px-6 py-4 text-sm text-gray-900">
//                           {emp.name}
//                         </td>
//                         <td className="px-6 py-4 text-sm text-gray-900">
//                           {emp.email}
//                         </td>
//                         <td className="px-6 py-4 text-sm text-gray-900">
//                           {emp.designation}
//                         </td>
//                         <td className="px-6 py-4 text-sm text-gray-900">
//                           {emp.mgr_id || "-"}
//                         </td>
//                         <td className="px-6 py-4">
//                           <div className="flex items-center space-x-2">
//                             <button
//                               onClick={() => openEditModal(emp)}
//                               className="text-indigo-600 hover:text-indigo-900 disabled:opacity-50"
//                               disabled={loading}
//                             >
//                               <Edit2 className="w-4 h-4" />
//                             </button>
//                             <button
//                               onClick={() => handleDeleteEmployee(emp.emp_id)}
//                               className="text-red-600 hover:text-red-900 disabled:opacity-50"
//                               disabled={loading}
//                             >
//                               <Trash2 className="w-4 h-4" />
//                             </button>
//                           </div>
//                         </td>
//                       </tr>
//                     ))
//                   )}
//                 </tbody>
//               </table>
//             </div>
//           </div>
//         )}

//         {/* Tasks Tab */}
//         {activeTab === "tasks" && (
//           <>
//             {/* View Toggle */}
//             <div className="flex justify-end mb-4 gap-2">
//               <button
//                 onClick={() => setViewMode("KANBAN")}
//                 className={`px-4 py-2 rounded-lg text-sm font-medium ${
//                   viewMode === "KANBAN"
//                     ? "bg-emerald-600 text-white"
//                     : "bg-white border"
//                 }`}
//               >
//                 Kanban
//               </button>
//               <button
//                 onClick={() => setViewMode("LIST")}
//                 className={`px-4 py-2 rounded-lg text-sm font-medium ${
//                   viewMode === "LIST"
//                     ? "bg-indigo-600 text-white"
//                     : "bg-white border"
//                 }`}
//               >
//                 List
//               </button>
//               <button
//                 onClick={() => setViewMode("PERFORMANCE")}
//                 className={`px-4 py-2 rounded-lg text-sm font-medium ${
//                   viewMode === "PERFORMANCE"
//                     ? "bg-orange-600 text-white"
//                     : "bg-white border"
//                 }`}
//               >
//                 Performance
//               </button>
//             </div>

//             {/* KANBAN View (Read-only) */}
//             {viewMode === "KANBAN" && (
//               <div className="grid grid-cols-4 gap-6">
//                 {STATUS_ORDER.map((status) => (
//                   <TaskColumn
//                     key={status}
//                     status={status}
//                     count={tasksByStatus[status].length}
//                   >
//                     {tasksByStatus[status].map((task) => (
//                       <TaskCard
//                         key={task.task_id}
//                         task={task}
//                         token={token}
//                         draggable={false} // Admin cannot drag/change status
//                         // No onUpdateTask for admin - read-only
//                       />
//                     ))}
//                   </TaskColumn>
//                 ))}
//               </div>
//             )}

//             {/* LIST View */}
//             {viewMode === "LIST" && (
//               <div className="bg-white rounded-xl shadow border overflow-x-auto">
//                 <table className="w-full text-sm">
//                   <thead className="bg-gray-100">
//                     <tr>
//                       <th className="px-4 py-3 text-left">Task</th>
//                       <th className="px-4 py-3 text-left">Assigned To</th>
//                       <th className="px-4 py-3 text-left">Status</th>
//                       <th className="px-4 py-3 text-left">Priority</th>
//                       <th className="px-4 py-3 text-left">Created</th>
//                       <th className="px-4 py-3 text-left">Deadline</th>
//                     </tr>
//                   </thead>
//                   <tbody>
//                     {sortedTasksByDate.map((task) => (
//                       <tr key={task.task_id} className="border-t">
//                         <td className="px-4 py-3">{task.name}</td>
//                         <td className="px-4 py-3">{task.assigned_to}</td>
//                         <td className="px-4 py-3">{task.status}</td>
//                         <td className="px-4 py-3">{task.priority}</td>
//                         <td className="px-4 py-3">
//                           {task.created_at
//                             ? new Date(task.created_at).toLocaleDateString()
//                             : "—"}
//                         </td>
//                         <td className="px-4 py-3">
//                           {task.expected_closure
//                             ? new Date(
//                                 task.expected_closure
//                               ).toLocaleDateString()
//                             : "—"}
//                         </td>
//                       </tr>
//                     ))}
//                   </tbody>
//                 </table>
//               </div>
//             )}

//             {/* PERFORMANCE View */}
//             {viewMode === "PERFORMANCE" && (
//               <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
//                 <PerformancePieChart
//                   tasksByStatus={tasksByStatus}
//                   title="Team Task Status"
//                 />
//                 <EmployeePerformanceBarChart
//                   tasks={adminTasks}
//                   title="Employee Completion Rates"
//                 />
//               </div>
//             )}
//           </>
//         )}

//         {/* Assign Tab (Placeholder) */}
//         {activeTab === "assign" && (
//           <div className="bg-white rounded-lg shadow p-6">
//             <h3 className="text-lg font-semibold mb-4">
//               Assign Employee to Manager
//             </h3>
//             <p className="text-gray-600 mb-4">
//               Select an employee and assign them to a manager
//             </p>
//             <div className="text-center text-gray-500 py-8">
//               Feature coming soon - Use the employee edit form to update manager
//               assignments
//             </div>
//           </div>
//         )}
//       </main>
//     </div>
//   );
// };

// export default AdminDashboard;
