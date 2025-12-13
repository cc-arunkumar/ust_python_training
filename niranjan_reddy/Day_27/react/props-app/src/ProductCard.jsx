import React from "react";

const ProductCard = ({ name,price,rating} = { ...props }) => {
  return (
    <div className="card">
      <h1>{name}</h1>
      <h2>Price= {price} 💸</h2>
      <h2>Rating = {rating} ⭐</h2>
    </div>
  );
};

export default ProductCard;
