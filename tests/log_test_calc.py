import pytest
import unittest
from app.main import Calculator
from app.error import InvalidInputException
from math import log


@pytest.fixture
def calculator():
    """Фикстура для создания объекта калькулятора."""
    return Calculator()

@pytest.mark.parametrize("a, base, expected", [
    (100, 10, 2),      # Логарифм 100 по основанию 10
    (81, 3, 4),        # Логарифм 81 по основанию 3
    (20, 2.718, log(20, 2.718))      # Логарифм 20 по основанию e
])
def test_log_valid_values(calculator, a, base, expected):
    """Тестирование корректных значений."""
    result = calculator.log(a, base)
    assert pytest.approx(result, rel=1e-5) == expected


@pytest.mark.parametrize("a, base", [
    ('a', 10),         # Некорректный тип для a
    (100, 'b'),        # Некорректный тип для base
    ('a', 'b'),        # Оба значения некорректные
])
def test_log_invalid_types(calculator, a, base):
    """Тестирование с некорректными типами данных."""
    with pytest.raises(TypeError):
        calculator.log(a, base)

@pytest.mark.parametrize("a, base", [
    (0, 10),            # a должно быть > 0
    (1, 10),            # a не должно быть равно 1
    (10, 0),            # Основание должно быть > 0
    (10, -4),           # Основание не может быть отрицательным
])
def test_log_invalid_domain(calculator, a, base):
    """Тестирование с нарушением ОДЗ функции."""
    with pytest.raises(InvalidInputException):
        calculator.log(a, base)


if __name__ == "__main__":
    unittest.main()