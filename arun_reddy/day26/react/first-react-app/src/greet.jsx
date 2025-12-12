import React, { useState } from 'react';
import './index.css';

export default function Greet({ bgColor = "lightblue",text }) {
  const [isHovered, setIsHovered] = useState(false);

  return (
    <div 
      className={`card ${isHovered ? 'card-hover' : ''}`}
      style={{ background: bgColor }}
      onMouseEnter={() => setIsHovered(true)}
      onMouseLeave={() => setIsHovered(false)}
    >
      <p>{text}</p>
      <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ipsam, quod ipsum blanditiis reprehenderit, a maxime asperiores veritatis debitis omnis veniam obcaecati illo, architecto vero perspiciatis recusandae? Molestias ut eos quas!</p>
    </div>
  );
}