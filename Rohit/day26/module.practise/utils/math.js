// Named exports
export const add = (a, b) => a + b;
export const subtract = (a, b) => a - b;

// Default export
export default function multiply(a, b) {
    
  return a * b;
}
export  function divide(a, b) {
    if (b==0){
        throw new Error("cannot divided by 0")
    }

  return a / b;
}
