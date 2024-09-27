// #1 - совершеннолетний студент
let Student = () => {
    let age = +prompt('Ваш возраст', 18);
    let isStudent = confirm('Вы студент?')

    if(isStudent && age>=18)
        console.log(true);
}

// #2 - член клуба 21+
let twentyOnePlus = () => {
    let membership = confirm('Вы являетесь членом клуба?')
    let age = +prompt('Сколько вам лет?', 21)

    if(membership || age>=21)
        alert('Можете проходить')

}

// #3 - условие, взять зонт
function umbrella() {
    let isRainy = confirm('На улице идет дождь?')
    let temperature = prompt('Сколько на улице градусов?', 10)

    if(isRainy && temperature<=10)
        alert('Следует взять дождь')
}

// #4 - проверка диапазона
function range() {
    let age = prompt('Сколько тебе лет?', 14)

    if(14<=age<=90)
        alert('Ты в диапазоне от 14 до 90')
}

// #5 - еще одна проверка диапазона
function range2() {
    let age = prompt('Сколько тебе лет?', 18)

    if(!(14<=age<=90))
        alert('Ты вне диапазона от 14 до 90')
    if(age <= 14 && age >= 90)
        alert('Ты вне диапазона от 14 до 90')
}

// #6 - проверка логина
function loggin() {
    let login = prompt('Введите свой логин', 'login')

    if(login == 'Админ'){
        let password = prompt('Введите пароль')

        if(password == false || password == null)
            alert('Отменено')
        else if(password == 'Я главный')
            alert('Здравствуйте!')
        else
            alert('Я вас не знаю')
    }
}

