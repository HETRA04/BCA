def calculator():

    number1 = input("Choose your first number")
    number2 = input("Choose your second number")
    Action = input("Choose a function: X , / , + , -")


    number1 = int(number1)
    number2 = int(number2)



    if Action == "X":
        ans = number1 * number2
    elif Action == "/":
        ans = number1 / number2
    elif Action == "+":
        ans =  number1 + number2
    elif Action == "-":
        ans =  number1 - number2
    print(ans)
    
calculator()
