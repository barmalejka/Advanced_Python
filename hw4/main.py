class Army:
    def train_swordsman(self, name):
        return Swordsman(name, self.army_type, self.swordsman)

    def train_lancer(self, name):
        return Lancer(name, self.army_type, self.lancer)

    def train_archer(self, name):
        return Archer(name, self.army_type, self.archer)


class Soldier:
    def __init__(self, name, army_type, warrior_type):
        self.name = name
        self.army_type = army_type
        self.warrior_type = warrior_type

    def introduce(self):
        return print(f'{self.warrior_type} {self.name}, {self.army_type} {self.specialization}')


class Swordsman(Soldier):
    specialization = 'swordsman'


class Lancer(Soldier):
    specialization = 'lancer'


class Archer(Soldier):
    specialization = 'archer'


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


if __name__ == '__main__':
    my_army = EuropeanArmy()
    enemy_army = AsianArmy()

    soldier_1 = my_army.train_swordsman("Jaks")
    soldier_2 = my_army.train_lancer("Harold")
    soldier_3 = my_army.train_archer("Robin")

    soldier_4 = enemy_army.train_swordsman("Kishimoto")
    soldier_5 = enemy_army.train_lancer("Ayabusa")
    soldier_6 = enemy_army.train_archer("Kirigae")

    soldier_1.introduce()
    soldier_2.introduce()
    soldier_3.introduce()

    soldier_4.introduce()
    soldier_5.introduce()
    soldier_6.introduce()