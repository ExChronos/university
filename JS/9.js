'use strict'

function one(){
    let styles = ['Джаз', 'Блюз']

    console.log(styles);
    

    styles.push('Рок-н-ролл')

    console.log(styles);

    styles.splice(+(styles.length/2), 1, 'Классика')

    console.log(styles);
    
    let first = styles.shift()

    console.log(first, styles);
    
    styles.unshift('Рэп', 'Регги')

    console.log(styles);
}

function sumInput(){
    let sum = 0;
    let vals = [];

    while(userinput = prompt('Введите число', '')){
        if(userinput == '' || isNaN(userinput))
            break
        else
            vals.push(+userinput)
    }

    vals.forEach((val) => {
        sum+=val
    })

    alert(sum)
}


function camelize(str){
    let newstr = ''
    
    for(let i = 0; i < str.length; i++){
        if(str[i] == '-'){
            newstr += str[i+1].toUpperCase();
            i++;
            continue;
        }
        newstr += str[i]
    }

    console.log(newstr)
}

function filterRange(arr, a, b){
    let retval = []
    arr.forEach((value) => {
        if(value >= a && value <= b)
            retval.push(value)
    })
    return retval
}

function filterRangeReplace(arr, a, b){
    arr.forEach((value) => {
        if(value <= a || value >= b){
            let pos = arr.indexOf(value)
            arr.splice(pos, 1)
        }
    })
}

let arr = [3,1,6,3,2,6,7,5,2,4]
filterRangeReplace(arr, 3, 6)
console.log(arr)