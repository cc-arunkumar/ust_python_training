import { Routes, Route, useNavigate, Navigate, Link, useLocation } from "react-router-dom"
import { ThemeProvider } from "@/components/theme-provider"
import { useState, useEffect } from "react"
import "./App.css"
import { Button } from "@/components/ui/button"

import { Login } from "./components/Login"
import { TaskTable } from "./components/Table"
import { CreateTaskForm } from "./components/CreateTaskForm"

function App() {
  const [token, setToken] = useState(localStorage.getItem("token"))
  const navigate = useNavigate()
  const location = useLocation()


  const handleLogin = (jwtToken) => {
    localStorage.setItem("token", jwtToken)
    setToken(jwtToken)
    navigate("/tasks")
  }


  const handleLogout = () => {
    localStorage.removeItem("token")
    setToken(null)
    navigate("/")
  }

  useEffect(() => {
    if (location.pathname === "/") {
      setToken(null)
      localStorage.removeItem("token")
    }
  }, [location])

  const isAuthenticated = !!token

  return (
    <ThemeProvider defaultTheme="dark" storageKey="vite-ui-theme">
      <main className="flex flex-col">
        <div>
          <h1 className="text-5xl font-bold text-center text-white m-2 mb-10">
            Task Manager
          </h1>
        </div>

        {isAuthenticated && (
          <div className="flex justify-end px-4 gap-2">
            <Link to="/create-task">
              <Button>Add Task</Button>
            </Link>
            <Button variant="outline" onClick={handleLogout}>
              Logout
            </Button>
          </div>
        )}

        <Routes>
          <Route
            path="/"
            element={
              <div className="flex justify-center items-center">
                <Login onLogin={handleLogin} />
              </div>
            }
          />
          <Route
            path="/tasks"
            element={
              isAuthenticated ? (
                <div className="flex justify-center items-center">
                  <TaskTable token={token} />
                </div>
              ) : (
                <Navigate to="/" replace />
              )
            }
          />
          <Route
            path="/create-task"
            element={
              isAuthenticated ? (
                <div className="flex justify-center items-center">
                  <CreateTaskForm token={token} />
                </div>
              ) : (
                <Navigate to="/" replace />
              )
            }
          />
        </Routes>
      </main>
    </ThemeProvider>
  )
}

export default App
