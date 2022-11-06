let arr= [3,4,5,56,6,7,6]
function sumOfArrayItems(arr){
    let sum=0
for(let i=0;i<arr.length;i++){
    
    sum=sum+arr[i]
}

return sum

}
let sum = sumOfArrayItems(arr)
console.log(sum)