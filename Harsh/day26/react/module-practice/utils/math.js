function add(a,b){
    return a+b
}

function sub(a,b){
    return a-b
}

function mul(a,b){
    return a*b
}

function div(a,b){
    if(b==0){
        throw new Error("cannot be zer0")
    }
    return a/b
}

export{add,sub,mul,div}