__author__ = 'YI CHEN'


from weapon import *


class Armory():
    """
    set weapon list, use method to store and provide weapons
    """
    weaponlist = []
    # def __init__(self, *weapon):
    #     """
    #
    #     :param weaps:
    #     :return:
    #     """
    #     self.weaponlist = []
    #     pass

    def addWeapon(self, weapon):
        """

        :param weapon:
        :return:
        """
        self.weaponlist.append(weapon)

    def gimmy_weapon(self, index):
        """

        :return:
        """
        # Wish list or a real stash
        return self.weaponlist.pop(index)
