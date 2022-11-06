function random_id(){
    let random_string=''
    let character='0123456789abcdef'
    for(let i=0;i<character.length;i++){
        random_string += character.charAt(Math.floor(Math.random() *character.length))
    }
    console.log(random_string)
}

random_id()