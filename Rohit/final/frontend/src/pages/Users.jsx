import { useEffect, useState } from "react";
import { listUsers, updateUserStatus, getUser } from "../api/users";
import toast from "react-hot-toast";

export default function Users() {
  const [me, setMe] = useState(null);
  const [users, setUsers] = useState([]);
  const [showCreate, setShowCreate] = useState(false);
  const [newUser, setNewUser] = useState({
    user_id: "",
    emp_id: "",
    role: "EMPLOYEE",
  });

  useEffect(() => {
    const token = localStorage.getItem("token");
    const payload = JSON.parse(atob(token.split(".")[1]));
    getUser(payload.user_id).then(setMe);
    listUsers().then(setUsers);
  }, []);

  const handleStatus = async (user_id, status) => {
    try {
      const res = await updateUserStatus(user_id, status);
      setUsers((prev) =>
        prev.map((u) =>
          u.user_id === user_id ? { ...u, status: res.status } : u
        )
      );
      toast.success(`Status updated to ${res.status}`);
    } catch {
      toast.error("Failed to update status");
    }
  };

  // Empty handlers for now
  const handleDelete = (user_id) => {};
  const handleEdit = (user_id) => {};
  const handleCreate = () => {};

  const statusBadge = (status) => {
    switch (status) {
      case "ACTIVE":
        return "bg-green-100 text-green-700 dark:bg-green-900 dark:text-green-200";
      case "INACTIVE":
        return "bg-yellow-100 text-yellow-700 dark:bg-yellow-900 dark:text-yellow-200";
      case "SUSPENDED":
        return "bg-pink-100 text-pink-700 dark:bg-pink-900 dark:text-pink-200";
      default:
        return "bg-gray-100 text-gray-700 dark:bg-gray-700 dark:text-gray-300";
    }
  };

  return (
    <div className="p-6 text-gray-800 dark:text-gray-200">
      <div className="flex justify-between items-center mb-6">
        <h1 className="text-3xl font-extrabold tracking-wide text-transparent bg-clip-text bg-gradient-to-r from-cyan-400 to-blue-500">
          Users
        </h1>
        {me?.role === "ADMIN" && (
          <button
            onClick={() => setShowCreate(true)}
            className="px-4 py-2 bg-green-600 text-white rounded-lg hover:bg-green-700"
          >
            + Create Employee
          </button>
        )}
      </div>

      <div className="bg-white dark:bg-gray-800 rounded-xl shadow-lg overflow-x-auto">
        <table className="min-w-full">
          <thead className="bg-gradient-to-r from-indigo-100 to-blue-100 dark:from-slate-700 dark:to-slate-800">
            <tr>
              <th className="px-4 py-3 text-left font-semibold">User ID</th>
              <th className="px-4 py-3 text-left font-semibold">Emp ID</th>
              <th className="px-4 py-3 text-left font-semibold">Role</th>
              <th className="px-4 py-3 text-left font-semibold">Status</th>
              {me?.role === "ADMIN" && (
                <th className="px-4 py-3 text-left font-semibold">Actions</th>
              )}
            </tr>
          </thead>
          <tbody>
            {users.map((u) => (
              <tr
                key={u.user_id}
                className="border-t dark:border-gray-700 hover:bg-indigo-50 dark:hover:bg-slate-700 transition"
              >
                <td className="px-4 py-3">{u.user_id}</td>
                <td className="px-4 py-3">{u.emp_id}</td>
                <td className="px-4 py-3">{u.role}</td>
                <td className="px-4 py-3">
                  <span
                    className={`px-3 py-1 rounded-full text-xs font-semibold ${statusBadge(
                      u.status
                    )}`}
                  >
                    {u.status}
                  </span>
                </td>
                {me?.role === "ADMIN" && (
                  <td className="px-6 py-3 flex items-center space-x-4">
                    <select
                      value={u.status}
                      onChange={(e) => handleStatus(u.user_id, e.target.value)}
                      className="border rounded-lg p-2 text-sm dark:bg-gray-700 dark:text-gray-200 focus:ring-2 focus:ring-cyan-400"
                    >
                      <option value="ACTIVE">ACTIVE</option>
                      <option value="INACTIVE">INACTIVE</option>
                      <option value="SUSPENDED">SUSPENDED</option>
                    </select>
                    <button
                      onClick={() => handleEdit(u.user_id)}
                      className="px-3 py-1 bg-blue-500 text-white rounded hover:bg-blue-600 text-sm"
                    >
                      Edit
                    </button>
                    <button
                      onClick={() => handleDelete(u.user_id)}
                      className="px-3 py-1 bg-red-500 text-white rounded hover:bg-red-600 text-sm"
                    >
                      Delete
                    </button>
                  </td>
                )}
              </tr>
            ))}
            {users.length === 0 && (
              <tr>
                <td
                  className="px-4 py-6 text-gray-500 dark:text-gray-400 text-center"
                  colSpan={5}
                >
                  No users found
                </td>
              </tr>
            )}
          </tbody>
        </table>
      </div>

      {/* Create Employee Modal */}
      {showCreate && (
        <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center">
          <div className="bg-white dark:bg-gray-800 p-6 rounded-lg shadow-lg w-96">
            <h2 className="text-xl font-bold mb-4">Create Employee</h2>
            <input
              type="text"
              placeholder="User ID"
              value={newUser.user_id}
              onChange={(e) =>
                setNewUser({ ...newUser, user_id: e.target.value })
              }
              className="w-full p-2 border rounded mb-3"
            />
            <input
              type="text"
              placeholder="Emp ID"
              value={newUser.emp_id}
              onChange={(e) =>
                setNewUser({ ...newUser, emp_id: e.target.value })
              }
              className="w-full p-2 border rounded mb-3"
            />
            <select
              value={newUser.role}
              onChange={(e) => setNewUser({ ...newUser, role: e.target.value })}
              className="w-full p-2 border rounded mb-3"
            >
              <option value="EMPLOYEE">EMPLOYEE</option>
              <option value="MANAGER">MANAGER</option>
              <option value="ADMIN">ADMIN</option>
            </select>
            <div className="flex justify-end space-x-3">
              <button
                onClick={() => setShowCreate(false)}
                className="px-4 py-2 bg-gray-300 rounded hover:bg-gray-400"
              >
                Cancel
              </button>
              <button
                onClick={handleCreate}
                className="px-4 py-2 bg-green-600 text-white rounded hover:bg-green-700"
              >
                Create
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
