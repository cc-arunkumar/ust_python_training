var a = 10
function demo() {
  if (a > 20) {
    var b = a+1;  
  } 
  else {
    var b = a-1;
     
  }
  console.log(a,b)
}

console.log(a)
demo()


const a = 10;
var b;
console.log(b)

const nums = [1,2,3,4];
console.log(nums)

nums.push(5)
console.log(nums)

nums[2] = 33
console.log(nums)

nums = [1,2]
console.log(nums)

const person = {name:"Sai Vamsi",age:22};
console.log(person.name)
console.log(person.age)

const person = {name:"Shakeel",age:23}; #this will not work as i have already declared reference person
console.log(person.name)
console.log(person.age)

var a = 10;
var a = 10;
console.log(a)

let a = 10;
let a = 20;   # This will not work as i have already declared 'a' using let.
console.log(a)



console.log(a)
const a = 20
var a = 20
let a = 20


const a = undefined
console.log(a)

for (let i = 0; i <= 5; i++) {
  console.log(i);
}

for (const i = 0; i <= 5; i++) {
  console.log(i);
}      # Error

for(const i in [1,2,3,4]){
    console.log(i)
}

for (let i = 0; i <= 5; i++) {
    setTimeout(() => {
        console.log(i);
    }, 100);
}

setTimeout ---> Call back function

for (var i = 0; i <= 5; i++) {
    setTimeout(() => {
        console.log(i);
    }, 100);
}

const nums = [1,2,3,4,5];
console.log(nums)

const doubles = nums.map((nums)=>nums*2)
// console.log(nums)
console.log(doubles)

const users = ["Sai Vamsi","Shakeel","Abhi"]
console.log(users)
const names = users.map((name,i)=>({id:i+1,name:name}))
console.log(names)

const name = ["Sai", "Vamsi", "Kodavati"];
const [firstname,middlename, lastname] = name;

console.log(firstname,middlename,lastname);     


const user = {
    name: "Sai Vamsi",
    age: 22,
    gender: "Male"
};

const { name, age, gender } = user;

console.log(name, age, gender);



const arr1 = [1,2,3]
const arr2 = [...arr1,4,5,6]
console.log(arr2)



const arr1 = [1,2,3,9]
const arr2 = [4,5,6,8]
const arr3  = [...arr1,...arr2]
console.log(JSON.stringify(arr3))


const arr = [0,1,2,3,4,5]
const[a,b,...c] = arr

console.log(a,b,c)

const arr = [0,1,2,3,4,5]
const[...a,b,c] = arr

console.log(a,b,c)

const name = "Sai Vamsi"
const age = 22

const greet = `My name is ${name} and My age is ${age}`;
console.log(greet);