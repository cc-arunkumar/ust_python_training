// Card.jsx
import React from "react";

export default function Card({ children }) {
  return (
    <div
      style={{
        padding: "16px",
        borderRadius: "12px",
        border: "1px solid #e5e7eb",
        boxShadow: "0 1px 3px rgba(0,0,0,0.08)",
        background: "linear-gradient(135deg, #fdfcfb 0%, #e2d1c3 100%)",
        transition: "transform 120ms ease, box-shadow 120ms ease",
      }}
      onMouseEnter={(e) => {
        e.currentTarget.style.boxShadow = "0 6px 16px rgba(0,0,0,0.12)";
        e.currentTarget.style.transform = "translateY(-1px)";
      }}
      onMouseLeave={(e) => {
        e.currentTarget.style.boxShadow = "0 1px 3px rgba(0,0,0,0.08)";
        e.currentTarget.style.transform = "translateY(0)";
      }}
    >
      {children}
    </div>
  );
}