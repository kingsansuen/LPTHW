from sys import exit
import time
import random
from random import randint
import threading



class mainroom(object):
    def intro(self):
        print "Please select a game:"
        print "1. Guesting Number"
        print "2. Guesting Number (versus computer version)"
        print "3. Moster Fighter"
        playerchoice = input(">")
        print "Do you need tutoial?"
        explain = raw_input(">")
        if explain == "yes":
            exroom.explain(playerchoice)
        elif explain == 'no':
            if playerchoice == 1:
                play1.playerturn()
            elif playerchoice == 2:
                play2.playerturn()
            elif playerchoice == 3:
                starteverything(True)

        else:
            print "Wrong Input!"
            return game.intro()


class exroom(object):
    def explain(self, choice):
        if choice == 1:
            print "You have to guest a number set by the computer from 1 to 100"
            print "Everytime you are wrong, the system will narrow down the range for you."
            print "You have maximum ten rounds to finish the game"
            print "Good Luck!"
            play1.playerturn()
        elif choice == 2:
            print "You will do a guesting game with the computer."
            print "There is a preset number in the computer from 1 to 100"
            print "Your mission is try not to type out that number"
            print "Either you or the computer type out the preset number will lose the game"
            print "Everytime you are not typing the preset number, the system will narrow down the range"
            print "Good Luck!"
            play2.playerturn()
        elif choice == 3:
            print "You are a monster fighter."
            print "Your only job is to focus on the weight of the monster."
            print "If the monster is heavier than 50, kill them"
            print "If the monster is lighter than 50, catch them"
            print "There will be other information that distract you."
            print "Every correct choice give you 100 marks."
            print "Wrong option will result in loosing the game."
            print "The time limit is 60 second."
            print "Good luck!"
            print "Press enter when ready."
            raw_input(">")
            starteverything(True)







class engin_num(object):
    def __init__(self):
        self.setnum = randint(1,100)
        self.playnum = None
        self.largest = 100
        self.smallest = 1
        self.correct = False

class must_not(engin_num):
    def __init__(self):
        super(must_not, self).__init__()
        self.player_round = True

    def playerturn(self):
        while (self.player_round == True):
            while (self.correct == False):
                print "Plase enter a number!"
                self.playnum = input(">")
                if self.playnum < self.smallest or self.playnum > self.largest:
                    print "Wrong Input"

                else:
                    print "Number you enter: %d" % self.playnum

                    if self.playnum > self.setnum:
                        self.largest = self.playnum
                        print "Smallest number = %d" % self.smallest
                        print "Largest number = %d" % self.largest
                        self.player_round = False
                        time.sleep(1.5)
                        play2.computerturn()


                    elif self.playnum < self.setnum:
                        self.smallest = self.playnum
                        print "Smallest number = %d" % self.smallest
                        print "Largest number = %d" % self.largest
                        self.player_round = False
                        time.sleep(1.5)
                        play2.computerturn()


                    else:
                        self.correct = True

                    if self.correct == True:
                        print "You loose!"
                        exit(0)




    def computerturn(self):
        while (self.player_round == False):
            self.playnum = randint(self.smallest,self.largest)
            print "Computer input: %d" % self.playnum

            if self.playnum > self.setnum:
                self.largest = self.playnum
                print "Smallest number = %d" % self.smallest
                print "Largest number = %d" % self.largest
                self.player_round = True
                play2.playerturn()


            elif self.playnum < self.setnum:
                self.smallest = self.playnum
                print "Smallest number = %d" % self.smallest
                print "Largest number = %d" % self.largest
                self.player_round = True
                play2.playerturn()

            else:
                self.correct = True

            if self.correct == True:
                print "You win!"
                exit(0)


class try_to_guess(engin_num):
    def __init__(self):
        super(try_to_guess, self).__init__()
        self.remain_round = 10

    def playerturn(self):
        while (self.correct == False):
            print "Plase enter a number!"
            self.playnum = input(">")
            if self.playnum < self.smallest or self.playnum > self.largest:
                print "Wrong Input"

            else:
                print "Number you enter: %d" % self.playnum

                if self.playnum > self.setnum:
                    self.largest = self.playnum
                    print "Smallest number = %d" % self.smallest
                    print "Largest number = %d" % self.largest
                    self.remain_round -= 1
                    print "Remaining round = %d" % self.remain_round



                elif self.playnum < self.setnum:
                    self.smallest = self.playnum
                    print "Smallest number = %d" % self.smallest
                    print "Largest number = %d" % self.largest
                    self.remain_round -= 1
                    print "Remaining round = %d" % self.remain_round

                else:
                    self.correct = True

        if (self.correct== True):
            print "Good job!"
            exit(0)

        if (self.remain_round==0 and self.correct == False):
            print "You lose"
            exit(0)

class monster(object):
    pass

def starteverything(ok):
    if __name__ == "__main__":
        if ok == True:
            t.begin()
            t.start()
            engine.generate(True)
        elif ok == False:
            t.stop()
            exit(0)




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


class engine(object):
    def __init__ (self, score):
        self.score = score

    def generate(self, a):
            while a == True:
                b_or_small=random.randint(0,1)
                if b_or_small == 0 :
                    print_big_monster.renew()
                    player_input = raw_input(">")
                    z = t.isAlive()
                    if z == True:
                        if player_input == "kill":
                            player.dead()
                            starteverything(False)
                        elif player_input == "catch":
                            player.catch()
                            self.score += 100
                            print "Your score: %d" % self.score
                            engine.generate(True)
                        else:
                            print "Wrong Input!"
                            engine.generate(True)

                    else:
                        exit(0)



                elif b_or_small == 1 :
                    print_small_monster.renew()
                    player_input2 = raw_input(">")
                    z = t.isAlive()
                    if z == True:
                        if player_input2 == "kill":
                            player.kill()
                            self.score += 100
                            print "Your score: %d" % self.score
                            engine.generate(True)
                        elif player_input2 == "catch":
                            player.dead()
                            starteverything(False)
                        else:
                            print "Wrong Input!"
                            engine.generate(True)

                    else:
                        exit(0)







class Timer(object):
    def timer(self):
        print "Ready"
        time.sleep(1)
        print "3"
        time.sleep(1)
        print "2"
        time.sleep(1)
        print "1"
        return

class Thread(threading.Thread):
    def begin(self):
        self.stopme = True

    def run(self):
        while self.stopme == True:
            print"Start"
            i = 0
            while i < 60:
                time.sleep(1)
                i+=1
            if i == 60:
                print "\nTimes up!"
                print "Stop typing!"
                print "Press any button to exit!"
                starteverything(False)




            ## Error may raise here, because one thread is still ruuning in the background
    def stop(self):
        self.stopme = False






class player(object):
    def dead(self):
        print "Wrong choice!"
        print "You are dead..."
    def kill(self):
        print "You have killed a monster"
    def catch (self):
        print "You have caught a monster"




player = player()
print_small_monster = small()
print_big_monster = big()
engine = engine(0)
count = Timer()
t = Thread()
t.setDaemon(True)
Begin_choice = None
game = mainroom()
play1 = try_to_guess()
play2 = must_not()
exroom = exroom()
game.intro()
