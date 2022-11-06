const arr = ['banana', 'orange', 'mango', 'lemon']
function capitalizeArray(arr){
    let upper=[]
for(let i=0;i<arr.length;i++)
{
     upper[i] = arr[i].toUpperCase()
     
}

return upper
}
let up=[]
up = capitalizeArray(arr)
console.log(up)