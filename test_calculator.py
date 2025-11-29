import calculator
def test_add():
    assert calculator.add(2, 3) == 5
    assert calculator.add(-1, 1) == 0

def test_subtract():
    assert calculator.subtract(5, 3) == 2

def test_divide_by_zero():
    try:
        calculator.divide(10, 0)
        assert False, "Ожидалось исключение ValueError"
    except ValueError:
        assert True

def test_power():
    assert calculator.power(2, 3) == 8

def test_bad_multiply():
    assert calculator.multiply(3, 3) == 9   