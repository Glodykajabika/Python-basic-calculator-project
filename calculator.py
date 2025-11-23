### BASIC CALCULATOR

## We need to create a simple a calculator that allows to perform basic calculations (addition, multiplication, substraction, and division), for that we need to be able to get the user input (numbers, operator), and print the result of the calculation, we could also add (power, and square root) as operators to the calculator if we want and last let's run the calculator for as long as the user hasn't decided to quit.git 


while True:
    try:
        print("Operators: \n1. Add \n2. Multiply \n3. subtract \n4. Divide")
        operator = input("Operator (1, 2, ...): ")

        num1 = int(input("1st num: "))
        num2 = int(input("2nd num: "))
        op = ""
        result = 0

        if operator.strip() == "1":
            result = num1 + num2
            op = "+"
            
        elif operator.strip() == "2":
            result = num1 * num2
            op = "*"

        elif operator.strip() == "3":
            result = num1 - num2
            op = "-"
            
        elif operator.strip() == "4":
            try:
                result = num1 / num2
                op = "/"
            
            except ZeroDivisionError:
                print("Cannot divide by zero!!")
            
        else: 
            print("Operator not recognized!!")
            
        print("\nResult: {} {} {} = {}".format(num1, op, num2, result))
        quit = input("Contine? (y/n): ")
        
        if quit == "n":
            break 
        
    except ValueError:
        print("Invalid number!")