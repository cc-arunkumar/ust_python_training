const { useState } = require("react");

function App()
{
    const[count,setcount]=useState(0)

    return(
        <>
        <h1>Hello World!</h1>
        <Hello/>
        </>
    )
}
export default App