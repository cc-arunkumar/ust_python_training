import axios from "axios";

const API_BASE_URL = "http://localhost:8000";


export const login = async (email, password) => {
  const res = await axios.post("http://localhost:8000/api/login", {
    email,
    password,
  });
  return res.data;
};


export const getEmployees = async () => {
  const res = await axios.get(`${API_BASE_URL}/api/employees`);
  return res.data; 
};

export const createEmployee = async (data) => {
  return axios.post(`${API_BASE_URL}/api/employees`, data);
};

export const updateEmployee = async (id, data) => {
  return axios.put(`${API_BASE_URL}/api/employees/${id}`, data);
};

export const deleteEmployee = async (id) => {
  return axios.delete(`${API_BASE_URL}/api/employees/${id}`);
};
