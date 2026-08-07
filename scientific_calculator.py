import math
import sympy as sym
import statistics
import random

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
