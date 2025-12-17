import { useState } from "react";
import api from "../api/api";

function UpdateEmployee() {
  const [id, setId] = useState("");
  const [employee, setEmployee] = useState({
    name: "",
    designation: "",
    location: "",
    project: "",
  });
  const [message, setMessage] = useState("");

  const handleChange = (e) => {
    setEmployee({ ...employee, [e.target.name]: e.target.value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    api
      .put(`/employees/${id}`, employee)
      .then((res) => setMessage("Employee updated successfully"))
      .catch((err) => setMessage("Error updating employee"));
  };

  return (
    <div>
      <h2>Update Employee</h2>
      <form onSubmit={handleSubmit}>
        <input
          type="number"
          placeholder="Employee ID"
          value={id}
          onChange={(e) => setId(e.target.value)}
        />
        <br />
        <br />
        <input
          type="text"
          name="name"
          placeholder="Name"
          value={employee.name}
          onChange={handleChange}
        />
        <br />
        <br />
        <input
          type="text"
          name="designation"
          placeholder="Designation"
          value={employee.designation}
          onChange={handleChange}
        />
        <br />
        <br />
        <input
          type="text"
          name="location"
          placeholder="Location"
          value={employee.location}
          onChange={handleChange}
        />
        <br />
        <br />
        <input
          type="text"
          name="project"
          placeholder="Project"
          value={employee.project}
          onChange={handleChange}
        />
        <br />
        <br />
        <button type="submit">Update Employee</button>
      </form>
      {message && <p>{message}</p>}
    </div>
  );
}

export default UpdateEmployee;
