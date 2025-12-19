import React, { useState } from "react";
import { X, AlertCircle, UserPlus } from "lucide-react";
import ApiService from "../../services/api";
import toast from "react-hot-toast";
import { useAuth } from "../../context/AuthContext";

const inputClass =
  "mt-1 w-full rounded-xl border border-gray-200 bg-white px-3 py-2 text-sm " +
  "focus:border-blue-500 focus:ring-1 focus:ring-blue-500 outline-none transition";

const UserModal = ({ user, onClose, onSuccess }) => {
  const { hasRole } = useAuth();
  const isAdmin = hasRole && hasRole("ADMIN");

  const [formData, setFormData] = useState({
    id: user?.id ?? user?.user_id ?? "",
    email: user?.email ?? "",
    full_name: user?.full_name ?? user?.name ?? "",
    role: user?.role ?? (user?.roles ? user.roles.join(",") : ""),
    password: "",
  });

  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleChange = (field, value) => {
    setFormData((prev) => ({ ...prev, [field]: value }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!isAdmin) return;
    setLoading(true);
    setError("");

    try {
      const payload = {
        email: formData.email.trim(),
        full_name: formData.full_name.trim(),
        role: formData.role.trim(),
      };

      if (!user) {
        if (formData.password) payload.password = formData.password;
        await ApiService.createUser(payload);
        toast.success("User created successfully");
      } else {
        await ApiService.updateUser(user.id ?? user.user_id, payload);
        toast.success("User updated successfully");
      }

      onSuccess();
    } catch (err) {
      const msg = err?.message || "Operation failed";
      setError(msg);
      toast.error(msg);
    } finally {
      setLoading(false);
    }
  };

  const handleDelete = async () => {
    if (!user || !isAdmin) return;
    if (!window.confirm(`Delete user ${user.email || user.full_name}?`)) return;
    setLoading(true);
    try {
      await ApiService.deleteUser(user.id ?? user.user_id);
      toast.success("User deleted successfully");
      onSuccess();
    } catch (err) {
      const msg = err?.message || "Operation failed";
      setError(msg);
      toast.error(msg);
    } finally {
      setLoading(false);
    }
  };

  if (!isAdmin) {
    return (
      <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/40 backdrop-blur-sm">
        <div className="w-full max-w-xl rounded-2xl bg-white shadow-xl border border-gray-200 p-6">
          <div className="text-center text-gray-600">
            <h2 className="text-lg font-semibold mb-4">Access Denied</h2>
            <p>You do not have permission to manage users.</p>
            <button
              onClick={onClose}
              className="mt-4 text-blue-600 hover:text-blue-700"
            >
              Close
            </button>
          </div>
        </div>
      </div>
    );
  }

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/40 backdrop-blur-sm">
      <div className="w-full max-w-xl rounded-2xl bg-white shadow-xl border border-gray-200">
        <div className="flex items-center justify-between px-6 py-4 border-b border-gray-200">
          <div className="flex items-center gap-2">
            <UserPlus className="text-blue-600" />
            <h2 className="text-lg font-semibold text-gray-800">
              {user ? "Edit User" : "Add User"}
            </h2>
          </div>
          <button
            onClick={onClose}
            className="text-gray-400 hover:text-gray-700"
          >
            <X />
          </button>
        </div>

        {error && (
          <div className="mx-6 mt-4 flex items-center gap-2 rounded-xl bg-red-50 px-4 py-3 text-red-700 border border-red-200">
            <AlertCircle size={18} />
            <span className="text-sm">{error}</span>
          </div>
        )}

        <form onSubmit={handleSubmit} className="px-6 py-6 space-y-4">
          {!user && (
            <div>
              <label className="text-sm font-medium text-gray-600">
                Email *
              </label>
              <input
                type="email"
                value={formData.email}
                onChange={(e) => handleChange("email", e.target.value)}
                required
                className={inputClass}
              />
            </div>
          )}

          <div>
            <label className="text-sm font-medium text-gray-600">
              Full name *
            </label>
            <input
              type="text"
              value={formData.full_name}
              onChange={(e) => handleChange("full_name", e.target.value)}
              required
              className={inputClass}
            />
          </div>

          <div>
            <label className="text-sm font-medium text-gray-600">Role *</label>
            <input
              type="text"
              value={formData.role}
              onChange={(e) => handleChange("role", e.target.value)}
              required
              className={inputClass}
            />
          </div>

          {!user && (
            <div>
              <label className="text-sm font-medium text-gray-600">
                Password
              </label>
              <input
                type="password"
                value={formData.password}
                onChange={(e) => handleChange("password", e.target.value)}
                className={inputClass}
                placeholder="Optional - set password for new user"
              />
            </div>
          )}

          <div className="flex gap-3 pt-6">
            <button
              type="button"
              onClick={onClose}
              className="flex-1 rounded-xl border border-gray-300 py-2 text-sm font-medium text-gray-700 hover:bg-gray-50 transition"
            >
              Cancel
            </button>
            <button
              type="submit"
              disabled={loading}
              className="flex-1 rounded-xl bg-blue-600 py-2 text-sm font-medium text-white hover:bg-blue-700 disabled:bg-blue-400 transition"
            >
              {loading ? "Saving..." : "Save"}
            </button>

            {user && (
              <button
                type="button"
                onClick={handleDelete}
                disabled={loading}
                className="flex-1 rounded-xl bg-red-600 py-2 text-sm font-medium text-white hover:bg-red-700 disabled:bg-red-400 transition"
              >
                {loading ? "Deleting..." : "Delete"}
              </button>
            )}
          </div>
        </form>
      </div>
    </div>
  );
};

export default UserModal;
