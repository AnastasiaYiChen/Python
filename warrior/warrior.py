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
        self.weapon1 = None
        self.weapon2 = None
        self.grade = grade
        self.combats = combats



    def show_stash(self):
        """

        :return: armory
        """
        sa = self.stash
        # sa = []



    def get_weapon(self):
        """

        :param :
        :return: weapon
        """
        getWP1 = self.weapon1.sa.pop
        getWP2 = self.weapon2.sa.pop

        return self.getWP1, self.getWP2

    # def set_grade(self):
    #     """
    #
    #     :return: level
    #     """
    #     sg = self.grade
    #     sg = []
    #     return sg



class Weapon():
    """

    """
    def __init__(self, name, av, dv, sc):
        """

        :param name:
        :param av:
        :param dv:
        :return:
        """
        self.name = name
        self.attack = av
        self.defense = dv
        self.capacity = sc

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

    def set_wc(self):
        """

        :return:
        """
        sc = self.capacity



class Armory():
    """

    """
    def __init__(self, *Weapon):
        """

        :param weaps:
        :return:
        """
        self.weaponlist = []
        pass

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


class combats():
    """
    set combat
    """
    def __init__(self, type, *warrior, compete, result):
        """
        
        :param type:
        :param warrior:
        :param compete:
        :param result:
        """
        pass

        
        


