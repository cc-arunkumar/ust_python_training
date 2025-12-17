// import { useEffect, useState } from "react";
// import Navbar from "../components/Navbar";
// import Sidebar from "../components/Sidebar";
// import Board from "./Board";
// import {
//   getTasks,
//   updateTaskStatus,
//   deleteTask,
// } from "../api/task.api";

// export default function Dashboard() {
//   const [tasks, setTasks] = useState([]);

//   // 🔹 Load all tasks
//   const loadTasks = async () => {
//     const data = await getTasks();   // ✅ FIXED
//     setTasks(data);
//   };

//   useEffect(() => {
//     loadTasks();
//   }, []);

//   return (
//     <div className="h-screen flex flex-col bg-gray-100">
//       {/* 🔹 TOP NAVBAR */}
//       <Navbar />

//       {/* 🔹 MAIN LAYOUT */}
//       <div className="flex flex-1 overflow-hidden">
//         {/* 🔹 SIDEBAR */}
//         <div className="w-64 shrink-0 border-r bg-white">
//           <Sidebar />
//         </div>

//         {/* 🔹 BOARD */}
//         <div className="flex-1 overflow-x-auto overflow-y-hidden">
//           <Board
//             tasks={tasks}
//             onStatusChange={async (id, payload) => {
//               await updateTaskStatus(id, payload);
//               loadTasks();
//             }}
//             onDelete={async (id) => {
//               await deleteTask(id);
//               loadTasks();
//             }}
//           />
//         </div>
//       </div>
//     </div>
//   );
// }

import Navbar from "../components/Navbar";
import Sidebar from "../components/Sidebar";
import Board from "./Board";

export default function Dashboard() {
  return (
    <div className="h-screen flex flex-col bg-gray-100">
      <Navbar />

      <div className="flex flex-1 overflow-hidden">
        <div className="w-64 shrink-0 border-r bg-white">
          <Sidebar />
        </div>

        <div className="flex-1 overflow-x-auto">
          <Board />
        </div>
      </div>
    </div>
  );
}
