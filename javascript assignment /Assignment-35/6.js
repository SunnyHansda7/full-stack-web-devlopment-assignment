function random_id(){
    let random_string=''
    let character='abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for(let i=0;i<character.length;i++){
        random_string += character.charAt(Math.floor(Math.random() *character.length))
    }
    console.log(random_string)
}

random_id()