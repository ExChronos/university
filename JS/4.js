// #1 - не работающий скрипт
let fix = () => {
    let a = +prompt('Введите число', 1);
    let b = +prompt('Введите число', 2);

    alert(a+b)
}

// #2 - сравниение строки и числа
let comp = () => {
    let num = 5;
    let str = '5';

    alert(str == num)   // true
    alert(num === str)  // false
}

// #3 - сравнение булевых значений
let comp2 = () => {
    alert(1 == true)
    alert(1 === true)
    alert(null == undefined)
    alert(null === undefined)
}

// №4 - сравнение строк с пробелами
let comp3 = () => {
    alert(' hello ' == 'hello')
    alert(' hello ' === 'hello')
}


// #5 - сравнение чисел
let comp4 = () => {
    alert(10==10.0)
    alert(10===10.0)
}

// #6 - четность числа
let odd = () => {
    let num = +prompt('Введите число', 10)

    if(num%2==0)
        alert('Четное')
    else
        alert('Нечетное')
}

// №7 - сравнение 2х чисел
let comp5 = () => {
    let num1 = +prompt('Введите число 1', 10)
    let num2 = +prompt('Введите число 2', 12)

    let bigger = (num1 > num2) ? num1 : num2
    alert(bigger)
}

// №8 - расчет скидки
let count = () => {
    let sum = +prompt('Введите сумму', 500)

    switch(true){
        case (sum > 500 && sum < 1000):
            alert(`Ваша скидка 5% и сумма = ${sum*95/100}`)
            break;
        case (sum > 1000):
            alert(`Ваша скидка 10% и сумма = ${sum*90/100}`)
            break;
        default:
            alert(`Ваша сумма без скидки = ${sum}`)
            break;
    }
}

// #9 - вывод if else
let question = () => {
    let answer = prompt('Какое официальное название JS?')

    if(answer=="ECMAScript")
        alert('Верно!')
    else
        alert('Не знаете? ECMAScript!')
}