import React from 'react';

const Cart = ({ cartItems, onRemoveFromCart, onChangeQuantity, totalPrice, discountApplied }) => {
  return (
    <div>
      <h2>Shopping Cart</h2>
      {cartItems.length === 0 ? (
        <p>Your cart is empty.</p>
      ) : (
        <ul>
          {cartItems.map(item => (
            <li key={item.id}>
              {item.name} - ₹{item.price} x {item.quantity}
              <button onClick={() => onRemoveFromCart(item.id)}>Remove</button>
              <input
                type="number"
                value={item.quantity}
                onChange={(e) => onChangeQuantity(item.id, parseInt(e.target.value))}
                min="1"
              />
            </li>
          ))}
        </ul>
      )}
      <h3>Total: ₹{totalPrice}</h3>
      {discountApplied && <p>Discount applied: 10%</p>}
    </div>
  );
};

export default Cart;
