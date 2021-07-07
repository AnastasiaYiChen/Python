__author__ = 'YI CHEN'


class Person():
    """
    base class for all humans, including warrior
    """

    def __init__(self, name, title=''):
        """

        :param name:
        :param title:
        """
        self.name = name
        self.title = title

    def get_name(self):
        """

        :return: Person name + title
        """

        result = self.name + "  "

        return result + self.title


class Warrior(Person):
    """
    set warrior level, get weapon, renturn weapon
    """

    def __init__(self, name, title, armory=None, grade=None):
        """

        :param name:
        :param title:
        :param armory:
        :param level:
        """
        super().__init__(name, title)

        self.stash = armory
        self.weapon = []
        self.grade = grade

    def get_weapons(self, weapon):
        """

        :return:
        """
        getWeap = self.weapon.append

        return getWeap

