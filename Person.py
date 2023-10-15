import random

class Person:
    list_names = [
        "Alice",
        "Bob",
        "Charlie",
        "David",
        "Eva",
        "Frank",
        "Grace",
        "Helen",
        "Ivy",
        "Jack",
        "Katherine",
        "Liam",
        "Mia",
        "Noah",
        "Olivia",
        "Penelope",
        "Quincy",
        "Rachel",
        "Samuel",
        "Tara",
        "Ulysses",
        "Victoria",
        "William",
        "Xander",
        "Yasmine",
        "Zachary",
        "Abigail",
        "Benjamin",
        "Chloe",
        "Daniel",
        "Emily",
        "Fiona",
        "George",
        "Hannah",
        "Isaac",
        "Julia",
        "Kevin",
        "Lily",
        "Mason",
        "Natalie",
        "Oscar",
        "Piper",
        "Quinn",
        "Ryan",
        "Sophia",
        "Thomas",
        "Uma",
        "Violet",
        "Wyatt",
        "Xavier",
    ]

    list_TZ = [
        938478261,
        540682193,
        723514987,
        189302274,
        654983732,
        482715639,
        375926418,
        249183637,
        812734796,
        629345718,
        135793846,
        768251394,
        926174483,
        357869342,
        694828517,
        823917436,
        419785532,
        586341497,
        297548616,
        431981576,
        864223971,
        179454628,
        372491845,
        985635472,
        665482713,
        216894765,
        948321967,
        749819632,
        572634989,
        381926974,
        297148856,
        613379428,
        894756623,
        518672394,
        465238978,
        392478761,
        728646591,
        146962875,
        879345126,
        631985574,
        549674283,
        917846423,
        284755396,
        675816942,
        362498875,
        495827134,
        781354962,
        436829576,
        221763894,
        926783414,
    ]

    list_ages = [
        25,
        32,
        42,
        19,
        50,
        38,
        28,
        67,
        22,
        33,
        56,
        41,
        29,
        60,
        24,
        37,
        45,
        31,
        55,
        47,
        21,
        40,
        52,
        27,
        36,
        30,
        49,
        63,
        26,
        34,
        58,
        44,
        23,
        39,
        51,
        35,
        48,
        64,
        43,
        53,
        20,
        54,
        46,
        57,
        61,
        62,
        65,
        66,
        68,
        69,
    ]

    def __init__(self) -> None:
        self._name = random.choice(Person.list_names)
        self._TZ = random.choice(Person.list_TZ)
        self._age = random.choice(Person.list_ages)

    def __str__(self) -> str:
        return f"name: {self._name}, tz: {self._TZ}, age: {self._age}"

    @property
    def name(self) -> str:
        return self._name

    @property
    def TZ(self) -> int:
        return self._TZ

    @property
    def age(self) -> int:
        return self._age

    @name.setter
    def name(self, new_name: str) -> None:
        self._name = new_name

    @TZ.setter
    def TZ(self, new_TZ: int) -> None:
        self._TZ = new_TZ

    @age.setter
    def age(self, new_age: int) -> None:
        self._age = new_age




