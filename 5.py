# 5.


def add_numbers(num_1=0, num_2=0) -> int:
    return num_1 + num_2


if __name__ == "__main__":
    number_1 = int(input("input the first number: ") or 0)
    number_2 = int(input("input the second number: ") or 0)
    print(add_numbers(number_1, number_2))
