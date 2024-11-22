function one(massive){
    if(massive.length <= 1){
        return massive;
    } else{
        let pivot = massive[0];
        let less = massive.filter(item => item < pivot)
        let greater = massive.filter(item => item > pivot)
        let same = massive.filter(item => item == pivot)

        return `${one(less)},${same},${one(greater)}`.split(',').join(' ').trim()
    }
}

let arr = [5,2,8,1,-10,5,3,0,4]
let newarr = one(arr)

function copySorted(massive){
    if(massive.length <= 1){
        return massive;
    } else{
        let pivot = massive[0];
        let less = massive.filter(item => item < pivot)
        let greater = massive.filter(item => item > pivot)
        let same = massive.filter(item => item == pivot)

        return `${one(greater)},${same},${one(less)}`.split(',').join(' ').trim()
    }
}

class Calculator{
    methods = {}
    calculate(str){
        let data = str.split(' ');
        let action = data[1];
        
        this.methods['+'] = (a, b) => {return a+b}
        this.methods['-'] = (a, b) => {return a-b}
        
        return this.methods[action](+data[0], +data[2])
    }

    addMethod(name, func){
        this.methods[name] = func
    }
}

let calc = new Calculator;

console.log(calc.calculate('3 + 1'))

calc.addMethod('**', (a, b) => a**b)

console.log(calc.calculate('2 ** 3'))

function sortByAge(users){
    let ages = [];

    for(let key of users){
        ages.push(key['age'])
    }

    ages = one(ages)

    return ages;
}

let user = [
    {
        name: 'Vasya',
        age: 21
    },
    {
        name: 'Petya',
        age: 32
    },
    {
        name: 'Kolya',
        age: 43
    }
]

console.log(sortByAge(user))