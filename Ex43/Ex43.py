from sys import exit
from random import randint


class Scene(object):
    def enter(self):
        print "This scene is not yet configured. Subclass it and impement enter()."
        exit(1)


class Engine(object):
    def __init__(self, scene_map):
        self.scene_map = scene_map


    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finshed')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        current_scene.enter()

class Death(Scene):

    quips = [ "You died. You kinda suck", "Your mom", "Loser","Small puppy"]
    def enter(self):
        print Death.quips[randint(0,len(self.quips)-1)]
        exit(1)


class CentralCorridor(Scene):
    def enter(self):
        print "shoot"
        print "dodge"
        print "tell a joke"

        action = raw_input(">")

        if action == "shoot":
            print "shooted"
            return 'death'
        elif action == "dodge":
            print "dodged"
            return 'death'
        elif action == "tell a joke":
            print "told"
            return 'GGWP'
        else:
            print "DOES NOT COMPUTE!"
            return 'central_corridor'


class LaserWeaponArmory(Scene):
    def enter(self):
        print "Get a bomb"
        code = "%d%d%d" %(randit(1,9),randint(1,9),randint(1,9))
        guess = raw_input("[keypad]>")
        guesses = 0

        while guess != code and guesses < 10:
            print "BZ!"
            guesses += 1
            guess = raw_input("[keypad]>")

        if guess == code:
            print "Bridge"
            return'the_bridge'
        else:
            print "Blow up"
            return 'death'




class TheBridge(Scene):
    def enter(self):
        print "You don't want to set it off."

        action = raw_input(">")

        if action == "throw the bomb":
            print "Stupid?"
            return 'death'

        elif action == "place the bomb":
            print "GGWP"
            return ' escape_pod'
        else:
            print "Does not compute!"
            return "the_bridge"

class EscapePod(Scene):
    def enter(self):
        print "5 pods, which one do you take?"
        good_pod = randit(1,5)
        guess = raw_input("[pod #]>")

        if int(guess) != good_pod:
            print "stupid?"
            return 'death'
        else:
            print "GGWP"
            print "You won!"
            return 'finished'

class Finished(Scene):
    def enter(self):
        print "You won! Good job."
        return 'finished'


class Map(object):

    scenes = {
    'central_corridor': CentralCorridor(),
    'laser_weapon_armory' : LaserWeaponArmory(),
    'the_bridge': TheBridge(),
    'escape_pod': EscapePod(),
    'death' : Death(),
    'finished' : Finished(),
    }
    def __init__(self,start_scene):
        self.start_scene = start_scene
    def next_scene(self, scene_name):
        val= Map.scenes.get(scene_name)
        return val
    def opening_scene(self):
        return self.next_scene(self .start_scene)


def next_scene(self, scene_name):
    val = Map.scenes.get(scene_name)
    return val

def opening_scene(self):
    return self.next_scene(self.start_scene)

a_map=Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
