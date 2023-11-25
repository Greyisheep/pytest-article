def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


class Calculator:
    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y == 0:
            raise ValueError("Cannot divide by zero")
        return x / y
