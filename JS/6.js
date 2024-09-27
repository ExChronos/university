// #1 - четные числа
let forOdd = () => {
    for(let i = 0; i <= 10; i += 2)
        alert(i)
}

// #2 - цикл больше 100
function cycle() {
    let num = prompt('Введите число больше 100', 101);

    while(num <= 100){
        num = prompt('Еще раз, введите число больше 100, либо Esc для выхода')
        if(num == null)
            break;
    }
}

// #3 - простые числа
function simple(){
    let n = +prompt('Введите число')
    let primares = []

    let simples = []

    for(let i = 2; i <= n; i++){
        simples[i] = true
    }
    for(let i = 2; i <= n; i++){
        if(simples[i] == true){
            for(let j = i**2; j <= n; j+=i){
                simples[j] = false
            }
        }
    }

    let k = 0;

    for(let i = 0; i <= n; i++){
        if(simples[i] == true){
            primares[k]=i
            k++;
        }
        else
            continue
    }

    alert(primares)
}

// #4 - if -> switch
function ifSwitch() {
    const num = +prompt('Введите число между 0 и 3')

    switch (num) {
        case 0:
            alert('Вы ввели число 0')
            break;
        case 1:
            alert('Вы ввели число 1')
            break;
        case 2:
            alert('Вы ввели число 2')
            break;
        
        default:
            alert('Число не из диапазона, либо ничего не ввели')
            break;
    }
}
