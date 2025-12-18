// import { Employee, User, Task, Remark } from "@/types";
// import api from "@/services/api";

// export const mockEmployees: Employee[] = [
//   {
//     e_id: "E001",
//     name: "niranjan",
//     email: "john.smith@ust.com",
//     designation: "Senior Developer",
//     mgr_id: "E003",
//   },
//   {
//     e_id: "E002",
//     name: "niranjan",
//     email: "sarah.connor@ust.com",
//     designation: "Junior Developer",
//     mgr_id: "E003",
//   },
//   {
//     e_id: "E003",
//     name: "Michael Chen",
//     email: "michael.chen@ust.com",
//     designation: "Engineering Manager",
//   },
//   {
//     e_id: "E004",
//     name: "sai",
//     email: "emily.davis@ust.com",
//     designation: "Full Stack Developer",
//     mgr_id: "E003",
//   },
//   {
//     e_id: "E005",
//     name: "niranjan",
//     email: "robert.wilson@ust.com",
//     designation: "DevOps Engineer",
//     mgr_id: "E006",
//   },
//   {
//     e_id: "E006",
//     name: "Lisa Anderson",
//     email: "lisa.anderson@ust.com",
//     designation: "Tech Lead",
//   },
//   {
//     e_id: "E007",
//     name: "sai",
//     email: "david.brown@ust.com",
//     designation: "Backend Developer",
//     mgr_id: "E006",
//   },
//   {
//     e_id: "E008",
//     name: "Admin User",
//     email: "admin@ust.com",
//     designation: "System Administrator",
//   },
// ];

// export const mockUsers: User[] = [
//   {
//     e_id: "E001",
//     password: "password123",
//     role: ["developer"],
//     status: "active",
//   },
//   {
//     e_id: "E002",
//     password: "password123",
//     role: ["developer"],
//     status: "active",
//   },
//   {
//     e_id: "E003",
//     password: "password123",
//     role: ["manager", "developer"],
//     status: "active",
//   },
//   {
//     e_id: "E004",
//     password: "password123",
//     role: ["developer"],
//     status: "active",
//   },
//   {
//     e_id: "E005",
//     password: "password123",
//     role: ["developer"],
//     status: "active",
//   },
//   {
//     e_id: "E006",
//     password: "password123",
//     role: ["manager", "developer"],
//     status: "active",
//   },
//   {
//     e_id: "E007",
//     password: "password123",
//     role: ["developer"],
//     status: "active",
//   },
//   { e_id: "E008", password: "password123", role: ["admin"], status: "active" },
// ];

// export const mockTasks: Task[] = [
//   {
//     t_id: "T001",
//     title: "Implement User Authentication",
//     description: "Add JWT-based authentication with role-based access control",
//     created_by: "E003",
//     assigned_to: "E001",
//     assigned_by: "E003",
//     assigned_at: "2024-01-15T09:00:00Z",
//     priority: "high",
//     status: "IN_PROGRESS",
//     reviewer: "E006",
//     expected_closure: "2024-01-25T17:00:00Z",
//   },
//   {
//     t_id: "T002",
//     title: "Design Database Schema",
//     description:
//       "Create normalized database schema for employee and task management",
//     created_by: "E008",
//     assigned_to: "E004",
//     assigned_by: "E003",
//     assigned_at: "2024-01-14T10:00:00Z",
//     priority: "high",
//     status: "REVIEW",
//     reviewer: "E003",
//     expected_closure: "2024-01-20T17:00:00Z",
//   },
//   {
//     t_id: "T003",
//     title: "Setup CI/CD Pipeline",
//     description:
//       "Configure GitHub Actions for automated testing and deployment",
//     created_by: "E006",
//     assigned_to: "E005",
//     assigned_by: "E006",
//     assigned_at: "2024-01-16T11:00:00Z",
//     priority: "medium",
//     status: "TO_DO",
//     reviewer: "E006",
//     expected_closure: "2024-01-28T17:00:00Z",
//   },
//   {
//     t_id: "T004",
//     title: "Implement REST API Endpoints",
//     description: "Create CRUD endpoints for employees and tasks",
//     created_by: "E003",
//     assigned_to: "E007",
//     assigned_by: "E006",
//     assigned_at: "2024-01-17T08:00:00Z",
//     priority: "high",
//     status: "IN_PROGRESS",
//     reviewer: "E003",
//     expected_closure: "2024-01-30T17:00:00Z",
//   },
//   {
//     t_id: "T005",
//     title: "Write Unit Tests",
//     description: "Add comprehensive unit tests for all API endpoints",
//     created_by: "E003",
//     priority: "medium",
//     status: "TO_DO",
//     expected_closure: "2024-02-05T17:00:00Z",
//   },
//   {
//     t_id: "T006",
//     title: "Frontend Dashboard",
//     description:
//       "Build React dashboard with task board and employee management",
//     created_by: "E008",
//     assigned_to: "E002",
//     assigned_by: "E003",
//     assigned_at: "2024-01-18T09:00:00Z",
//     priority: "high",
//     status: "DONE",
//     reviewer: "E006",
//     expected_closure: "2024-01-22T17:00:00Z",
//     actual_closure: "2024-01-21T16:30:00Z",
//   },
//   {
//     t_id: "T007",
//     title: "API Documentation",
//     description: "Create Swagger/OpenAPI documentation for all endpoints",
//     created_by: "E006",
//     assigned_to: "E001",
//     assigned_by: "E006",
//     assigned_at: "2024-01-19T10:00:00Z",
//     priority: "low",
//     status: "TO_DO",
//     reviewer: "E003",
//     expected_closure: "2024-02-10T17:00:00Z",
//   },
//   {
//     t_id: "T008",
//     title: "Performance Optimization",
//     description: "Optimize database queries and add caching layer",
//     created_by: "E003",
//     priority: "medium",
//     status: "TO_DO",
//     expected_closure: "2024-02-15T17:00:00Z",
//   },
// ];

// export const mockRemarks: Remark[] = [
//   {
//     id: "R001",
//     task_id: "T001",
//     comment: "Started working on JWT implementation",
//     created_by: "E001",
//     created_at: "2024-01-16T10:00:00Z",
//   },
//   {
//     id: "R002",
//     task_id: "T002",
//     comment: "Schema design completed, ready for review",
//     created_by: "E004",
//     created_at: "2024-01-18T14:00:00Z",
//   },
//   {
//     id: "R003",
//     task_id: "T006",
//     comment: "Dashboard completed with all features",
//     created_by: "E002",
//     created_at: "2024-01-21T15:00:00Z",
//   },
//   {
//     id: "R004",
//     task_id: "T006",
//     comment: "Approved and deployed",
//     created_by: "E006",
//     created_at: "2024-01-21T16:30:00Z",
//   },
// ];

// export const getEmployeeById = (id: string): Employee | undefined => {
//   return mockEmployees.find((e) => e.e_id === id);
// };

// export const getUserByEmail = (
//   email: string
// ): (User & { employee: Employee }) | undefined => {
//   const employee = mockEmployees.find((e) => e.email === email);
//   if (!employee) return undefined;
//   const user = mockUsers.find((u) => u.e_id === employee.e_id);
//   if (!user) return undefined;
//   return { ...user, employee };
// };

// export const getUserByEmployeeId = (
//   e_id: string
// ): (User & { employee: Employee }) | undefined => {
//   const employee = mockEmployees.find((e) => e.e_id === e_id);
//   if (!employee) return undefined;
//   const user = mockUsers.find((u) => u.e_id === e_id);
//   if (!user) return undefined;
//   return { ...user, employee };
// };

// export const getEmployeesByManagerId = (mgrId: string): Employee[] => {
//   return mockEmployees.filter((e) => e.mgr_id === mgrId);
// };

// export const getTasksByAssignee = (empId: string): Task[] => {
//   return mockTasks.filter((t) => t.assigned_to === empId);
// };

// export const getTasksByReviewer = (mgrId: string): Task[] => {
//   return mockTasks.filter((t) => t.reviewer === mgrId);
// };

// // On module load, try to fetch real data from backend and replace mock arrays.
// (async function refreshFromBackend() {
//   try {
//     const [empRes, usersRes, taskRes] = await Promise.all([
//       api.get("/public/employees"),
//       api.get("/public/users"),
//       api.get("/public/tasks"),
//     ]);

//     if (Array.isArray(empRes.data) && empRes.data.length) {
//       mockEmployees.length = 0;
//       for (const e of empRes.data) {
//         mockEmployees.push({
//           e_id: e.e_id,
//           name: e.name,
//           email: e.email,
//           designation: e.designation || "",
//           mgr_id: e.mgr_id || undefined,
//         });
//       }
//     }

//     if (Array.isArray(usersRes.data) && usersRes.data.length) {
//       mockUsers.length = 0;
//       for (const u of usersRes.data) {
//         mockUsers.push({
//           e_id: u.e_id,
//           password: u.password || "",
//           role: u.role || [],
//           status: u.status || "active",
//         });
//       }
//     }

//     if (Array.isArray(taskRes.data) && taskRes.data.length) {
//       mockTasks.length = 0;
//       for (const t of taskRes.data) {
//         mockTasks.push({
//           t_id: t.t_id,
//           title: t.title,
//           description: t.description,
//           created_by: t.created_by,
//           assigned_to: t.assigned_to,
//           assigned_by: t.assigned_by,
//           assigned_at: t.assigned_at,
//           priority: (t.priority || "medium") as any,
//           status: t.status || "TO_DO",
//           reviewer: t.reviewer,
//           expected_closure: t.expected_closure,
//           actual_closure: t.actual_closure,
//         });
//       }
//     }
//   } catch (err) {
//     // Keep mock data if backend unavailable
//     console.warn("Could not refresh mockData from backend:", err);
//   }
// })();
