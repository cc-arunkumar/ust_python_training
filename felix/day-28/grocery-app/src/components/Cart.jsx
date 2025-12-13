import React from 'react';
import { ShoppingCart, Plus, Minus, Trash2, Tag } from 'lucide-react';

const Cart = ({ cartItems, onUpdateQuantity, onRemoveItem, totalPrice, discount }) => {
  if (cartItems.length === 0) {
    return (
      <div className="cart-container">
        <h2 className="section-title">
          <ShoppingCart className="icon-orange" />
          Your Cart
        </h2>
        <div className="empty-cart">
          <ShoppingCart size={48} className="empty-cart-icon" />
          <p>Your cart is empty</p>
        </div>
      </div>
    );
  }

  const subtotal = totalPrice;
  const discountAmount = discount ? subtotal * 0.1 : 0;
  const finalTotal = subtotal - discountAmount;

  return (
    <div className="cart-container">
      <h2 className="section-title">
        <ShoppingCart className="icon-orange" />
        Your Cart ({cartItems.length} items)
      </h2>
      
      <div className="cart-items">
        {cartItems.map(item => (
          <div key={item.id} className="cart-item">
            <div className="cart-item-info">
              <h3 className="cart-item-name">{item.name}</h3>
              <p className="cart-item-price">₹{item.price} per {item.unit}</p>
            </div>
            
            <div className="cart-item-actions">
              <div className="quantity-controls">
                <button
                  onClick={() => onUpdateQuantity(item.id, item.quantity - 1)}
                  className="quantity-btn"
                  disabled={item.quantity <= 1}
                >
                  <Minus size={16} />
                </button>
                <span className="quantity-display">{item.quantity}</span>
                <button
                  onClick={() => onUpdateQuantity(item.id, item.quantity + 1)}
                  className="quantity-btn"
                >
                  <Plus size={16} />
                </button>
              </div>
              
              <span className="item-total">
                ₹{item.price * item.quantity}
              </span>
              
              <button
                onClick={() => onRemoveItem(item.id)}
                className="remove-btn"
              >
                <Trash2 size={20} />
              </button>
            </div>
          </div>
        ))}
      </div>
      
      <div className="cart-summary">
        <div className="summary-row">
          <span>Subtotal:</span>
          <span className="summary-value">₹{subtotal}</span>
        </div>
        
        {discount && (
          <div className="summary-row discount-row">
            <span className="discount-label">
              <Tag size={18} />
              Discount (10%):
            </span>
            <span className="discount-value">-₹{discountAmount.toFixed(2)}</span>
          </div>
        )}
        
        <div className="summary-total">
          <span>Total:</span>
          <span className="total-value">₹{finalTotal.toFixed(2)}</span>
        </div>
        
        {discount && (
          <div className="discount-message success">
            <p>🎉 You saved ₹{discountAmount.toFixed(2)} on this order!</p>
          </div>
        )}
        
        {!discount && subtotal > 800 && (
          <div className="discount-message info">
            <p>Add ₹{(1000 - subtotal).toFixed(2)} more to get 10% discount!</p>
          </div>
        )}
      </div>
    </div>
  );
};

export default Cart;