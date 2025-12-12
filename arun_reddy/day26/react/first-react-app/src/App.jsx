import { useState } from 'react';
import './App.css';
import Greet from './greet.jsx';

function App() {
  const [count, setCount] = useState(0);

  return (
    <div className="app-container">
      <h1 className="heading">HELLO REACT</h1>
      
      <div className="cards-container">
        <div className="left-group">
          <Greet bgColor="lightblue"  text="Hello Arun ,Welcome in "/>
          <Greet bgColor="lightblue" />
          <Greet bgColor="lightblue" />
        </div>
        <div className="right-group">
          <Greet bgColor="#fda4af" />
          <Greet bgColor="#fda4af" />
          <Greet bgColor="#fda4af" />
        </div>
      </div>
    </div>
  );
}

export default App;
