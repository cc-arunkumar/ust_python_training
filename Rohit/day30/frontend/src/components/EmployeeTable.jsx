import {
  Table,
  TableBody,
  TableCaption,
  TableCell,
  TableFooter,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table";
import { Button } from "@/components/ui/button";
import { useNavigate } from "react-router-dom";
import { useState, useEffect } from "react";
import axios from "axios";

export function EmployeeTable() {
  const navigate = useNavigate();
  const [employees, setEmployees] = useState([]);

  useEffect(() => {
    const fetchEmployees = async () => {
      try {
        const token = localStorage.getItem("token");
        console.log("reached")
        const res = await axios.get("http://localhost:8000/api/users/employees", {
          headers: { Authorization: `Bearer ${token}` },
        });
        console.log("reached")
        setEmployees(res.data);
      } catch (err) {
        console.error("Error fetching employees:", err);
      }
    };
    fetchEmployees();
  }, []);

  const handleEdit = (employee) => {
    console.log("Edit employee", employee);
    // navigate("/edit-employee", { state: employee });
  };

  const handleDelete = (empId) => {
    console.log("Delete employee", empId);
  };

  return (
    <div className="">
      <h1 className="text-4xl font-extrabold mb-20">Employee Table</h1>
      <div className="w-full overflow-x-auto">
        <Table className="min-w-200">
          <TableCaption>A list of your employees.</TableCaption>
          <TableHeader>
            <TableRow>
              <TableHead>ID</TableHead>
              <TableHead>Name</TableHead>
              <TableHead>Designation</TableHead>
              <TableHead>Manager ID</TableHead>
              <TableHead>Actions</TableHead>
            </TableRow>
          </TableHeader>
          <TableBody>
            {employees.map((emp) => (
              <TableRow key={emp.emp_id}>
                <TableCell>{emp.emp_id}</TableCell>
                <TableCell>{emp.name}</TableCell>
                <TableCell>{emp.designation}</TableCell>
                <TableCell>{emp.manager_id}</TableCell>
                <TableCell className="space-x-2">
                  <Button
                    variant="outline"
                    size="sm"
                    onClick={() => handleEdit(emp)}
                  >
                    Edit
                  </Button>
                  <Button
                    variant="destructive"
                    size="sm"
                    onClick={() => handleDelete(emp.emp_id)}
                  >
                    Delete
                  </Button>
                </TableCell>
              </TableRow>
            ))}
          </TableBody>
          <TableFooter>
            <TableRow>
              <TableCell colSpan={4}>Total Employees</TableCell>
              <TableCell className="text-right">{employees.length}</TableCell>
            </TableRow>
          </TableFooter>
        </Table>
      </div>
    </div>
  );
}
