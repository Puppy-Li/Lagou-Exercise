import pytest


@pytest.mark.parametrize("name", ["哈利", "赫敏"])
def test_mm(name):
    print(name)


def test_login():
    print("login")


def test_login_fail():
    print("login failed.")
    assert False


def test_env(cmdoption):
    print(cmdoption)