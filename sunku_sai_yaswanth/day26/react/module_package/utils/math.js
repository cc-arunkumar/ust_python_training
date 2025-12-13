export function subtract(a,b){
    return a-b
}
export function multiply(a,b){
    return a*b

}
export function divide(a,b){
    if (b===0){
        throw new Error("Connot divide by zero")

    }
    return a/b;
}