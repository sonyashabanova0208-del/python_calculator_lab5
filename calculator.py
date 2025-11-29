def add(a, b):
    result = a + b
    return result

def subtract(a, b):
    return a - b

def multiply(a, b):
    result = a * b # Умножение в conflict-branch
    return result

def divide(a, b):
    if b == 0:
        raise ValueError("На ноль делить нельзя!")
    return a / b

def power(a, b):
    return a ** b

def sqrt(a):
    if a < 0:
        raise ValueError("Корень из отрицательного числа извлечь нельзя")
    return a ** 0.5

if __name__ == "__main__":
    print("Калькулятор запущен!")
    x = 10
    y = 5
    sum_result = add(x, y)
    print(f"{x} + {y} = {sum_result}")