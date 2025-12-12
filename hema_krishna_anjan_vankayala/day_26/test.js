// let a = 10;
// function new_function() {
    
//     if (a>40){
//         let b = a+1;
//     }
//     else{
//         let b = a-1;
//     }
//     console.log(a,b)
// }
// console.log(a)
// new_function()

// const a=10;
// const b;
// b=10;

// const a=10;
// let b;
// const c = b;
// b=10;
// console.log(c)


// const nums = [1,2,3,4];
// console.log(nums);
// nums.push(6);
// console.log(nums);
// nums[2]=5;
// console.log(nums);
// const nums2 = [2,4,5];
// nums=nums2;
// console.log(nums)


// const person = {name: "ABC", age:25};
// console.log(person.name,person.age);


// var a =10;
// console.log(a);
// var a =20;
// console.log(a);

// let a =10;
// console.log(a);
// let a =20;
// console.log(a);

// const a =10;
// console.log(a);
// const a =20;
// console.log(a);

// let a; 
// console.log(a);
// a=10;

// console.log(a);
// var a = 10;
// console.log(a);


// console.log(a);
// let a = 10;

// const a = undefined;
// console.log(a);


// for(let i=0;i<3;i++){
//     console.log(i);
// }

// for(const i=0;i<3;i++){
//     console.log(i);
// }


// for (const i of [1,2,3,4]){
    // console.log(i);
// }

// for(var i=0;i<3;i++){
//     setTimeout(()=>{
//         console.log(i);
//     },100)
// }


// const a= [1,2,3,4,5,6];
// console.log(a);
// const doubled = a.map(x => x*2)
// console.log(doubled);

// const users = ['anjan','suresh','ramesh'];
// let i =0;
// const updated = users.map((user,i) => ({id: i+1, user:user}))
// console.log(updated)

// const name = ["first","second","third","fourth",'fifth']
// const [fName, sName,lName,...rest] = name
// console.log(fName,sName,lName,rest)

// const person = {
//     name:"anjan",
//     age:21,
//     gender: "male"
// }
// const {name,age,gender} = person
// console.log(name,age,gender)

// const arr1=[1,2,3,4,5]
// const arr2=[4,5,6,7]
// const arr3 = [...arr1,...arr2]
// console.log(arr3)
// for(const i of arr3){
//     console.log(i)
// }

// const arr= [0,1,2,3,4,5,6]
// const [a,b,c,...d] = arr 
// console.log(a,b,c,d)

// const arr= [0,1,2,3,4,5,6]
// const [...d,a,b,c] = arr 
// console.log(a,b,c,d)


// const name ="anjan"
// const age = 22

// const greet = `Hi My Name is ${name} and age is ${age}`
// console.log(greet)