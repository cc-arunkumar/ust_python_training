import React from "react";

// Cart component receives props for cartItems, removal and quantity change handlers, total price, discount flag, and dynamic discount style
const Cart = ({
  cartItems,
  onRemoveFromCart,
  onChangeQuantity,
  totalPrice,
  discountApplied,
  dynamicDiscountStyle,
}) => {
  return (
    <div className="cart">
      <h2>Your Cart</h2>
      {/* Display message if cart is empty */}
      {cartItems.length === 0 ? (
        <p>Your cart is empty</p>
      ) : (
        // Display list of items in the cart if it's not empty
        <div className="cart-items">
          {cartItems.map((item) => (
            <div key={item.id} className="cart-item">
              {/* Display item name and price */}
              <p>
                {item.name} - ₹{item.price}
              </p>
              {/* Input for changing the quantity of the item */}
              <input
                type="number"
                min="1" // Prevents entering values less than 1
                value={item.quantity}
                onChange={(e) =>
                  onChangeQuantity(item.id, parseInt(e.target.value))
                } // Calls onChangeQuantity with updated quantity
              />
              {/* Display total price for this item (price * quantity) */}
              <p>Total: ₹{item.price * item.quantity}</p>
              {/* Button to remove item from cart */}
              <button onClick={() => onRemoveFromCart(item.id)}>Remove</button>
            </div>
          ))}
        </div>
      )}
      {/* Display total price and final price with or without discount */}
      <div className="cart-total">
        <p>Total Price: ₹{totalPrice}</p>
        {/* Show discount message if discount is applied */}
        {discountApplied && (
          <p className="discount" style={dynamicDiscountStyle}>
            Discount Applied: 10% Off
          </p>
        )}
        {/* Final price after applying discount, if applicable */}
        <p>Final Price: ₹{discountApplied ? totalPrice * 0.9 : totalPrice}</p>
      </div>
    </div>
  );
};

export default Cart;
