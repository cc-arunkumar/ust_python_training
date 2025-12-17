import { useState } from "react";
import api from "../api/api";

function UpdateEmployee() {
  const [employeeId, setEmployeeId] = useState("");
  const [employee, setEmployee] = useState({
    name: "",
    designation: "",
    location: "",
    project: "",
  });

  const [message, setMessage] = useState("");
  const [error, setError] = useState("");

  const handleChange = (e) => {
    setEmployee({ ...employee, [e.target.name]: e.target.value });
  };

  const handleUpdate = (e) => {
    e.preventDefault();

    if (!employeeId) {
      setError("Employee ID is required");
      return;
    }

    setError("");
    api
      .put(`/employees/${employeeId}`, employee)
      .then(() => {
        setMessage("Employee updated successfully");
      })
      .catch(() => {
        setError("Failed to update employee");
      });
  };

  return (
    <div className="employee-form">
      <h3>Update Employee</h3>

      {error && <p className="error">{error}</p>}
      {message && <p className="success">{message}</p>}

      <input
        type="text"
        placeholder="Employee ID"
        value={employeeId}
        onChange={(e) => setEmployeeId(e.target.value)}
        className="input-field"
      />
      <br /><br />

      <form onSubmit={handleUpdate}>
        <input
          type="text"
          name="name"
          placeholder="Name"
          value={employee.name}
          onChange={handleChange}
          className="input-field"
        />
        <br /><br />

        <input
          type="text"
          name="designation"
          placeholder="Designation"
          value={employee.designation}
          onChange={handleChange}
          className="input-field"
        />
        <br /><br />

        <input
          type="text"
          name="location"
          placeholder="Location"
          value={employee.location}
          onChange={handleChange}
          className="input-field"
        />
        <br /><br />

        <input
          type="text"
          name="project"
          placeholder="Project"
          value={employee.project}
          onChange={handleChange}
          className="input-field"
        />
        <br /><br />

        <button type="submit" className="submit-button">
          Update Employee
        </button>
      </form>
    </div>
  );
}

export default UpdateEmployee;
