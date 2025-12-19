import React from "react";
import { ChartContainer, ChartTooltipContent } from "@/components/ui/chart";
import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  CartesianGrid,
  Cell,
  ResponsiveContainer,
} from "recharts";
import { taskService } from "@/services/taskService";
import { useAuth } from "@/context/AuthContext";

const STATUS_ORDER = ["to_do", "in_progress", "review", "done"];

const STATUS_LABELS: Record<string, string> = {
  to_do: "To Do",
  in_progress: "In Progress",
  review: "Review",
  done: "Done",
};

const STATUS_COLORS: Record<string, string> = {
  to_do: "#FF6B6B",
  in_progress: "#FFD93D",
  review: "#6BCB77",
  done: "#4D96FF",
};

const Analytics: React.FC = () => {
  const { currentRole } = useAuth();
  const [data, setData] = React.useState<
    { name: string; count: number; key: string }[]
  >([]);
  const [loading, setLoading] = React.useState(true);

  React.useEffect(() => {
    let mounted = true;

    const fetchStats = async () => {
      setLoading(true);
      try {
        const backendRoleMap: { [k: string]: string } = {
          admin: "Admin",
          manager: "Manager",
          developer: "Developer",
        };
        const backendRole = backendRoleMap[currentRole] || "Developer";
        const res = await taskService.getStats(backendRole);
        const map: Record<string, number> = {};
        (res || []).forEach((r: any) => (map[r.status] = r.count));

        const chartData = STATUS_ORDER.map((k) => ({
          key: k,
          name: STATUS_LABELS[k] || k,
          count: Number(map[k] || 0),
        }));
        if (mounted) setData(chartData);
      } catch (e) {
        console.error("Failed to load stats", e);
        if (mounted)
          setData(
            STATUS_ORDER.map((k) => ({
              key: k,
              name: STATUS_LABELS[k] || k,
              count: 0,
            }))
          );
      } finally {
        if (mounted) setLoading(false);
      }
    };

    fetchStats();
    return () => {
      mounted = false;
    };
  }, [currentRole]);

  return (
    <div className="p-6">
      <h2 className="text-2xl font-semibold mb-4">
        Analytics — Tasks by Status
      </h2>

      <div className="bg-card p-6 rounded-lg shadow-md">
        <div className="flex items-center justify-between mb-4">
          <h3 className="text-lg font-medium">Tasks by Status</h3>
          <div className="text-sm text-muted-foreground">
            Total:{" "}
            <span className="font-medium">
              {data.reduce((s, d) => s + d.count, 0)}
            </span>
          </div>
        </div>

        <div className="mb-4 flex gap-3">
          {data.map((d) => (
            <div key={d.key} className="flex items-center gap-2">
              <span
                className="inline-block w-3 h-3 rounded-full"
                style={{ background: STATUS_COLORS[d.key] }}
              />
              <div className="text-sm">
                <div className="font-medium">{d.count}</div>
                <div className="text-muted-foreground text-xs">{d.name}</div>
              </div>
            </div>
          ))}
        </div>

        <div className="w-full h-40 sm:h-56">
          <ChartContainer
            config={{
              todo: { color: STATUS_COLORS.to_do },
              in_progress: { color: STATUS_COLORS.in_progress },
              review: { color: STATUS_COLORS.review },
              done: { color: STATUS_COLORS.done },
            }}
          >
            <ResponsiveContainer width="100%" height="100%">
              <BarChart
                data={data}
                margin={{ top: 4, right: 8, left: 0, bottom: 0 }}
                barCategoryGap="24%"
                barSize={36}
              >
                <defs>
                  {data.map((d) => (
                    <linearGradient
                      id={`grad-${d.key}`}
                      key={d.key}
                      x1="0"
                      x2="0"
                      y1="0"
                      y2="1"
                    >
                      <stop
                        offset="0%"
                        stopColor={STATUS_COLORS[d.key]}
                        stopOpacity={0.95}
                      />
                      <stop
                        offset="100%"
                        stopColor={STATUS_COLORS[d.key]}
                        stopOpacity={0.6}
                      />
                    </linearGradient>
                  ))}
                </defs>
                <CartesianGrid strokeDasharray="3 3" strokeOpacity={0.5} />
                <XAxis dataKey="name" tick={{ fontSize: 12 }} interval={0} />
                <YAxis allowDecimals={false} width={36} />
                <Tooltip content={<ChartTooltipContent nameKey="key" />} />
                <Bar
                  dataKey="count"
                  radius={[8, 8, 8, 8]}
                  animationDuration={1000}
                  animationEasing="ease-out"
                >
                  {data.map((entry, idx) => (
                    <Cell
                      key={entry.key}
                      fill={`url(#grad-${entry.key})`}
                      style={{
                        filter: "drop-shadow(0 6px 12px rgba(0,0,0,0.08))",
                      }}
                    />
                  ))}
                </Bar>
              </BarChart>
            </ResponsiveContainer>
          </ChartContainer>
        </div>
      </div>
    </div>
  );
};

export default Analytics;
