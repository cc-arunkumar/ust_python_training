// api.js
import axios from "axios";

const API_URL = "http://127.0.0.1:8000"; // FastAPI default

export const getEmployees = async () => {
  return await axios.get(`${API_URL}/employees`);
};

export const getEmployee = async (name) => {
  return await axios.get(`${API_URL}/employees/${name}`);
};

export const addEmployee = async (employee) => {
  return await axios.post(`${API_URL}/employees`, employee);
};

export const updateEmployee = async (name, employee) => {
  return await axios.put(`${API_URL}/employees/${name}`, employee);
};

export const deleteEmployee = async (name) => {
  return await axios.delete(`${API_URL}/employees/${name}`);
};
