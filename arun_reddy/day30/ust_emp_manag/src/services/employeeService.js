import { api } from "./api";

export const employeeService = {
  getById: async (empId) => {
    return api.get(`/employee/${empId}`);
  },

  getByManager: async (managerId) => {
    return api.get(`/employee/manager/${managerId}`);
  },

  create: async (employeeData) => {
    return api.post("/employee", employeeData);
  },

  update: async (empId, employeeData) => {
    return api.put(`/employee/${empId}`, employeeData);
  },

  delete: async (empId) => {
    return api.delete(`/employee/${empId}`);
  },
};
