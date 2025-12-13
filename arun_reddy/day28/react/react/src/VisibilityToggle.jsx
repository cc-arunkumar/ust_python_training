import { useState } from "react";

export default function VisibilityToggle() {
  const [isVisible, setIsVisible] = useState(false);

  return (
    <div className="visibility-container">
      <div className="visibility-card">
        <h2 className="visibility-title">Profile Information</h2>

        <button
          onClick={() => setIsVisible(!isVisible)}
          className="visibility-btn"
        >
          {isVisible ? "Hide Details" : "Show Details"}
        </button>

        {isVisible && (
          <div className="visibility-details">
            <p>
              <strong>Name:</strong> John Doe
            </p>
            <p>
              <strong>Email:</strong> john.doe@example.com
            </p>
            <p>
              <strong>Location:</strong> New York, USA
            </p>
            <p>
              <strong>Member Since:</strong> January 2024
            </p>
          </div>
        )}
      </div>
    </div>
  );
}
