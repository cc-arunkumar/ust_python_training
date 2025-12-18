import React, { useState, useEffect } from "react";
import Header from "@/components/layout/Header";
import Sidebar from "@/components/layout/Sidebar";
import { useAuth } from "@/contexts/AuthContext";
import { Role } from "@/types";
import { Switch } from "@/components/ui/switch";
import { Input } from "@/components/ui/input";
import { Button } from "@/components/ui/button";

const SettingsPage: React.FC = () => {
  const { highestRole, user } = useAuth();
  const [viewMode, setViewMode] = useState<Role>(highestRole);
  const [sidebarOpen, setSidebarOpen] = useState(true);
  const [emailNotifications, setEmailNotifications] = useState(true);
  const [inAppNotifications, setInAppNotifications] = useState(true);
  const [notificationEmail, setNotificationEmail] = useState(
    user?.employee?.email || ""
  );

  useEffect(() => {
    setViewMode(highestRole);
  }, [highestRole]);

  if (!user) return null;

  const save = () => {
    // Local UI only — don't change backend connections per instructions
    alert("Settings saved (frontend only)");
  };

  return (
    <div className="min-h-screen bg-background">
      <Header
        currentView={viewMode}
        onViewChange={setViewMode}
        onToggleSidebar={() => setSidebarOpen((s) => !s)}
        // sidebarOpen={sidebarOpen}
      />
      <div className="flex">
        <Sidebar
          isOpen={sidebarOpen}
          onClose={() => setSidebarOpen(false)}
          onToggle={() => setSidebarOpen((s) => !s)}
        />
        <main className="flex-1 p-6">
          <h2 className="text-2xl font-bold mb-4">Settings</h2>

          <section className="mb-6 max-w-xl">
            <h3 className="font-semibold mb-2">Notification Settings</h3>
            <div className="flex items-center justify-between mb-3">
              <div>
                <p className="font-medium">In-app Notifications</p>
                <p className="text-sm text-muted-foreground">
                  Show notifications for task updates
                </p>
              </div>
              <Switch
                checked={inAppNotifications}
                onCheckedChange={setInAppNotifications}
              />
            </div>

            <div className="flex items-center justify-between mb-3">
              <div>
                <p className="font-medium">Email Notifications</p>
                <p className="text-sm text-muted-foreground">
                  Receive email notifications
                </p>
              </div>
              <Switch
                checked={emailNotifications}
                onCheckedChange={setEmailNotifications}
              />
            </div>
          </section>

          <section className="mb-6 max-w-xl">
            <h3 className="font-semibold mb-2">Email Settings</h3>
            <div className="mb-3">
              <p className="text-sm text-muted-foreground mb-1">
                Notification email
              </p>
              <Input
                value={notificationEmail}
                onChange={(e) => setNotificationEmail(e.target.value)}
              />
            </div>
            <div className="flex gap-2">
              <Button onClick={save}>Save</Button>
              <Button
                variant="outline"
                onClick={() => {
                  setNotificationEmail(user?.employee?.email || "");
                  setEmailNotifications(true);
                  setInAppNotifications(true);
                }}
              >
                Reset
              </Button>
            </div>
          </section>
        </main>
      </div>
    </div>
  );
};

export default SettingsPage;
