import React from 'react';
import { ShoppingBag, Plus } from 'lucide-react';

const GroceryList = ({ items, onAddToCart }) => {
  return (
    <div className="grocery-list-container">
      <h2 className="section-title">
        <ShoppingBag className="icon-green" />
        Available Groceries
      </h2>
      <div className="grocery-grid">
        {items.map(item => (
          <div key={item.id} className="grocery-item">
            <h3 className="item-name">{item.name}</h3>
            <p className="item-unit">per {item.unit}</p>
            <div className="item-footer">
              <span className="item-price">₹{item.price}</span>
              <button
                onClick={() => onAddToCart(item)}
                className="add-button"
              >
                <Plus size={16} />
                Add
              </button>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default GroceryList;