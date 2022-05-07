




def god():
    calculator = input("\n\n1 for Standard Mathematical Operations Calculator\n2 for Percentage Increase/Decrease Calculator.\n\n\n " )

    def OperCalc():

        print("Welcome to Will's Standard Mathematical Operations Calculator.\n Here are the instructions:\n   Step 1: type in your first number (number1)\n    Step 2: type in your operator (*, /, +, -)\n     Step 3: type in your second number (number2)\nThe result will be (number1) (operator) (number2)\n basically like a normal calculator.\n\n\n")




        number1 = float(input('num1= ' ))
        operator = input('oper= ' )
        number2 = float(input('num2= ' ))



        def multiply():
            answer = number1 * number2
            print(number1, "*", number2, "=", answer)

        def divide():
           answer = number1 / number2
           print(number1, "/", number2, "=", answer)

        def add():
            answer = number1 + number2
            print(number1, '+', number2, '+', answer)

        def subtract():
            answer = number1 - number2
            print(number1, '-', number2, '=', answer)

        if operator == '*':
            multiply()
        elif operator == '/':
            divide()
        elif operator == '+':
            add()
        elif operator == '-':
            subtract()
        
    

    def percentage():
    
        print("Welcome to Will's Percentage Increase/Decrease Calculator.\n here are the instructions:\n  enter the number to be increased/decreased (num)\n   enter the percentage to increase or decrease num (percent) make percent a negative (-percent) for decrease\n\nHow it works:\n takes inputted num and multiplies it by (1+percent/100) to get the answer to the increase/decrease.\n\n")

        num = float(input("#= " ))
        percent = float(input("%= " ))
        print('\n\n')
        answer = (num * (1+percent/100))
    
        print("How solution was reached:", num, '*', '1+', percent, '/100\n\n', num, 'increased/decreased by', percent, '% =', answer,)


    if calculator == "1":
        OperCalc()
    elif calculator == "2":
        percentage()

god()
def loop():
    global god
    gloop = input("Start calculator again? y/n ")
    if gloop == 'y':
        god()
    if gloop == 'y':
        loop()
loop()

