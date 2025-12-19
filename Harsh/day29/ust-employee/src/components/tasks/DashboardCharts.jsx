import React from "react";
import { TASK_STATUSES } from "../../utils/constants";

// Simple, dependency-free charts using SVG
const COLORS = {
  LOW: "#60a5fa", // blue
  MEDIUM: "#f59e0b", // amber
  HIGH: "#ef4444", // red
  TODO: "#94a3b8",
  ON_PROCESS: "#fbbf24",
  REVIEW: "#7c3aed",
  DONE: "#16a34a",
};

const BarChart = ({ counts = {} }) => {
  const keys = ["HIGH", "MEDIUM", "LOW"];
  const values = keys.map((k) => counts[k] || 0);
  const max = Math.max(...values, 1);
  const chartHeight = 140; // px

  return (
    <div className="p-4 bg-white rounded-lg shadow-sm">
      <div className="text-sm font-medium text-slate-600 mb-3">
        Tasks by Priority
      </div>
      <div className="flex items-end gap-6" style={{ height: chartHeight }}>
        {keys.map((k) => {
          const v = counts[k] || 0;
          const heightPx = Math.max(
            8,
            Math.round((v / max) * (chartHeight - 40))
          );
          const color = COLORS[k] || "#cbd5e1";
          return (
            <div key={k} className="flex flex-col items-center text-sm w-16">
              <div
                className="w-full rounded-md shadow-sm"
                style={{
                  height: `${heightPx}px`,
                  background: `linear-gradient(180deg, ${color}33, ${color})`,
                  display: "flex",
                  alignItems: "flex-end",
                  justifyContent: "center",
                }}
                title={`${k}: ${v}`}
              >
                {/* small top cap to improve look */}
              </div>
              <div className="mt-2 font-semibold text-sm">{v}</div>
              <div className="text-xs text-slate-500 mt-1 uppercase">{k}</div>
            </div>
          );
        })}
      </div>
    </div>
  );
};

const DonutChart = ({ statusCounts = {} }) => {
  const statusKeys = Object.values(TASK_STATUSES);
  const total = statusKeys.reduce((s, k) => s + (statusCounts[k] || 0), 0);
  const size = 140;
  const stroke = 18;
  const radius = (size - stroke) / 2;
  const circumference = 2 * Math.PI * radius;
  let offset = 0; // cumulative dash length

  return (
    <div className="p-4 bg-white rounded-lg shadow-sm flex items-center gap-4">
      <div>
        <div className="text-sm font-medium text-slate-600 mb-3">
          Tasks by Status
        </div>
        <svg width={size} height={size} viewBox={`0 0 ${size} ${size}`}>
          <g transform={`translate(${size / 2}, ${size / 2})`}>
            {/* background ring */}
            <circle
              r={radius}
              cx={0}
              cy={0}
              fill="transparent"
              stroke="#eef2f7"
              strokeWidth={stroke}
            />
            {statusKeys.map((k) => {
              const v = statusCounts[k] || 0;
              const portion = total === 0 ? 0 : v / total;
              const dash = portion * circumference;
              const color = COLORS[k] || COLORS.TODO || "#cbd5e1";
              const dashArray = `${dash} ${circumference - dash}`;
              const dashOffset = circumference - offset;
              offset += dash;
              return (
                <circle
                  key={k}
                  r={radius}
                  cx={0}
                  cy={0}
                  fill="transparent"
                  stroke={color}
                  strokeWidth={stroke}
                  strokeDasharray={dashArray}
                  strokeDashoffset={dashOffset}
                  strokeLinecap="round"
                  style={{
                    transition:
                      "stroke-dasharray 300ms, stroke-dashoffset 300ms",
                  }}
                />
              );
            })}
            {/* center label */}
            <text
              x="0"
              y="4"
              textAnchor="middle"
              className="text-sm font-semibold"
              style={{ fontSize: 14 }}
            >
              {total}
            </text>
          </g>
        </svg>
      </div>

      <div className="flex-1">
        <div className="space-y-2">
          {statusKeys.map((k) => {
            const v = statusCounts[k] || 0;
            const pct = total === 0 ? 0 : Math.round((v / total) * 100);
            return (
              <div key={k} className="flex items-center justify-between">
                <div className="flex items-center gap-3">
                  <span
                    className="w-3 h-3 rounded-full"
                    style={{ background: COLORS[k] || "#cbd5e1" }}
                  />
                  <div className="text-sm text-slate-700">{k}</div>
                </div>
                <div className="text-sm font-medium text-slate-800">
                  {v} <span className="text-xs text-slate-500">({pct}%)</span>
                </div>
              </div>
            );
          })}
        </div>
      </div>
    </div>
  );
};

const DashboardCharts = ({ priorityCounts = {}, statusCounts = {} }) => {
  return (
    <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
      <div className="md:col-span-2">
        <BarChart counts={priorityCounts} />
      </div>
      <div className="md:col-span-1">
        <DonutChart statusCounts={statusCounts} />
      </div>
    </div>
  );
};

export default DashboardCharts;
