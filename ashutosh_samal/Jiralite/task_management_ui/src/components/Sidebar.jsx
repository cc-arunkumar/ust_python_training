// import { Link, useLocation } from "react-router-dom";
// import { useAuth } from "../context/AuthContext";

// export default function Sidebar() {
//   const { user, activeRole } = useAuth();
//   const location = useLocation();

//   if (!user) return null;

//   const isActive = (path) =>
//     location.pathname.startsWith(path)
//       ? "bg-gray-200 font-medium"
//       : "hover:bg-gray-100";

//   return (
//     <aside className="w-60 h-screen border-r bg-white px-4 py-6">
//       {/* HEADER */}
//       <div className="mb-6">
//         <h1 className="text-lg font-semibold">Task Manager</h1>
//         <p className="text-xs text-gray-500 mt-1">
//           Logged in as <span className="font-medium">{activeRole}</span>
//         </p>
//       </div>

//       {/* NAVIGATION */}
//       <nav>
//         <ul className="space-y-1 text-sm">
//           {/* COMMON */}
//           <li>
//             <Link
//               to="/dashboard"
//               className={`block px-3 py-2 rounded ${isActive("/dashboard")}`}
//             >
//               Dashboard
//             </Link>
//           </li>

//           {/* ADMIN */}
//           {activeRole === "ADMIN" && (
//             <>
//               <li>
//                 <Link
//                   to="/tasks/create"
//                   className={`block px-3 py-2 rounded ${isActive("/tasks/create")}`}
//                 >
//                   Create Task
//                 </Link>
//               </li>
//               <li>
//                 <Link
//                   to="/admin/employees"
//                   className={`block px-3 py-2 rounded ${isActive("/admin/employees")}`}
//                 >
//                   Employees
//                 </Link>
//               </li>
//               <li>
//                 <Link
//                   to="/admin/users"
//                   className={`block px-3 py-2 rounded ${isActive("/admin/users")}`}
//                 >
//                   Users
//                 </Link>
//               </li>
//             </>
//           )}

//           {/* MANAGER */}
//           {activeRole === "MANAGER" && (
//             <>
//               <li>
//                 <Link
//                   to="/tasks/create"
//                   className={`block px-3 py-2 rounded ${isActive("/tasks/create")}`}
//                 >
//                   Create Task
//                 </Link>
//               </li>
//               <li>
//                 <Link
//                   to="/dashboard"
//                   className={`block px-3 py-2 rounded ${isActive("/dashboard")}`}
//                 >
//                   Team Tasks
//                 </Link>
//               </li>
//             </>
//           )}

//           {/* DEVELOPER */}
//           {activeRole === "DEVELOPER" && (
//             <li>
//               <Link
//                 to="/dashboard"
//                 className={`block px-3 py-2 rounded ${isActive("/dashboard")}`}
//               >
//                 My Tasks
//               </Link>
//             </li>
//           )}
//         </ul>
//       </nav>
//     </aside>
//   );
// }


import { Link, useLocation } from "react-router-dom";
import { useAuth } from "../context/AuthContext";

export default function Sidebar() {
  const { activeRole, user } = useAuth();
  const location = useLocation();

  const isActive = (path) =>
    location.pathname.startsWith(path)
      ? "bg-gray-200 font-medium"
      : "hover:bg-gray-100";

  /* Fallback avatar initials */
  const initials = user?.emp_id
    ? `E${user.emp_id}`
    : "U";

  return (
    <aside className="h-full w-full bg-white px-4 py-6">
      {/* 👤 USER PROFILE */}
      <div className="flex items-center gap-3 mb-8">
        {/* Avatar */}
        <img
          src={`https://api.dicebear.com/7.x/personas/svg?seed=${activeRole}`}
          alt="User Avatar"
          className="w-11 h-11 rounded-full border shadow-sm bg-white"
        />

        {/* Role Info */}
        <div>
          <p className="text-xs text-gray-500">
            Logged in as
          </p>
          <p className="text-sm font-semibold text-gray-800">
            {activeRole || "—"}
          </p>
        </div>
      </div>

      {/* NAVIGATION */}
      <nav>
        <ul className="space-y-1 text-sm text-gray-800">
          {/* COMMON */}
          <li>
            <Link
              to="/dashboard"
              className={`block px-3 py-2 rounded ${isActive("/dashboard")}`}
            >
              Dashboard
            </Link>
          </li>

          {/* ADMIN */}
          {activeRole === "ADMIN" && (
            <>
              <li>
                <Link
                  to="/tasks/create"
                  className={`block px-3 py-2 rounded ${isActive("/tasks/create")}`}
                >
                  Create Task
                </Link>
              </li>

              <li>
                <Link
                  to="/admin/employees"
                  className={`block px-3 py-2 rounded ${isActive("/admin/employees")}`}
                >
                  Employees
                </Link>
              </li>

              <li>
                <Link
                  to="/admin/users"
                  className={`block px-3 py-2 rounded ${isActive("/admin/users")}`}
                >
                  Users
                </Link>
              </li>
            </>
          )}

          {/* MANAGER */}
          {activeRole === "MANAGER" && (
            <>
              <li>
                <Link
                  to="/tasks/create"
                  className={`block px-3 py-2 rounded ${isActive("/tasks/create")}`}
                >
                  Create Task
                </Link>
              </li>

              {/* <li>
                <Link
                  to="/dashboard"
                  className={`block px-3 py-2 rounded ${isActive("/dashboard")}`}
                >
                  Team Tasks
                </Link>
              </li> */}
            </>
          )}

          {/* DEVELOPER */}
          {activeRole === "DEVELOPER" && (
            <li>
              <Link
                to="/dashboard"
                className={`block px-3 py-2 rounded ${isActive("/dashboard")}`}
              >
                My Tasks
              </Link>
            </li>
          )}
        </ul>
      </nav>
    </aside>
  );
}
