def add(a, b):
    result = a + b
    return result

def subtract(a, b):
    return a - b

def multiply(a, b):
    temp = a * b
    return temp

def divide(a, b):
    if b == 0:
        raise ValueError("На ноль делить нельзя!")
    return a / b

if __name__ == "__main__":
    print("Калькулятор запущен!")
    x = 10
    y = 5
    sum_result = add(x, y)
    print(f"{x} + {y} = {sum_result}")