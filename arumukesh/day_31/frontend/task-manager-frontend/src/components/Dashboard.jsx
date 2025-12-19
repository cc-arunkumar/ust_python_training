import React from "react";
import { Routes, Route, Navigate } from "react-router-dom";
import Navbar from "./Navbar";
import Sidebar from "./Sidebar";
import Employees from "../pages/Employees";
import Tasks from "../pages/Tasks";

export default function Dashboard() {
  return (
    <div className="app-container">
      <Navbar />
      <div className="flex flex-1 h-[calc(100vh-64px)]">
        <Sidebar />
        <main className="flex-1 p-6 overflow-auto">
          <Routes>
            <Route path="/dashboard" element={<div>Welcome to TaskFlow</div>} />
            <Route path="/employees" element={<Employees />} />
            <Route path="/tasks" element={<Tasks />} />
            <Route path="/" element={<Navigate to="/dashboard" replace />} />
          </Routes>
        </main>
      </div>
    </div>
  );
}
