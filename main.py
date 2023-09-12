import random
from monster import Monster
from hero import Hero


def choose_action(hero: Hero) -> None:
    action = input(
        "enter action: \n'a' - (attack) \n'u' - (upgrade) \n'r' - (revive) \n'd' - (defense) \n"
    )
    if action == "a":
        hero.attack(monster1)
    elif action == "u":
        hero.level_up()
    elif action == "r":
        hero.heal()
    elif action == "d":
        hero.defend()

    ezra.increase_coins(1)


if __name__ == "__main__":
    hero_dead = False
    ezra = Hero("ezra")
    monster1 = Monster("m1", random.choice([ezra.level - 1, ezra.level + 1]))

    while not hero_dead:
        print(ezra)
        print(monster1)
        choose_action(ezra)
        if monster1.hp == 0:
            monster1 = Monster("m1", random.choice([ezra.level - 1, ezra.level + 1]))
        hero_dead = monster1.attack(ezra)

    print("you lost!")
