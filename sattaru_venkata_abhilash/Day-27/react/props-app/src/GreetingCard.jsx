import React from "react";

const GreetingCard = ({ name = "Guest", greet = "Welcome!" }) => {
  return (
    <div className="product-card GreetingCard"> {/* Same styling as ProductCard; add GreetingCard for gradients */}
      <h2>{name}</h2> {/* Display name */}
      <h4>{greet}</h4> {/* Display greeting */}
    </div>
  );
};

export default GreetingCard;
