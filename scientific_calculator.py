import math
import random
import statistics
import sympy as sym

from arithmetic_calculator import ArithmeticCalculator


class ScientificCalculator(ArithmeticCalculator):
    def __init__(self):
        super().__init__()

    def power(self):
        a, b = self.get_two_numbers()
        self.show_result(a ** b)

    def square_root(self):
        number = float(input("Number: "))

        if number < 0:
            print(
                "\nCannot calculate the real square root "
                "of a negative number.\n"
            )
            return

        self.show_result(math.sqrt(number))

    def inverse(self):
        number = float(input("Number: "))

        if number == 0:
            print("\nZero does not have a reciprocal.\n")
            return

        self.show_result(1 / number)

    def sine(self):
        angle = float(input("Angle in degrees: "))
        radians = math.radians(angle)
        self.show_result(math.sin(radians))

    def cosine(self):
        angle = float(input("Angle in degrees: "))
        radians = math.radians(angle)
        self.show_result(math.cos(radians))

    def tangent(self):
        angle = float(input("Angle in degrees: "))
        radians = math.radians(angle)

        if math.isclose(math.cos(radians), 0, abs_tol=1e-12):
            print("\nTangent is undefined at this angle.\n")
            return

        self.show_result(math.tan(radians))
    
    def inverse_sine(self):
        value = float(input("Enter a value between -1 and 1: "))

        if value < -1 or value > 1:
            print("\nInput must be between -1 and 1.\n")
            return

        angle = math.degrees(math.asin(value))
        self.show_result(angle)
    
    def inverse_cosine(self):
        value = float(input("Enter a value between -1 and 1: "))

        if value < -1 or value > 1:
            print("\nInput must be between -1 and 1.\n")
            return

        angle = math.degrees(math.acos(value))
        self.show_result(angle)
    
    def inverse_tangent(self):
        value = float(input("Enter a number: "))

        angle = math.degrees(math.atan(value))
        self.show_result(angle)

    def log10(self):
        number = float(input("Positive number: "))

        if number <= 0:
            print("\nLogarithm requires a positive number.\n")
            return

        self.show_result(math.log10(number))

    def natural_log(self):
        number = float(input("Positive number: "))

        if number <= 0:
            print("\nNatural logarithm requires a positive number.\n")
            return

        self.show_result(math.log(number))

    def factorial(self):
        number = int(input("Non-negative integer: "))

        if number < 0:
            print("\nFactorial is not defined for negative integers.\n")
            return

        self.show_result(math.factorial(number))

    def differentiate(self):
        x = sym.Symbol("x")
        expression = input("Enter a function in x: ")

        function = sym.sympify(expression)
        derivative = sym.diff(function, x)

        self.show_result(derivative)

    def integrate(self):
        x = sym.Symbol("x")
        expression = input("Enter a function in x: ")

        function = sym.sympify(expression)
        integral = sym.integrate(function, x)

        self.show_result(integral)

    def random_number(self):
        minimum = int(input("Minimum integer: "))
        maximum = int(input("Maximum integer: "))

        if minimum > maximum:
            print("\nMinimum cannot be greater than maximum.\n")
            return

        result = random.randint(minimum, maximum)
        self.show_result(result)

    def get_number_list(self):
        user_input = input("Enter numbers separated by commas: ")
        values = user_input.split(",")
        number_list = []

        for value in values:
            number = float(value.strip())
            number_list.append(number)

        if not number_list:
            raise ValueError("At least one number is required.")

        return number_list

    def statistics_summary(self):
        numbers = self.get_number_list()

        mean_value = statistics.mean(numbers)
        median_value = statistics.median(numbers)
        mode_values = statistics.multimode(numbers)

        self.display = mean_value

        print(f"\nMean = {mean_value}")
        print(f"Median = {median_value}")

        if len(mode_values) == 1:
            print(f"Mode = {mode_values[0]}\n")
        else:
            print(f"Modes = {mode_values}\n")