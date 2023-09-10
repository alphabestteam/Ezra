# 8.

import random


def random_int_generator(min_num: int, num_max_num: int) -> int:
    return random.randint(min_num, max_num)


def random_float_generator(min_num: int, max_num: int) -> float:
    return random.uniform(min_num, max_num)


if __name__ == "__main__":
    min_num = int(input("enter your min range: "))
    max_num = int(input("enter your max range: "))

    print(f"random int value: {random_int_generator(min_num,max_num)}")
    print(f"random float value: {random_float_generator(min_num,max_num)}")
