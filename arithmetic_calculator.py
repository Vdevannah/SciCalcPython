import numbers


class ArithmeticCalculator:
    def __init__(self):
        self.display = 0
        self.memory = 0

    def get_two_numbers(self):
        a = float(input("First number: "))
        b = float(input("Second number: "))
        return a, b

    def show_result(self, value):
        self.display = value
        print(f"\nResult = {self.display}\n")

    def add(self):
        a, b = self.get_two_numbers()
        self.show_result(a + b)

    def subtract(self):
        a, b = self.get_two_numbers()
        self.show_result(a - b)

    def multiply(self):
        a, b = self.get_two_numbers()
        self.show_result(a * b)

    def divide(self):
        a, b = self.get_two_numbers()

        if b == 0:
            print("\nCannot divide by zero.\n")
            return

        self.show_result(a / b)

    def memory_add(self):
        if not isinstance(self.display, numbers.Number):
            print("\nM+ requires a numeric value on the display.\n")
            return

        self.memory += self.display
        self.display = self.memory

        print(f"\nMemory = {self.memory}\n")

    def memory_clear(self):
        self.memory = 0
        print("\nMemory cleared.\n")

    def memory_recall(self):
        self.display = self.memory
        print(f"\nRecalled value = {self.display}\n")

