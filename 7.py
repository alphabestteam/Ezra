# 7.

from math import sqrt


def quadratic_equation(a=0, b=0, c=0) -> list:
    if b**2 - 4 * a * c >= 0:
        x1 = (-b + sqrt(b**2 - 4 * a * c)) / 2 * a
        x2 = (-b - sqrt(b**2 - 4 * a * c)) / 2 * a
        return [x1, x2]
    else:
        return 0


if __name__ == "__main__":
    a = int(input('enter the value of "a": '))
    b = int(input('enter the value of "b": '))
    c = int(input('enter the value of "c": '))
    print(quadratic_equation(a, b, c))
