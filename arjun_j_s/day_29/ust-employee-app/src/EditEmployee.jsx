import { useState } from "react";
import api from "./api/api";
 
function EditEmployee({ employee, onUpdated, onCancel }) {
  const [form, setForm] = useState(employee);
 
  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };
 
  const handleUpdate = (e) => {
    e.preventDefault();
 
    api.put(`/employees/${employee.id}`, form).then((res) => {
      onUpdated(res.data);
    });
  };
 
  return (
    <div>
      <h3>Edit Employee</h3>
 
      <form onSubmit={handleUpdate}>
        <input name="name" value={form.name} onChange={handleChange} />
        <input name="designation" value={form.designation} onChange={handleChange} />
        <input name="location" value={form.location} onChange={handleChange} />
        <input name="project" value={form.project} onChange={handleChange} />
 
        <button type="submit">Update</button>
        <button type="button" onClick={onCancel}>Cancel</button>
      </form>
    </div>
  );
}
 
export default EditEmployee;
 
 