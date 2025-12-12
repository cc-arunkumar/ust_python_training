// var a =10;
// function new_func(){
    
//     if(a>20){
//     var b= a+1;
//     }
//     else{
//         var b=a-1;

//     }
//     console.log(a,b)
// }
// console.log(a)
// new_func
   


// const a=10;
// const b;
// console.log(b)



// const a=10;
// var b;
// console.log(b)



// const nums=[1,2,3,4,5]
// console.log(nums)

// nums.push(6)
// console.log(nums)

// nums[2]=33
// console.log(nums)

// nums=[1,2]
// console.log(nums)


// const person={name:"Shakeel",age:22}
// console.log(person.name)
// console.log(person.age)

// const person={name:"Sai",age:22}
// console.log(person.name)
// console.log(person.age)



// var a=10;
// console.log(a)
// var a=20;
// console.log(a)

// let a=10;
// console.log(a)
// let a=20;
// console.log(a)

//  const a=10;
// console.log(a)
// const a=20;
// console.log(a)



// var a;
// console.log(a)
// a=10

// let a;
// console.log(a)
// a=10

// console.log(a)
// let a=10

// console.log(a)
// var a=10

// console.log(a)
// const a=10

// const a="undefined";
// console.log(a)


// for (let i = 0; i < 5; i++) {
//   console.log(i);
// }

// for (const i = 0; i < 5; i++) {

//   console.log(i);
// }


// for(const i in[1,2,3]){
//     console.log(i)
// }


// for (let i = 0; i < 5; i++) {
//   setTimeout(() => {
//     console.log(i);
//   }, 100);
// }

// const nums=[1,2,3,4,5]
// console.log("Original",nums)
// const doubles=nums.map((num)=>num*2)
// console.log(nums)
// console.log(doubles)


// const users=["shakeel","abhi","sai"]
// console.log(users)
// const names= users.map((name,i)=>({id:i+1,name:name}));
// console.log(names)


// const name =["shaik","Mohammed","Shakeel"];
// const [fname,mname,lname]=name;
// console.log(fname)
// console.log(mname)
// console.log(lname)


// const user={name:"shakeel",age:22,gender:"male"};
// const{name,age,gender}=user;
// console.log(name)
// console.log(age)

// const arr1=[1,2,3]
// const arr2=[...arr1,4,5]
// console.log(arr2)

// const arr1=[1,2,3,9]
// const arr2=[4,5,6,7]
// const arr3=[...arr1,...arr2]
// console.log(JSON.stringify(arr3))

// const arr1=[1,2,3,4,5]
// const [a,b,...c]=arr1
// console.log(a)
// console.log(b)
// console.log(c)

// const arr1=[1,2,3,4,5]
// const [...a,b,c]=arr1
// console.log(a)
// console.log(b)
// console.log(c)

const name="shakeel";
const age=22;
const greet=`${name} and my age is ${age}`;

console.log(greet)