import random


#card parent object
# never really used directly
class Card(object):

    #constructor, takes a reference to the gamestate object as an argument
    def __init__(self, gs):
        self.inPlay = False

        #self.used determins whether a card has been "used" during a turn or not yet
        #cards are marked as "used" when they are first in play, and aren't reset until the end of the turn, so that they can't attack on their first turn
        self.used = True

        #reference to the gamestate
        self.g = gs

        self.name = "unnamed card"
        #print self.name + " has been created"

    #overriding string method
    def __str__(self):
        return self.name

    #overriding add methods so you can add it to a string for easy printing
    def __add__(self, other):
        return str(self) + other

    #overriding add methods so you can add it to a string for easy printing
    def __radd__(self, other):
        return other + str(self)


    #and now for the card effects
    #these can be overridden by individual effect monsters

    #default activate effect
    def activate(self):
        self.inPlay = True
        return False

    #default use effect - does nothings
    def use(self, target):
        return False

    #default discard effect
    def discard(self):
        self.inPlay = False
        print self.name + " is no longer in play"
        return False



#the Monster class, which is a child of the Card class
#this contains the more specific implimentation of a monster
#as of right now, all cards are Monsters, but i might add in other children later (spell cards, etc.)
class Monster(Card):

    #constructor, takes in as arguments: name, gamestate, attack, hp, and then three optional effects (activate, use, destroy)
    def __init__(self, nn, gs, natk=1, nhp=1, nact=Card.activate, nut=Card.use, ndis=Card.discard):
        #call the parent constructor
        super(Monster, self).__init__(gs)
        #set the card's name, attck, hp, and effects
        self.name = nn
        self.atk = natk
        self.hp = nhp
        #assign the functions that get called if an effect is activated
        self.act = nact
        self.us = nut
        self.dis = ndis

    #overriding str() to display name, atk, and hp
    def __str__(self):
        s = "{"+ self.name + ": " + str(self.atk) + "," + str(self.hp) + "}"
        return s

    #this function damages the card for a certain amount
    #this is used when a card is attacked, or damaged by an effect
    def damage(self, amt):
        #subtract the amount from hp
        self.hp -= amt
        #check to see if the card is destroyed
        if self.hp <= 0:
            print self + " was destroyed"
            #sometimes card effects can chain on eachother, so it might get ~destroyed~ twice, which is why we only Try to remove it from play
            try:
                #remove card from inplay
                 self.g.inplay.remove(self)
            except:
                 pass
            #move it to the discard pile
            self.g.discard.append(self)
            #call the discard effect
            self.discard()

    #when the card is activated
    def activate(self):
        print ""
        #call the function that was passed in as activation effect
        self.act(self)

    #when the card is "used"
    def use(self, target):
        #call the function that was passed in as use effect, check to see if it destroyed the other card
        destroyeffect = self.us(self, target)
        #if the other card was not Destroyed by an effect, damage it for attack
        if not destroyeffect:
            print self + " attacks " + target
            target.damage(self.atk)
        return destroyeffect

    #when the card is discarded
    def discard(self):
        #call the funciton that was passed in as discard effect
        self.dis(self)
