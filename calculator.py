while True:
    print("Choose an operation:")
    print("1 for Addition")
    print("2 for Subtraction")
    print("3 for Multiplication")
    print("4 for Division")
    print("q to Quit")

    operation = input("Choose an operation: ").strip()

    if operation.lower() == "q":
        print("Goodbye!")
        break

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid number input. Please try again.")
        continue

    if operation == "1":
        result = num1 + num2
        print("The answer is: " + str(result))
    elif operation == "2":
        result = num1 - num2
        print("The answer is: " + str(result))
    elif operation == "3":
        result = num1 * num2
        print("The answer is: " + str(result))
    elif operation == "4":
        if num2 == 0:
            print("Cannot divide by zero")
        else:
            result = num1 / num2
            print("The answer is: " + str(result))
    else:
        print("Invalid input")