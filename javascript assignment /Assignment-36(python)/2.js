let sumeven=0
for(let i=0;i<=100;i++){
    if(i%2==0)
    sumeven=sumeven+i
}
console.log(sumeven)
let sumodd=0
for(let i=0;i<=100;i++){
    if(i%2!=0)
    sumodd=sumodd+i
}
console.log(sumodd)
let arr=[]
arr.push(sumeven,sumodd)
console.log(arr)
