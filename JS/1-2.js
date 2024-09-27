
// #1 - alert()
let al1 = () => {
    alert('Hello world')
}
// #2 - alert() из внешнего файла
// #3 - переменные
let vars = () => {
    let name, admin;
    name = 'Джон';
    admin = name
    alert(admin)
}

// #4 - simple page
let data = () => {
    let name = prompt('Ваше имя', 'Mark');
    alert(`Hello, ${name}`)
}

// #5 - access to data
let access = () => {
    let password = '12345';
    let userpass = prompt('Введите пароль');

    if(password == userpass)
        alert('Добро пожаловать, мой господин')
    else
        alert('Ты думал, что меня переиграешь...? У тебя нет доступа сюда')
}

access()