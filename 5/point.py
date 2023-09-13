class Point:
    def __init__(self, x, y) -> None:
        self._x = x
        self._y = y

    def __str__(self) -> str:
        return f"({self._x},{self._y})"

    def __eq__(self, __value: object) -> bool:
        return self._x == __value._x and self._y == __value._y

    def __add__(self, __value: object) -> object:
        return Point(self._x + __value._x, self._y + __value._y)
