import React, { useState, useMemo, useEffect } from "react";
import { Employee, Role } from "@/types";
import api from "@/services/api";
import { useAuth } from "@/contexts/AuthContext";
import { useEmployees } from "@/contexts/EmployeesContext";
import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Badge } from "@/components/ui/badge";
import { Card, CardContent, CardHeader } from "@/components/ui/card";
import {
  Search,
  Users,
  Plus,
  Mail,
  Briefcase,
  UserCircle,
  Edit,
  Trash,
} from "lucide-react";

interface EmployeeListProps {
  viewMode: Role;
}

interface ManagerOption {
  emp_id: number;
  name: string;
  e_id: string;
}

// Modal form component for creating employee
const AddEmployeeForm: React.FC<{
  onCreated: (emp: Employee) => void;
  onClose: () => void;
}> = ({ onCreated, onClose }) => {
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [designation, setDesignation] = useState("");
  const [manager, setManager] = useState("");
  const [managersList, setManagersList] = useState<ManagerOption[]>([]);
  const { employees, getEmployeeById } = useEmployees();

  useEffect(() => {
    (async () => {
      try {
        // Fetch managers from the new managers endpoint (backend returns users with manager role)
        const res = await api.get("/api/users/managers");
        const all = Array.isArray(res.data) ? res.data : [];
        setManagersList(
          all
            .filter((u: any) => {
              const roles = u.roles || u.role || [];
              return Array.isArray(roles)
                ? roles.some((r: any) =>
                    String(r).toLowerCase().includes("manager")
                  )
                : String(roles).toLowerCase().includes("manager");
            })
            .map((u: any) => {
              const empId = u.emp_id != null ? u.emp_id : u.id;
              const empRec = getEmployeeById
                ? getEmployeeById(String(empId))
                : undefined;
              return {
                emp_id: empId,
                name:
                  (empRec && empRec.name) ||
                  u.name ||
                  u.username ||
                  u.email ||
                  `User ${empId}`,
                e_id: empId
                  ? `E${String(empId).padStart(3, "0")}`
                  : u.e_id || "",
              };
            })
        );
      } catch (error) {
        console.error("Failed fetching managers", error);
      }
    })();
  }, []);

  const handleSubmit = async () => {
    if (!name || !email || !designation) return alert("Fill all fields!");
    try {
      const payload = {
        name,
        email,
        designation,
        manager_id: manager ? parseInt(manager) : null,
      };
      const res = await api.post("/api/employees", payload);
      const created = res.data;
      const mapped: Employee = {
        e_id: `E${String(created.emp_id).padStart(3, "0")}`,
        name: created.name,
        email: created.email,
        designation: created.designation,
        mgr_id: created.manager_id
          ? `E${String(created.manager_id).padStart(3, "0")}`
          : undefined,
      };
      onCreated(mapped);
      onClose();
    } catch (err) {
      console.error("Error creating employee:", err);
      alert("Failed to create employee");
    }
  };

  return (
    <div className="fixed inset-0 flex items-center justify-center bg-black/50 z-50 p-4">
      <div className="bg-white p-6 rounded-lg w-full max-w-md">
        <h3 className="text-lg font-bold mb-4">Add Employee</h3>

        <label className="block mb-2">Name</label>
        <input
          type="text"
          value={name}
          onChange={(e) => setName(e.target.value)}
          className="w-full mb-3 border rounded px-2 py-1"
        />

        <label className="block mb-2">Email</label>
        <input
          type="email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          className="w-full mb-3 border rounded px-2 py-1"
        />

        <label className="block mb-2">Designation</label>
        <input
          type="text"
          value={designation}
          onChange={(e) => setDesignation(e.target.value)}
          className="w-full mb-3 border rounded px-2 py-1"
        />

        <label className="block mb-2">Manager</label>
        <select
          value={manager}
          onChange={(e) => setManager(e.target.value)}
          className="w-full mb-3 border rounded px-2 py-1"
        >
          <option value="">— None —</option>
          {managersList.map((m) => (
            <option key={m.emp_id} value={m.emp_id}>
              {m.e_id} — {m.name}
            </option>
          ))}
        </select>

        <div className="flex justify-end gap-2 mt-4">
          <Button onClick={handleSubmit}>Create</Button>
          <Button variant="outline" onClick={onClose}>
            Cancel
          </Button>
        </div>
      </div>
    </div>
  );
};

// Edit form modal — single form that also displays/edits roles from users table
const EditEmployeeForm: React.FC<{
  employee: Employee;
  usersList: any[];
  onUpdated: (emp: Employee) => void;
  onClose: () => void;
}> = ({ employee, usersList, onUpdated, onClose }) => {
  const [name, setName] = useState(employee.name);
  const [email, setEmail] = useState(employee.email);
  const [designation, setDesignation] = useState(employee.designation);
  const [manager, setManager] = useState(employee.mgr_id || "");

  // derive available roles from usersList (robust to `role` or `roles` field)
  const allRoles = Array.from(
    new Set(usersList.flatMap((u) => u.roles || u.role || []))
  );

  // find corresponding user record (match by e_id or emp_id)
  const digits = String(employee.e_id).replace(/\D/g, "");
  const userRecord = usersList.find(
    (u) =>
      String(u.e_id) === employee.e_id ||
      String(u.emp_id) === digits ||
      String(u.id) === digits
  );

  const [selectedRoles, setSelectedRoles] = useState<string[]>(
    userRecord ? userRecord.roles || userRecord.role || [] : []
  );

  const toggleRole = (r: string) => {
    setSelectedRoles((prev) =>
      prev.includes(r) ? prev.filter((x) => x !== r) : [...prev, r]
    );
  };

  const handleSubmit = async () => {
    try {
      const idNum = Number(digits);
      if (!Number.isFinite(idNum)) throw new Error("Invalid employee id");

      const payload = {
        name,
        email,
        designation,
        manager_id: manager ? Number(String(manager).replace(/\D/g, "")) : null,
      };

      const res = await api.put(`/api/employees/${idNum}`, payload);
      const updated = res.data;

      const mapped: Employee = {
        e_id: `E${String(updated.emp_id).padStart(3, "0")}`,
        name: updated.name,
        email: updated.email,
        designation: updated.designation,
        mgr_id: updated.manager_id
          ? `E${String(updated.manager_id).padStart(3, "0")}`
          : undefined,
      };

      // update roles on users table if we have a user id
      if (userRecord && (userRecord.id || userRecord.emp_id)) {
        try {
          const userId = userRecord.id || userRecord.emp_id;
          // send as PATCH with roles; backend accepts UserUpdate on PUT
          await api.put(`/api/users/${userId}`, { roles: selectedRoles });
        } catch (uerr) {
          console.warn("Failed to update user roles", uerr);
          // continue — employee update succeeded
        }
      }

      onUpdated(mapped);
      onClose();
    } catch (err) {
      console.error("Failed to update employee", err);
      alert("Failed to update employee");
    }
  };

  return (
    <div className="fixed inset-0 flex items-center justify-center bg-black/50 z-50 p-4">
      <div className="bg-white p-6 rounded-lg w-full max-w-md">
        <h3 className="text-lg font-bold mb-4">Edit Employee</h3>

        <label className="block mb-2">Name</label>
        <input
          type="text"
          value={name}
          onChange={(e) => setName(e.target.value)}
          className="w-full mb-3 border rounded px-2 py-1"
        />

        <label className="block mb-2">Email</label>
        <input
          type="email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          className="w-full mb-3 border rounded px-2 py-1"
        />

        <label className="block mb-2">Designation</label>
        <input
          type="text"
          value={designation}
          onChange={(e) => setDesignation(e.target.value)}
          className="w-full mb-3 border rounded px-2 py-1"
        />

        <label className="block mb-2">Manager</label>
        <input
          type="text"
          value={manager}
          onChange={(e) => setManager(e.target.value)}
          placeholder="E001 or numeric id"
          className="w-full mb-3 border rounded px-2 py-1"
        />

        <div className="flex justify-end gap-2 mt-4">
          <Button onClick={handleSubmit}>Save</Button>
          <Button variant="outline" onClick={onClose}>
            Cancel
          </Button>
        </div>
      </div>
    </div>
  );
};

const EmployeeList: React.FC<EmployeeListProps> = ({ viewMode }) => {
  const { user } = useAuth();
  const [employees, setEmployees] = useState<Employee[]>([]);
  const [usersList, setUsersList] = useState<any[]>([]);
  const [editingEmployee, setEditingEmployee] = useState<Employee | null>(null);
  const [searchTerm, setSearchTerm] = useState("");
  const [page, setPage] = useState(1);
  const [showAddForm, setShowAddForm] = useState(false);
  const limit = 10;

  useEffect(() => {
    let mounted = true;
    const fetchData = async () => {
      try {
        const [empRes, usersRes] = await Promise.all([
          api.get("/api/employees"),
          api.get("/api/users"),
        ]);
        if (mounted) {
          const mappedEmployees = (empRes.data || []).map((e: any) => ({
            e_id: `E${String(e.emp_id).padStart(3, "0")}`,
            name: e.name,
            email: e.email,
            designation: e.designation,
            mgr_id: e.manager_id
              ? `E${String(e.manager_id).padStart(3, "0")}`
              : undefined,
          }));

          setEmployees(mappedEmployees);

          setUsersList(Array.isArray(usersRes.data) ? usersRes.data : []);
        }
      } catch (err) {
        console.error("Failed to fetch employees/users", err);
      }
    };
    fetchData();
    return () => {
      mounted = false;
    };
  }, []);

  const handleCreated = (created: Employee) => {
    setEmployees((prev) => [created, ...prev]);
  };

  const filteredEmployees = useMemo(() => {
    let employeesLocal = employees;

    // Managers should see all employees (no filtering) but actions are admin-only

    if (searchTerm) {
      const term = searchTerm.toLowerCase();
      employeesLocal = employeesLocal.filter(
        (e) =>
          e.name.toLowerCase().includes(term) ||
          e.email.toLowerCase().includes(term) ||
          e.designation.toLowerCase().includes(term)
      );
    }

    return employeesLocal;
  }, [viewMode, user?.employee?.e_id, searchTerm, employees]);

  const paginatedEmployees = useMemo(() => {
    const start = (page - 1) * limit;
    return filteredEmployees.slice(start, start + limit);
  }, [filteredEmployees, page]);

  const totalPages = Math.ceil(filteredEmployees.length / limit);

  const getEmployeeByIdLocal = (id?: string) => {
    if (!id) return undefined;
    return employees.find((e) => e.e_id === id);
  };

  const handleDelete = async (emp: Employee) => {
    if (!confirm(`Delete employee ${emp.name}? This cannot be undone.`)) return;
    try {
      const idNum = Number(String(emp.e_id).replace(/\D/g, ""));
      if (!Number.isFinite(idNum)) throw new Error("Invalid employee id");
      await api.delete(`/api/employees/${idNum}`);
      setEmployees((prev) => prev.filter((e) => e.e_id !== emp.e_id));
    } catch (err) {
      console.error("Failed to delete employee", err);
      alert("Failed to delete employee");
    }
  };

  const handleEdit = (emp: Employee) => {
    setEditingEmployee(emp);
  };

  return (
    <div className="p-6">
      <div className="flex items-center justify-between mb-6">
        <div>
          <h2 className="text-2xl font-bold text-foreground flex items-center gap-2">
            <Users className="h-6 w-6" />
            Employees
          </h2>
          <p className="text-muted-foreground text-sm">
            {viewMode === "admin" && "Manage all employees in the organization"}
            {viewMode === "manager" && "View employees under your management"}
          </p>
        </div>
        {viewMode === "admin" && (
          <Button onClick={() => setShowAddForm(true)}>
            <Plus className="h-4 w-4 mr-2" />
            Add Employee
          </Button>
        )}
      </div>

      {showAddForm && (
        <AddEmployeeForm
          onCreated={handleCreated}
          onClose={() => setShowAddForm(false)}
        />
      )}
      {editingEmployee && (
        <EditEmployeeForm
          employee={editingEmployee}
          usersList={usersList}
          onUpdated={(updated) => {
            setEmployees((prev) =>
              prev.map((p) => (p.e_id === updated.e_id ? updated : p))
            );
            setEditingEmployee(null);
          }}
          onClose={() => setEditingEmployee(null)}
        />
      )}

      <Card>
        <CardHeader className="pb-4">
          <div className="flex items-center gap-4">
            <div className="relative flex-1 max-w-sm">
              <Search className="absolute left-3 top-1/2 -translate-y-1/2 h-4 w-4 text-muted-foreground" />
              <Input
                placeholder="Search employees..."
                value={searchTerm}
                onChange={(e) => setSearchTerm(e.target.value)}
                className="pl-9"
              />
            </div>
            <div className="text-sm text-muted-foreground">
              {filteredEmployees.length} employee
              {filteredEmployees.length !== 1 ? "s" : ""}
            </div>
          </div>
        </CardHeader>
        <CardContent>
          <Table>
            <TableHeader>
              <TableRow>
                <TableHead>Employee</TableHead>
                <TableHead>Designation</TableHead>
                <TableHead>Manager</TableHead>

                {viewMode === "admin" && <TableHead>Actions</TableHead>}
              </TableRow>
            </TableHeader>
            <TableBody>
              {paginatedEmployees.map((emp) => {
                const manager = emp.mgr_id
                  ? getEmployeeByIdLocal(emp.mgr_id)
                  : null;
                return (
                  <TableRow key={emp.e_id} className="animate-card-enter">
                    <TableCell>
                      <div className="flex items-center gap-3">
                        <div className="h-10 w-10 rounded-full bg-primary/10 flex items-center justify-center">
                          <UserCircle className="h-5 w-5 text-primary" />
                        </div>
                        <div>
                          <div className="font-medium text-foreground">
                            {emp.name}
                          </div>
                          <div className="text-sm text-muted-foreground flex items-center gap-1">
                            <Mail className="h-3 w-3" />
                            {emp.email}
                          </div>
                        </div>
                      </div>
                    </TableCell>
                    <TableCell>
                      <div className="flex items-center gap-2 text-sm">
                        <Briefcase className="h-4 w-4 text-muted-foreground" />
                        {emp.designation}
                      </div>
                    </TableCell>
                    <TableCell>
                      {manager ? (
                        <span className="text-sm">{manager.name}</span>
                      ) : (
                        <span className="text-sm text-muted-foreground">—</span>
                      )}
                    </TableCell>

                    {viewMode === "admin" && (
                      <TableCell>
                        <div className="flex items-center gap-2">
                          <Button
                            variant="ghost"
                            size="sm"
                            onClick={() => handleEdit(emp)}
                          >
                            <Edit className="h-4 w-4" />
                          </Button>
                          <Button
                            variant="destructive"
                            size="sm"
                            onClick={() => handleDelete(emp)}
                          >
                            <Trash className="h-4 w-4" />
                          </Button>
                        </div>
                      </TableCell>
                    )}
                  </TableRow>
                );
              })}
            </TableBody>
          </Table>

          {totalPages > 1 && (
            <div className="flex items-center justify-between mt-4 pt-4 border-t">
              <Button
                variant="outline"
                size="sm"
                onClick={() => setPage((p) => Math.max(1, p - 1))}
                disabled={page === 1}
              >
                Previous
              </Button>
              <span className="text-sm text-muted-foreground">
                Page {page} of {totalPages}
              </span>
              <Button
                variant="outline"
                size="sm"
                onClick={() => setPage((p) => Math.min(totalPages, p + 1))}
                disabled={page === totalPages}
              >
                Next
              </Button>
            </div>
          )}
        </CardContent>
      </Card>
    </div>
  );
};

export default EmployeeList;
