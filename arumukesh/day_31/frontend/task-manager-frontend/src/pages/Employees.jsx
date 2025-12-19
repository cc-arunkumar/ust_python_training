import React, { useEffect, useState } from "react";
import { getEmployees, createEmployee } from "../api/employeeApi";

export default function Employees() {
  const [employees, setEmployees] = useState([]);
  const [loading, setLoading] = useState(true);
  const [form, setForm] = useState({
    name: "",
    designation: "",
    location: "",
    project: "",
  });

  async function load() {
    try {
      const res = await getEmployees();
      setEmployees(res.data);
    } catch (e) {
      console.error(e);
    }
    setLoading(false);
  }

  useEffect(() => {
    const t = setTimeout(() => {
      load();
    }, 0);
    return () => clearTimeout(t);
  }, []);

  const handleChange = (e) =>
    setForm({ ...form, [e.target.name]: e.target.value });

  const handleCreate = async (ev) => {
    ev.preventDefault();
    try {
      await createEmployee(form);
      setForm({ name: "", designation: "", location: "", project: "" });
      load();
    } catch (err) {
      console.error(err);
    }
  };

  if (loading) return <div>Loading...</div>;

  return (
    <div>
      <h2 className="text-xl font-semibold mb-4">Employees</h2>
      <form
        onSubmit={handleCreate}
        className="mb-4 grid grid-cols-4 gap-2 items-end"
      >
        <input
          name="name"
          value={form.name}
          onChange={handleChange}
          placeholder="Name"
          className="p-2 border rounded"
        />
        <input
          name="designation"
          value={form.designation}
          onChange={handleChange}
          placeholder="Designation"
          className="p-2 border rounded"
        />
        <input
          name="location"
          value={form.location}
          onChange={handleChange}
          placeholder="Location"
          className="p-2 border rounded"
        />
        <div>
          <button
            type="submit"
            className="px-4 py-2 bg-[var(--accent)] text-white rounded"
          >
            Add Employee
          </button>
        </div>
      </form>
      <div className="grid gap-3">
        {employees.map((e) => (
          <div key={e.id} className="p-3 bg-white rounded shadow">
            <div className="flex justify-between items-center">
              <div>
                <div className="font-semibold">{e.name}</div>
                <div className="text-sm text-gray-500">
                  {e.designation} • {e.location}
                </div>
              </div>
              <div className="space-x-2">
                <button className="px-3 py-1 bg-yellow-100 rounded">
                  Edit
                </button>
                <button className="px-3 py-1 bg-red-100 rounded">Delete</button>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
