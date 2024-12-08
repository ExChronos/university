'use strict'

function sum(a) {

    let currentSum = a;
  
    function f(b) {
      currentSum += b;
      return f;
    }
  
    f.toString = function() {
      return currentSum;
    };
  
    return f;
}

// let sum1 = sum(1)(2)(3)(4);

// console.log(sum1)

function createCounter(){
    let current = 0;
    let iter = 0;
    function f(){
        let next = current+1;
        return `${iter++}: current - ${current++}, next${next}`;
    }
    
    return f;
}

// let counter = createCounter();

// console.log(counter())
// console.log(counter())

function createUser(name){
    return {
        greet(){
            return `Hello, ${name}`
        }
    }
}

// let mark = createUser('Mark')

// console.log(mark.greet())

function memoize(fn){
    let cash = new Map();

    return function(x){
        if (cash.has(x)){
            return cash.get(x);
        }

        let result = fn(x);

        cash.set(result);
        return result;
    }
}

