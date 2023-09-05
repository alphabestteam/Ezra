# adding numbers from 1 till 100


def factorial(number: int) -> int:
    factorial_number = 1
    for x in range(1, number+1):
        factorial_number *= x
    return factorial_number


if __name__ == "__main__":
    added_numbers = 0
    for index in range(101):
        added_numbers += index
    print(added_numbers)

    print(f'5 {factorial(5)}')
    print(f'6 {factorial(6)}')
    print(f'7 {factorial(7)}')
    print(f'8 {factorial(8)}')
