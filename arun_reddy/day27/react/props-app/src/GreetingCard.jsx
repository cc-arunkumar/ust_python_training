import React from "react";
import { useState } from "react";
import "./index.css";

export default function GreetingCard({ bgColor, name, text }) {
  const [isHovered, setIsHovered] = useState(false);

  return (
    <div
      className={`card ${isHovered ? "card-hover" : ""}`}
      style={{ background: bgColor }}
      onMouseEnter={() => setIsHovered(true)}
      onMouseLeave={() => setIsHovered(false)}
    >
      <h1>{name}</h1>
      <h2>{text}</h2>
    </div>
  );
}
