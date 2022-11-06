const ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
let n=10
let max = ages[0]
for (let i=0;i < ages.length;i++) {
    if(ages[i] >max){
        max=ages[i]
    }
}
console.log('Max number is:',max)
let min = ages[0]
for (let i=0;i < ages.length;i++) {
    if(ages[i] <min){
        min=ages[i]
    }
}
console.log('Min number is:',min)
//if  n is even median is
if(n%2==0){
    let median
    median=((n/2)+((n/2)+1))/2
    console.log('if  n is even median is',median)
}
//if n is odd median is
if(n%2!=0){
    let median
    median=((n/2)+1)/2
    console.log('if n is odd median is',median)
}
function average(ages,n){
  let sum=0
  for (const iter of ages) {
    sum = sum+iter
    
    
  }
  let ave=sum/n
  return ave
}
console.log(average(ages,10))
range=max-min
console.log(range)