import { useState } from 'react';
import './EmployeeManager.css'

export default function EmployeeManager() {
  const [empName, setEmpName] = useState('');
  const [empRole, setEmpRole] = useState('');
  const [employees, setEmployees] = useState([]);

  const addEmployee = () => {
    if (empName && empRole) {
      setEmployees([
        ...employees, 
        { id: Date.now(), name: empName, role: empRole }
      ]);
      setEmpName('');
      setEmpRole('');
    }
  };

  const removeEmployee = (id) => {
    setEmployees(employees.filter(emp => emp.id !== id));
  };

  return (
    <div className="bg-white rounded-lg shadow p-6">
      <h3 className="font-semibold text-lg mb-3 text-slate-700">
        2 & 3. Add/Remove Employee
      </h3>
      <div className="space-y-2 mb-3">
        <input 
          type="text" 
          value={empName}
          onChange={(e) => setEmpName(e.target.value)}
          placeholder="Employee Name"
          className="w-full border border-slate-300 rounded px-3 py-2"
        />
        <input 
          type="text" 
          value={empRole}
          onChange={(e) => setEmpRole(e.target.value)}
          placeholder="Role"
          className="w-full border border-slate-300 rounded px-3 py-2"
        />
        <button 
          onClick={addEmployee} 
          className="w-full bg-blue-500 text-white py-2 rounded hover:bg-blue-600"
        >
          Add Employee
        </button>
      </div>
      <ul className="space-y-2">
        {employees.map(emp => (
          <li 
            key={emp.id} 
            className="flex items-center justify-between bg-slate-50 p-3 rounded"
          >
            <div>
              <div className="font-medium text-slate-700">{emp.name}</div>
              <div className="text-sm text-slate-500">{emp.role}</div>
            </div>
            <button 
              onClick={() => removeEmployee(emp.id)}
              className="bg-red-500 text-white px-3 py-1 rounded text-sm hover:bg-red-600"
            >
              Remove
            </button>
          </li>
        ))}
      </ul>
      {employees.length === 0 && (
        <p className="text-center text-slate-400 py-4">No employees added yet</p>
      )}
    </div>
  );
}