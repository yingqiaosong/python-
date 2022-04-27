from weapon import *

EDU = 3

# sw1 = Sword(2, EDU)
# sh1 = Shield(100)
#
# for i in range(EDU+1):
#     sw1.attack(sh1)
#
# sw1 = KnightSword(3,EDU)
#
# sw1.attack(sh1)
# sw1.attack(sh1)
# sw1.strike(sh1)
# sw1.attack(sh1)

ss1 = SwordShield(3, 10)
ss2 = SwordShield(3, 10)
sw = Sword(2, 5)
sh = Shield(20)
ks = KnightSword(4, 6)

ss1.attack(ss2)
sw.attack(sh)
ks.strike(sh)

