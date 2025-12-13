import React from "react";

function Cart({
  cartItems,
  removeFromCart,
  updateQuantity,
  totalPrice,
  discountApplied,
  successMessage,
}) {
  return (
    <div>
      <h2>Your Cart</h2>
      {successMessage && <p>{successMessage}</p>}
      {cartItems.length === 0 ? (
        <p>Your cart is empty.</p>
      ) : (
        <ul>
          {cartItems.map((item) => (
            <li key={item.id}>
              {item.name} - ₹{item.price} x{" "}
              <input
                type="number"
                value={item.quantity}
                onChange={(e) =>
                  updateQuantity(item.id, parseInt(e.target.value))
                }
                min="1"
              />{" "}
              = ₹{item.price * item.quantity}{" "}
              <button onClick={() => removeFromCart(item.id)}>Remove</button>
            </li>
          ))}
        </ul>
      )}
      <h3>Total Price: ₹{totalPrice}</h3>
      {discountApplied && <h4>Discount Applied: 10%</h4>}
      {discountApplied && (
        <h4>Final Price After Discount: ₹{totalPrice * 0.9}</h4>
      )}
    </div>
  );
}

export default Cart;
