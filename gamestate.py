import random, enemy
import cards
import sys

#this is the gamestate object, used to keep track of your cards / hp / etc.
class GameState(object):
    #constructor
    def __init__(self, nm="player"):
        #set the hp and max hp
        self.hp = 20
        self.mhp = 20
        #create arrays for deck, hand, inplay, and discard
        self.deck = []
        self.hand = []
        self.inplay = []
        self.discard = []
        #create an enemy gamestate
        self.e = enemy.Enemy(self)
        self.name = nm

    #heals you for a certain amount
    def heal(self, amt):
        #increment the health
        self.hp += amt
        #make sure the health doesn't go over the max health
        if self.hp > self.mhp:
            self.hp = self.mhp
        #print out your health
        print self.name + "'s health: " + str(self.hp)  +"/"+ str(self.mhp)

    #shuffles your deck
    def shuffle(self):
        random.shuffle(self.deck)

    #draw a card
    def draw(self, silent=False):
        #see if there are cards left to draw
        if len(self.deck) <= 0:
            print "you don't have any more cards to draw!"
        else:
            #pop a card from the deck, add it to the hand
            nc = self.deck.pop()
            self.hand.append(nc)
            #let you know what card you drew
            if not silent:
                print "you drew a " + nc

    #called when you need to pick a card to discard
    def dodiscard(self):
        #see if you have any cards in your hand
        if len(self.hand)<=0:
            print "you don't have any cards to discard!"
        else:
            #input loop
            waiting = True
            while waiting:

                print "select a card to discard!"

                self.printhand()
                #take in player input
                pin = raw_input("discard card #: ")
                #check for quit
                if pin == "q":
                    sys.exit("quit")
                try:
                    #see if the input is a number
                    pnum = int(pin) - 1
                    #see if the input is in range
                    if (pnum >= 0) and (pnum < len(self.hand)):
                        print "-----------------------********************-----------------------"
                        #pop and discard the card
                        nc = self.hand[pnum]
                        self.hand.remove(self.hand[pnum])
                        print nc + " is now discarded"
                        self.discard.append(nc)
                        waiting = False
                    else:
                        print "that wasn't in range!"

                except ValueError:
                    print "that's not a number!"

    #deals an amount of damage to your health
    def damage(self, amt):
        #subtract the amount
        self.hp -= amt
        print self.name + "'s health: " + str(self.hp)  +"/"+ str(self.mhp)
        #check to see if the enemy has won
        if self.hp <= 0:
            print self.name + " LOSES!"
            sys.exit("game over")

    #print out the cards in your hand
    def printhand(self):
        print ""
        print "your hand:"
        #number them
        for i in xrange(len(self.hand)):
            print str(i+1) + " - " + self.hand[i]
        print ""

    #print out the cards you have in play
    def printinplay(self):
        print ""
        print self.name + "'s cards in play:"
        #number them
        for i in xrange(len(self.inplay)):
            s = ""
            c = self.inplay[i]
            if c.used == False:
                s = " !"
            print str(i+1)+ " - " + c + s

        print ""

    #pick a card to play from your hand
    def playcard(self):
        #input loop
        waiting = True
        while waiting:
            #output the relevant info
            print "select a card to play!"
            print "you: " + str(self.hp) + " | enemy: " + str(self.e.hp)
            self.e.printinplay()
            self.printinplay()
            self.printhand()
            #take in player input
            pin = raw_input("play card #: ")
            #check for quit
            if pin == "q":
                sys.exit("quit")
            try:
                #try casting to an int
                pnum = int(pin) - 1
                #check if in range
                if (pnum >= 0) and (pnum < len(self.hand)):
                    print "-----------------------********************-----------------------"
                    #remove the card from the hand
                    nc = self.hand[pnum]
                    self.hand.remove(self.hand[pnum])
                    print nc + " is now in play"
                    #put it in play
                    self.inplay.append(nc)
                    #self.printinplay()
                    #activate it
                    nc.activate()
                    waiting = False
                else:
                    print "that wasn't in range!"

            except ValueError:
                print "that's not a number!"

    #this funcion is called once each turn to use cards in play
    def usecards(self):
        #check to see if there are any cards that can be used
        canplay = False
        #loop through and look for unused cards
        for x in self.inplay:
            if x.used == False and (x.atk >0 or x.us != cards.Card.use):
                canplay = True
        while canplay:

            print "select a card to use!"
            self.e.printinplay()
            #call the function to select a card in play
            c = self.selectcardinplay()
            c.used = True
            #call the functioin to select a target
            t = self.selecttarget()
            #see if the enemy has a card to target
            if t != False:
                #if so, use the card
                c.use(t)
            else:
                print "enemy has no cards in play, you attack enemy directly"
                self.e.damage(c.atk)
            #see whether you can still play
            canplay = False
            #loop through and check for unused cards
            for x in self.inplay:
                if x.used == False:
                    canplay = True


    #used when picking an ally card to updgrade/heal
    def selectally(self):
        #input loop
        waiting = True
        while waiting:
            self.printinplay()
            #get user input
            pin = raw_input("target card #: ")
            #check for quit
            if pin == "q":
                sys.exit("quit")
            try:
                #try casting as int
                pnum = int(pin) - 1
                #check if in range
                if (pnum >= 0) and (pnum < len(self.inplay)):
                    nc = self.inplay[pnum]
                    print "-----------------------********************-----------------------"
                    waiting = False
                    #return the card
                    return nc

                else:
                    print "that wasn't in range!"

            except ValueError:
                print "that's not a number!"

    #used to select which card to use
    def selectcardinplay(self):
        waiting = True
        #input loop
        while waiting:
            self.printinplay()
            #get user input
            pin = raw_input("use card #: ")
            #check for quit
            if pin == "q":
                sys.exit("quit")
            try:
                #try casting as int
                pnum = int(pin) - 1
                #check if it's in range
                if (pnum >= 0) and (pnum < len(self.inplay)):
                    nc = self.inplay[pnum]
                    if nc.used == False:
                        print "-----------------------********************-----------------------"
                        waiting = False
                        #return the card
                        return nc
                    else:
                        print "that card has already been used this turn!"

                else:
                    print "that wasn't in range!"

            except ValueError:
                print "that's not a number!"

    #used to select which enemy card to target
    def selecttarget(self):
        #check to see if the enemy even has cards to play
        if len(self.e.inplay) == 0:
            return False
        else:
            #if so, go into input loop
            waiting = True
            while waiting:
                self.e.printinplay()
                #get user input
                pin = raw_input("select target #: ")
                #check for quit
                if pin == "q":
                    sys.exit("quit")
                try:
                    #try casting as int
                    pnum = int(pin) - 1
                    #check if it's in range
                    if (pnum >= 0) and (pnum < len(self.e.inplay)):
                        print "-----------------------********************-----------------------"
                        nc = self.e.inplay[pnum]
                        #return the card
                        waiting = False
                        return nc

                    else:
                        print "that wasn't in range!"

                except ValueError:
                    print "that's not a number!"
