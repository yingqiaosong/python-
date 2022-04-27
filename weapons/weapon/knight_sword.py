from weapon.virtual_weapon import *
from weapon.sword import *


class KnightSword(Sword):

    def strike(self, other):
        if self.life <= 0:
            self.print_broken()
        else:
            self.life -= 2
            print("strike success!")
            print("weapon rested durability:{}".format(self.life))
            if self.life <= 0:
                self.print_destroy()
            other.defend(self, 2*self.power)
        print()

    @staticmethod
    def print_broken():
        print("This knightsword is already broken!")

    @staticmethod
    def print_destroy():
        print("This knightsword is destroyed!")


