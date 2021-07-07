__author__ = 'YI CHEN'



class Weapon():
    """

    """
    def __init__(self, name, av, dv):
        """

        :param name:
        :param av:
        :param dv:
        :return:
        """
        self.name = name
        self.attack = av
        self.defense = dv

    def set_weapons(self):
        def __iter__(self):
            self.name = 1
            return self

        def __next__(self):
            if self.a <= 20:
                x = self.a
                self.a += 1
                return x
            else:
                raise StopIteration

    def get_attack(self):
        """

        :return:
        """
        return self.attack

    def get_defense(self):
        """

        :return:
        """
        return self.defense

