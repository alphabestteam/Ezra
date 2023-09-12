from costumer import Costumer


class Register:
    _gained_amount = int
    _costumer_list = list

    def __init__(self, name: str) -> None:
        self._gained_amount = 0
        self._costumer_list = []
        self._name = name

    def __str__(self) -> str:
        return (
            f"Register: {self.name} gained amount: {self.gained_amount}, costumer list: {self.costumer_list}"
        )

    @property
    def gained_amount(self) -> int:
        return self._gained_amount

    @property
    def costumer_list(self) -> list:
        return self._costumer_list
    
    @property
    def name(self) -> list:
        return self._name


    @gained_amount.setter
    def gained_amount(self, new_gained_amount) -> None:
        self._gained_amount = new_gained_amount

    def checkout_customer(self, customer: Costumer) -> None:
        self._gained_amount += customer.payment
        self.costumer_list.append((customer.name))

    
    def print_summary(self) -> None:
        print(self)
