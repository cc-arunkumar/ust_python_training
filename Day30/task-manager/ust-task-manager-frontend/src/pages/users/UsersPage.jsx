import { useState, useEffect } from "react";
import { userService } from "../../services/userService";
import { useForm } from "react-hook-form";
import { toast } from "react-toastify";

const UsersPage = () => {
  const [users, setUsers] = useState([]);
  const { register, handleSubmit, reset } = useForm();
  const [isModalOpen, setIsModalOpen] = useState(false);

  const fetchUsers = async () => {
    const data = await userService.getAll();
    setUsers(data);
  };

  useEffect(() => {
    fetchUsers();
  }, []);

  const onSubmit = async (data) => {
    try {
      await userService.create(data);
      toast.success("User Created");
      setIsModalOpen(false);
      reset();
      fetchUsers();
    } catch (error) {
      toast.error("Failed. Ensure Employee ID exists first.");
    }
  };

  return (
    <div className="p-6">
      <div className="flex justify-between mb-6">
        <h1 className="text-2xl font-bold">System Users</h1>
        <button onClick={() => setIsModalOpen(true)} className="bg-green-600 text-white px-4 py-2 rounded">
          + Create Login User
        </button>
      </div>

      <table className="w-full bg-white shadow rounded">
        <thead className="bg-gray-50 border-b">
          <tr>
            <th className="p-4 text-left">Emp ID</th>
            <th className="p-4 text-left">Role</th>
            <th className="p-4 text-left">Status</th>
          </tr>
        </thead>
        <tbody>
          {users.map((u) => (
            <tr key={u.emp_id} className="border-b">
              <td className="p-4">{u.emp_id}</td>
              <td className="p-4 capitalize">{u.role}</td>
              <td className="p-4">
                <span className={`px-2 py-1 rounded text-xs ${u.status === 'active' ? 'bg-green-100 text-green-800' : 'bg-red-100 text-red-800'}`}>
                  {u.status}
                </span>
              </td>
            </tr>
          ))}
        </tbody>
      </table>

      {isModalOpen && (
        <div className="fixed inset-0 bg-black bg-opacity-50 flex justify-center items-center">
          <div className="bg-white p-6 rounded w-96">
            <h2 className="text-xl font-bold mb-4">Create User Login</h2>
            <form onSubmit={handleSubmit(onSubmit)} className="space-y-3">
              <input {...register("emp_id")} placeholder="Employee ID" className="w-full border p-2" required />
              <input {...register("password")} type="password" placeholder="Password" className="w-full border p-2" required />
              <select {...register("role")} className="w-full border p-2">
                <option value="employee">Employee</option>
                <option value="manager">Manager</option>
                <option value="admin">Admin</option>
              </select>
              <div className="flex justify-end gap-2 mt-4">
                <button type="button" onClick={() => setIsModalOpen(false)} className="text-gray-500">Cancel</button>
                <button type="submit" className="bg-green-600 text-white px-4 py-1 rounded">Create</button>
              </div>
            </form>
          </div>
        </div>
      )}
    </div>
  );
};

export default UsersPage;