let arr= [3,4,5,56,6,7,6]
function modifyArray(arr){
    let arr2=[]
    if(arr.length<5){
    console.log('item not found')
    }
    arr[5]=43
for(let i=0;i<arr.length;i++){
    
    arr2.push(arr[i])
}

return arr2

}
let sum=[] 
sum = modifyArray(arr)
console.log(sum)