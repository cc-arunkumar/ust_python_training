import { useEffect, useState } from "react";
import { getTasks, updateTaskStatus } from "../api/taskApi";

const MyTasks = () => {
  const [tasks, setTasks] = useState([]);

  useEffect(() => {
    loadTasks();
  }, []);

  const loadTasks = async () => {
    try {
      const res = await getTasks();
      setTasks(res.data);
    } catch (err) {
      console.error("Failed to load tasks", err);
    }
  };

  const changeStatus = async (id, status) => {
    try {
      await updateTaskStatus(id, status);
      loadTasks();
    } catch (err) {
      console.error("Failed to update status", err);
    }
  };

  return (
    <div className="p-6">
      <h2 className="text-xl font-bold mb-4">My Tasks</h2>

      <table className="w-full border">
        <thead>
          <tr className="bg-gray-200">
            <th className="p-2">Title</th>
            <th className="p-2">Status</th>
            <th className="p-2">Update</th>
          </tr>
        </thead>

        <tbody>
          {tasks.map((t) => (
            <tr key={t.t_id} className="border-t">
              <td className="p-2">{t.title}</td>
              <td className="p-2">{t.status}</td>
              <td className="p-2">
                <select
                  value={t.status}
                  onChange={(e) =>
                    changeStatus(t.t_id, e.target.value)
                  }
                  className="border p-1"
                >
                  <option value="Pending">Pending</option>
                  <option value="In Progress">In Progress</option>
                  <option value="Done">Done</option>
                </select>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default MyTasks;
