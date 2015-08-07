class Ninja(object):   #class names are always capitalized in python
    def __init__(self,name,level):
        self.name = name
        self.level = level
    def fight(self, other):
        if self.level > other.level:
            print "I win"
        elif self.level == other.level:
            print "Draw!"
        else:
            print "I lose"
    def describe(self):
        print 'I am Ninja' + self.name + 'level' + self.level

ninja1 = Ninja('Renee', 1)
ninja2 = Ninja('Molly', 1)

ninja1.fight(ninja2)
