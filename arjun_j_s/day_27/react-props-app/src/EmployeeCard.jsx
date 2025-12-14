// Card.jsx
import React from "react";

export default function EmployeeCard({ children,style }) {
  return (
    <div
        style={{
            padding: "16px",
            borderRadius: "12px",
            border: "1px solid #e5e7eb",
            margin:"10px",
            maxWidth: "400px",
            minWidth: "150px",
            maxHeight: "500px",
            boxShadow: "0 1px 3px rgba(0,0,0,0.08)",
            background: "linear-gradient(135deg, #fdfcfb 0%, #e2d1c3 100%)",
            transition: "transform 120ms ease, box-shadow 120ms ease",
            ...style,
        }}
    >
      {children}
    </div>
  );
}