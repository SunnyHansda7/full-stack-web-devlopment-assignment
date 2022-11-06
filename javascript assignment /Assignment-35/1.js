const shoppingCart=['Milk','Coffee', 'Tea', 'Honey']
if(shoppingCart[0]=='Meat'){
    return;
}
else{
    shoppingCart[0]='Meat'
}
if(shoppingCart[shoppingCart.length-1]!='Sugar'){
    shoppingCart.push('Sugar')
    //console.log(shoppingCart)
    
}

  
shoppingCart.splice(3,1)
//console.log(shoppingCart)
shoppingCart.splice(2,1,'Green Tea')
console.log(shoppingCart)