import math
import sympy as sym

def scientific_calculator():
    while True:
        print("\nScientific Calculator")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Power")
        print("6. Square Root")
        print("7.Inverse")
        print("8. Sine")
        print("9. Cosine")
        print("10. Tangent")
        print("11. Log (base 10)")
        print("12. Natural Log (ln)")
        print("13. Factorial")
        print("14. Differentiation")
        print("15. Integration")
        print("16. Exit")

        choice = input("\nEnter your choice (1-15): ")
        

        try:
            if choice == "1":
                a = int(input("Enter first number: "))
                b = int(input("Enter second number: "))
                Add = a + b
                print(f"That's a arithmatic function\nThe Result = {Add}")

            elif choice == "2":
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
                Sub = a - b
                print(f"That's a arithmatic function\nThe Result = {Sub}")

            elif choice == "3":
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
                Multiply = a * b
                print(f"That's a arithmatic function\nThe Result = {Multiply}")

            elif choice == "4":
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
                if b == 0:
                    print("Error: Cannot divide by zero.")
                else:
                    Divide = a / b
                print(f"That's a arithmatic function\nThe Result = {Divide}")

            elif choice == "5":
                a = float(input("Enter base: "))
                b = float(input("Enter exponent: "))
                Power = a ** b
                print(f"That's a exponential function\nThe Result = {Power}")

            elif choice == "6":
                a = float(input("Enter a number: "))
                x = math.sqrt(a) 
                print(f"That's a exponential function\nThe Result = {x}")

            elif choice == "7":
                a = float(input("Enter a number: "))
                Inverse = 1/a 
                print(f"That's a inverse function\nThe Result = {Inverse}")

            elif choice == "8":
                angle = float(input("Enter angle in degrees: "))
                radians = math.radians(angle)
                result = math.sin(radians)
                print(f"That's a Sine function\nThe Result = {result}")

            elif choice == "9":
                angle = float(input("Enter angle in degrees: "))
                radians = math.radians(angle)
                result = math.cos(radians)
                print(f"That's a Cosine function\nThe Result = {result}")

            elif choice == "10":
                angle = float(input("Enter angle in degrees: "))
                radians = math.radians(angle)
                result = math.tan(radians)
                print(f"That's a Tan function\nThe Result = {result}")

            elif choice == "11":
                a = float(input("Enter a positive number: "))
                if a <= 0:
                    print("Error: Logarithm is defined only for positive numbers.")
                else:
                    result = math.log10(a)
                    print(f"That's a logarithmic function\nResult = {result}")

            elif choice == "12":
                a = float(input("Enter a positive number: "))
                if a <= 0:
                    print("Error: Natural logarithm is defined only for positive numbers.")
                else:
                    result = math.log(a)
                    print(f"That's a logarithmic function\nResult = {result}")

            elif choice == "13":
                n = int(input("Enter a non-negative integer: "))
                if n < 0:
                    print("Error: Factorial is not defined for negative numbers.")
                else:
                    result = math.factorial(x)
                    print(f"That's a Factorial function\nResult = {result}")

            elif choice == "14":
                x = sym.Symbol('x')
                expression = (input("Enter funtion in x: "))
                function = sym.sympify(expression)
                derivative = sym.diff(function, x)
                print(f"The Result = {derivative}")

            elif choice == "15":
                x = sym.Symbol('x')
                expression = (input("Enter funtion in x: "))
                function = sym.sympify(expression)
                derivative = sym.diff(function, x)
                print(f"The Result = {derivative}")

            elif choice == "16":
                print("Thank you for using the calculator!")
                break

            else:
                print("Invalid choice. Please select between 1 and 13.")

        except ValueError:
            print("Invalid input. Please enter numeric values.")


scientific_calculator()

