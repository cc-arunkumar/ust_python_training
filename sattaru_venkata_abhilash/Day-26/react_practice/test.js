// var a = 10;
// var i = 5;

// function var_function() {
//     if (a > 40) {  
//         var b = a + i;
//     } else {
//         var b = a - i;
//     }
//     console.log(a, b);
// }

// var_function();

// let a = 10;
// // let i = 5;

// function var_function() {
//     let b;
//     if (a > 20) {  
//         b = a + 1;
//     } else {
//         b = a - 1;
//     }
//     console.log(a, b);
// }

// var_function();


// const a=10;
// let b;

// console.log(b)



// const a=10;
// var b;
// console.log(b)



// const nums=[1,2,3,4]
// console.log(nums); 

// nums.push(5)
// console.log(nums); 

// nums[2]=33
// console.log(nums); 

// nums=[1,2]
// console.log(nums); 


// const person={Name:"Abhi", age:22}
// console.log(person.Name)
// console.log(person.age)


// const person={Name:"sai", age:22}
// console.log(person.Name)
// console.log(person.age)


// var a=10;
// console.log(a)
// var a=20;
// console.log(a)


// let a=10;
// console.log(a)
// let a=20;
// console.log(a)


// const a=10;
// console.log(a)
// const a=20;
// console.log(a)


// let a
// console.log(a)
// a=10



// console.log(a)
// let a=10


// console.log(a)
// var a=10


// console.log(a)
// const a=10




// for (let i = 0; i < 5; i++) {
//     console.log(i);
// }

// for (const i = 0; i < 5; i++) {
//     console.log(i);
// }



// for (const i in [1,2,3,4,5]) {
//     console.log(i);
// }



// for (let i = 0; i < 3; i++) {
//     setTimeout(() => {
//         console.log(i);
//     }, 100 ); 
// }


// for (var i = 0; i < 3; i++) {
//     setTimeout(() => {
//         console.log(i);
//     }, 100 ); 
// }


// const numbers = [1, 2, 3, 4, 5];
// console.log(numbers)

// const doubled=numbers.map(x => x * 2);
// console.log(doubled);

// const users = ["Abhi", "Shakeel", "Sai"];
// const names =users.map((name, i) => ({ id: i + 1, name:name }));

// console.log(names);

// const users = ["Sattaru", "Venkata", "Abhilash"];
// const [firstUser, secondUser, thirdUser] = users;

// console.log(firstUser); 
// console.log(secondUser); 
// console.log(thirdUser);     



// const user = { name: "Abhi", age: 22, gender: "Male" };
// const { name, age, gender } = user;

// console.log(name);    
// console.log(age);    
// console.log(gender); 


// const arr1=[1,2]
// const arr2=[arr1, 3,4]

// console.log(arr2)


// const arr1=[1,2,3]
// const arr2=[4,5,6]

// const arr3 =[...arr1,...arr2]
// console.log(arr3)

// const arr1=[1,2,3,4,5]
// const [a,b,...c]=arr1
// console.log(a,b,c)
// // console.log(b)
// // console.log(c)


const name = "Abhi";
const age = 22;
const greet = `Hi my name is ${name} and my age is ${age}`;
console.log(greet);
