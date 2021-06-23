import pytest


class Calculator:
    # 加法
    def add(self, a, b):
        return a + b

    # 减法
    def substract(self, a, b):
        return a - b

    # 乘法
    def multiply(self, a, b):
        return a * b

    # 除法
    def divide(self, a, b):
        if b == 0:
            with pytest.raises(ZeroDivisionError) as excinfo:
                a / b
                assert excinfo.type == ZeroDivisionError
            return "divisor cannot be zero"
        else:
            return a / b
