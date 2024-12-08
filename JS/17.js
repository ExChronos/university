function printNums(from, to){
    let current = from;

    let timerID = setInterval(function(){
        console.log(current);

        if(current == to){
            clearInterval(timerID);
        };
        current++;
    }, 1000)
}

function printNumbers2(from, to) {
    let current = from;
  
    setTimeout(function go() {
      console.log(current);
      if (current < to) {
        setTimeout(go, 1000);
      }
      current++;
    }, 1000);
  }

// printNums(10, 20)
// printNumbers2(10, 20)

function delayGreeting(name, delay){
    setTimeout(() => console.log(`Hello, ${name}`), delay);
}

// delayGreeting('Mark', 1500)

function countdown(num){
    let current = num;
    let innercounter = setInterval(() => {
        console.log(current);

        if(current == 0){
            console.log('Время вышло!');
            clearInterval(innercounter);
        };
        
        current--;
    }, 1000)
}

// countdown(10)

function repeatAction(fn, interval){
    let current = interval;
    let countdown = setInterval(() => {
        fn();

        if(current == 5000){
            clearInterval(countdown);
        }
        current += 1000;
    }, interval)
}

function inner(){
    console.log('tick');
}

// repeatAction(inner, 1000)