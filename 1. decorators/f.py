import time


def timer(func):
    def inner():
        start_time = time.time()  # get's the time
        func()
        end_time = time.time()
        print(end_time - start_time)

    return inner


@timer
def random_function():
    print("doing something")
    for x in range(100):
        print("*" * x)


def main():
    random_function()


if __name__ == "__main__":
    main()
