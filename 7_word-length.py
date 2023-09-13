def words_length(*args: str) -> None:
    total_length = 0
    for word in args:
        total_length += len(word)
    print(total_length)


if __name__ == "__main__":
    words_length("asfas", "asf", "wobhsadflkgjara")
