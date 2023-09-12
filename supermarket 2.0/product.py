class Product:
    
    def __init__(self, name : str, price : int) -> None:
        self._name = name
        self._price = price
    
    def __str__(self) -> str:
        return f"name: {self.name}, price: {self.price}"
    
    # getters
    @property
    def name(self) -> str:
        return self._name
    
    @property
    def price(self) -> int:
        return self._price
    

