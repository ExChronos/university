// #1 - if -> || ... ?
function checkAge(age) {
    return (age > 18 ? true : false)
}

function checkAge2(age){
    return(false || age>18)
}

// #2 - min

function min(a, b){
    return (a < b ? a : b)
}

// #3 - pow

function pow(x, n){
    let po = 1
    for(let i = 0; i < n; i++){
        po *= x
    }

    return po
}

// #4 - function -> () -> {}
let ask = (question, yes, no) => {
    if(confirm(question)) 
        yes()
    else 
        no()
}

ask(
    "Вы согласны?",
    () => {alert('Вы согласились')},
    () => {alert('Вы не согласились')},
)

