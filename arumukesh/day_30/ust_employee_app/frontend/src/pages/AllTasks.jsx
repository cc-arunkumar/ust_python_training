import { useEffect, useState } from "react";
import { getTasks } from "../api/taskApi";

const AllTasks = () => {
  const [tasks, setTasks] = useState([]);

  useEffect(() => {
    getTasks().then(res => setTasks(res.data));
  }, []);

  return (
    <div className="p-6">
      <h2 className="text-xl font-bold mb-4">All Tasks</h2>

      <table className="w-full border">
        <thead className="bg-gray-200">
          <tr>
            <th>Title</th>
            <th>Status</th>
            <th>Assigned To</th>
            <th>Created By</th>
          </tr>
        </thead>

        <tbody>
          {tasks.map(t => (
            <tr key={t.id} className="border-t">
              <td>{t.title}</td>
              <td>{t.status}</td>
              <td>{t.assigned_to}</td>
              <td>{t.created_by}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default AllTasks;
