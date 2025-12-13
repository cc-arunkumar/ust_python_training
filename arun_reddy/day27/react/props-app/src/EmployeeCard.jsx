import React from "react";
import { useState } from "react";
import "./index.css";

export default function EmployeeCard({
  bgColor,
  img_url,
  name,
  employee_id,
  role,
  location,
}) {
  const [isHovered, setIsHovered] = useState(false);
  return (
    <div
      className={`employee-card ${isHovered ? "employee-card-hover" : ""}`}
      style={{ background: bgColor }}
      onMouseEnter={() => setIsHovered(true)}
      onMouseLeave={() => setIsHovered(false)}
    >
      <div className="employee-header">
        <img src={img_url} alt="Felix pic" className="employee-image" />
        <h2 className="employee-name">{name}</h2>
      </div>

      <div className="employee-details">
        <div className="detail-item">
          <span className="detail-icon">🎫</span>
          <span className="detail-text">ID: {employee_id}</span>
        </div>
        <div className="detail-item">
          <span className="detail-icon">⚡</span>
          <span className="detail-text">{role}</span>
        </div>
        <div className="detail-item">
          <span className="detail-icon">🌍</span>
          <span className="detail-text">{location}</span>
        </div>
      </div>
    </div>
  );
}
