import axios from "axios";

const API_BASE_URL = "http://localhost:8000";

// LOGIN
export const login = async (email, password) => {
  const res = await axios.post(`${API_BASE_URL}/api/login`, {
    email,
    password,
  });
  return res.data;
};

// GET ALL EMPLOYEES
export const getEmployees = async () => {
  const res = await axios.get(`${API_BASE_URL}/api/employees`);
  return res.data; 
};

// CREATE EMPLOYEE
export const createEmployee = async (data) => {
  return axios.post(`${API_BASE_URL}/api/employees`, data);
};

// UPDATE EMPLOYEE
export const updateEmployee = async (id, data) => {
  return axios.put(`${API_BASE_URL}/api/employees/${id}`, data);
};

// DELETE EMPLOYEE
export const deleteEmployee = async (id) => {
  return axios.delete(`${API_BASE_URL}/api/employees/${id}`);
};
