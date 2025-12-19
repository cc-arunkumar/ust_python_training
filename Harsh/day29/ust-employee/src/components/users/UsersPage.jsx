import React, { useState, useEffect } from "react";
import { Plus, Edit2, Trash2, AlertCircle, Search } from "lucide-react";
import { useAuth } from "../../context/AuthContext";
import ApiService from "../../services/api";
import UserModal from "./UserModal";
import toast from "react-hot-toast";

const UsersPage = () => {
  const { hasRole } = useAuth();
  const isAdmin = hasRole && hasRole("ADMIN");

  const [users, setUsers] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");
  const [showModal, setShowModal] = useState(false);
  const [editingUser, setEditingUser] = useState(null);
  const [query, setQuery] = useState("");

  useEffect(() => {
    fetchUsers();
  }, []);

  const fetchUsers = async () => {
    setLoading(true);
    try {
      const data = await ApiService.getUsers();
      setUsers(Array.isArray(data) ? data : []);
      setError("");
    } catch (err) {
      setError(err.message || "Failed to load users");
      toast.error(err.message || "Failed to load users");
    } finally {
      setLoading(false);
    }
  };

  const handleDelete = async (id) => {
    if (!window.confirm("Are you sure you want to delete this user?")) return;
    try {
      await ApiService.deleteUser(id);
      toast.success("User deleted successfully");
      fetchUsers();
    } catch (err) {
      toast.error(err.message || "Failed to delete user");
    }
  };

  const handleEdit = (u) => {
    setEditingUser(u);
    setShowModal(true);
  };

  const handleAdd = () => {
    setEditingUser(null);
    setShowModal(true);
  };

  const filtered = users.filter((u) => {
    if (!query.trim()) return true;
    const q = query.trim().toLowerCase();
    return (
      (u.full_name && u.full_name.toLowerCase().includes(q)) ||
      (u.email && u.email.toLowerCase().includes(q)) ||
      (u.role && u.role.toLowerCase().includes(q))
    );
  });

  return (
    <div className="p-6 bg-gray-50 min-h-screen">
      <div className="flex flex-col md:flex-row justify-between items-start md:items-center gap-4 mb-6">
        <div>
          <h1 className="text-3xl font-bold text-gray-900">Users</h1>
          <p className="text-gray-500 mt-1">Manage application users</p>
        </div>

        <div className="flex items-center gap-3 w-full md:w-auto">
          <div className="relative w-full md:w-64">
            <input
              className="px-3 py-2 rounded-lg w-full border border-slate-200 focus:outline-none"
              placeholder="Search users by name, email or role..."
              value={query}
              onChange={(e) => setQuery(e.target.value)}
            />
            <div className="absolute right-2 top-2 text-slate-400 pointer-events-none">
              <Search size={16} />
            </div>
          </div>

          {isAdmin && (
            <button
              onClick={handleAdd}
              className="bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700 transition flex items-center gap-2"
            >
              <Plus size={18} />
              Add User
            </button>
          )}
        </div>
      </div>

      {error && (
        <div className="bg-red-100 border border-red-300 text-red-700 px-4 py-3 rounded mb-4 flex items-center gap-2">
          <AlertCircle size={20} />
          <span>{error}</span>
        </div>
      )}

      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
        {loading ? (
          <div className="col-span-full text-center py-12">Loading...</div>
        ) : filtered.length === 0 ? (
          <div className="col-span-full text-center py-12 bg-white rounded-lg shadow">
            No users found
          </div>
        ) : (
          filtered.map((u) => (
            <div
              key={u.id ?? u.user_id}
              className="bg-white rounded-lg shadow p-4 flex flex-col justify-between hover:shadow-lg transition"
            >
              <div>
                <div className="flex items-center gap-3">
                  <div className="w-10 h-10 rounded-full bg-indigo-600 text-white flex items-center justify-center font-semibold">
                    {u.full_name ? u.full_name.charAt(0).toUpperCase() : "-"}
                  </div>
                  <div className="truncate">
                    <div className="font-semibold text-gray-900 truncate max-w-[14rem]">
                      {u.full_name || u.email}
                    </div>
                    <div className="text-xs text-slate-500">{u.email}</div>
                  </div>
                </div>

                <div className="mt-3 text-sm text-slate-600">
                  Role:{" "}
                  <span className="font-medium text-slate-800">
                    {u.role || "-"}
                  </span>
                </div>
              </div>

              {isAdmin && (
                <div className="flex justify-end gap-2 mt-4">
                  <button
                    onClick={() => handleEdit(u)}
                    className="text-blue-500 hover:text-blue-700"
                  >
                    <Edit2 size={18} />
                  </button>
                  <button
                    onClick={() => handleDelete(u.id ?? u.user_id)}
                    className="text-red-500 hover:text-red-700"
                  >
                    <Trash2 size={18} />
                  </button>
                </div>
              )}
            </div>
          ))
        )}
      </div>

      {showModal && (
        <UserModal
          user={editingUser}
          onClose={() => setShowModal(false)}
          onSuccess={() => {
            setShowModal(false);
            fetchUsers();
          }}
        />
      )}
    </div>
  );
};

export default UsersPage;
