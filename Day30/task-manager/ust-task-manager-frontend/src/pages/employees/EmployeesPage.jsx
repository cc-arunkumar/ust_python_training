import { useState, useEffect } from "react";
import { employeeService } from "../../services/employeeService";
import { userService } from "../../services/userService";
import { useForm } from "react-hook-form";
import { toast } from "react-toastify";
import { Users, Plus, Search, Mail, Briefcase, UserCircle } from "lucide-react";
import { useAuth } from "../../context/AuthContext";

const EmployeesPage = () => {
  const [employees, setEmployees] = useState([]);
  const [loading, setLoading] = useState(true);
  const [searchTerm, setSearchTerm] = useState("");
  const [isModalOpen, setIsModalOpen] = useState(false);

  const { register, handleSubmit, reset, setValue } = useForm();
  const { user } = useAuth();
  const [editingEmployee, setEditingEmployee] = useState(null);

  // Fetch Data
  const fetchEmployees = async () => {
    try {
      const data = await employeeService.getAll();
      // Handle different API response structures (array vs object)
      const empList = Array.isArray(data) ? data : data.data || [];

      // Also fetch users to get status (active/inactive) and role which is stored on users table
      let users = [];
      try {
        const udata = await userService.getAll();
        users = Array.isArray(udata) ? udata : udata.users || udata.data || [];
      } catch (e) {
        // ignore user fetch failures; we'll show default status
        console.error("Failed to fetch users for status merge", e);
      }

      const userMap = new Map();
      users.forEach((u) =>
        userMap.set(Number(u.emp_id), {
          status: u.status || "active",
          role: u.role || null,
        })
      );

      const merged = empList.map((emp) => ({
        ...emp,
        _user_status: userMap.get(Number(emp.emp_id))?.status || null,
        _user_role: userMap.get(Number(emp.emp_id))?.role || null,
      }));
      setEmployees(merged);
    } catch (err) {
      console.error(err);
      toast.error("Failed to load employees");
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchEmployees();
  }, []);

  const onSubmit = async (data) => {
    try {
      // If admin chose a role but didn't provide a password, generate a temporary one
      let generatedTemp = null;
      const payload = { ...data };
      if (payload.role && !payload.password) {
        generatedTemp =
          Math.random().toString(36).slice(-8) +
          Date.now().toString().slice(-4);
        payload.password = generatedTemp;
      }

      // Normalize types: manager_id should be omitted or a number (not empty string)
      if (payload.manager_id === "" || payload.manager_id == null) {
        delete payload.manager_id;
      } else if (typeof payload.manager_id === "string") {
        const n = Number(payload.manager_id);
        if (Number.isNaN(n)) delete payload.manager_id;
        else payload.manager_id = n;
      }

      // Remove empty optional fields so backend Pydantic validation won't fail
      if (payload.role === "" || payload.role == null) delete payload.role;
      if (payload.password === "" || payload.password == null)
        delete payload.password;
      if (payload.status === "" || payload.status == null)
        delete payload.status;

      if (editingEmployee) {
        await employeeService.update(editingEmployee.emp_id, payload);
        toast.success("Employee updated successfully");
      } else {
        await employeeService.create(payload);
        toast.success("Employee Added Successfully");
      }

      // Show temporary password to the admin after successful creation
      if (generatedTemp) {
        toast.info(`Temporary password for user: ${generatedTemp}`, {
          autoClose: 8000,
        });
      }

      setIsModalOpen(false);
      setEditingEmployee(null);
      reset();
      fetchEmployees();
    } catch (error) {
      // Show server error if available to help debugging
      const msg =
        error?.response?.data?.detail ||
        error?.message ||
        "Failed to add employee.";
      toast.error(msg);
    }
  };

  // Filter Logic
  const filteredEmployees = employees.filter(
    (emp) =>
      emp.name?.toLowerCase().includes(searchTerm.toLowerCase()) ||
      emp.email?.toLowerCase().includes(searchTerm.toLowerCase()) ||
      emp.emp_id?.toString().includes(searchTerm)
  );

  if (loading)
    return (
      <div className="p-10 text-center text-gray-500">Loading Employees...</div>
    );

  return (
    <div className="p-6 max-w-6xl mx-auto h-[calc(100vh-64px)] flex flex-col">
      {/* Header Section */}
      <div className="flex flex-col md:flex-row justify-between items-center mb-6 gap-4">
        <div className="flex items-center gap-3 w-full md:w-auto">
          <div className="p-2 bg-purple-100 text-purple-600 rounded-lg">
            <Users size={24} />
          </div>
          <div>
            <h1 className="text-2xl font-bold text-gray-800">Employees</h1>
            <p className="text-sm text-gray-500">Manage your team members</p>
          </div>
        </div>

        <div className="flex items-center gap-3 w-full md:w-auto">
          {/* Search Bar */}
          <div className="relative flex-1 md:w-64">
            <Search
              className="absolute left-3 top-1/2 -translate-y-1/2 text-gray-400"
              size={16}
            />
            <input
              type="text"
              placeholder="Search by name, email..."
              value={searchTerm}
              onChange={(e) => setSearchTerm(e.target.value)}
              className="pl-9 pr-4 py-2 border rounded-lg text-sm focus:ring-2 focus:ring-purple-500 w-full outline-none"
            />
          </div>

          {/* Add Button (only visible to admin) */}
          {user?.role === "admin" && (
            <button
              onClick={() => {
                reset();
                setEditingEmployee(null);
                setIsModalOpen(true);
              }}
              className="bg-purple-600 text-white px-4 py-2 rounded-lg flex items-center gap-2 hover:bg-purple-700 font-medium transition-colors shadow-sm"
            >
              <Plus size={18} />{" "}
              <span className="hidden sm:inline">Add Employee</span>
            </button>
          )}
        </div>
      </div>

      {/* Table Section */}
      <div className="flex-1 bg-white shadow-sm border border-gray-200 rounded-xl overflow-hidden flex flex-col">
        <div className="overflow-auto">
          <table className="min-w-full divide-y divide-gray-200">
            <thead className="bg-gray-50 sticky top-0 z-10">
              <tr>
                <th className="px-6 py-3 text-left text-xs font-semibold text-gray-500 uppercase tracking-wider">
                  Employee
                </th>
                <th className="px-6 py-3 text-left text-xs font-semibold text-gray-500 uppercase tracking-wider">
                  Designation
                </th>
                <th className="px-6 py-3 text-left text-xs font-semibold text-gray-500 uppercase tracking-wider">
                  Manager
                </th>
                <th className="px-6 py-3 text-left text-xs font-semibold text-gray-500 uppercase tracking-wider">
                  Status
                </th>
              </tr>
            </thead>
            <tbody className="bg-white divide-y divide-gray-200">
              {filteredEmployees.map((emp) => (
                <tr
                  key={emp.emp_id}
                  className="hover:bg-gray-50 transition-colors"
                >
                  <td className="px-6 py-4">
                    <div className="flex items-center">
                      <div className="h-10 w-10 shrink-0 rounded-full bg-linear-to-tr from-purple-500 to-indigo-500 flex items-center justify-center text-white font-bold text-sm">
                        {emp.name?.charAt(0)}
                      </div>
                      <div className="ml-4">
                        <div className="text-sm font-medium text-gray-900">
                          {emp.name}
                        </div>
                        <div className="text-sm text-gray-500 flex items-center gap-1">
                          <Mail size={12} /> {emp.email}
                        </div>
                      </div>
                    </div>
                  </td>
                  <td className="px-6 py-4">
                    <div className="flex items-center gap-2 text-sm text-gray-700">
                      <Briefcase size={14} className="text-gray-400" />
                      {emp.designation}
                    </div>
                  </td>
                  <td className="px-6 py-4">
                    {emp.manager_id ? (
                      <span className="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-blue-100 text-blue-800">
                        <UserCircle size={12} className="mr-1" /> ID:{" "}
                        {emp.manager_id}
                      </span>
                    ) : (
                      <span className="text-gray-400 text-xs italic">
                        No Manager
                      </span>
                    )}
                  </td>
                  <td className="px-6 py-4">
                    {emp._user_status ? (
                      <span
                        className={`px-2 inline-flex text-xs leading-5 font-semibold rounded-full ${
                          emp._user_status === "active"
                            ? "bg-green-100 text-green-800"
                            : "bg-red-100 text-red-800"
                        }`}
                      >
                        {emp._user_status === "active" ? "Active" : "Inactive"}
                      </span>
                    ) : (
                      <span className="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-gray-100 text-gray-700">
                        No Status
                      </span>
                    )}
                  </td>
                  {user?.role === "admin" && (
                    <td className="px-6 py-4 text-right text-sm font-medium">
                      <button
                        onClick={() => {
                          // open modal for edit
                          setEditingEmployee(emp);
                          setValue("name", emp.name);
                          setValue("email", emp.email);
                          setValue("designation", emp.designation);
                          setValue("manager_id", emp.manager_id || "");
                          setValue("role", emp._user_role || "employee");
                          setValue("status", emp._user_status || "active");
                          setIsModalOpen(true);
                        }}
                        className="text-indigo-600 hover:text-indigo-900 mr-3"
                      >
                        Edit
                      </button>
                      <button
                        onClick={async () => {
                          if (
                            !window.confirm(
                              "Are you sure you want to delete this employee?"
                            )
                          )
                            return;
                          try {
                            await employeeService.delete(emp.emp_id);
                            toast.success("Employee deleted");
                            fetchEmployees();
                          } catch (err) {
                            toast.error("Failed to delete employee");
                          }
                        }}
                        className="text-red-600 hover:text-red-900"
                      >
                        Delete
                      </button>
                    </td>
                  )}
                </tr>
              ))}
              {filteredEmployees.length === 0 && (
                <tr>
                  <td
                    colSpan="4"
                    className="px-6 py-10 text-center text-gray-500"
                  >
                    No employees found matching your search.
                  </td>
                </tr>
              )}
            </tbody>
          </table>
        </div>
      </div>

      {/* Add Employee Modal */}
      {isModalOpen && (
        <div className="fixed inset-0 bg-black bg-opacity-50 flex justify-center items-center z-50 backdrop-blur-sm p-4">
          <div className="bg-white p-6 rounded-xl shadow-xl w-full max-w-md transform transition-all">
            <h2 className="text-xl font-bold text-gray-800 mb-6 border-b pb-2">
              {editingEmployee ? "Edit Employee" : "Add New Employee"}
            </h2>

            <form onSubmit={handleSubmit(onSubmit)} className="space-y-4">
              {/* emp_id is auto-generated by the DB; do not ask the admin to enter it */}

              <div>
                <label className="block text-sm font-medium text-gray-700 mb-1">
                  Full Name
                </label>
                <input
                  {...register("name", { required: true })}
                  className="w-full border p-2 rounded-lg focus:ring-2 focus:ring-purple-500 outline-none"
                  placeholder="John Doe"
                />
              </div>

              <div>
                <label className="block text-sm font-medium text-gray-700 mb-1">
                  Email Address
                </label>
                <input
                  {...register("email", { required: true })}
                  type="email"
                  className="w-full border p-2 rounded-lg focus:ring-2 focus:ring-purple-500 outline-none"
                  placeholder="john@example.com"
                />
              </div>

              <div className="grid grid-cols-2 gap-4">
                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-1">
                    Designation
                  </label>
                  <input
                    {...register("designation", { required: true })}
                    className="w-full border p-2 rounded-lg focus:ring-2 focus:ring-purple-500 outline-none"
                    placeholder="Developer"
                  />
                </div>
                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-1">
                    Manager ID
                  </label>
                  <input
                    {...register("manager_id")}
                    className="w-full border p-2 rounded-lg focus:ring-2 focus:ring-purple-500 outline-none"
                    placeholder="Optional"
                  />
                </div>
              </div>

              <div className="grid grid-cols-2 gap-4">
                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-1">
                    Password
                  </label>
                  <input
                    {...register("password")}
                    type="password"
                    className="w-full border p-2 rounded-lg focus:ring-2 focus:ring-purple-500 outline-none"
                    placeholder="Temporary password"
                  />
                </div>
                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-1">
                    Role
                  </label>
                  <select
                    {...register("role")}
                    className="w-full border p-2 rounded-lg focus:ring-2 focus:ring-purple-500 outline-none"
                    defaultValue="employee"
                  >
                    <option value="employee">Employee</option>
                    <option value="manager">Manager</option>
                  </select>
                </div>
              </div>

              <div>
                <label className="block text-sm font-medium text-gray-700 mb-1">
                  Status
                </label>
                <select
                  {...register("status")}
                  className="w-full border p-2 rounded-lg focus:ring-2 focus:ring-purple-500 outline-none"
                  defaultValue="active"
                >
                  <option value="active">Active</option>
                  <option value="inactive">Inactive</option>
                </select>
              </div>

              <div className="flex justify-end gap-3 mt-6 pt-2">
                <button
                  type="button"
                  onClick={() => {
                    setIsModalOpen(false);
                    setEditingEmployee(null);
                    reset();
                  }}
                  className="px-4 py-2 text-gray-600 bg-gray-100 rounded-lg hover:bg-gray-200"
                >
                  Cancel
                </button>
                <button
                  type="submit"
                  className="px-4 py-2 bg-purple-600 text-white rounded-lg hover:bg-purple-700 shadow"
                >
                  Save Employee
                </button>
              </div>
            </form>
          </div>
        </div>
      )}
    </div>
  );
};

export default EmployeesPage;
