import React from "react";
import "./App.css";

const Cart = ({
  cartItems,
  removeFromCart,
  updateQuantity,
  totalPrice,
  discountApplied,
}) => {
  return (
    <div className="cart-container">
      <h2>Your Cart</h2>

      {cartItems.length === 0 ? (
        <p>No items in cart.</p>
      ) : (
        cartItems.map((item) => (
          <div
            key={item.id}
            className={`cart-item ${item.quantity >= 5 ? "bulk" : ""}`}
          >
            <span>
              {item.name} - ₹{item.price}
            </span>

            <input
              type="number"
              min="1"
              value={item.quantity}
              onChange={(e) => updateQuantity(item.id, e.target.value)}
              className="quantity-input"
            />

            <span>₹{item.price * item.quantity}</span>

            <button
              className={`remove-btn ${
                item.quantity >= 5 ? "danger" : ""
              }`}
              onClick={() => removeFromCart(item.id)}
            >
              Remove
            </button>
          </div>
        ))
      )}

      {discountApplied && (
        <p className="discount-text">10% discount applied!</p>
      )}

      <h3 className={`total-price ${discountApplied ? "discount" : ""}`}>
        Total Price: ₹{totalPrice}
      </h3>
    </div>
  );
};

export default Cart;
