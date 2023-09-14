from e import People


def main():
    peoples1 = People(["moshe", "ezra", "avi", "dan", "chaim"])
    for person in peoples1:
        print(person)


if __name__ == "__main__":
    main()
