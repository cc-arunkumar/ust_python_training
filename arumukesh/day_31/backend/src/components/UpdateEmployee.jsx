import { useEffect, useState } from "react";
import api from "../api/api";

function EmployeeUpdate({ employee, onUpdated }) {
  const [form, setForm] = useState(null);

  // 🔴 THIS MUST RUN
  useEffect(() => {
    if (employee) {
      setForm(employee);
      console.log("Editing employee:", employee); // DEBUG
    }
  }, [employee]);

  if (!form) return null;

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    console.log("Updating ID:", form.id); // DEBUG

    // ✅ MUST BE PUT (NOT POST)
    api.put(`/employees/${form.id}`, {
      name: form.name,
      designation: form.designation,
      location: form.location,
      project: form.project
    })
    .then(() => {
      alert("Employee updated successfully");
      onUpdated();
    })
    .catch(err => console.error(err));
  };

  return (
    <form onSubmit={handleSubmit}>
      <h3>Update Employee</h3>

      <input name="name" value={employee.name} onChange={handleChange}  placeholder="Name"/>
      <input name="designation" value={employee.designation} onChange={handleChange} placeholder="Designation" />
      <input name="location" value={employee.location} onChange={handleChange} placeholder="Location"/>
      <input name="project" value={employee.project} onChange={handleChange} placeholder="Project" />
      <button>Add/Update</button>
    </form>
  );
}

export default EmployeeUpdate;
