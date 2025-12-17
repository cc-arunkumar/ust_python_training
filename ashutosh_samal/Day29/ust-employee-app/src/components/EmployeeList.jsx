import { useState } from "react";

function EmployeeList({ employees, onDelete, onUpdate }) {
  const [editingId, setEditingId] = useState(null);
  const [editedEmployee, setEditedEmployee] = useState({});

  const startEdit = (emp) => {
    setEditingId(emp.id);
    setEditedEmployee(emp);
  };

  const handleChange = (e) => {
    setEditedEmployee({
      ...editedEmployee,
      [e.target.name]: e.target.value,
    });
  };

  const saveUpdate = () => {
    onUpdate(editingId, editedEmployee);
    setEditingId(null);
  };

  return (
    <div>
      <h3>Employee List</h3>

      {employees.map((emp) => (
        <div key={emp.id} style={{ border: "1px solid #ccc", padding: "10px", marginBottom: "10px" }}>
          {editingId === emp.id ? (
            <>
              <input name="name" value={editedEmployee.name} onChange={handleChange} />
              <input name="designation" value={editedEmployee.designation} onChange={handleChange} />
              <input name="location" value={editedEmployee.location || ""} onChange={handleChange} />
              <input name="project" value={editedEmployee.project || ""} onChange={handleChange} />
              <br />
              <button onClick={saveUpdate}>Save</button>
              <button onClick={() => setEditingId(null)}>Cancel</button>
            </>
          ) : (
            <>
              <p><b>Name:</b> {emp.name}</p>
              <p><b>Designation:</b> {emp.designation}</p>
              <p><b>Location:</b> {emp.location}</p>
              <p><b>Project:</b> {emp.project}</p>

              <button onClick={() => startEdit(emp)}>Edit</button>
              <button onClick={() => onDelete(emp.id)}>Delete</button>
            </>
          )}
        </div>
      ))}
    </div>
  );
}

export default EmployeeList;
