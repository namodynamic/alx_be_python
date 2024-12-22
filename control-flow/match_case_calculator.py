def calculator():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operations = input("Choose the operation (+, -, *, /): ")

    match operations:
        case "+":
            result = num1 + num2
        case "-":
            result = num1 - num2
        case "*":
            result = num1 * num2
        case "/":
            if num2 == 0:
                print("Cannot divide by zero.")
                return
            else:
                result = num1 / num2
        case _:
            print("Invalid operator")
            return

    print(f"The result is {result}")

calculator()
