import React from 'react';

const GroceryList = ({ groceryItems, onAddToCart }) => {
  return (
    <div>
      <h2>Available Groceries</h2>
      <ul>
        {groceryItems.map(item => (
          <li key={item.id}>
            {item.name} - ₹{item.price}
            <button onClick={() => onAddToCart(item)}>Add to Cart</button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default GroceryList;
