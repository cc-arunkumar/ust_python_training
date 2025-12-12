import { error } from "console";

export function add(a,b){
    return a+b;
}
export function sub(a,b){
    return a-b;
}
export function multiply(a,b){
    return a*b;
}
export function division(a,b){
    if (b==0){
        throw new Error("Cannot divide by zero");
    }
    else{
        return a/b;
    }
}