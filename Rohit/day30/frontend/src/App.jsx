// App.jsx
import { useState } from "react"
import { ThemeProvider } from "@/components/theme-provider"
import "./App.css"
import { SidebarProvider, SidebarTrigger, useSidebar } from "@/components/ui/sidebar"
import { AppSidebar } from "@/components/app-sidebar"
import Home from "./components/Home"
import Cia_section from "./components/Cia_section"
import Stats from "./components/Stats"

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

function App() {
  const [count, setCount] = useState(0)

  return (
    <ThemeProvider defaultTheme="dark" storageKey="vite-ui-theme">
       <div className="grid-background"></div>
      <SidebarProvider>
        {/* Overlay sidebar */}
        <AppSidebar />

        <Backdrop />

        <main className="relative">
          <div className="p-4">
            <SidebarTrigger />
          </div>

          {/* Full-screen background image */}
          {/* <div className="text-3xl text-center" >Hello from browser side</div>
           */}
           <Home/>
           <Stats/>
           <Cia_section/>
        </main>
      </SidebarProvider>
    </ThemeProvider>
  )
}

export default App
