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
      setEmployees(res.data || []);
    } catch (err) {
      console.error("Failed to load employees", err);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchEmployees();
  }, []);

  const value: EmployeesContextValue = {
    employees,
    loading,
    getEmployeeById: (e_id?: string) => employees.find((e) => e.e_id === e_id),
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
