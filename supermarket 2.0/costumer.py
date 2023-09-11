from product import Product


class Costumer:
    _shopping_cart: list
    _payment: int

    def __init__(self, name: int) -> None:
        self._name = name
        self._shopping_cart = []
        self._payment = 0

    def __str__(self) -> str:
        return f"name: {self._name}, shopping cart: {self._shopping_cart}, payment: {self._payment}"

    @property
    def name(self) -> str:
        return self._name

    @property
    def shopping_cart(self) -> list:
        return self._shopping_cart

    @property
    def payment(self) -> int:
        return self._payment

    @payment.setter
    def payment(self, new_payment: int) -> None:
        self._payment = new_payment

    def add_product(self):
        name = input("Product name: ")
        found = False

        for item in self.shopping_cart:
            if name in item:
                amount = int(input("Product amount: "))
                item[name]["amount"] += amount
                self.payment += item[name]["price"] * amount
                found = True
                break

        if not found:
            price = int(input("Product price: "))
            amount = int(input("Product amount: "))

            product = Product(name, price)
            self.shopping_cart.append(
                {product.name: {"price": product.price, "amount": amount}}
            )
            self.payment += product.price * amount

        print(self)

    def remove_product(self):
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
            else:
                print("Enter a valid item")

        print(self)
