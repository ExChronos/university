
function isEmpty(obj) {
    return !(Object.keys(obj).length > 0);
}

let schedule = {}
schedule['8:30']='get up'

// console.log(isEmpty(schedule))

function salarySum(obj){
    let sum = 0;

    if(Object.keys(obj).length == 0){
        return sum;
    } else{
        for(let i of Object.values(obj)){
            sum += i;
        }
        return sum;
    }
}

let salaries = {
    John: 100,
    Ann: 160,
    Pete: 130
}

let sum = salarySum(salaries)
// console.log(sum)

function round(obj){
    for(let key of Object.values(obj)){
        console.log(key)
    }
}

function multiplyNumber(obj){
    for(let key of Object.keys(obj)){
        if(Number(obj[key]))
            Object.defineProperty(obj, key, {
            value: obj[key]*2
        })
        
    }
}

let meny = {
    width: 200,
    height: 400,
    title: 'My menu'
}

// round(meny)
// multiplyNumber(meny)
// round(meny)

let Calculator = {
    read(a, b){
        this.a=a
        this.b=b
    },
    sum(){
        return this.a+this.b;
    },
    mul(){
        return this.a*this.b;
    }
}

let calc = Calculator