import sympy as sym

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
11. Log Base 10
12. Natural Log
13. Factorial
14. Differentiate
15. Integrate
16. M+  - Add display value to memory
17. MC  - Clear memory
18. MRC - Recall memory
19. Return to Main Menu

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
                calculator.log10()

            elif choice == "12":
                calculator.natural_log()

            elif choice == "13":
                calculator.factorial()

            elif choice == "14":
                calculator.differentiate()

            elif choice == "15":
                calculator.integrate()

            elif choice == "16":
                calculator.memory_add()

            elif choice == "17":
                calculator.memory_clear()

            elif choice == "18":
                calculator.memory_recall()

            elif choice == "19":
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
