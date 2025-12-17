import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import EmployeeForm from "./components/EmployeeForm"; // POST
import GetEmployees from "./components/GetEmployees"; // GET
import UpdateEmployee from "./components/UpdateEmployee"; // PUT
import DeleteEmployee from "./components/DeleteEmployee"; // DELETE
import "./App.css"; // custom styles

function App() {
  return (
    <Router>
      <div className="app-container">
        <h1 className="app-title">Employee Management System</h1>

        {/* Elegant Navigation Bar */}
        <nav className="navbar">
          <ul className="nav-links">
            <li>
              <Link to="/add">Add Employee</Link>
            </li>
            <li>
              <Link to="/get">View Employees</Link>
            </li>
            <li>
              <Link to="/update">Update Employee</Link>
            </li>
            <li>
              <Link to="/delete">Delete Employee</Link>
            </li>
          </ul>
        </nav>

        {/* Page Routes */}
        <div className="page-content">
          <Routes>
            <Route
              path="/add"
              element={<EmployeeForm onEmployeeAdded={() => {}} />}
            />
            <Route path="/get" element={<GetEmployees />} />
            <Route path="/update" element={<UpdateEmployee />} />
            <Route path="/delete" element={<DeleteEmployee />} />
          </Routes>
        </div>
      </div>
    </Router>
  );
}

export default App;
