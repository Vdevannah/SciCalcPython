import sympy as sym
import random
import statistics

from arithmetic_calculator import ArithmeticCalculator
from scientific_calculator import ScientificCalculator


def run_arithmetic_menu():
    calculator = ArithmeticCalculator()

    while True:
        print(
            """
Arithmetic Calculator 

1. Add
2. Subtract
3. Multiply
4. Divide
5. M+  - Add display value to memory
6. MC  - Clear memory
7. MRC - Recall memory
8. Return to Main Menu

"""
        )

        choice = input("Enter your choice: ").strip()

        try:
            if choice == "1":
                calculator.add()

            elif choice == "2":
                calculator.subtract()

            elif choice == "3":
                calculator.multiply()

            elif choice == "4":
                calculator.divide()

            elif choice == "5":
                calculator.memory_add()

            elif choice == "6":
                calculator.memory_clear()

            elif choice == "7":
                calculator.memory_recall()

            elif choice == "8":
                print("\nReturning to the main menu.\n")
                break

            else:
                print("\nInvalid choice. Enter a number from 1 to 8.\n")

        except ValueError as error:
            print(f"\nInvalid numerical input: {error}\n")

        except Exception as error:
            print(f"\nError: {error}\n")


def run_scientific_menu():
    calculator = ScientificCalculator()

    while True:
        print(
            """
Scientific Calculator 

1.  Add
2.  Subtract
3.  Multiply
4.  Divide
5.  Power
6.  Square Root
7.  Reciprocal
8.  Sine
9.  Cosine
10. Tangent
11. Inverse Sine
12. Inverse Cosine
13. Inverse Tangent
14. Log Base 10
15. Natural Log
16. Factorial
17. Differentiate
18. Integrate
19. Random number generator
20. Mean, Median and Mode
21. M+  - Add display value to memory
22. MC  - Clear memory
23. MRC - Recall memory
24. Return to Main Menu

"""
        )

        choice = input("Enter your choice: ").strip()

        try:
            if choice == "1":
                calculator.add()

            elif choice == "2":
                calculator.subtract()

            elif choice == "3":
                calculator.multiply()

            elif choice == "4":
                calculator.divide()

            elif choice == "5":
                calculator.power()

            elif choice == "6":
                calculator.square_root()

            elif choice == "7":
                calculator.inverse()

            elif choice == "8":
                calculator.sine()

            elif choice == "9":
                calculator.cosine()

            elif choice == "10":
                calculator.tangent()
            
            elif choice == "11":
                calculator.inverse_sine()

            elif choice == "12":
                calculator.inverse_cosine()

            elif choice == "13":
                calculator.inverse_tangent()

            elif choice == "14":
                calculator.log10()

            elif choice == "15":
                calculator.natural_log()

            elif choice == "16":
                calculator.factorial()

            elif choice == "17":
                calculator.differentiate()

            elif choice == "18":
                calculator.integrate()

            elif choice == "19":
                calculator.random_number()

            elif choice == "20":
                calculator.statistics_summary()

            elif choice == "21":
                calculator.memory_add()

            elif choice == "22":
                calculator.memory_clear()

            elif choice == "23":
                calculator.memory_recall()

            elif choice == "24":
                print("\nReturning to the main menu.\n")
                break

            else:
                print("\nInvalid choice. Enter a number from 1 to 19.\n")

        except ValueError as error:
            print(f"\nInvalid numerical input: {error}\n")

        except sym.SympifyError:
            print("\nInvalid mathematical expression.\n")

        except Exception as error:
            print(f"\nError: {error}\n")