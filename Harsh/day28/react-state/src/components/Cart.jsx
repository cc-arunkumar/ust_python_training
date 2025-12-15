import React from "react";

const Cart = ({
  cartItems,
  removeFromCart,
  updateQuantity,
  totalPrice,
  discountApplied,
  finalPrice,
  successMessage,
}) => {
  return (
    <div className="cart">
      {successMessage && <p className="success">{successMessage}</p>}

      <h2>Your Cart</h2>
      {cartItems.length === 0 ? (
        <p>No items in cart</p>
      ) : (
        <ul>
          {cartItems.map((item) => (
            <li key={item.id}>
              {item.name} - ₹{item.price} ×
              <input
                type="number"
                min="1"
                value={item.quantity}
                onChange={(e) => updateQuantity(item.id, e.target.value)}
              />
              = ₹{item.price * item.quantity}
              <button onClick={() => removeFromCart(item.id)}>Remove</button>
            </li>
          ))}
        </ul>
      )}

      <h3>Total: ₹{totalPrice}</h3>
      {discountApplied && (
        <p className="discount">
          10% Discount Applied! Final Price: ₹{finalPrice}
        </p>
      )}
    </div>
  );
};

export default Cart;
