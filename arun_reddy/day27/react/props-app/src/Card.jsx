import React from "react";
import { useState } from "react";
import "./index.css";

export default function Card({ bgColor,children }) {
  const [isHovered, setIsHovered] = useState(false);
  return (
    <div
      className={`card ${isHovered ? "card-hover" : ""}`}
      style={{ background: bgColor }}
      onMouseEnter={() => setIsHovered(true)}
      onMouseLeave={() => setIsHovered(false)}
    >
      {children}
    </div>
  );
}
