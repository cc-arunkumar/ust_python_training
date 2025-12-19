import { Link } from "react-router-dom";
import { useState } from "react";
import { useAuth } from "../auth/AuthContext";

const Sidebar = () => {
  // 🔹 Hooks MUST be first
  const { user } = useAuth();

  const [openTasks, setOpenTasks] = useState(false);
  const [openUsers, setOpenUsers] = useState(false);
  const [openEmployees, setOpenEmployees] = useState(false);

  // 🔹 Safe guard AFTER hooks
  if (!user || !Array.isArray(user.roles)) return null;

  // Normalize roles (case-insensitive)
  const roles = user.roles.map((r) => r.toLowerCase());

  const isAdmin = roles.includes("admin");
  const isManager = roles.includes("manager");
  const isDeveloper = roles.includes("developer");

  return (
    <aside className="w-64 bg-gray-900 text-white p-5 min-h-screen">
      <h2 className="text-xl font-bold mb-6">Task Manager</h2>

      <nav className="space-y-2">

        {/* Dashboard */}
        <Link className="block hover:text-gray-300" to="/dashboard">
          Dashboard
        </Link>

        {/* ---------------- TASKS ---------------- */}
        {(isAdmin || isManager || isDeveloper) && (
          <div>
            <button
              onClick={() => setOpenTasks(!openTasks)}
              className="w-full text-left font-semibold hover:text-gray-300"
            >
              Tasks
            </button>

            {openTasks && (
              <div className="ml-4 mt-2 space-y-1">
                {isDeveloper && (
                  <Link to="/my-tasks" className="block hover:text-gray-300">
                    My Tasks
                  </Link>
                )}

                {(isManager || isAdmin) && (
                  <Link to="/review-tasks" className="block hover:text-gray-300">
                    Review Tasks
                  </Link>
                )}

                {(isManager || isAdmin) && (
                  <Link to="/create-task" className="block hover:text-gray-300">
                    Create Task
                  </Link>
                )}
              </div>
            )}
          </div>
        )}

        {/* ---------------- USER ACTIONS ---------------- */}
        {isAdmin && (
          <div>
            <button
              onClick={() => setOpenUsers(!openUsers)}
              className="w-full text-left font-semibold hover:text-gray-300"
            >
              User Actions
            </button>

            {openUsers && (
              <div className="ml-4 mt-2 space-y-1">
                <Link to="/users/create" className="block hover:text-gray-300">
                  Create User
                </Link>
                <Link to="/users/update" className="block hover:text-gray-300">
                  Update User
                </Link>
                <Link to="/users/delete" className="block hover:text-gray-300">
                  Delete User
                </Link>
              </div>
            )}
          </div>
        )}

        {/* ---------------- EMPLOYEE ---------------- */}
        {isAdmin && (
          <div>
            <button
              onClick={() => setOpenEmployees(!openEmployees)}
              className="w-full text-left font-semibold hover:text-gray-300"
            >
              Employee
            </button>

            {openEmployees && (
              <div className="ml-4 mt-2 space-y-1">
                <Link to="/employees/create" className="block hover:text-gray-300">
                  Create Employee
                </Link>
                <Link to="/employees/update" className="block hover:text-gray-300">
                  Update Employee
                </Link>
                <Link to="/employees/delete" className="block hover:text-gray-300">
                  Delete Employee
                </Link>
              </div>
            )}
          </div>
        )}
      </nav>
    </aside>
  );
};

export default Sidebar;
