import { useState } from 'react'
import './App.css'
import Hello from './Hello'
import GreetingCard from './GreetingCard';
function App() {

    const handledelete = () => alert("Deleted");
    const handlecancel = () => alert("cancelled");
    return(
      <>
      <GreetingCard>
        <h2>
          Times of India
        </h2>
        <p>ISRO successfully launches new SSLV rocket today</p>
      </GreetingCard>
    

      <GreetingCard>
        <h2>
          Sport News
        </h2>
        <p>CSK becomes king of ipl</p>
      </GreetingCard>

      </>
    )
    



  
};

export default App;