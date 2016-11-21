class Paren (object):
    def implicit (self):
        print "PARENT implicit()"

class Child(Parent):
    pass
dad = Parent()
son = Child()

dad.implicit()
son.implicit()
