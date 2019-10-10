from random import randint


class Army:
    def __init__(self):
        self.troop = []

    def __len__(self):
        return len(self.troop)

    def train_units(self, warrior_type, number):
        if warrior_type == Swordsman:
            for warrior_to_add in range(number):
                self.troop.append(Swordsman())
        elif warrior_type == Lancer:
            for warrior_to_add in range(number):
                self.troop.append(Lancer())
        elif warrior_type == Archer:
            for warrior_to_add in range(number):
                self.troop.append(Archer())


class Soldier:
    def __init__(self, name, army_type, warrior_type):
        self.name = name
        self.army_type = army_type
        self.warrior_type = warrior_type

    def introduce(self):
        return print(f'{self.warrior_type} {self.name}, {self.army_type} {self.specialization}')


class Swordsman(Soldier):
    def __init__(self):
        self.health = 100
        self.attack = 10
        self.is_alive = True
        self.specialization = 'swordsman'


class Lancer(Soldier):
    def __init__(self):
        self.health = 80
        self.attack = 15
        self.is_alive = True
        self.specialization = 'lancer'


class Archer(Soldier):
    def __init__(self):
        self.health = 100
        self.attack = randint(5, 25)
        self.is_alive = True
        self.specialization = 'archer'


class AsianArmy(Army):
    army_type = 'Asian'
    swordsman = 'Samurai'
    lancer = 'Ronin'
    archer = 'Shinobi'


class EuropeanArmy(Army):
    army_type = 'European'
    swordsman = 'Knight'
    lancer = 'Raubritter'
    archer = 'Ranger'


class Battle:
    def fight(self, army_1, army_2):
        while len(army_1) > 0 and len(army_2) > 0:
            soldier_1_won = fight(army_1.troop[0], army_2.troop[0])
            if soldier_1_won:
                army_2.troop.pop(0)
            else:
                army_1.troop.pop(0)

        if len(army_1) > 0:
            return True
        else:
            return False


def fight(unit_1, unit_2):
    """
    Function for one-on-one duel.
    Every turn, the first warrior will hit the second and this second will lose health in the same value
    as the attack of the first warrior. After that, if still alive, the second warrior will do the same
    to the first one. The fight ends with the death of one of them. If the first warrior is still alive
    (and thus the other one is not anymore), the function should return True, False otherwise
    """

    while True:
        unit_2.health -= unit_1.attack
        if unit_2.health <= 0:
            unit_2.is_alive = False
            return True

        unit_1.health -= unit_2.attack
        if unit_1.health <= 0:
            unit_1.is_alive = False
            return False


if __name__ == '__main__':
    my_army = EuropeanArmy()
    enemy_army = AsianArmy()

    my_army.train_units(Swordsman, 3)
    my_army.train_units(Archer, 3)
    my_army.train_units(Lancer, 8)

    enemy_army.train_units(Swordsman, 5)
    enemy_army.train_units(Archer, 3)
    enemy_army.train_units(Lancer, 6)

    battle = Battle()
    print(battle.fight(my_army, enemy_army))
