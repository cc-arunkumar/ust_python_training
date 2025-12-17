import { useEffect, useState } from "react";
import { useNavigate, useParams } from "react-router-dom";
import {
  createUser,
  getUserById,
  updateUser,
} from "../api/user.api";
import { useAuth } from "../context/AuthContext";

const ALL_ROLES = ["ADMIN", "MANAGER", "DEVELOPER"];

export default function UserForm() {
  const { activeRole } = useAuth();
  const navigate = useNavigate();
  const { id } = useParams(); // this is e_id
  const isEdit = Boolean(id);

  // 🔐 Only ADMIN allowed
  if (activeRole !== "ADMIN") {
    return <div className="p-6">Unauthorized</div>;
  }

  const [form, setForm] = useState({
    e_id: "",
    password: "",
    roles: [],
    status: "ACTIVE",
  });

  const [loading, setLoading] = useState(false);

  // 🔹 Load user for edit
  useEffect(() => {
    if (isEdit) {
      loadUser();
    }
  }, [id]);

  const loadUser = async () => {
    setLoading(true);
    try {
      const data = await getUserById(id);
      setForm({
        e_id: data.e_id,
        password: "", // do NOT preload password
        roles: data.roles,
        status: data.status,
      });
    } finally {
      setLoading(false);
    }
  };

  // 🔹 Handle input change
  const handleChange = (e) => {
    const { name, value } = e.target;
    setForm({ ...form, [name]: value });
  };

  // 🔹 Handle role toggle
  const toggleRole = (role) => {
    setForm((prev) => ({
      ...prev,
      roles: prev.roles.includes(role)
        ? prev.roles.filter((r) => r !== role)
        : [...prev.roles, role],
    }));
  };

  // 🔹 Submit
  const handleSubmit = async (e) => {
    e.preventDefault();

    if (form.roles.length === 0) {
      alert("Select at least one role");
      return;
    }

    const payload = {
      roles: form.roles,
      status: form.status,
    };

    // Only send password if provided
    if (form.password) {
      payload.password = form.password;
    }

    try {
      if (isEdit) {
        await updateUser(id, payload);
      } else {
        await createUser({
          e_id: Number(form.e_id),
          password: form.password,
          roles: form.roles,
          status: form.status,
        });
      }

      navigate("/admin/users");
    } catch (err) {
      alert("Error saving user");
    }
  };

  return (
    <div className="p-6 max-w-xl mx-auto">
      <h2 className="text-xl font-semibold mb-4">
        {isEdit ? "Edit User" : "Create User"}
      </h2>

      <form
        onSubmit={handleSubmit}
        className="bg-white p-6 rounded shadow space-y-4"
      >
        {/* Employee ID */}
        {!isEdit && (
          <input
            name="e_id"
            type="number"
            placeholder="Employee ID"
            className="w-full border p-2 rounded"
            value={form.e_id}
            onChange={handleChange}
            required
          />
        )}

        {/* Password */}
        <input
          name="password"
          type="password"
          placeholder={
            isEdit
              ? "New Password (leave blank to keep existing)"
              : "Password"
          }
          className="w-full border p-2 rounded"
          value={form.password}
          onChange={handleChange}
          required={!isEdit}
        />

        {/* Roles */}
        <div>
          <p className="text-sm font-medium mb-2">Roles</p>
          <div className="flex gap-3 flex-wrap">
            {ALL_ROLES.map((role) => (
              <label
                key={role}
                className="flex items-center gap-2 text-sm"
              >
                <input
                  type="checkbox"
                  checked={form.roles.includes(role)}
                  onChange={() => toggleRole(role)}
                />
                {role}
              </label>
            ))}
          </div>
        </div>

        {/* Status */}
        <select
          name="status"
          className="w-full border p-2 rounded"
          value={form.status}
          onChange={handleChange}
        >
          <option value="ACTIVE">ACTIVE</option>
          <option value="INACTIVE">INACTIVE</option>
        </select>

        {/* Actions */}
        <div className="flex justify-end gap-3">
          <button
            type="button"
            onClick={() => navigate("/admin/users")}
            className="px-4 py-2 border rounded"
          >
            Cancel
          </button>

          <button
            type="submit"
            className="px-4 py-2 bg-blue-600 text-white rounded"
          >
            {isEdit ? "Update User" : "Create User"}
          </button>
        </div>
      </form>
    </div>
  );
}
