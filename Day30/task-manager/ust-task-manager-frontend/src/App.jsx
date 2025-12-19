// import { Routes, Route, Navigate } from "react-router-dom";
// import LoginPage from "./pages/auth/LoginPage";
// import ProtectedRoute from "./components/auth/ProtectedRoute";
// import Layout from "./components/layout/Layout";
// import Dashboard from "./pages/dashboard/Dashboard";
// import TasksPage from "./pages/tasks/TasksPage";
// import EmployeesPage from "./pages/employees/EmployeesPage";
// import UsersPage from "./pages/users/UsersPage";
// import { useAuth } from "./context/AuthContext";

// function App() {
//   const { user } = useAuth();

//   return (
//     <Routes>
//       {/* Redirect root */}
//       <Route path="/" element={<Navigate to="/login" />} />
//       <Route path="/login" element={<LoginPage />} />

//       {/* Protected Routes */}
//       <Route
//         path="/*"
//         element={
//           <ProtectedRoute>
//             <Layout>
//               <Routes>
//                 <Route path="/dashboard" element={<Dashboard />} />
//                 <Route path="/tasks" element={<TasksPage />} />
                
//                 {/* Admin/Manager Only */}
//                 {(user?.role === "admin" || user?.role === "manager") && (
//                   <Route path="/employees" element={<EmployeesPage />} />
//                 )}

//                 {/* Admin Only */}
//                 {user?.role === "admin" && (
//                   <Route path="/users" element={<UsersPage />} />
//                 )}
                
//                 {/* Fallback 404 for protected area */}
//                 <Route path="*" element={<Navigate to="/dashboard" />} />
//               </Routes>
//             </Layout>
//           </ProtectedRoute>
//         }
//       />
//     </Routes>
//   );
// }

// export default App;