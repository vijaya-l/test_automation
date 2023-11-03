import pytest
a=5
b=3

@pytest.mark.group_a
def test_add():
    assert a+b!=0,"sum of a and b is zero"

@pytest.mark.skip()
def test_sub():
    assert a>b,"b is greater than a"
    print(a-b)
@pytest.mark.group_a
def test_mul():
    assert a*b >0,"product of a and b is less than 0"

def test_div():
    assert a/b!=1,"quotient is equal to 1"