// // var c, d;

// function f1(a, b) {

//   if (a === 1) {
//     c = a + b;
//     return c;
//   } else {
//     d = b + a;
//     return d;
//   }
// }

// console.log(f1(1, 5)); 
// console.log(f1(2, 5)); 
// var a=10
// var b
// b=10

// console.log(a)
// console.log(b)

// const nums=[1,2,3,4]
// console.log(nums)
// nums.push(5)
// console.log(nums)
// nums[2]=33
// console.log(nums)
// nums=[1,2]
// console.log(nums)

// const person={name:"Sovan",age:"22"}
// console.log(person.name)
// console.log(person.age)
// person.name="Raj"
// person.age="24"
// console.log(person.name)
// console.log(person.age)
// var a=10
// console.log(a)
// var a=20
// console.log(a)
// let a=10
// console.log(a)
// let a=20
// console.log(a)
// console.log(a)
// const a=10
// const a=undefined
// console.log(a)

// for(const i=0;i<=10;i++)
// {
//   console.log(i)
// }

// for(var i=0;i<=3;i++)
// {
//   setTimeout(()=>{console.log(i)},100)
// }

// const d=[1,2,3,4,5]
// console.log(d)
// const double=d.map(n=>n*2)
// console.log(double)
// const u = ["Rahul", "Sovan", "Sohan"];

// const mu = u.map((name, i) => ({ id: i + 1, name }));

// console.log(mu);

// const n=["Sovan","Mohanty"]
// const[fname,lname]=n
// console.log(fname)
// console.log(lname)
// const user={
//   n:"Sovan",
//   age:22,
//   gender:"m"
// }
// const{n,age,gender}=user
// console.log(user)

// const arr1=[1,2,3]
// const arr2=[...arr1,4,5]
// console.log(arr1)
// console.log(arr2)
// const arr1=[1,2,3,4]
// const arr2=[4,5,6]
// const arr3=[...arr1,...arr2]
// console.log(arr3)
// console.log(JSON.stringify(arr3)); 
// const arr=[0,1,2,3,4,5,6]
// const [a,b,c,...arr1]=arr
// console.log(arr1,a,b,c)
const n="Sovan"
const age=22
const greet=`My name is ${n} and my age is ${age}` //template literals
console.log(greet)