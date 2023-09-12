from product import Product


class Costumer:
    _shopping_cart: list
    _payment: int

    def __init__(self, name: str) -> None:
        self._name = name
        self._shopping_cart = []
        self._payment = 0

    def __str__(self) -> str:
        return f"name: {self.name}, shopping cart: {self.shopping_cart}, payment: {self.payment}"

    @property
    def name(self) -> str:
        return self._name

    @property
    def shopping_cart(self) -> list:
        return self._shopping_cart

    @property
    def payment(self) -> float:
        return self._payment

    @payment.setter
    def payment(self, new_payment: float) -> None:
        self._payment = new_payment

    def add_product(self) -> None:
        name = input(f"({self.name}) Product name: ")
        found = False

        for item in self.shopping_cart:
            if name in item:
                amount = int(input(f"({self.name}) Product amount: "))
                item[name]["amount"] += amount
                self.payment += item[name]["price"] * amount
                found = True
                break

        if not found:
            price = float(input(f"({self.name}) Product price: "))
            amount = int(input(f"({self.name}) Product amount: "))

            product = Product(name, price)
            self.shopping_cart.append(
                {product.name: {"price": product.price, "amount": amount}}
            )
            self.payment += product.price * amount

        print(self)

    def remove_product(self) -> None:
        found = False
        while not found:
            name_remove = input("Item name to remove: ")
            for item in self.shopping_cart:
                if name_remove in item:
                    enough_product = False
                    while not enough_product:
                        amount_remove = int(input("Amount to remove: "))
                        if item[name_remove]["amount"] >= amount_remove:
                            enough_product = True
                            item[name_remove]["amount"] -= amount_remove
                            self.payment -= item[name_remove]["price"] * amount_remove

                            # if you remove all of the item
                            if item[name_remove]["amount"] == 0:
                                self.shopping_cart.remove(item)
                        else:
                            print("enter a sufficient amount to remove")
                    found = True

        print(self)

    def add_json(self) -> list:
        user = {
            "name": self.name,
            "shopping cart": [{name : {"price" : item[name]["price"], "amount" : item[name]["amount"]}} for item in self.shopping_cart for name in item],
            "payment": self.payment,
        }
        return user
