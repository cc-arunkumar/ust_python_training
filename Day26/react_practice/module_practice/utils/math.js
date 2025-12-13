export function add(a,b){
    return a+b;
}
export function sub(a,b){
    return a-b;
}
export function mul(a,b){
    return a*b;
}
export function div(a,b){
    if (b===0){
        throw new Error("denominator must greater than zero")
    }
    return a/b;
}
