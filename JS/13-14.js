function divide(a, b){
    let divByZero = new Error("You can't divide by zero");

    if(b == 0){
        throw divByZero.message;
    } else{
        console.log(a/b)
    }
}

function checkNum(prob){
    let notNumber = new Error('It is not a number');
    if(isNaN(Number(prob))){
        throw notNumber;
    } else{
        console.log(prob)
    }
}

function checkAge(age){
    let notInZone = new Error("Age not in range 0-100");

    if(age > 100 || age < 0){
        throw notInZone;
    } else{
        console.log(age)
    }
}

function checkString(str){
    let emptyString = new Error("This string is empty");

    if(str.length == 0){
        throw emptyString;
    } else{
        console.log(str)
    }
}

function findElement(arr, elem){
    let notInArr = new Error("Element not in array");
    let isElem = false;

    for(let el of arr){
        if(el == elem){
            isElem = true;
            break;
        }
    }

    if(!isElem)
        throw notInArr;
    else{
        console.log('All done');
    }

}

function stringToNumber(str){
    let notNumber = new Error("It's not a number");

    if(isNaN(Number(str))){
        throw notNumber;
    } else{
        console.log('All right')
    }
}

