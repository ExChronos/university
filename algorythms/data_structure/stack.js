class Stack {
    items=[];

    push(value){
        this.items.push(value)
    };

    pop(){
        return this.items.pop()
    };

    isEmpty(){
        return this.items.length == 0
    };
}

let stack = new Stack();

const expression = '3 2 + 4 5 + *';
const lexems = expression.split(' ');

for(let lexem of lexems){
    let a,b;

    switch(lexem){
        case '+':
            b = stack.pop();
            a = stack.pop();
            stack.push(a+b);
            break;
        case '-':
            b = stack.pop();
            a = stack.pop();
            stack.push(a-b);
            break;
        case '*':
            b = stack.pop();
            a = stack.pop();
            stack.push(a*b);
            break;
        case '/':
            b = stack.pop();
            a = stack.pop();
            stack.push(a/b);
            break;
        default:
            stack.push(parseFloat(lexem));
    }
}

console.log(stack.pop());
