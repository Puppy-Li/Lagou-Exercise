import pytest
import yaml
from calculator import Calculator

with open("./testdata/calculator_data.yaml") as f:
    data = yaml.safe_load(f)
    add = data['add']
    sub = data['sub']
    mul = data['mul']
    div = data['div']


@pytest.fixture(scope="class")
def setup_teardown():
    print("开始计算")
    calc = Calculator()
    yield calc
    print("计算结束")


class TestCalculator:
    @pytest.mark.parametrize("a, b, expect", add)
    def test_add(self, a, b, expect, setup_teardown):
        result = setup_teardown.add(a, b)
        if isinstance(result, float):
            result = round(result, 2)
        assert result == expect

    @pytest.mark.parametrize("a, b, expect", sub)
    def test_sub(self, a, b, expect, setup_teardown):
        result = setup_teardown.substract(a, b)
        if isinstance(result, float):
            result = round(result, 2)
        assert result == expect

    @pytest.mark.parametrize("a, b, expect", mul)
    def test_mul(self, a, b, expect, setup_teardown):
        result = setup_teardown.multiply(a, b)
        if isinstance(result, float):
            result = round(result, 2)
        assert result == expect

    @pytest.mark.parametrize("a, b, expect", div)
    def test_div(self, a, b, expect, setup_teardown):
        result = setup_teardown.divide(a, b)
        if isinstance(result, float):
            result = round(result, 2)
        assert result == expect

