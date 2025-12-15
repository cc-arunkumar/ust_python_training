import { useState } from "react";
import api from "../api/api";

function EmployeeItem({ employee, onEmployeeUpdated, onEmployeeDeleted }) {
  const [editing, setEditing] = useState(false);
  const [formData, setFormData] = useState(employee);

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleUpdate = () => {
    api.put(`/employees/${employee.id}`, formData)
      .then((res) => {
        onEmployeeUpdated(res.data);
        setEditing(false);
      })
      .catch((err) => console.error("Error updating:", err));
  };

  const handleDelete = () => {
    api.delete(`/employees/${employee.id}`)
      .then(() => onEmployeeDeleted(employee.id))
      .catch((err) => console.error("Error deleting:", err));
  };

  return (
    <div className="employee-item">
      {editing ? (
        <>
          <input name="name" value={formData.name} onChange={handleChange} />
          <input name="designation" value={formData.designation} onChange={handleChange} />
          <input name="location" value={formData.location || ""} onChange={handleChange} />
          <input name="project" value={formData.project || ""} onChange={handleChange} />
          <button onClick={handleUpdate}>Save</button>
          <button onClick={() => setEditing(false)}>Cancel</button>
        </>
      ) : (
        <>
          <p><strong>{employee.name}</strong> - {employee.designation}</p>
          <p>{employee.location} | {employee.project}</p>
          <button onClick={() => setEditing(true)}>Edit</button>
          <button onClick={handleDelete}>Delete</button>
        </>
      )}
    </div>
  );
}

export default EmployeeItem;
