from sys import exit
from random import randint


def start():
    print "You are in a forest and cannot find your way out."
    print "You can choose to walk foward or go around the forest"
    print "What will you do? (Walk forward or Go around)"

    Direction = raw_input(">")
    if Direction == "Walk forward":
        savior()
    elif Direction == "Go around":
        trap()
    else:
        print"Maybe you are a bit confuse."
        print "Let's try again."
        return start()



def savior():
    print "You find yourself in a control room of a train station."
    print "In front of you is 2 rail tracks"
    print "On one of the rail tracks, there are five people laying with their hands and legs tied."
    print "On the other track, there is only one man which is also laying with his hands and legs tied."
    print "press ENTER to continue..."

    raw_input(">")

    print "A train is coming..."
    print "It is going to the direction where 5 men is laying."
    print "A controller is in front of you."
    print "You can change the direction of the train such that it will go towards the track which has one man laying on top."
    print "That man will be killed."
    print "Or you can ignore everything and five people will die."
    decision_making()


def decision_making():
    print "What will you do? (Change the direction or Ignore)"

    Save = raw_input(">")

    if Save == "Change the direction":
        print "Saving five people by killing one guy?"
        print "Are you sure? (Yes or No)"
        sure = raw_input(">")

        if sure == "Yes":
            print "Interesting choice."
            print "Will you consider your self as a hero then? (Yes or No)"
            hero = raw_input(">")

            if hero == "Yes":
                print "You have killed someone to save someone."
                print "And you are claming that live itself has a value."
                print "5 people is more valuable then 1 guy."
                print "If that is what a hero would think..."
                exit(0)

            elif hero == "No":
                print "You have killed someone and have saved someone at the same time"
                print "Are you a murderer? Are you a savior?"
                print "Who knows?"
                exit(0)

            else:
                print"Maybe you are a bit confuse."
                print "Let's try again."
                return decision_making()

        elif sure == "No":
            return decision_making()

        else:
            print"Maybe you are a bit confuse."
            print "Let's try again."
            return decision_making()

    elif  Save == "Ignore":
        print "5 people die in front of you!"
        print "The man that has 'saved' by you eventually suffered from a serious heart attack by watching this."
        print "No one survive..."
        print "Will you consider yourself as a murderer? (Yes or No)"
        murderer = raw_input(">")

        if murderer == "Yes" or murderer == "No":
            print ("Why?")
            reason = raw_input(">")
            print "%s is your answer." % reason
            print "You may have your reason."
            print "But the fact is that 6 people die because of this decision."
            print "No matter what you say, they are dead..."
            exit(0)

        else:
            print"Maybe you are a bit confuse."
            print "Let's try again."
            return decision_making()

    else:
        print"Maybe you are a bit confuse."
        print "Let's try again."
        return decision_making()





def trap():
    print "You fall in to a trap..."
    print "press Enter to continue..."

    raw_input(">")

    print "You find yourself laying on a rail track"
    print "Your hands and legs are tied so you can hardly move."
    print "There is another rail track next to you."
    print "On the other track, there are five man which are in the same situation."
    print "press Enter to continue..."

    raw_input(">")

    print "You can hear that a train is coming in your direction."
    print "You see a stranger in the control station."
    print "Will you try to shout for help? (Yes or No)"

    decision = raw_input(">")

    if decision == "Yes":
        print "The stranger told you that he can either save you or those 5 people."
        print "Will you sacrifice your life or you will try to persuade that stranger to save you?"
        print "What will you do? (Sacrifice or Persuade)"

        Stranger = raw_input(">")

        if Stranger == "Sacrifice":
            die()

        elif Stranger == "Persuade":
            print "What will you say?"
            Content = raw_input(">")
            special(Content)
        else:
            print"Maybe you are a bit confuse."
            print "Let's try again."
            return trap()

    elif decision == "No":
        print "Seriously?"
        print "Without even trying?"
        print "Well, you deserve to die."
        exit(0)

    else:
        print"Maybe you are a bit confuse."
        print "Let's try again."
        return trap()

def die():
    print "You would rather sacrifice your own life?"
    print "Interesting!"
    print "Is it stupid or noble? Who knows?"
    exit(0)

def special(comment2):
    print comment2 , "is what you are going to say."
    print "But will that save your life?"
    print "press Enter to continue..."
    raw_input(">")
    num = randint(0,9)
    if num > 5:
        print "Not likely! Good bye .."
    else:
        print "Well, you have made your point"
        print "You survive!"
        print "But the 5 men beside you..."
    exit(0)

start()
