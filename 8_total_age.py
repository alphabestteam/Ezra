def total_age(**kwargs) -> None:
    t_age = 0
    for key, value in kwargs.items():
        print(key, value)
        t_age += value
    print(t_age)


if __name__ == "__main__":
    total_age(age1=10, age2=20, age3=30, age4=40)
