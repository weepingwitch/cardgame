import random
import sys


#this is the enemy gamestate object, used to keep track of the enemy's cards / hp / etc.
class Enemy(object):
    #constructor function - takes in the player's gamestate as an argument
    def __init__(self,pgs):
        #set the hp and max hp
        self.hp = 20
        self.mhp = 20
        #create arrays for deck, hand, inplay, and dscard
        self.deck = []
        self.hand = []
        self.inplay = []
        self.discard = []
        #set the "enemy" to the player's gamestate (so cards can reference it)
        self.e = pgs
        self.name = "enemy"

    #heals the enemy for a certain amount
    def heal(self, amt):
        #increment the health
        self.hp += amt
        #make sure the health doesn't go over the max health
        if self.hp > self.mhp:
            self.hp = self.mhp
        #print out the enemy's health
        print "enemy health: " + str(self.hp)  +"/"+ str(self.mhp)

    #shuffle the enemy's deck
    def shuffle(self):
        #yay random.shuffle
        random.shuffle(self.deck)

    #draw a card
    def draw(self, silent=False):
        #make sure there are cards left to draw
        if len(self.deck) <= 0:
            print "enemy doesn't have any more cards to draw!"
        else:
            #pop a card from te deck, add it to the hand
            nc = self.deck.pop()
            self.hand.append(nc)
            if not silent:
                print "enemy drew a card"

    #for when the enemy needs to discard a card
    def dodiscard(self):
        #check to see if there are enough cards to discard
        if len(self.hand)<=0:
            print "enemy doesn't have any cards to discard!"
        else:

            print "enemy discards a card"
            #discard the last card in the hand
            nc = self.hand.pop()
            self.discard.append(nc)
            #note - this does Not call the discard effect (of a bomb, for instance).

    #deals an amount of damage to the enemy's health
    def damage(self, amt):
        #subtract the amount
        self.hp -= amt
        print "enemy health: " + str(self.hp)  +"/"+ str(self.mhp)
        #check to see if enemy has gone below 0, if so, you win!
        if self.hp <= 0:
            print "YOU WIN!"
            sys.exit("YOU WIN")

    #prints out the enemy's current cards in play
    def printinplay(self):
        print ""
        print "enemy's cards in play:"
        #number them
        for i in xrange(len(self.inplay)):
            print str(i+1)+ " - " + self.inplay[i]

    #the code that detemines how the AI picks a card to play
    def playcard(self):
        found = False
        #first, see if there are any cards with a * in the name (as these are usually the strongest)
        for c in self.hand:
            if found == False and "*" in c.name:
                self.hand.remove(c)
                nc = c
                found = True
        #if not, check to see if there are any cards with a "d" in the name (catches d.bomb, and a.thunder)
        for c in self.hand:
            if found == False and "d" in c.name:
                self.hand.remove(c)
                nc = c
                found = True
        #if not, see if there are any with a "w" in the name (catches a.weakeaner, a.spawner)
        for c in self.hand:
            if found == False and "w" in c.name:
                self.hand.remove(c)
                nc = c
                found = True
        #if we still haven't found a ~good~ card, just play a random card
        if not found:
            #shuffle the hand,
            random.shuffle(self.hand)
            #and pop the top card
            nc = self.hand.pop()
        #let the player know
        print "enemy plays " + nc
        #put it in play and activate it
        self.inplay.append(nc)
        nc.activate()

    #when the enemy needs to use their cards
    def usecards(self):
        #check to see whether there are any cards in play to use
        if len(self.inplay) == 0:
            print "enemy has no cards to use!"
        else:
            #loop through the cards in play
            for c in self.inplay:
                #if it hasn't been used yet, use it
                if c.used == False:
                    #mark it as used
                    c.used = True
                    #generate a target
                    t = self.selecttarget()
                    #if there are no cards for enemy to attack,
                    if t == False:
                        print "you have no cards in play, enemy attacks you directly"
                        #directly damage your health
                        self.e.damage(c.atk)
                    else:
                        #otherwise,
                        print ""
                        print "enemey attacks!"
                        #use the card on the target
                        c.use(t)

    #randomly picks a card in play on the enemy's side
    def selectcardinplay(self):
        nc = random.choice(self.inplay)
        return nc

    #used to select an ally card for enemy to upgrade/heal
    def selectally(self):
        return self.selectcardinplay()

    #used to select a target card for enemy to attack
    def selecttarget(self):
        #if you have no cards in play, return False
        if len(self.e.inplay) <= 0:

            return False
        else:
            #else, randomly pick one of your cards
            tc = random.choice(self.e.inplay)
            return tc
