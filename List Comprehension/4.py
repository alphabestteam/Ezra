from Person import Person

if __name__ == "__main__":
    amount_of_persons = int(
        input("enter the amount of people that you'd like to enter: ")
    )

    people = [Person() for _ in range(amount_of_persons)]
    people_over_18 = [p for p in people if p.age > 18]
    

    for p in people:
        print(p)