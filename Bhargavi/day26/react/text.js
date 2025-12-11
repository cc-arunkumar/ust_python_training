// const nums = [1,2,3,4]
// console.log(nums);

// nums.push(18);
// console.log(nums);

// nums[2]=33;
// console.log(nums);

// nums = [10, 20, 30];
// console.log(nums);

// const person = { "name": "Bhargavi", "age": 34 };
// console.log(person);

// const person = { "name": "meena", "age": 51 };
// console.log(person);

// var a = 10;
// console.log(a);
// var a = 20;
// console.log(a);

// function add(a, b) {
//     let sum;
//     if (a > b) {
//         sum = a + b;
//     } else {
//         var diff = a - b;
//         console.log(diff);
//     }
//     console.log(sum);
// }

// add(10, 5);
// add(3, 8);

// hoisting = taking out without defining default value is undefining
// var a;
// console.log(a);
// a = 10;

// console.log(a);
// let a = 10;

// function varExample() {
//     if (true) {
//         var x = 10;  // var is function-scoped
//     }
//     console.log(x);  // Outputs: 10, accessible outside the if block
// }

// varExample();

// function letExample() {
//     if (true) {
//         let y = 20;  // let is block-scoped
//     }
//     console.log(y);  // Error: y is not defined, not accessible outside the block
// }

// letExample();

// function constExample() {
//     const z = 30;
//     z = 40;  // Error: Assignment to constant variable
//     console.log(z);  // This will not be executed due to the error
// }

// constExample();

// const a = undefined;
// console.log(a);


// console.log(a);  // undefined
// var a = 10;

// for (let i = 0; i < 5; i++) {
//     console.log(i);  
// }


// for (const i = 0; i < 5; i++) {
//     console.log(i);  
// }

// for(const i in [1,2,3]){ i point to object
//     console.log(i)
// }

// console.log(a);  // undefined
// var a = 10;

// console.log(b);  // ReferenceError


// for (let i = 0; i < 3; i++) {
//     setTimeout(() => {
//         console.log(i); // Logs 0, 1, 2 after a delay
//     },10);  
// }

// for (const i = 0; i < 3; i++) {
//     setTimeout(() => {
//         console.log(i); // Logs 0, 1, 2 after a delay
//     });  // Delays each iteration 
// }



// arrow function = shorter the expression
// const a = [1, 2, 3, 4];
// console.log(a);  

// const double = a.map((num) => num * 2);
// console.log(double);  



// const users = ["bhargavi", "Meena", "Veeena"];
// const result = users.map((name, i) => ({ name:name , index: i + 1 }));
// console.log(result);

// const name = ["bhargavi", "Meena", "Harhsa"];
// const [fname, lname] = name;
// console.log(fname); 
// console.log(lname); 


// const user = {
//     name: "Bhargavi",
//     age: 25,
//     gender: "female"
// };

// const {name, age, gender} = user;
// console.log(user);

// const arr1=[1,2,3,4,5];
// console.log(arr1);
// const arr2=[arr1,7,8];
// console.log(arr2);

// spread
// const arr1=[1,2,3,9];
// const arr2=[4,5,6];
// const arr3 = [...arr1, ...arr2];
// console.log(arr3);


// const arr1 = [1, 2, 3, 4, 5];
// const [a, b,  ...arr] = arr1;
// console.log(a);
// console.log(b);

// const arr1 = [1, 2, 3, 4, 5];
// const [a, b, ...rest] = arr1;
// console.log(rest); 

// const name = "bhargavi";
// const age = 22;
// const greet = ` ${name} and  ${age} years old.`;
// console.log(greet);  

