// import { use } from "react"

function run(){
    if (true){
        var a = 5
        var b =6
        var sum = a+b
    }
    console.log(sum)
}

function constLearning(){
    // const a = 10
    // // const b; 
    // // b=10
    // let b
    // const val=b 

    // const nums = [1,2,3,4,5]
    // console.log(nums)
    // nums[4] = 6
    // console.log(nums)
    // const person = {name:"Rohit",age:20}
    // console.log(person.name)
    // console.log(person.age)
    // person.name = "Harsh"
    // console.log(person.name)
    // console.log(person.age)
    // var a = 10
    // console.log(a)
    // var a = 20
    // console.log(a)
    // let a = 10
    // console.log(a)
    // let a = 20
    // console.log(a)
    // const a = 10
    // console.log(a)
    // const a = 20
    // console.log(a)

    // console.log(a)
    // var a  =10
    // const val = undefined
    // console.log(val)
}
const hello = (a)=>{
    console.log(a)
}
// hello(6)

constLearning()
// // run()
// const nums = [1,2,3,4,5]
// for (let index = 0; index < nums.length; index++) {
//     const element = nums[index];
//     console.log(element)
    
// }

// for(const i of [1,2,3,4,8]){
//     console.log(i)
// }
// setTimeout(()=>{
//     console.log("Running")
// },1000)



// const nums = [1,2,3,4,5]
// console.log(nums)
// ans = nums.map((x)=> x**2)
// console.log(ans)


const users= ["ROhit","Harsh", "Rohan"]
// console.log(users)
// let val =  users.map( user =>user.toUpperCase())

// console.log(val)


// const val = users.map((name,i)=> ({id:i+1,name:name}))
// console.log(typeof(val))

// const user = {name:"Rohit", age:22,gander:"male"}

// const {name ,age} = user
// console.log(name ,age)


// const val = [1,3,4,6]
// const val2 = [8,6]
// const nums = [...val,7,8,9]
// console.log(JSON.stringify(nums)); 


// const arr = [0,1,2,3,4,5,6,7,9]
// const[a,b,c,...val] = arr
// console.log(a,b,c,val)


const name = "Rohit"
const age = 22
const greet = `My name is ${name} and my age is ${age}`
console.log(greet)