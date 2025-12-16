// app-sidebar.jsx
import { Calendar, Home, Inbox, Search, Settings, Mail } from "lucide-react"
import {
  Sidebar,
  SidebarContent,
  SidebarGroup,
  SidebarGroupContent,
  SidebarGroupLabel,
  SidebarMenu,
  SidebarMenuButton,
  SidebarMenuItem,
  useSidebar,
} from "@/components/ui/sidebar"

const items = [
  { title: "Login", url: "#", icon: Home },
  { title: "Admin", url: "#", icon: Home },
  { title: "Create Task", url: "#", icon: Inbox },
  { title: "Add User", url: "#", icon: Calendar },
  { title: "All Task", url: "#", icon: Search },
  { title: "Help", url: "#", icon: Settings },
]

export function AppSidebar() {
  const { open } = useSidebar()

  return (
    <div
      className={[
        "fixed inset-y-0 left-0 z-50 w-64",
        "transform transition-transform duration-300",
        open ? "translate-x-0" : "-translate-x-full",
      ].join(" ")}
    >
      <Sidebar className="h-full bg-gray-900 shadow-lg">
        <SidebarContent className="flex flex-col h-full">
          {/* Top menu */}
          <SidebarGroup>
            <SidebarGroupLabel >
                <span className=" font-extrabold text-xl mb-2">Jira Lite</span>

                </SidebarGroupLabel>
            <SidebarGroupContent>
              <SidebarMenu>
                {items.map((item) => (
                  <SidebarMenuItem key={item.title}>
                    <SidebarMenuButton asChild>
                      <a
                        href={item.url}
                        className="flex items-center gap-2 text-gray-300 hover:text-white"
                      >
                        <item.icon className="w-4 h-4" />
                        <span>{item.title}</span>
                      </a>
                    </SidebarMenuButton>
                  </SidebarMenuItem>
                ))}
              </SidebarMenu>
            </SidebarGroupContent>
          </SidebarGroup>

          {/* Bottom email */}
          <div className="mt-auto p-4 border-t border-gray-700">
            <a
              href="mailto:yourmail@example.com"
              className="flex items-center gap-2 text-sm text-gray-300 hover:text-white"
            >
              <Mail className="w-4 h-4" />
              <span>yourmail@example.com</span>
            </a>
          </div>
        </SidebarContent>
      </Sidebar>
    </div>
  )
}
