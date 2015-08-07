import random
print random.randint(10)


class Monster(object):
    def __init__ (self, color, scare_level, skin_type):
        self.color = color
        self.scare_level = scare_level
        self.skin_type = skin_type

    def scare_comp(self, opponent):
        if self.scare_level < opponent.scare_level:
            print "You lost the scare competition!"
        elif self.scare_level == opponent.scare_level:
            print "Draw!"
        else:
            print "You win!"

    def describe(self):
        print "I am a monster who is " + self.color + " and " + self.skin_type

monster1 = Monster('green', 3, 'smooth')
monster2 = Monster('pink', 7, 'hairy')

monster1.scare_comp(monster2)
monster1.describe()
monster2.describe()

class Ninja(object):   #class names are always capitalized in python
    def __init__(self,name, scare_level):
        self.name = name
        self.scare_level = scare_level
    def fight(self, other):
        if self.level > other.scare_level:
            print "I win"
        elif self.level == other.scare_level:
            print "Draw!"
        else:
            print "I lose"
    def scare_comp(self, opponent):
        if self.scare_level < opponent.scare_level:
            print "You lost the scare competition!"
        elif self.scare_level == opponent.scare_level:
            print "Draw!"
        else:
            print "You win!"

ninja1 = Ninja('Jon', 6)

ninja1.scare_comp(monster2)
