from character import Character


def any_alive(enemy):
    for e in enemy:
        if e.is_alive():
            return True
    return False


def main():
    hero = Character("Knight", 30, 5)
    enemy = [Character("Goblin", 20, 3), Character("Ant", 50, 4)]

    print(hero)
    for i in enemy:
        print(i)
    print()

    while hero.is_alive() and any_alive(enemy):
        for i in enemy:
            if i.is_alive():
                hero.attack(i)
                break

        for o in enemy:
            if o.is_alive() and hero.is_alive():
                o.attack(hero)

        print(hero)
        for i in enemy:
            print(i)
        print()

    print("Battle over!")
    if hero.is_alive():
        print(f"{hero.name} wins!")
    else:
        print("The enemies win!")


if __name__ == "__main__":
    main()
