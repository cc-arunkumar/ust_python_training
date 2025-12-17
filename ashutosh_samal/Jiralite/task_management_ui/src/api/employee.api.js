import API from "./axios";

// 🔹 Get all employees (ADMIN)
export const getEmployees = async () => {
  const res = await API.get("/employees/");
  return res.data;
};

// 🔹 Get employee by ID
export const getEmployeeById = async (id) => {
  const res = await API.get(`/employees/${id}`);
  return res.data;
};

// 🔹 Create employee
export const createEmployee = async (data) => {
  const res = await API.post("/employees/", data);
  return res.data;
};

// 🔹 Update employee (PUT)
export const updateEmployee = async (id, data) => {
  const res = await API.put(`/employees/${id}`, data);
  return res.data;
};

// 🔹 Delete employee
export const deleteEmployee = async (id) => {
  await API.delete(`/employees/${id}`);
};
