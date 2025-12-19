import { useState } from "react";
import api from "../api/api";

function EmployeeCreate({ onSuccess }) {
  const [employee, setEmployee] = useState({
    name: "",
    designation: "",
    location: "",
    project: ""
  });

  const handleChange = (e) => {
    setEmployee({ ...employee, [e.target.name]: e.target.value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    api.post("/employees", employee)
      .then(() => {
        onSuccess();
        setEmployee({ name: "", designation: "", location: "", project: "" });
      })
      .catch(err => console.error(err));
  };

  return (
    <form onSubmit={handleSubmit}>
      <input name="name" value={employee.name} onChange={handleChange}  placeholder="Name"/>
      <input name="designation" value={employee.designation} onChange={handleChange} placeholder="Designation" />
      <input name="location" value={employee.location} onChange={handleChange} placeholder="Location"/>
      <input name="project" value={employee.project} onChange={handleChange} placeholder="Project" />
      <button>Add</button>
    </form>
  );
}

export default EmployeeCreate;
