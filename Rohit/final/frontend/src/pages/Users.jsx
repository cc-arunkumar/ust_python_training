import { useEffect, useState } from "react";
import { listUsers, updateUserStatus, getUser } from "../api/users";
import toast from "react-hot-toast";

export default function Users() {
  const [me, setMe] = useState(null);
  const [users, setUsers] = useState([]);

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
        prev.map((u) => (u.user_id === user_id ? { ...u, status: res.status } : u))
      );
      toast.success(`Status updated to ${res.status}`);
    } catch {
      toast.error("Failed to update status");
    }
  };

  return (
    <div className="p-6 text-gray-800 dark:text-gray-200">
      <h1 className="text-2xl font-bold mb-4">Users</h1>
      {me?.role !== "ADMIN" && (
        <p className="text-sm text-gray-600 dark:text-gray-400 mb-3">
          You do not have admin rights to change statuses.
        </p>
      )}
      <div className="bg-white dark:bg-gray-800 rounded shadow overflow-x-auto">
        <table className="min-w-full">
          <thead className="bg-gray-50 dark:bg-gray-700">
            <tr>
              <th className="px-4 py-2 text-left">User ID</th>
              <th className="px-4 py-2 text-left">Emp ID</th>
              <th className="px-4 py-2 text-left">Role</th>
              <th className="px-4 py-2 text-left">Status</th>
              {me?.role === "ADMIN" && <th className="px-4 py-2 text-left">Actions</th>}
            </tr>
          </thead>
          <tbody>
            {users.map((u) => (
              <tr key={u.user_id} className="border-t dark:border-gray-700">
                <td className="px-4 py-2">{u.user_id}</td>
                <td className="px-4 py-2">{u.emp_id}</td>
                <td className="px-4 py-2">{u.role}</td>
                <td className="px-4 py-2">{u.status}</td>
                {me?.role === "ADMIN" && (
                  <td className="px-4 py-2">
                    <select
                      value={u.status}
                      onChange={(e) => handleStatus(u.user_id, e.target.value)}
                      className="border rounded p-1 text-sm dark:bg-gray-700 dark:text-gray-200"
                    >
                      <option value="ACTIVE">ACTIVE</option>
                      <option value="INACTIVE">INACTIVE</option>
                      <option value="SUSPENDED">SUSPENDED</option>
                    </select>
                  </td>
                )}
              </tr>
            ))}
            {users.length === 0 && (
              <tr>
                <td className="px-4 py-6 text-gray-500 dark:text-gray-400" colSpan={5}>
                  No users found
                </td>
              </tr>
            )}
          </tbody>
        </table>
      </div>
    </div>
  );
}
