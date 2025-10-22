from new import Stack

expression = Stack()

while True:
    user_input = input('> ')
    if user_input == 'exit':
        running = False
        break

    if user_input in ['+','-','*','/']:
        if expression.size() > 1:
            a = expression.pop()
            b = expression.pop()
            if user_input == '+':
                expression.push(a+b)
                c = expression.pop()
                print(c)
                expression.push(c)
            elif user_input == '-':
                expression.push(b-a)
                c = expression.pop()
                print(c)
                expression.push(c)
            elif user_input == '/':
                expression.push(b/a)
                c = expression.pop()
                print(c)
                expression.push(c)
            elif user_input == '*':
                expression.push(b * a)
                c = expression.pop()
                print(c)
                expression.push(c)
        else:
            print("You need 2 numbers before calculating")
    else:
        expression.push(int(user_input))



