function f1(){
    // if (a){
    //     const b=10
    //     b++
    // }
    // else{
    //     const b=10
    //     b--
    // }
    // console.log(b)
    // const nums = [1,2,3,4]
    // console.log(nums)
    // nums.push(5)
    // console.log(nums)
    // nums[2] = 33
    // console.log(nums)
    // nums = [1,2]
    // const person = {name:"akhil",age:22}
    // console.log(person.name,person.age)
    // person.age=23
    // console.log(person.name,person.age)
    // var a =12
    // console.log(a)
    // var a=13
    // console.log(a)
    // const a =1
    // console.log(a)
    // const a=13
    // console.log(a)
    // const a = undefined
    // console.log(a)
    // var a=10
    // const l =[1,2,3]
    // for(var i in l){
    //     setTimeout(()=>{
    //         console.log(i)
    //     },100)
    // }
    
    // const l =[1,2,3]
    // console.log(l)
    // const double = l.map((nums)=> nums*2)
    // console.log(double)
    // const users = ["akhil","fdh","hgchgc"]
    // const h = users.map((name,i)=>({id:i+1,name:name}))

    // console.log(h)

    // const name = ["first","middle","last"]
    // const [fname,mname] = name
    // console.log(fname,mname)
    // const user = {
    //     name : "akhil",
    //     age : 22,
    //     gender : "male"
    // }
    // const {name,age,gender} = user
    // console.log(name,age,gender)
    // const arr1 = [1,2,3]
    // const arr2 = [...arr1,4,5]
    // console.log(arr2)
    const arr1 = [0,1,2,3,4,5,6]
    // const arr2 = [4,5,6,7]
    // const arr3 = [...arr1,...arr2]
    // console.log(arr3)
    const [a,b,c,...arr2] = arr1
    console.log(a,b,c,arr2)
    const name="Akhil"
    const age=22
    const greating = `My name is ${name} and my age is ${age}`
    console.log(greating)
}
f1()