import pytest


@pytest.fixture(autouse=True)
def setup():
    print('\nSetup')


def test1(setup):
    print('executing test1')
    assert True


def test2():
    print('executing test 2')
    assert True