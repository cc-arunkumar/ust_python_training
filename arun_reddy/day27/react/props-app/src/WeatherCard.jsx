import React from "react";
import { useState } from "react";
import "./index.css";

export default function WeatherCard({ bgColor, city, temperature }) {
  const [isHovered, setIsHovered] = useState(false);
  return (
    <div
      className={`card ${isHovered ? "card-hover" : ""}`}
      style={{ background: bgColor }}
      onMouseEnter={() => setIsHovered(true)}
      onMouseLeave={() => setIsHovered(false)}
    >
      <p>
        CITY={city} temperature={temperature}°C
      </p>
    </div>
  );
}
