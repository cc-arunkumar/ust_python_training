
// function add(a){
//     var temp=a;
//     if (a<10){
//         let res=a;
        
//     }
//     console.log(res);
// }
// add(9)


function test(){
    var x=4
    if (true)
    {
        const a=10
        var b

        console.log(b)
    }
    console.log(a,b)
}
const nums=[1,2,3,4]
console.log(nums)
nums.push(5)
console.log(nums)
nums[2]=33
console.log(nums)
// nums=[1,2]
// console.log(nums)


const person={
    name:"Arun",
    age:67

}
// person={
//     name:"Aryan",
//     age:90
// }
console.log(person)
console.log(person.name)
console.log(person.age)
// var a=10
// console.log(a)
// var a=20
// console.log(a)
// let a=10
// console.log(a)
// let a=20
// console.log(a)
// const a=10
// console.log(a)
// const a=20
// console.log(a)
// in the memory location the initialisation is not done so it is undefined 
// this is known as the  variable hoisting,it willbe in temporal dead zone(TDZ) 
// let a;
// console.log(a)
// a=10;

// console.log(a)
// var a=10;

let a =undefined;
console.log(a)
// for(let i=0;i<5;i++)
// {
//     console.log(i)
// }
//callback function 
// for(var i of [1,2,3])
// {
//     setTimeout(()=>
//         console.log(i),100)
// }
const nums1=[1,2,3,4,5]
console.log(nums1)
const nums2=nums1.map((item)=>item*2);
console.log(nums1)
console.log(nums2)
const users=["Arun","Arjun","Felix","Aryan"];
const res = users.map((nae, i) => ({ id: i + 1, name:nae}));
console.log(res)



//destrcuting teh arrays 
// const names=["Arun","Reddy","Hi"]
// const [firstname,lastname]=names
// console.log(firstname)
// console.log(lastname)

// const employee={
//     names:"Arun",
//     age:90,
//     gender:"Male"
// }
// const {names,age,gender}=employee
// console.log(names,age,gender)

// const nums3=[1,2,3]
// const arr2=[...nums3,4,5]
// console.log(arr2)
// const arr1=[1,2,3,9]
// const arr2=[...arr1,4,5,6,]
// const res1=[...arr2]
// console.log(res1)

// const nums4=[1,2,3,4,5]
// const [...arr3,d,b]=nums4  Rest element must be last element
// console.log(d,b,arr3)


const name="Arun"
const age=24
const greet= `My name is ${name} and my age is ${age}`
console.log(greet)


