class People:
    def __init__(self, people: list) -> None:
        self._people = people

    @property
    def people(self) -> list:
        return self._people

    def add_person(self, new_name: str) -> None:
        self.people.append(new_name)

    def __iter__(self) -> object:
        self.curr_index = 0
        return self

    def __next__(self):
        if self.curr_index >= len(self.people):
            del self.curr_index
            raise StopIteration
        current_person = self.people[self.curr_index]
        self.curr_index += 1
        return current_person

    def __str__(self) -> str:
        return f"list of people: \n{self.people}"
