import React from "react";

const Cart = ({ cartItems, removeFromCart, updateQuantity }) => {
  const totalPrice = cartItems.reduce(
    (acc, item) => acc + item.price * item.quantity,
    0
  );

  const discountApplied = totalPrice > 1000;
  const finalPrice = discountApplied ? totalPrice * 0.9 : totalPrice;

  return (
    <div>
      <h2>🛒 Cart</h2>
      {cartItems.length === 0 ? (
        <p>No items in cart</p>
      ) : (
        <ul>
          {cartItems.map((item) => (
            <li key={item.id}>
              {item.name} - ₹{item.price} ×{" "}
              <input
                type="number"
                value={item.quantity}
                min="1"
                onChange={(e) => updateQuantity(item.id, e.target.value)}
              />{" "}
              = ₹{item.price * item.quantity}
              <button onClick={() => removeFromCart(item.id)}>Remove</button>
            </li>
          ))}
        </ul>
      )}

      <h3>Total: ₹{totalPrice}</h3>
      {discountApplied && (
        <p style={{ color: "blue" }}>
          Discount Applied (10%) → Final Price: ₹{finalPrice}
        </p>
      )}
    </div>
  );
};

export default Cart;
