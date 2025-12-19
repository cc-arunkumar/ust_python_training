import React, { useEffect, useState } from "react";
import { useAuth } from "@/context/AuthContext";
import { employeeService } from "@/services/employeeService";
import { authService } from "@/services/authService";
import { Card } from "@/components/ui/card";

const Profile: React.FC = () => {
  const { user, currentRole } = useAuth();
  const [details, setDetails] = useState<any>(null);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    const load = async () => {
      setLoading(true);
      try {
        const stored = authService.getCurrentUser();
        if (!stored) return;
        const e_id = stored.e_id;
        // Map frontend role to backend role string
        const roleMap: Record<string, string> = {
          admin: "Admin",
          manager: "Manager",
          developer: "Developer",
        };
        const backendRole = roleMap[currentRole] || "Developer";
        const emp = await employeeService.getEmployeeById(e_id, backendRole);
        setDetails({ ...stored, ...emp });
      } catch (err) {
        console.error("Failed to load profile", err);
      } finally {
        setLoading(false);
      }
    };
    load();
  }, [currentRole]);

  if (loading) return <div className="p-4">Loading...</div>;
  if (!details) return <div className="p-4">No profile data available</div>;

  return (
    <div className="p-6 max-w-3xl mx-auto">
      <h2 className="text-2xl font-semibold mb-4">Profile</h2>
      <Card className="overflow-hidden">
        <div className="bg-gradient-to-r from-indigo-500 via-fuchsia-500 to-amber-400 p-6 text-white">
          <div className="flex items-center gap-4">
            <div className="h-16 w-16 rounded-full bg-white/20 flex items-center justify-center text-xl font-semibold">
              {details.name
                .split(" ")
                .map((n: string) => n[0])
                .join("")}
            </div>
            <div>
              <div className="text-lg font-semibold">{details.name}</div>
              <div className="text-sm opacity-90">
                {details.designation || "-"}
              </div>
            </div>
          </div>
        </div>

        <div className="p-4">
          <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div>
              <p className="text-sm text-muted-foreground">Employee ID</p>
              <p className="font-medium">{details.e_id || details.id}</p>
            </div>
            <div>
              <p className="text-sm text-muted-foreground">Name</p>
              <p className="font-medium">{details.name}</p>
            </div>
            <div>
              <p className="text-sm text-muted-foreground">Email</p>
              <p className="font-medium">{details.email}</p>
            </div>
            <div>
              <p className="text-sm text-muted-foreground">Designation</p>
              <p className="font-medium">{details.designation || "-"}</p>
            </div>
            <div>
              <p className="text-sm text-muted-foreground">Manager ID</p>
              <p className="font-medium">{details.mgr_id || "-"}</p>
            </div>
            <div>
              <p className="text-sm text-muted-foreground">Roles</p>
              <p className="font-medium">
                {(details.roles || details.role || []).toString()}
              </p>
            </div>
            <div>
              <p className="text-sm text-muted-foreground">Status</p>
              <p className="font-medium">{details.status || "active"}</p>
            </div>
          </div>
        </div>
      </Card>
    </div>
  );
};

export default Profile;
