class Stack:
    items=[]

    def push(self, value):
        self.items.append(value)
    
    def pop(self):
        return self.items.pop()
    
    def isEmpty(self):
        return len(self.items) == 0
    


stack = Stack()
expression = '3 2 + 4 5 + *'
lexems = expression.split(' ')
for lexem in lexems:

    if lexem == '+':
        a = stack.pop()
        b = stack.pop()
        stack.push(a + b)

    elif lexem == '-':
        a = stack.pop()
        b = stack.pop()
        stack.push(a - b)

    elif lexem == '*':
        a = stack.pop()
        b = stack.pop()
        stack.push(a * b)

    elif lexem == '':
        a = stack.pop()
        b = stack.pop()
        stack.push(a / b)

    else:
        stack.push(float(lexem))

print(stack.pop())