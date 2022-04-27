from weapon.virtual_weapon import *


class Shield(Weapon):

    def __init__(self, life_=100):
        self.life = life_

    def defend(self, other, power):
        if self.life <= 0:
            self.print_broken()
        else:
            self.life -= power
            self.defend_info(power)
            if self.life <= 0:
                self.print_destroy()
    print()

    def attack_back(self, other):
        pass

    def defend_info(self, power):
        print('The shield take {} damage!'.format(power))
        print('shield remaining durability:{}'.format(self.life))

    @staticmethod
    def print_broken():
        print("This shield is already broken!")

    @staticmethod
    def print_destroy():
        print("This shield is destroyed!")
