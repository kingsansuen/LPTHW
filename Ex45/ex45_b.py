from sys import exit
import time
import ex45_b
import random
from threading import Thread
import threading


class monster(object):
    pass



class small(monster):
    def renew(self):
        a_color = ["red", "blue", "yellow", "green"]
        self.color = a_color[random.randint(0,len(a_color)-1)]
        self.height = random.randint(1,100)
        self.weight = random.randint(50,100)
        print_small_monster.describtion()

    def describtion(self):

        monster_de = ["This is a monster which is %d height" % self.height, "This is a monster which is %d heavy" % self.weight, "This is a %s monster." % self.color]



        a = monster_de[random.randint(0,len(monster_de)-1)]
        b = monster_de[random.randint(0,len(monster_de)-1)]
        while b == a:
            b = monster_de[random.randint(0,len(monster_de)-1)]
        c = monster_de[random.randint(0,len(monster_de)-1)]
        while c == a or c == b:
            c = monster_de[random.randint(0,len(monster_de)-1)]

        print a
        print b
        print c




class big(monster):
    def renew(self):
        a_color = ["red", "blue", "yellow"]
        self.color = a_color[random.randint(0,len(a_color)-1)]
        self.height = random.randint(1,100)
        self.weight = random.randint(1,49)
        print_big_monster.describtion()

    def describtion(self):
        monster_de = ["This is a monster which is %d height" % self.height, "This is a monster which is %d heavy" % self.weight, "This is a %s monster." % self.color]



        a = monster_de[random.randint(0,len(monster_de)-1)]
        b = monster_de[random.randint(0,len(monster_de)-1)]
        while b == a:
            b = monster_de[random.randint(0,len(monster_de)-1)]
        c = monster_de[random.randint(0,len(monster_de)-1)]
        while c == a or c == b:
            c = monster_de[random.randint(0,len(monster_de)-1)]

        print a
        print b
        print c


class engine(threading.Thread):
    def __init__ (self, score):
        self.score = score

    def generate(self):
            b_or_small=random.randint(0,1)
            if b_or_small == 0 :
                print_big_monster.renew()
                player_input = raw_input(">")
                if player_input == "kill":
                    player.dead()
                    exit(0)
                elif player_input == "catch":
                    player.catch()
                    self.score += 100
                    print "Your score: %d" % self.score
                    engine.generate()
                else:
                    print "Wrong Input!"
                    engine.generate()

            elif b_or_small == 1 :
                print_small_monster.renew()
                player_input2 = raw_input(">")
                if player_input2 == "kill":
                    player.kill()
                    self.score += 100
                    print "Your score: %d" % self.score
                    engine.generate()
                elif player_input2 == "catch":
                    player.dead()
                    exit(0)
                else:
                    print "Wrong Input!"
                    engine.generate()






class Timer(threading.Thread):
    def timer(self):
        print "Ready"
        time.sleep(1)
        print "3"
        time.sleep(1)
        print "2"
        time.sleep(1)
        print "1"
        return
    def timelimit(self):
            print"Start"
            time.sleep(60)
            print "\nTime up!"
            print "Stop typing!"
            print "Press Ctrl + c to quit the program!"
            ## Error may raise here, because one thread is still ruuning in the background
            exit(0)

class player(object):
    def dead(self):
        print "Wrong choice!"
        print "You are dead..."
        print "Please wait a bit. The game will close automatically."
        ## I know this is kind of stupid, but I have been searching for few days and still cannot figure out how to kill a thread
    def kill(self):
        print "You have killed a monster"
    def catch (self):
        print "You have caught a monster"






player = player()
print_small_monster = small()
print_big_monster = big()
engine = engine(0)
count = Timer()
