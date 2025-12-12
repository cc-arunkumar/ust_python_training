// App.jsx
import { useState } from 'react';
import Hello from './hello'; // Import the Hello component
import './App.css';

function App() {
  const [count, setCount] = useState(0);

  return (
    <>
      <header>
        <h1>Welcome to the Ultimate Fun Zone! 🎉</h1>
        <p>Ready to unlock some awesome vibes and non-stop fun? Let’s go!</p>
      </header>
      <Hello /> 
      <Hello /> 
      <Hello /> 
      <Hello />
      <Hello />
      <Hello />
      <Hello />
      <Hello />
    </>
  );
}

export default App;
