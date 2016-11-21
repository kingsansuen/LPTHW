from sys import exit
import time
import ex45_b
import random
from random import randint
from threading import Thread
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
                ex45_b.count.timer()
                t1 = Thread(target=ex45_b.count.timelimit)
                t2 = Thread(target=ex45_b.engine.generate)
                t1.start()
                t2.start()
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
            ex45_b.count.timer()
            t1 = Thread(target=ex45_b.count.timelimit)
            t2 = Thread(target=ex45_b.engine.generate)
            t1.start()
            t2.start()







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




Begin_choice = None
game = mainroom()
play1 = try_to_guess()
play2 = must_not()
exroom = exroom()
game.intro()
