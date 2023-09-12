class Hero:
    _hp: int
    _damage: int
    _level: int
    _coins: int
    HEAL_AMOUNT = 1.4
    LEVEL_UP = 2.5
    COINS_TO_LEVEL = 10
    defend_on = False

    def __init__(self, name) -> None:
        self._name = name
        self._hp = 100
        self._damage = 2
        self._level = 1
        self._coins = 0

    def __str__(self) -> str:
        return f"name: {self._name}, hp: {self._hp}, damage: {self._damage}, level: {self._level}, coins: {self._coins}"

    # getters
    @property
    def name(self) -> str:
        return self._name

    @property
    def hp(self) -> int:
        return self._hp

    @property
    def damage(self) -> int:
        return self._damage

    @property
    def level(self) -> int:
        return self._level

    @property
    def coins(self) -> int:
        return self._coins

    # setters
    @hp.setter
    def hp(self, new_hp) -> None:
        self._hp = new_hp

    @damage.setter
    def damage(self, new_damage) -> None:
        self._damage = new_damage

    @level.setter
    def level(self, new_level) -> None:
        self._level = new_level

    @coins.setter
    def coins(self, new_coins) -> None:
        self._coins = new_coins

    def heal(self) -> None:
        self.hp *= Hero.HEAL_AMOUNT

    def level_up(self) -> None:
        coins_needed_to_upgrade = self.level * Hero.COINS_TO_LEVEL
        if self.coins >= coins_needed_to_upgrade:
            self.damage *= Hero.LEVEL_UP
            self.hp *= Hero.LEVEL_UP
            self.level += 1
            if self.hp < 100:
                self.hp == 100
            self.coins -= coins_needed_to_upgrade
        else:
            print("you don't have enough coins to upgrade")

    def attack(self, monster: object) -> None:
        killed = monster.reduce_health(self)
        if killed == 0:
            Hero.increase_coins(self, monster.level)

    def defend(self) -> None:
        Hero.defend == True

    def reduce_health(self, monster: object) -> int:
        if Hero.defend_on == True:
            self.hp -= monster.damage * 0.2
            Hero.defend_on == False
        else:
            self.hp -= monster.damage
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def increase_coins(self, coins_to_add: int) -> None:
        self.coins += coins_to_add
