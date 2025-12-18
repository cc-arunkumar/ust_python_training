import React, { createContext, useContext, useEffect, useState } from "react";
import api from "@/services/api";

interface Employee {
  e_id: string;
  name: string;
  email?: string;
  designation?: string;
  [key: string]: any;
}

interface EmployeesContextValue {
  employees: Employee[];
  loading: boolean;
  getEmployeeById: (e_id?: string) => Employee | undefined;
  refresh: () => Promise<void>;
}

const EmployeesContext = createContext<EmployeesContextValue | undefined>(
  undefined
);

export const EmployeesProvider: React.FC<{ children: React.ReactNode }> = ({
  children,
}) => {
  const [employees, setEmployees] = useState<Employee[]>([]);
  const [loading, setLoading] = useState(true);

  const fetchEmployees = async () => {
    setLoading(true);
    try {
      // call backend employees route (requires auth)
      const res = await api.get("/api/employees");
      // Normalize backend employee shape to frontend-friendly shape (e_id)
      const fetched = (res.data || []).map((emp: any) => ({
        ...emp,
        // normalize e_id to the prefixed form used across the UI (E###)
        e_id:
          emp.e_id ||
          (emp.emp_id != null
            ? `E${String(emp.emp_id).padStart(3, "0")}`
            : undefined),
      }));
      setEmployees(fetched || []);
    } catch (err) {
      console.error("Failed to load employees", err);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchEmployees();
  }, []);

  const normalizeId = (id?: string | number) =>
    id == null ? "" : String(id).replace(/\D/g, "");

  const value: EmployeesContextValue = {
    employees,
    loading,
    // Accepts either numeric string, prefixed like 'E001' or a number.
    getEmployeeById: (e_id?: string) => {
      if (!e_id) return undefined;
      const target = normalizeId(e_id);
      return employees.find((e) => normalizeId(e.e_id) === target);
    },
    refresh: fetchEmployees,
  };

  return (
    <EmployeesContext.Provider value={value}>
      {children}
    </EmployeesContext.Provider>
  );
};

export const useEmployees = () => {
  const ctx = useContext(EmployeesContext);
  if (!ctx)
    throw new Error("useEmployees must be used within EmployeesProvider");
  return ctx;
};

export default EmployeesContext;
