if(4>3 && 10<12){
console.log(true,"a")           //a

}
if(4>3 && 10>12){
    console.log(true,"b")           //b
}
if(4>3 || 10<12){
    console.log(true,"c")           //c
}
if(4>3 || 10>12){
    console.log(true,'d')          //d
}
if(!(4>3)){
    console.log(true,"e")       //e
}
if(!(4<3)){
    console.log(true,"f")       //f
}
else if(!(false)){
    console.log(true,"g")       //g
}
if(!(4>3 && 10<12)){
    console.log(true,"h")           //h
}
if(!(4>3 && 10>12)){
    console.log(true,"i")           //i
}
if(!(4 === '4')){
    console.log(true,"j")           //j
}

