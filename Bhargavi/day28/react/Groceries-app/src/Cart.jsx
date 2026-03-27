import React, { useEffect } from "react";
import "./App.css";

function Cart({
  cartItems,
  removeFromCart,
  updateQuantity,
  totalPrice,
  discountApplied,
  calculateTotalPrice,
}) {
  useEffect(() => {
    calculateTotalPrice();
  }, [cartItems, calculateTotalPrice]);

  return (
    <div className="cart">
      <h2>Shopping Cart</h2>
      {cartItems.length === 0 ? (
        <p>Your cart is empty.</p>
      ) : (
        <div>
          <div className="cart-items">
            {cartItems.map((item) => (
              <div key={item.id} className="cart-item">
                <h3>{item.name}</h3>
                <p>₹{item.price}</p>
                <div>
                  <button
                    onClick={() => updateQuantity(item.id, item.quantity - 1)}
                  >
                    -
                  </button>
                  <input
                    type="number"
                    value={item.quantity}
                    onChange={(e) =>
                      updateQuantity(item.id, Number(e.target.value))
                    }
                  />
                  <button
                    onClick={() => updateQuantity(item.id, item.quantity + 1)}
                  >
                    +
                  </button>
                </div>
                <p>Total: ₹{item.price * item.quantity}</p>
                <button onClick={() => removeFromCart(item.id)}>Remove</button>
              </div>
            ))}
          </div>
          <div className="cart-total">
            <p>Total: ₹{totalPrice}</p>
            {discountApplied && <p>Discount Applied: 10% Off</p>}
          </div>
        </div>
      )}
    </div>
  );
}

export default Cart;
