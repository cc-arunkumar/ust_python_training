import React from "react";
import { useState } from "react";
import "./index.css";

export default function ProductCard({ bgColor, product, price, rating }) {
  const [isHovered, setIsHovered] = useState(false);
  return (
    <div
      className={`card ${isHovered ? "card-hover" : ""}`}
      style={{ background: bgColor }}
      onMouseEnter={() => setIsHovered(true)}
      onMouseLeave={() => setIsHovered(false)}
    >
      <h1>{product}</h1>
      <h3>Price={price}💰</h3>
      <h3>Rating={rating}⭐</h3>
    </div>
  );
}
