import math
import random
import statistics
import numbers
import sympy as sym

memory = 0
display = 0
display_mode = "DECIMAL"
units_mode = "DEGREES"

def parse_list(user_input):
        try:
            return [float(num.strip()) for num in user_input.split(",")]
        except ValueError:
            print("Error: Please enter only numbers separated by commas.")
            return []


def scientific_calculator():
        while True:
            print("\nScientific Calculator")
            print("1. Addition")
            print("2. Subtraction")
            print("3. Multiplication")
            print("4. Division")
            print("5. Power")
            print("6. Square Root")
            print("7. Inverse")
            print("8. Sine")
            print("9. Cosine")
            print("10. Tangent")
            print("11. Log (base 10)")
            print("12. Natural Log (ln)")
            print("13. Factorial")
            print("14. Inverse Sine (arcsin)")
            print("15. Inverse Cosine (arccos)")
            print("16. Inverse Tangent (arctan)")
            print("17. Differentiation")
            print("18. Integration")
            print("19. Mean")
            print("20. Median")
            print("21. Mode")
            print("22. Random Number Generator")
            print("23. Exit")

            choice = input("\nEnter your choice (1-23): ")
            

            try:
                if choice == "1":
                    a = float(input("Enter first number: "))
                    b = float(input("Enter second number: "))
                    Add = a + b
                    print(f"That's an arithmetic function\nThe Result = {Add}")

                elif choice == "2":
                    a = float(input("Enter first number: "))
                    b = float(input("Enter second number: "))
                    Sub = a - b
                    print(f"That's an arithmetic function\nThe Result = {Sub}")

                elif choice == "3":
                    a = float(input("Enter first number: "))
                    b = float(input("Enter second number: "))
                    Multiply = a * b
                    print(f"That's an arithmetic function\nThe Result = {Multiply}")

                elif choice == "4":
                    a = float(input("Enter first number: "))
                    b = float(input("Enter second number: "))
                    if b == 0:
                        print("Error: Cannot divide by zero.")
                    else:
                        Divide = a / b
                        print(f"That's an arithmatic function\nThe Result = {Divide}")

                elif choice == "5":
                    a = float(input("Enter base: "))
                    b = float(input("Enter exponent: "))
                    Power = a ** b
                    print(f"That's an exponential function\nThe Result = {Power}")

                elif choice == "6":
                    a = float(input("Enter a number: "))
                    if a < 0:
                        print("Error: Cannot take the square root of a negative number.")
                    else:
                        result = math.sqrt(a)    
                    print(f"That's a square root function\nThe Result = {x}")

                elif choice == "7":
                    a = float(input("Enter a number: "))
                    Inverse = 1/a 
                    print(f"That's an inverse function\nThe Result = {Inverse}")

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
                        result = math.factorial(n)
                        print(f"That's a Factorial function\nResult = {result}")

                elif choice == "14":
                    a = float(input("Enter a value between -1 and 1:"))
                    if a < -1 or a > 1:
                        print("Error: Input must be between -1 and 1.")
                    else:
                        result = math.degrees(math.asin(a))
                        print(f"That's an Inverse Sine function\nThe Result = {result}")
                
                elif choice == "15":
                    a = float(input("Enter a value between -1 and 1:")) 
                    if a < -1 or a > 1:
                        print("Error: Input must between -1 and 1.")
                    else:
                        result = math.degrees(math.acos(a))
                        print(f"That's an Inverse Cosine function\nThe Result = {result}")

                elif choice == "16":
                    a = float(input("Enter a value: "))
                    result = math.degrees(math.atan(a))
                    print(f"That's an Inverse Tangent function\nThe Result = {result}")

                elif choice == "17":
                    x = sym.Symbol('x')
                    expression = input("Enter function in x: ")
                    function = sym.sympify(expression)
                    derivative = sym.diff(function, x)
                    print(f"The Result (Derivative) = {derivative}")

                elif choice == "18":
                    x = sym.Symbol('x')
                    expression = input("Enter function in x: ")
                    function = sym.sympify(expression)
                    integral = sym.integrate(function, x)
                    print(f"The Result (Integral) = {integral}")

                elif choice == "19":
                    user_input = input("Enter numbers seperated by commas (e.g., 1, 2, 3, 4): ")
                    num_list = parse_list(user_input)
                    if not num_list:
                        print("Error: No numbers entered.")
                    else:
                        mean_val = statistics.mean(num_list)
                        print(f"That's a statistical funtion\nThe Mean = {mean_val}")

                elif choice == "20":
                    user_input = input("Enter numbers separated by commas (e.g., 1, 2, 3, 4): ")
                    num_list = parse_list(user_input)
                    if not num_list:
                        print("Error: No numbers entered.")
                    else:
                        median_val = statistics.median(num_list)
                        print(f"That's a statistical function\nThe Median = {median_val}")

                elif choice == "21":
                    user_input = input("Enter numbers separated by commas (e.g., 1, 2, 2, 3): ")
                    num_list = parse_list(user_input)
                    if not num_list:
                        print("Error: No numbers entered.")
                    else:
                        mode_vals = statistics.multimode(num_list)
                        print(f"That's a statistical function\nThe Mode(s) = {mode_vals}")

                elif choice == "22":
                    lower = int(input("Enter lower bound (inclusive): "))
                    upper = int(input("Enter upper bound (inclusive): "))
                    if lower > upper:
                        print("Error: Lower bound cannot be greater than upper bound.")
                    else:
                        result = random.randint(lower, upper)
                        print(f"Generated a random integer = {result}")
                        
                elif choice == "23":
                    print("Thank you for using the calculator!")
                    break

                else:
                    print("Invalid choice. Please select between 1 and 23.")

            except ValueError:
                print("Invalid input. Please enter numeric values.")


scientific_calculator()
