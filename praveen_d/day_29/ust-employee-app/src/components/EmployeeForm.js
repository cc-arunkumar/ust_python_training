import { useEffect, useState } from "react";
import api from "../api/api";

export default function EmployeeForm() {
  const [employee, setEmployee] = useState({
    name: "",
    designation: "",
    location: "",
    project: "",
  });

  const [employees, setEmployees] = useState([]);
  const [selected, setSelected] = useState(null);
  const [loading, setLoading] = useState(false);
  const [message, setMessage] = useState("");
  const [error, setError] = useState("");

  useEffect(() => {
    loadEmployees();
  }, []);

  const loadEmployees = () => {
    api.get("/employee")
      .then((res) => setEmployees(res.data))
      .catch(() => {});
  };

  const handleChange = (e) => {
    if (selected) {
      setSelected({ ...selected, [e.target.name]: e.target.value });
    } else {
      setEmployee({ ...employee, [e.target.name]: e.target.value });
    }
  };

  const addEmployee = (e) => {
    e.preventDefault();

    if (!employee.name || !employee.designation) {
      setError("Name & Designation required");
      return;
    }

    setLoading(true);
    setError("");

    api
      .post("/employee", employee)
      .then((res) => {
        setEmployees([...employees, res.data]);
        setEmployee({ name: "", designation: "", location: "", project: "" });
        setMessage("Employee added!");
      })
      .catch(() => setError("Error adding employee"))
      .finally(() => setLoading(false));
  };

  const deleteEmployee = (id) => {
    api
      .delete(`/employee/${id}`)
      .then(() => {
        setEmployees(employees.filter((emp) => emp.id !== id));
        setMessage("Employee deleted!");
      })
      .catch(() => {});
  };

  const updateEmployee = () => {
    api
      .put(`/employee/${selected.id}`, selected)
      .then(() => {
        setEmployees(
          employees.map((emp) => (emp.id === selected.id ? selected : emp))
        );
        setSelected(null);
        setMessage("Updated successfully!");
      })
      .catch(() => setError("Update failed"));
  };

  return (
    <div
      className="min-h-screen p-6 bg-gradient-to-br from-purple-600 via-purple-700 to-purple-900 text-white"
    >
      <div className="max-w-6xl mx-auto">
        <h1 className="text-4xl font-bold mb-6 text-center">
          Employee Management
        </h1>

        {message && (
          <p className="bg-green-500 text-white p-2 rounded mb-4 text-center">
            {message}
          </p>
        )}
        {error && (
          <p className="bg-red-500 text-white p-2 rounded mb-4 text-center">
            {error}
          </p>
        )}

        {/* ------------------ ADD EMPLOYEE ------------------ */}
        {!selected && (
          <div className="bg-white/20 backdrop-blur-lg p-6 rounded-xl shadow-xl mb-8">
            <h2 className="text-2xl font-semibold mb-4">Add Employee</h2>

            <form onSubmit={addEmployee} className="space-y-4">
              <input
                type="text"
                name="name"
                placeholder="Employee Name"
                value={employee.name}
                onChange={handleChange}
                className="w-full p-3 rounded bg-white/30 text-white placeholder-white/70"
              />

              <input
                type="text"
                name="designation"
                placeholder="Designation"
                value={employee.designation}
                onChange={handleChange}
                className="w-full p-3 rounded bg-white/30 text-white placeholder-white/70"
              />

              <input
                type="text"
                name="location"
                placeholder="Location"
                value={employee.location}
                onChange={handleChange}
                className="w-full p-3 rounded bg-white/30 text-white placeholder-white/70"
              />

              <input
                type="text"
                name="project"
                placeholder="Project"
                value={employee.project}
                onChange={handleChange}
                className="w-full p-3 rounded bg-white/30 text-white placeholder-white/70"
              />

              <button
                type="submit"
                disabled={loading}
                className="w-full py-3 rounded bg-purple-900 hover:bg-purple-950 transition"
              >
                {loading ? "Adding..." : "Add Employee"}
              </button>
            </form>
          </div>
        )}

        {/* ------------------ UPDATE EMPLOYEE ------------------ */}
        {selected && (
          <div className="bg-white/20 backdrop-blur-lg p-6 rounded-xl shadow-xl mb-8">
            <h2 className="text-2xl font-semibold mb-4">
              Edit Employee (ID: {selected.id})
            </h2>

            <div className="space-y-4">
              <input
                type="text"
                name="name"
                value={selected.name}
                onChange={handleChange}
                className="w-full p-3 rounded bg-white/30 text-white"
              />

              <input
                type="text"
                name="designation"
                value={selected.designation}
                onChange={handleChange}
                className="w-full p-3 rounded bg-white/30 text-white"
              />

              <input
                type="text"
                name="location"
                value={selected.location}
                onChange={handleChange}
                className="w-full p-3 rounded bg-white/30 text-white"
              />

              <input
                type="text"
                name="project"
                value={selected.project}
                onChange={handleChange}
                className="w-full p-3 rounded bg-white/30 text-white"
              />

              <div className="flex gap-4">
                <button
                  onClick={updateEmployee}
                  className="flex-1 py-3 rounded bg-yellow-400 text-black font-semibold hover:bg-yellow-500"
                >
                  Update
                </button>
                <button
                  onClick={() => setSelected(null)}
                  className="flex-1 py-3 rounded bg-red-500 hover:bg-red-600"
                >
                  Cancel
                </button>
              </div>
            </div>
          </div>
        )}

        {/* ------------------ EMPLOYEE TABLE ------------------ */}
        <div className="bg-white/20 backdrop-blur-lg p-6 rounded-xl shadow-xl">
          <h2 className="text-2xl font-semibold mb-4">Employee List</h2>

          <table className="w-full text-left">
            <thead>
              <tr className="border-b border-white/40">
                <th className="p-2">ID</th>
                <th className="p-2">Name</th>
                <th className="p-2">Designation</th>
                <th className="p-2">Location</th>
                <th className="p-2">Project</th>
                <th className="p-2">Actions</th>
              </tr>
            </thead>

            <tbody>
              {employees.map((emp) => (
                <tr key={emp.id} className="border-b border-white/20">
                  <td className="p-2">{emp.id}</td>
                  <td className="p-2">{emp.name}</td>
                  <td className="p-2">{emp.designation}</td>
                  <td className="p-2">{emp.location}</td>
                  <td className="p-2">{emp.project}</td>

                  <td className="p-2 flex gap-3">
                    <button
                      onClick={() => setSelected(emp)}
                      className="px-3 py-1 bg-yellow-400 text-black rounded hover:bg-yellow-500"
                    >
                      Edit
                    </button>

                    <button
                      onClick={() => deleteEmployee(emp.id)}
                      className="px-3 py-1 bg-red-500 rounded hover:bg-red-600"
                    >
                      Delete
                    </button>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
}
