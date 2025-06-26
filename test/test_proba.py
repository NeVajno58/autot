import pytest

@pytest.fixture()
def before_after():
    print('\nBefor')
    yield
    print('\nAfter')

def test_dem1():
    assert 1 == 1

def test_dem2(before_after):
    assert 2 + 3 == 5
