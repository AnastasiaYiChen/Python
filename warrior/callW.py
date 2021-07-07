__author__ = 'YI CHEN'

from P_Worrior import*
from Armory import*

# get name and title
W1 = Person("Koroo", "SEVN")
W2 = Person("Boo", "Beauty")

print(W1.get_name())
print(W2.get_name())

# get name title and weapon and combats ability

# W = Warrior("Pika","p")
# print(W.weapon(1,2))
sa = [Warrior("Mary", "Monster", "sword", 5), Warrior("Jack", "Elf", "bow", 8), Warrior("Dodo", "Bird", "noise", 10)]

for i in sa:
    print(i.name, i.title, i.stash, i.grade)

# print(W.get_weapons("bow"))
# print(Warrior.stash)
# print(Warrior.grade)
# Weapon = W.weapon1
# print(W.sa)

# help(warrior)

# print(Warrior.getWeap)

print("-----------------------------------------------------------------------------------------------------------------")

# store weapon and provide weapon
wA = Armory()
# wA.addWeapon("bow")
weaps = ["bow", "ax", "sword"]
wl = len(wA.weaponlist)

for weaponss in weaps:
    if wl == 0:
        wA.addWeapon(weaps)
        print(weaponss)
    else:
        wA.gimmy_weapon(0)
        print(weaponss)

# wA.addWeapon("sword")
# wA.gimmy_weapon(0)
print(wA.weaponlist)
