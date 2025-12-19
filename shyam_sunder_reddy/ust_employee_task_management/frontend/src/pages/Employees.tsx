import { useEffect, useState } from "react";
import { useAuth } from "../context/AuthContext";
import { employeeAPI } from "../services/api";
import { Plus, Search, Edit, Trash2, X as XIcon } from "lucide-react";
import { userAPI } from "../services/api";
import type { Employee } from "../types";

const Employees = () => {
  const { activeRole } = useAuth();
  const [employees, setEmployees] = useState<Employee[]>([]);
  const [filteredEmployees, setFilteredEmployees] = useState<Employee[]>([]);
  const [isLoading, setIsLoading] = useState(true);
  const [searchTerm, setSearchTerm] = useState("");
  const [showCreateModal, setShowCreateModal] = useState(false);
  const [editingEmployee, setEditingEmployee] = useState<Employee | null>(null);

  useEffect(() => {
    const fetchEmployees = async () => {
      if (!activeRole) return;

      try {
        const role = activeRole;
        const data = await employeeAPI.getAll(role as string);
        setEmployees(data);
        setFilteredEmployees(data);
      } catch (error) {
        console.error("Error fetching employees:", error);
      } finally {
        setIsLoading(false);
      }
    };

    fetchEmployees();
  }, [activeRole]);

  useEffect(() => {
    if (searchTerm) {
      const filtered = employees.filter(
        (emp) =>
          emp.name.toLowerCase().includes(searchTerm.toLowerCase()) ||
          emp.email.toLowerCase().includes(searchTerm.toLowerCase()) ||
          emp.designation.toLowerCase().includes(searchTerm.toLowerCase())
      );
      setFilteredEmployees(filtered);
    } else {
      setFilteredEmployees(employees);
    }
  }, [searchTerm, employees]);

  const handleDelete = async (id: number) => {
    if (
      !activeRole ||
      !confirm("Are you sure you want to delete this employee?")
    )
      return;

    try {
      await employeeAPI.delete(id, activeRole as string);
      setEmployees(employees.filter((emp) => emp.e_id !== id));
      setFilteredEmployees(filteredEmployees.filter((emp) => emp.e_id !== id));
    } catch (error) {
      console.error("Error deleting employee:", error);
      alert("Failed to delete employee");
    }
  };

  if (isLoading) {
    return (
      <div className="flex items-center justify-center h-64">
        <div className="animate-spin rounded-full h-12 w-12 border-t-2 border-b-2 border-primary-500"></div>
      </div>
    );
  }

  return (
    <div className="space-y-6 animate-fade-in text-sm">
      <div className="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-4">
        <div>
          <h1 className="text-3xl font-bold text-gray-800 mb-2">Employees</h1>
          <p className="text-gray-600">Manage your team members</p>
        </div>
        {activeRole === "Admin" && (
          <button
            onClick={() => setShowCreateModal(true)}
            className="btn-primary flex items-center gap-2"
          >
            <Plus size={20} />
            Add Employee
          </button>
        )}
      </div>

      <div className="card">
        <div className="mb-6">
          <div className="relative">
            <Search
              className="absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-400"
              size={20}
            />
            <input
              type="text"
              placeholder="Search employees..."
              value={searchTerm}
              onChange={(e) => setSearchTerm(e.target.value)}
              className="input-field pl-10"
            />
          </div>
        </div>

        <div className="overflow-x-auto">
          <table className="w-full">
            <thead>
              <tr className="border-b border-gray-200">
                <th className="text-left py-3 px-4 font-semibold text-gray-700">
                  ID
                </th>
                <th className="text-left py-3 px-4 font-semibold text-gray-700">
                  Name
                </th>
                <th className="text-left py-3 px-4 font-semibold text-gray-700">
                  Email
                </th>
                <th className="text-left py-3 px-4 font-semibold text-gray-700">
                  Designation
                </th>
                <th className="text-left py-3 px-4 font-semibold text-gray-700">
                  Manager ID
                </th>
                {activeRole === "Admin" && (
                  <th className="text-right py-3 px-4 font-semibold text-gray-700">
                    Actions
                  </th>
                )}
              </tr>
            </thead>
            <tbody>
              {filteredEmployees.length === 0 ? (
                <tr>
                  <td colSpan={6} className="text-center py-12 text-gray-500">
                    No employees found
                  </td>
                </tr>
              ) : (
                filteredEmployees.map((employee, index) => (
                  <tr
                    key={employee.e_id}
                    className="border-b border-gray-100 hover:bg-gray-50 transition-colors animate-slide-up"
                    style={{ animationDelay: `${index * 0.05}s` }}
                  >
                    <td className="py-3 px-4 text-gray-800 font-medium">
                      {employee.e_id}
                    </td>
                    <td className="py-3 px-4 text-gray-800">{employee.name}</td>
                    <td className="py-3 px-4 text-gray-600">
                      {employee.email}
                    </td>
                    <td className="py-3 px-4 text-gray-600">
                      {employee.designation}
                    </td>
                    <td className="py-3 px-4 text-gray-600">
                      {employee.mgr_id}
                    </td>
                    {activeRole === "Admin" && (
                      <td className="py-3 px-4">
                        <div className="flex items-center justify-end gap-2">
                          <button
                            onClick={() => setEditingEmployee(employee)}
                            className="p-2 text-primary-600 hover:bg-primary-50 rounded-lg transition-colors"
                          >
                            <Edit size={18} />
                          </button>
                          <button
                            onClick={() =>
                              employee.e_id && handleDelete(employee.e_id)
                            }
                            className="p-2 text-red-600 hover:bg-red-50 rounded-lg transition-colors"
                          >
                            <Trash2 size={18} />
                          </button>
                        </div>
                      </td>
                    )}
                  </tr>
                ))
              )}
            </tbody>
          </table>
        </div>
      </div>

      {showCreateModal && (
        <EmployeeModal
          onClose={() => setShowCreateModal(false)}
          onSuccess={() => {
            setShowCreateModal(false);
            window.location.reload();
          }}
        />
      )}

      {editingEmployee && (
        <EmployeeModal
          employee={editingEmployee}
          onClose={() => setEditingEmployee(null)}
          onSuccess={() => {
            setEditingEmployee(null);
            window.location.reload();
          }}
        />
      )}
    </div>
  );
};

const EmployeeModal: React.FC<{
  employee?: Employee;
  onClose: () => void;
  onSuccess: () => void;
}> = ({ employee, onClose, onSuccess }) => {
  const { activeRole } = useAuth();
  const [formData, setFormData] = useState({
    name: employee?.name || "",
    email: employee?.email || "",
    designation: employee?.designation || "",
    mgr_id: employee?.mgr_id?.toString() || "",
  });
  const [assigningRole, setAssigningRole] = useState<string[]>([]);
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [managers, setManagers] = useState<{ e_id?: number; name?: string }[]>(
    []
  );

  useEffect(() => {
    let mounted = true;
    (async () => {
      try {
        // try to fetch users who have Manager role
        let mgrUsers: any[] = [];
        try {
          mgrUsers = await userAPI.getByRole("Manager");
        } catch (err) {
          // fallback: fetch all and filter client-side
          const all = await userAPI.getAll("");
          mgrUsers = (all || []).filter((u: any) => {
            const r = (u as any).role;
            if (Array.isArray(r)) return r.includes("Manager");
            if (typeof r === "string") {
              const trimmed = r.trim();
              if (trimmed.startsWith("[") && trimmed.endsWith("]")) {
                try {
                  const parsed = JSON.parse(trimmed);
                  return Array.isArray(parsed) && parsed.includes("Manager");
                } catch (_e) {
                  return trimmed.includes("Manager");
                }
              }
              return trimmed.includes("Manager");
            }
            return false;
          });
        }

        const resolved = await Promise.all(
          mgrUsers.map(async (u: any) => {
            try {
              const emp = await employeeAPI.getById(u.e_id, "Manager");
              return { e_id: u.e_id, name: emp?.name };
            } catch (_e) {
              return { e_id: u.e_id, name: undefined };
            }
          })
        );
        if (!mounted) return;
        setManagers(resolved || []);
      } catch (err) {
        console.debug("Failed to load managers:", err);
      }
    })();
    return () => {
      mounted = false;
    };
  }, []);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!activeRole) return;

    setIsSubmitting(true);
    try {
      if (employee?.e_id) {
        // Update
        await employeeAPI.update(employee.e_id, activeRole as string, {
          ...formData,
          mgr_id: parseInt(formData.mgr_id),
        });
      } else {
        // Create
        await employeeAPI.create(activeRole as string, {
          employee: {
            ...formData,
            mgr_id: parseInt(formData.mgr_id),
          },
          assigning_role: assigningRole,
        });
      }
      onSuccess();
    } catch (error) {
      console.error("Error saving employee:", error);
      alert("Failed to save employee. Please try again.");
    } finally {
      setIsSubmitting(false);
    }
  };

  return (
    <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50 p-4 animate-fade-in">
      <div
        className="relative z-10 bg-white rounded-lg shadow-xl w-full max-w-md md:max-w-[28rem] md:h-[28rem] overflow-hidden animate-scale-in"
        onClick={(e) => e.stopPropagation()}
      >
        <div className="flex items-center justify-between px-4 py-3 border-b">
          <h2 className="text-lg font-medium text-gray-800">
            {employee ? "Edit Employee" : "Add New Employee"}
          </h2>
          <button
            type="button"
            onClick={onClose}
            className="text-gray-500 hover:text-gray-700 p-1 rounded"
            aria-label="Close"
          >
            <XIcon size={16} />
          </button>
        </div>

        <form onSubmit={handleSubmit} className="flex flex-col h-full">
          <div className="px-4 py-3 overflow-auto flex-1 space-y-3 pb-20">
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-2">
                Name *
              </label>
              <input
                type="text"
                required
                value={formData.name}
                onChange={(e) =>
                  setFormData({ ...formData, name: e.target.value })
                }
                className="input-field"
                pattern="^[a-zA-Zà-ÿÀ-ÿ' -]+$"
              />
            </div>

            <div>
              <label className="block text-sm font-medium text-gray-700 mb-2">
                Email *
              </label>
              <input
                type="email"
                required
                value={formData.email}
                onChange={(e) =>
                  setFormData({ ...formData, email: e.target.value })
                }
                className="input-field"
                pattern="^[a-zA-Z0-9_.+-]+@ust\\.com$"
              />
              <p className="text-xs text-gray-500 mt-1">
                Must end with @ust.com
              </p>
            </div>

            <div className="grid grid-cols-1 md:grid-cols-2 gap-3">
              <div>
                <label className="block text-sm font-medium text-gray-700 mb-2">
                  Designation *
                </label>
                <input
                  type="text"
                  required
                  value={formData.designation}
                  onChange={(e) =>
                    setFormData({ ...formData, designation: e.target.value })
                  }
                  className="input-field"
                />
              </div>
              <div>
                <label className="block text-sm font-medium text-gray-700 mb-2">
                  Manager *
                </label>
                <select
                  value={formData.mgr_id}
                  onChange={(e) =>
                    setFormData({ ...formData, mgr_id: e.target.value })
                  }
                  className="input-field"
                >
                  <option value="">-- Select manager --</option>
                  {managers.map((m) => (
                    <option key={m.e_id} value={String(m.e_id)}>
                      {m.name ? String(m.name) : `#${m.e_id}`}
                    </option>
                  ))}
                </select>
              </div>
            </div>

            {!employee && (
              <div>
                <label className="block text-sm font-medium text-gray-700 mb-2">
                  Assign Roles
                </label>
                <div className="grid grid-cols-1 gap-2">
                  {["Admin", "Manager", "Developer"].map((role) => (
                    <label key={role} className="flex items-center gap-2">
                      <input
                        type="checkbox"
                        checked={assigningRole.includes(role)}
                        onChange={(e) => {
                          if (e.target.checked)
                            setAssigningRole([...assigningRole, role]);
                          else
                            setAssigningRole(
                              assigningRole.filter((r) => r !== role)
                            );
                        }}
                        className="rounded"
                      />
                      <span className="text-sm text-gray-700">{role}</span>
                    </label>
                  ))}
                </div>
              </div>
            )}
          </div>

          <div className="sticky bottom-0 bg-white px-4 py-3 border-t flex gap-3 z-20">
            <button
              type="submit"
              className="btn-primary flex-1"
              disabled={isSubmitting}
            >
              {isSubmitting ? "Saving..." : employee ? "Update" : "Create"}
            </button>
            <button type="button" onClick={onClose} className="btn-secondary">
              Cancel
            </button>
          </div>
        </form>
      </div>
    </div>
  );
};

export default Employees;
