import React from 'react';

function Cart({ cartItems, removeFromCart, updateQuantity, totalPrice, discountApplied }) {
  return (
    <div>
      <h2>Shopping Cart</h2>
      {cartItems.length === 0 ? (
        <p>Your cart is empty!</p>
      ) : (
        <ul>
          {cartItems.map(item => (
            <li key={item.id}>
              <span>{item.name} - ₹{item.price} x {item.quantity}</span>
              <button onClick={() => removeFromCart(item.id)}>Remove</button>
              <input 
                type="number" 
                value={item.quantity} 
                min="1" 
                onChange={(e) => updateQuantity(item.id, parseInt(e.target.value))}
              />
            </li>
          ))}
        </ul>
      )}
      <h3>Total: ₹{totalPrice}</h3>
      {discountApplied && <p>Discount Applied: 10% off!</p>}
    </div>
  );
}

export default Cart;
