import React from 'react'

const ProductCard = ({name, price,rating}) => {
  return (
    <div className="product-card">
        <h4>{name}</h4>
        <p>Cost:{price}</p>
        <p>Rating:{rating}</p>
      
    </div>
  );
};

export default ProductCard
