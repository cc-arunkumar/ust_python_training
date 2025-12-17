import { useEffect, useState } from "react";
import { useNavigate, useParams } from "react-router-dom";
import {
  createEmployee,
  getEmployeeById,
  updateEmployee,
} from "../api/employee.api";

export default function EmployeeForm() {
  const { id } = useParams(); // edit if exists
  const navigate = useNavigate();

  const [form, setForm] = useState({
    name: "",
    email: "",
    designation: "",
    manager_id: "",
  });

  useEffect(() => {
    if (id) {
      getEmployeeById(id).then((data) =>
        setForm({
          name: data.name,
          email: data.email,
          designation: data.designation,
          manager_id: data.manager_id || "",
        })
      );
    }
  }, [id]);

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    const payload = {
      ...form,
      manager_id: form.manager_id
        ? Number(form.manager_id)
        : null,
    };

    if (id) {
      await updateEmployee(id, payload);
    } else {
      await createEmployee(payload);
    }

    navigate("/admin/employees");
  };

  return (
    <div className="p-6 max-w-xl mx-auto">
      <h1 className="text-xl font-semibold mb-4">
        {id ? "Edit Employee" : "Create Employee"}
      </h1>

      <form
        onSubmit={handleSubmit}
        className="bg-white p-6 rounded shadow space-y-4"
      >
        <input
          name="name"
          placeholder="Name"
          className="w-full border p-2 rounded"
          value={form.name}
          onChange={handleChange}
          required
        />

        <input
          name="email"
          placeholder="Email"
          className="w-full border p-2 rounded"
          value={form.email}
          onChange={handleChange}
          required
        />

        <input
          name="designation"
          placeholder="Designation"
          className="w-full border p-2 rounded"
          value={form.designation}
          onChange={handleChange}
          required
        />

        <input
          name="manager_id"
          placeholder="Manager ID (optional)"
          type="number"
          className="w-full border p-2 rounded"
          value={form.manager_id}
          onChange={handleChange}
        />

        <div className="flex justify-end gap-2">
          <button
            type="button"
            onClick={() => navigate("/admin/employees")}
            className="px-4 py-2 border rounded"
          >
            Cancel
          </button>

          <button
            type="submit"
            className="bg-blue-600 text-white px-4 py-2 rounded"
          >
            Save
          </button>
        </div>
      </form>
    </div>
  );
}
