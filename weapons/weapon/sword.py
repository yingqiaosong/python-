from weapon.virtual_weapon import *


class Sword(Weapon):
    power = 1
    
    def __init__(self, power_=1, life_=5):
        self.power = power_
        self.life = life_

    def attack(self, other):
        if self.life <= 0:
            self.print_broken()
        else:
            self.life -= 1
            print("attack success!")
            print("weapon rested durability:{}".format(self.life))
            if self.life <= 0:
                self.print_destroy()
            other.defend(self, self.power)
            other.attack_back(self)
        print()

    @staticmethod
    def print_broken():
        print("This sword is already broken!")

    @staticmethod
    def print_destroy():
        print("This sword is destroyed!")



