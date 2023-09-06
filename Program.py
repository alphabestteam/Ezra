import math


def is_prime(number: int) -> bool:
    for x in range(2, math.ceil(math.sqrt(number))):
        if number % x == 0:
            return False
    return True


if __name__ == "__main__":
    added_numbers = 0
    for index in range(101):
        added_numbers += index
    print(added_numbers)

    print(f"5 {is_prime(5)}")
    print(f"6 {is_prime(6)}")
    print(f"7 {is_prime(7)}")
    print(f"14 {is_prime(14)}")
    print(f"152 {is_prime(152)}")
    print(f"60693 {is_prime(60693)}")
