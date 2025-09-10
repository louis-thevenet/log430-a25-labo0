"""
Calculator app tests
SPDX - License - Identifier: LGPL - 3.0 - or -later
Auteurs : Gabriel C. Ullmann, Fabio Petrillo, 2025
"""

from calculator import Calculator


def test_app():
    my_calculator = Calculator()
    assert my_calculator.get_hello_message() == "== Calculatrice v1.0 =="


# TODO: ajoutez les tests
def test_addition_positive():
    my_calculator = Calculator()
    assert my_calculator.addition(2, 3) == 5


def test_addition_negative():
    my_calculator = Calculator()
    assert my_calculator.addition(-2, -3) == -5


def test_subtraction_positive():
    my_calculator = Calculator()
    assert my_calculator.subtraction(3, 2) == 1


def test_subtraction_negative():
    my_calculator = Calculator()
    assert my_calculator.subtraction(-3, -2) == -1


def test_multiplication():
    my_calculator = Calculator()
    assert my_calculator.multiplication(2, 3) == 6


def test_multiplication_negative():
    my_calculator = Calculator()
    assert my_calculator.multiplication(-2, -3) == 6


def test_division_positive():
    my_calculator = Calculator()
    assert my_calculator.division(6, 3) == 2


def test_division_negative():
    my_calculator = Calculator()
    assert my_calculator.division(-6, -3) == 2


def test_division_zero():
    my_calculator = Calculator()
    assert my_calculator.division(6, 0) == "Erreur : division par zéro"
