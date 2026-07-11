import math
import sympy as sym

def scientific_calculator():
    while True:
        print("\n===== Scientific Calculator =====")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Power")
        print("6. Square Root")
        print("7. Sine")
        print("8. Cosine")
        print("9. Tangent")
        print("10. Log (base 10)")
        print("11. Natural Log (ln)")
        print("12. Factorial")
        print("13. Differentiate")
        print("14. Integrate")
        print("15. Exit")

        choice = input("\nEnter your choice (1-15): ")

        try:
            if choice == "1":
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
                Add = a + b
                print(f"The Result = {Add}")

            elif choice == "2":
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
                Sub = a - b
                print(f"The Result = {Sub}")

            elif choice == "3":
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
                Multiply = a * b
                print(f"The Result = {Multiply}")

            elif choice == "4":
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
                Divide = a / b
                print(f"The Result = {Divide}")

            elif choice == "5":
                a = float(input("Enter base: "))
                b = float(input("Enter exponent: "))
                Power = a ** b
                print(f"The Result = {Power}")

            elif choice == "6":
                a = float(input("Enter a number: "))
                x = math.sqrt(a) 
                print(f"The Result = {x}")

            elif choice == "7":
                angle = float(input("Enter angle in degrees: "))
                print("Result =", math.sin(math.radians(angle)))

            elif choice == "8":
                angle = float(input("Enter angle in degrees: "))
                print("Result =", math.cos(math.radians(angle)))

            elif choice == "9":
                angle = float(input("Enter angle in degrees: "))
                print("Result =", math.tan(math.radians(angle)))

            elif choice == "10":
                a = float(input("Enter a positive number: "))
                if a <= 0:
                    print("Error: Logarithm is defined only for positive numbers.")
                else:
                    print("Result =", math.log10(a))

            elif choice == "11":
                a = float(input("Enter a positive number: "))
                if a <= 0:
                    print("Error: Natural logarithm is defined only for positive numbers.")
                else:
                    print("Result =", math.log(a))

            elif choice == "12":
                n = int(input("Enter a non-negative integer: "))
                if n < 0:
                    print("Error: Factorial is not defined for negative numbers.")
                else:
                    print("Result =", math.factorial(n))

            elif choice == "13":
                x = sym.Symbol('x')
                expression = (input("Enter funtion in x: "))
                function = sym.sympify(expression)
                derivative = sym.diff(function, x)
                print(f"The Result = ", {derivative})

            elif choice == "15":
                print("Thank you for using the calculator!")
                break

            else:
                print("Invalid choice. Please select between 1 and 13.")

        except ValueError:
            print("Invalid input. Please enter numeric values.")


scientific_calculator()

