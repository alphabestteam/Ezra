def fibonacci_multi(N):
    a, b = 1, 2
    for i in range(N):
        yield a
        a, b = b, a * b


def main():
    for index in fibonacci_multi(10):
        print(index)


if __name__ == "__main__":
    main()
