from weapon.sword import *
from weapon.shield import *


class SwordShield(Sword, Shield):

    def __init__(self, power_=1, life_=100):
        self.power = power_
        self.life = life_

    def attack_back(self, other):
        if self.life <= 0:
            pass
        else:
            print()
            self.print_attackback()
            other.defend(self, self.power*0.5)
        print()

    def defend_info(self, power):
        print('The swordshield take {} damage!'.format(power))
        print('swordshield remaining durability:{}'.format(self.life))

    @staticmethod
    def print_broken():
        print("This swordshield is already broken!")

    @staticmethod
    def print_destroy():
        print("This swordshield is destroyed!")

    @staticmethod
    def print_attackback():
        print("Attack back!")