// App.jsx
import { useState } from "react"
import { ThemeProvider } from "@/components/theme-provider"
import "./App.css"
import { SidebarProvider, SidebarTrigger, useSidebar } from "@/components/ui/sidebar"
import { AppSidebar } from "@/components/app-sidebar"
import Home from "./components/Home"
import Cia_section from "./components/Cia_section"
import Stats from "./components/Stats"
import { TaskTable } from "./components/TaskTable" 
import { Routes, Route, Navigate } from "react-router-dom"
import { CreateTaskForm } from "./components/CreateTaskForm"
import { Login } from "./components/Login"
import { CreateEmployeeForm } from "./components/CreateEmployeeForm"
import { EmployeeTable } from "./components/EmployeeTable"

// Helper: read role from localStorage
const getUserRole = () => {
  console.log(localStorage.getItem("role"))
  return localStorage.getItem("role") || null

}

function Backdrop() {
  const { open, setOpen } = useSidebar()
  if (!open) return null
  return (
    <div
      className="fixed inset-0 bg-red/50 z-40"
      onClick={() => setOpen(false)}
      aria-hidden="true"
    />
  )
}

// Wrapper for protected routes
function ProtectedRoute({ element, allowedRoles }) {
  const role = getUserRole()
  if (!role) {
    // not logged in → redirect to login
    return <Navigate to="/login" replace />
  }
  return allowedRoles.includes(role) ? element : <Navigate to="/" replace />
}

function App() {
  return (
    <ThemeProvider defaultTheme="dark" storageKey="vite-ui-theme">
      <div className="grid-background"></div>
      <SidebarProvider>
        <AppSidebar />
        <Backdrop />

        <main className="">
          <div className="p-4 mr-270">
            <SidebarTrigger />
          </div>

          <Routes>
            {/* Public routes */}
            <Route path="/" element={
              <>
                <Home />
                <Stats />
                <Cia_section />
              </>
            } />
            <Route path="/login" element={<Login />} />

            {/* Accessible to all authenticated roles */}
            <Route path="/show-task" element={
              <ProtectedRoute element={ <TaskTable />} allowedRoles={["MANAGER","ADMIN"]}/>
             } />

            {/* Restricted routes */}
            <Route path="/create-task" element={
              <ProtectedRoute element={<CreateTaskForm />} allowedRoles={["ADMIN"]} />
            } />
            <Route path="/add-employee" element={
              <ProtectedRoute element={<CreateEmployeeForm />} allowedRoles={["ADMIN"]} />
            } />
            <Route path="/all-employee" element={
              <ProtectedRoute element={<EmployeeTable />} allowedRoles={["MANAGER","ADMIN"]} />
            } />
          </Routes>
        </main>
      </SidebarProvider>
    </ThemeProvider>
  )
}

export default App
