import { useEffect, useState } from "react";
import { useAuth } from "../context/AuthContext";
import { userAPI } from "../services/api";
import { Plus, Search, Edit, Trash2, Shield } from "lucide-react";
import type { User } from "../types";

const Users = () => {
  const { user: currentUser, activeRole } = useAuth();
  const [users, setUsers] = useState<User[]>([]);
  const [filteredUsers, setFilteredUsers] = useState<User[]>([]);
  const [isLoading, setIsLoading] = useState(true);
  const [searchTerm, setSearchTerm] = useState("");
  const [showCreateModal, setShowCreateModal] = useState(false);
  const [editingUser, setEditingUser] = useState<User | null>(null);

  useEffect(() => {
    const fetchUsers = async () => {
      if (!activeRole) return;

      try {
        const role = activeRole;
        const data = await userAPI.getAll(role);
        setUsers(data);
        setFilteredUsers(data);
      } catch (error) {
        console.error("Error fetching users:", error);
      } finally {
        setIsLoading(false);
      }
    };

    fetchUsers();
  }, [currentUser, activeRole]);

  useEffect(() => {
    if (searchTerm) {
      const filtered = users.filter(
        (u) =>
          u.e_id?.toString().includes(searchTerm) ||
          u.role?.some((r) =>
            r.toLowerCase().includes(searchTerm.toLowerCase())
          ) ||
          u.status?.toLowerCase().includes(searchTerm.toLowerCase())
      );
      setFilteredUsers(filtered);
    } else {
      setFilteredUsers(users);
    }
  }, [searchTerm, users]);

  const handleDelete = async (id: number) => {
    if (!activeRole || !confirm("Are you sure you want to delete this user?"))
      return;

    try {
      await userAPI.delete(id, activeRole);
      setUsers(users.filter((u) => u.e_id !== id));
      setFilteredUsers(filteredUsers.filter((u) => u.e_id !== id));
    } catch (error) {
      console.error("Error deleting user:", error);
      alert("Failed to delete user");
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
    <div className="space-y-6 animate-fade-in">
      <div className="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-4">
        <div>
          <h1 className="text-3xl font-bold text-gray-800 mb-2">Users</h1>
          <p className="text-gray-600">Manage user accounts and permissions</p>
        </div>
        {currentUser?.role?.includes("Admin") && (
          <button
            onClick={() => setShowCreateModal(true)}
            className="btn-primary flex items-center gap-2"
          >
            <Plus size={20} />
            Add User
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
              placeholder="Search users..."
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
                  Employee ID
                </th>
                <th className="text-left py-3 px-4 font-semibold text-gray-700">
                  Roles
                </th>
                <th className="text-left py-3 px-4 font-semibold text-gray-700">
                  Status
                </th>
                {currentUser?.role?.includes("Admin") && (
                  <th className="text-right py-3 px-4 font-semibold text-gray-700">
                    Actions
                  </th>
                )}
              </tr>
            </thead>
            <tbody>
              {filteredUsers.length === 0 ? (
                <tr>
                  <td colSpan={4} className="text-center py-12 text-gray-500">
                    No users found
                  </td>
                </tr>
              ) : (
                filteredUsers.map((user, index) => (
                  <tr
                    key={user.e_id}
                    className="border-b border-gray-100 hover:bg-gray-50 transition-colors animate-slide-up"
                    style={{ animationDelay: `${index * 0.05}s` }}
                  >
                    <td className="py-3 px-4 text-gray-800 font-medium">
                      {user.e_id}
                    </td>
                    <td className="py-3 px-4">
                      <div className="flex flex-wrap gap-2">
                        {user.role?.map((role) => (
                          <span
                            key={role}
                            className="px-2 py-1 bg-primary-100 text-primary-700 rounded text-xs font-medium"
                          >
                            {role}
                          </span>
                        ))}
                      </div>
                    </td>
                    <td className="py-3 px-4">
                      <span
                        className={`px-2 py-1 rounded text-xs font-medium ${
                          user.status === "active"
                            ? "bg-green-100 text-green-800"
                            : "bg-gray-100 text-gray-800"
                        }`}
                      >
                        {user.status}
                      </span>
                    </td>
                    {currentUser?.role?.includes("Admin") && (
                      <td className="py-3 px-4">
                        <div className="flex items-center justify-end gap-2">
                          <button
                            onClick={() => setEditingUser(user)}
                            className="p-2 text-primary-600 hover:bg-primary-50 rounded-lg transition-colors"
                          >
                            <Edit size={18} />
                          </button>
                          <button
                            onClick={() => user.e_id && handleDelete(user.e_id)}
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
        <UserModal
          onClose={() => setShowCreateModal(false)}
          onSuccess={() => {
            setShowCreateModal(false);
            window.location.reload();
          }}
        />
      )}

      {editingUser && (
        <UserModal
          user={editingUser}
          onClose={() => setEditingUser(null)}
          onSuccess={() => {
            setEditingUser(null);
            window.location.reload();
          }}
        />
      )}
    </div>
  );
};

const UserModal: React.FC<{
  user?: User;
  onClose: () => void;
  onSuccess: () => void;
}> = ({ user, onClose, onSuccess }) => {
  const { user: currentUser, activeRole } = useAuth();
  const [formData, setFormData] = useState({
    e_id: user?.e_id?.toString() || "",
    password: "",
    role: user?.role || [],
    status: user?.status || "active",
  });
  const [isSubmitting, setIsSubmitting] = useState(false);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!activeRole) return;

    setIsSubmitting(true);
    try {
      if (user?.e_id) {
        // Update
        await userAPI.update(user.e_id, activeRole, {
          ...formData,
          e_id: parseInt(formData.e_id),
          password: formData.password || undefined,
        });
      } else {
        // Create
        await userAPI.create(activeRole, {
          ...formData,
          e_id: parseInt(formData.e_id),
          password: formData.password,
        });
      }
      onSuccess();
    } catch (error) {
      console.error("Error saving user:", error);
      alert("Failed to save user. Please try again.");
    } finally {
      setIsSubmitting(false);
    }
  };

  const toggleRole = (role: string) => {
    if (formData.role.includes(role)) {
      setFormData({
        ...formData,
        role: formData.role.filter((r) => r !== role),
      });
    } else {
      setFormData({ ...formData, role: [...formData.role, role] });
    }
  };

  return (
    <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50 p-4 animate-fade-in">
      <div className="bg-white rounded-xl shadow-xl max-w-lg w-full animate-scale-in">
        <div className="p-6 border-b border-gray-200">
          <h2 className="text-2xl font-bold text-gray-800 flex items-center gap-2">
            <Shield size={24} />
            {user ? "Edit User" : "Add New User"}
          </h2>
        </div>
        <form onSubmit={handleSubmit} className="p-6 space-y-4">
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-2">
              Employee ID *
            </label>
            <input
              type="number"
              required
              value={formData.e_id}
              onChange={(e) =>
                setFormData({ ...formData, e_id: e.target.value })
              }
              className="input-field"
              disabled={!!user}
            />
          </div>
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-2">
              Password {!user && "*"}
            </label>
            <input
              type="password"
              required={!user}
              value={formData.password}
              onChange={(e) =>
                setFormData({ ...formData, password: e.target.value })
              }
              className="input-field"
              minLength={6}
            />
            {user && (
              <p className="text-xs text-gray-500 mt-1">
                Leave blank to keep current password
              </p>
            )}
          </div>
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-2">
              Roles *
            </label>
            <div className="space-y-2">
              {["Admin", "Manager", "Developer"].map((role) => (
                <label key={role} className="flex items-center gap-2">
                  <input
                    type="checkbox"
                    checked={formData.role.includes(role)}
                    onChange={() => toggleRole(role)}
                    className="rounded"
                  />
                  <span className="text-sm text-gray-700">{role}</span>
                </label>
              ))}
            </div>
          </div>
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-2">
              Status *
            </label>
            <select
              required
              value={formData.status}
              onChange={(e) =>
                setFormData({ ...formData, status: e.target.value })
              }
              className="input-field"
            >
              <option value="active">Active</option>
              <option value="inactive">Inactive</option>
            </select>
          </div>
          <div className="flex gap-3 pt-4">
            <button
              type="submit"
              className="btn-primary flex-1"
              disabled={isSubmitting}
            >
              {isSubmitting ? "Saving..." : user ? "Update" : "Create"}
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

export default Users;

