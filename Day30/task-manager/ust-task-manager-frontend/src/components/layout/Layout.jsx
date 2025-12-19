// import Navbar from "./Navbar";
// import Sidebar from "./Sidebar";

// function Layout({ children }) {
//   return (
//     <div className="h-screen flex flex-col">
//       <Navbar />
//       <div className="flex flex-1">
//         <Sidebar />
//         <div className="flex-1 p-4 bg-gray-50">{children}</div>
//       </div>
//     </div>
//   );
// }

// export default Layout;

import { Outlet } from "react-router-dom"; // <--- CRITICAL IMPORT
import Navbar from "./Navbar";
import Sidebar from "./Sidebar";

function Layout() {
  return (
    <div className="flex h-screen bg-gray-50 overflow-hidden">
      {/* Sidebar - Fixed Width */}
      <div className="flex-shrink-0">
        <Sidebar />
      </div>

      {/* Main Content - Flex Grow */}
      <div className="flex-1 flex flex-col min-w-0">
        <Navbar />

        <main className="flex-1 overflow-auto p-4 md:p-6">
          {/* 👇 THIS IS WHERE THE DASHBOARD LOADS. IF MISSING, SCREEN IS BLANK */}
          <Outlet />
        </main>
      </div>
    </div>
  );
}

export default Layout;
