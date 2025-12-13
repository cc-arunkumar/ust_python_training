// function f1(a){
//     let a=25;
//     if (a>10) {
//         a++;
//         console.log(a);
//     }
//     else {
//         a--;
//         console.log(a);
//     }
// }
// var a=5
// f1(a)

// const a=10
// var b;
// console.log(a)
// console.log(b)

// const a=[1, 2, 3];
// console.log(a);
// a.push(4);
// console.log(a);
// a[2]=10
// console.log(a);
// a=[1,2]
// console.log(a);


// const person={
//     name:"Deva Prasath",
//     age:21}
// console.log(person.name)
// console.log(person.age)

// person.name="Raj"
// console.log(person.name)
// const person={
//     name:"Deva ",
//     age:18}
// console.log(person)



// Allows redeclaration
// var a=10;
// var a=20;
// console.log(a);


// Does not allow redeclaration
// let a=10;
// let a=20;
// console.log(a);


// Does not allow redeclaration
// const a=10;
// const a=20;
// console.log(a);

// var a
// console.log(a)
// var a=10



// const a
// console.log(a)
// const a=10

// const a=undefined
// console.log(a)

// for (let i=0;i<5;i++){
//     console.log(i);
// }


// for (var i=0;i<5;i++){
//     setTimeout(()=>{
//         console.log(i);
//     },1000);
// }


// const num=[1,2,3,4,5];
// console.log(num);

// const doubles=num.map((num)=>num*2);
// console.log(doubles);
// console.log(num);


// const users=["Deva","Raj","Kumar"];

// const modi=users.map((name,i)=>({id:i+1,name:name}));
// console.log(modi);


// const names=["Deva","Prasath","Raj"];
// const [fname,lname]=names;
// console.log(fname);
// console.log(lname);

// const users=[
//     names="Deva Prasath",
//     age=21,
//     gender="Male"
// ];
// const [names,age,gender]=users;
// console.log(names);
// console.log(age);
// console.log(gender);

// const arr1=[1,2,3];
// const arr2=[...arr1,4,5]
// console.log(arr2);


// const arr1=[1,2,3,90];
// const arr2=[4,5,6];
// const arr3=[...arr1,...arr2]
// console.log(arr3)

// [ 1, 2, 3, 4, 5, 6 ]


// const [first, second, ...rest] = [1, 2, 3, 4, 5];
// console.log(first);  
// console.log(second);  
// console.log(rest);  


// use bactick

// const names="Deva"
// const age=21
// const greet=`My name is ${names} and my age is ${age}`
// console.log(greet)

