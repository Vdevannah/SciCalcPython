from menu import run_arithmetic_menu, run_scientific_menu


def main():
    while True:
        print(
            """
Calculator Application

1. Arithmetic Calculator
2. Scientific Calculator
3. Exit

"""
        )

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            run_arithmetic_menu()

        elif choice == "2":
            run_scientific_menu()

        elif choice == "3":
            print("\nProgram closed.\n")
            break

        else:
            print("\nInvalid choice. Enter 1, 2, or 3.\n")


if __name__ == "__main__":
    main()
