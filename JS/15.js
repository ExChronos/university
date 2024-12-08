function outer(){
    let x = 0;

    function inner(){
        return x;
    }
}

// console.log(outer())

function createCounter(){
    let count = 0;

    return countPlus = () => {
        return count++;
    }
}

let counter = createCounter();

// console.log(counter())
// console.log(counter())
// console.log(counter())

function outerFunction(){
    let msg = 'oldString';

    let innerFunction = () => {
        msg = 'newString';
        console.log(msg);
    }
    innerFunction();
    console.log(msg);
}

// outerFunction()

function lastFunction(){
    let global_local = 34;

    function lastInner(){
        let global_local = 43;
        console.log(global_local)
    }
    lastInner()
    console.log(global_local)
}

lastFunction()