import pytest

def f():
    return 3


def test_function():
    assert f() == 4


# assertions about expected exceptions
def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        1 / 0


# actually access to above exception info
def test_recursion_depth():
    with pytest.raises(RuntimeError) as excinfo:

        def f():
            f()

        f()
    assert "maximum recursion" in str(excinfo.value)


def myfunc():
    raise ValueError("Exception 123 raised")


def test_match():
    with pytest.raises(ValueError, match=r".* 123 .*"):
        myfunc()


@pytest.mark.xfail(raises=IndexError)
def test_f():
    f()


class Foo:
    def __init__(self, val):
        self.val = val

    def __eq__(self, other):
        return self.val == other.val


def test_compare():
    f1 = Foo(1)
    f2 = Foo(2)
    assert f1 == f2