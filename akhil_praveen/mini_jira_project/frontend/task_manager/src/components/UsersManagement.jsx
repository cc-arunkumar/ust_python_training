import React, { useState, useEffect } from "react";
import { Plus, Edit2, Trash2, User, Mail } from "lucide-react";
import UserFormModal from "./UserFormModal";
import api from "../api/api";
import { publish } from "../utils/events";

function UsersManagement({ onRefresh, role, users: propUsers }) {
  const [users, setUsers] = useState(propUsers || []);
  const [loading, setLoading] = useState(false);
  const [showForm, setShowForm] = useState(false);
  const [editingUser, setEditingUser] = useState(null);

  const load = async () => {
    setLoading(true);
    try {
      const data = await api.getUsers();
      // backend may return array or object { users: [...] }
      const list = Array.isArray(data) ? data : data?.users || [];
      setUsers(list);
    } catch (err) {
      console.error("Failed to load users", err);
      alert(err.message || "Failed to load users");
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    // if parent provided users, use them; otherwise fetch
    if (propUsers && Array.isArray(propUsers)) {
      setUsers(propUsers);
      setLoading(false);
      return;
    }
    load();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [propUsers]);

  const handleEdit = (u) => {
    setEditingUser(u);
    setShowForm(true);
  };

  const handleDelete = async (id) => {
    if (!confirm("Delete this user?")) return;
    try {
      await api.deleteUser(id);
      await load();
      onRefresh && onRefresh();
      try {
        publish("app:updated", { resource: "users", id });
      } catch (e) {}
    } catch (err) {
      alert(err.message || "Delete failed");
    }
  };

  const handleStatusChange = async (id, status) => {
    try {
      await api.updateUser(id, { status });
      await load();
      onRefresh && onRefresh();
      try {
        publish("app:updated", { resource: "users", id });
      } catch (e) {}
    } catch (err) {
      alert(err.message || "Status update failed");
    }
  };

  const handleSave = async (formData) => {
    try {
      if (editingUser) {
        await api.updateUser(
          editingUser.id || editingUser.user_id || editingUser.uid,
          formData
        );
      } else {
        await api.createUser(formData);
      }
      setShowForm(false);
      setEditingUser(null);
      await load();
      onRefresh && onRefresh();
      try {
        publish("app:updated", { resource: "users" });
      } catch (e) {}
    } catch (err) {
      alert(err.message || "Save failed");
    }
  };

  return (
    <div className="p-6">
      <div className="flex justify-between items-center mb-6 bg-white rounded-2xl p-5 shadow-sm border border-gray-100">
        <div className="flex items-center gap-3">
          <div className="p-3 bg-gradient-to-br from-indigo-500 to-purple-600 rounded-xl shadow-md">
            <User className="text-white" size={24} />
          </div>
          <div>
            <h2 className="text-2xl font-bold text-gray-800">
              User Management
            </h2>
            <p className="text-sm text-gray-600">Manage application users</p>
          </div>
        </div>

        {role && role.includes("ADMIN") ? (
          <button
            onClick={() => setShowForm(true)}
            className="bg-gradient-to-r from-indigo-600 to-purple-600 text-white px-5 py-3 rounded-xl flex items-center gap-2 hover:shadow-lg"
          >
            <Plus size={20} /> Create User
          </button>
        ) : (
          <div />
        )}
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-5">
        {users.map((u) => (
          <div
            key={u.id || u.user_id || u.uid}
            className="bg-white rounded-2xl p-6 shadow-md hover:shadow-xl transition-all border border-gray-100 group hover:scale-105"
          >
            <div className="flex items-start justify-between mb-4">
              <div className="flex items-center gap-3">
                <div className="w-12 h-12 bg-gradient-to-br from-indigo-500 to-purple-600 rounded-full flex items-center justify-center text-white font-bold text-lg shadow-md">
                  {(u.username || u.name || "U").charAt(0).toUpperCase()}
                </div>
                <div>
                  <h3 className="font-bold text-gray-800 text-lg">
                    {u.username || u.name}
                  </h3>
                  <span className="text-xs text-gray-500 font-medium">
                    ID: {u.id || u.user_id || u.uid}
                  </span>
                </div>
              </div>

              <div className="flex gap-1 opacity-0 group-hover:opacity-100 transition-opacity items-center">
                <button
                  onClick={() => handleEdit(u)}
                  className="p-2 rounded-lg text-blue-600 hover:bg-blue-50"
                >
                  <Edit2 size={18} />
                </button>
                <button
                  onClick={() => handleDelete(u.id || u.user_id || u.uid)}
                  className="p-2 rounded-lg text-red-600 hover:bg-red-50"
                >
                  <Trash2 size={18} />
                </button>
                <select
                  value={u.status || "ACTIVE"}
                  onChange={(e) =>
                    handleStatusChange(
                      u.id || u.user_id || u.uid,
                      e.target.value
                    )
                  }
                  className="p-2 rounded-lg border-gray-200 bg-white text-sm"
                >
                  <option value="ACTIVE">Active</option>
                  <option value="INACTIVE">InActive</option>
                </select>
              </div>
            </div>

            <div className="space-y-3">
              <div className="flex items-center gap-2 text-sm">
                <Mail size={16} className="text-gray-400" />
                <span className="text-gray-700">{u.email}</span>
              </div>
              <div className="text-sm text-gray-600">
                Role:{" "}
                <span className="font-medium text-gray-800">{u.role}</span>
              </div>
            </div>
          </div>
        ))}
      </div>

      {users.length === 0 && (
        <div className="text-center py-16 bg-white rounded-2xl border-2 border-dashed border-gray-200">
          <User size={48} className="mx-auto text-gray-300 mb-4" />
          <h3 className="text-xl font-bold text-gray-600 mb-2">No Users Yet</h3>
          <p className="text-gray-500 mb-4">Start by creating users</p>
          {role && role.includes("ADMIN") && (
            <button
              onClick={() => setShowForm(true)}
              className="bg-gradient-to-r from-indigo-600 to-purple-600 text-white px-5 py-2 rounded-lg inline-flex items-center gap-2 hover:shadow-lg"
            >
              <Plus size={18} /> Create First User
            </button>
          )}
        </div>
      )}

      {showForm && (
        <UserFormModal
          user={editingUser}
          onClose={() => {
            setShowForm(false);
            setEditingUser(null);
          }}
          onSave={handleSave}
        />
      )}
    </div>
  );
}

export default UsersManagement;
