import React from "react";
import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  CartesianGrid,
  Cell,
} from "recharts";

import { ChartContainer, ChartTooltipContent } from "@/components/ui/chart";
import type { Task } from "@/types";

type Props = {
  tasks: Task[];
};

const STATUS_KEYS = ["todo", "inprogress", "review", "done"] as const;

const LABELS: Record<(typeof STATUS_KEYS)[number], string> = {
  todo: "To Do",
  inprogress: "In Progress",
  review: "Review",
  done: "Done",
};

const COLORS: Record<(typeof STATUS_KEYS)[number], string> = {
  todo: "#2563eb", // blue
  inprogress: "#f59e0b", // amber
  review: "#ef4444", // red
  done: "#10b981", // green
};

export const AnalyticsBar: React.FC<Props> = ({ tasks }) => {
  const counts = React.useMemo(() => {
    const c: Record<string, number> = {
      todo: 0,
      inprogress: 0,
      review: 0,
      done: 0,
    };
    for (const t of tasks || []) {
      const s = t.status || "todo";
      if (s in c) c[s] = (c[s] || 0) + 1;
    }
    return c as Record<(typeof STATUS_KEYS)[number], number>;
  }, [tasks]);

  const data = STATUS_KEYS.map((k) => ({
    key: k,
    name: LABELS[k],
    count: counts[k] || 0,
  }));

  const config = Object.fromEntries(
    STATUS_KEYS.map((k) => [k, { label: LABELS[k], color: COLORS[k] }])
  );

  return (
    <div className="w-full">
      <h2 className="text-lg font-semibold mb-2">Tasks by Status</h2>
      <ChartContainer config={config} className="w-full h-64">
        <BarChart
          data={data}
          margin={{ top: 10, right: 16, left: 8, bottom: 6 }}
        >
          <CartesianGrid strokeDasharray="3 3" strokeOpacity={0.5} />
          <XAxis dataKey="name" tick={{ fontSize: 12 }} />
          <YAxis allowDecimals={false} />
          <Tooltip content={<ChartTooltipContent nameKey="key" />} />
          <Bar dataKey="count" radius={[6, 6, 6, 6]}>
            {data.map((entry) => (
              <Cell
                key={entry.key}
                fill={COLORS[entry.key as (typeof STATUS_KEYS)[number]]}
              />
            ))}
          </Bar>
        </BarChart>
      </ChartContainer>
    </div>
  );
};

export default AnalyticsBar;
