// #1 - не рабочий вариант
let round = () => {
    let number = prompt('Введите рациональное число', 41.2215)
    let alnum = Math.round(number)
    alert(alnum)
}

// #2 - рабочий вариант
let fround = () => {
    let number = +prompt('Введите рациональное число', 41.2215)
    let alnum = number.toFixed(2)
    alert(alnum)
}

// #3 - NaN
let nan = () => {
    let number = prompt('Введите число')
    if(isNaN(number))
        alert(false)
    else
        alert(true)
}

// #4 - преобразование с ед изм
let translate = () => {
    let number = prompt('Введите число и ед измерения', '12.1em');
    
    alert(parseFloat(number))
}

// #5 - первая буква заглавная
let up = () => {
    let msg = 'hello';
    let new_msg = msg[0].toUpperCase()+msg.slice(1)

    alert(new_msg)
}

// #6 - удаление пробелов
let del = () => {
    let msg = 'Hello World without spaces'.split(' ').join('')
    let another_msg = '  Hello World without start/end spaces   '.trim()

    alert(msg)
    alert(another_msg)
}

// #7 - поиск подстроки
let find = () => {
    let msg = 'Hello finding working World'

    alert(msg.search('мир'))

}

// #8 - вывод подстроки
let show = () => {
    let msg = 'Hello this beautiful world with so many flowers...';

    alert(msg.slice(2, 6))
}

// #9 - замена 1го символа
let change = () => {
    let msg = 'Hi. This is your personal helper';

    let new_msg = msg.replace(msg[0], 'G')
    alert(new_msg)
}
