import React from "react";
import GreetingCard from "./GreetingCard";
import "./index.css";

export default function App() {
  return (
    <div style={{ padding: 24 }}>
      <h1 style={{ color: "white", marginBottom: 16 }}>Greeting Cards</h1>
      <div style={{ display: "flex", gap: 16, flexWrap: "wrap" }}>
        <GreetingCard name="Alice" greet="Hello Alice!" />
        <GreetingCard name="Bob" greet="Hi Bob!" />
        <GreetingCard name="Carol" greet="Welcome Carol!" />
        <GreetingCard name="Dave" greet="Good day Dave!" />
      </div>
    </div>
  );
}
