class Monster:
    _hp: int
    _damage: int

    def __init__(self, name: str, level: int) -> None:
        self._name = name
        self._level = level
        self._hp = level * 40 
        self._damage = level * 2

    def __str__(self) -> str:
        return f"name: {self._name}, level: {self._level}, hp: {self._hp}, damage: {self._damage}"

    @property
    def name(self) -> str:
        return self._name

    @property
    def level(self) -> int:
        return self._level

    @property
    def hp(self) -> int:
        return self._hp

    @property
    def damage(self) -> int:
        return self._damage

    @level.setter
    def level(self, new_level) -> None:
        self._level = new_level

    @hp.setter
    def hp(self, new_hp) -> None:
        self._hp = new_hp

    @damage.setter
    def damage(self, new_damage) -> None:
        self._damage = new_damage

    def attack(self, hero: object) -> bool:
        killed = hero.reduce_health(self)
        if killed == 0:
            return True
        return False

    def reduce_health(self, hero: object) -> int:
        self.hp -= hero.damage
        if self.hp < 0:
            self.hp = 0
        return self.hp
