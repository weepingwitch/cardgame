import gamestate
import stddeck
import sys, os
import cards

#initialize the two decks
def initdecks(g):
    #call the deck generator, assign it to the gamestate
    g.deck = stddeck.genDeck(g)
    #shuffle the deck
    g.shuffle()
    #do the same for the enemy's deck
    g.e.deck = stddeck.genDeck(g.e)
    g.e.shuffle()

#to start the game, both players draw two cards
def inithands(g):
    #just calling the gamestate's draw function twice
    g.draw(True)
    g.draw(True)
    #and then doing the same thing for the enemy's gamestate
    g.e.draw(True)
    g.e.draw(True)

#reset the .used on all of the cards at the end of the turn
def resetturn(g):
    for x in g.inplay:
        if x.atk == 0 and x.us == cards.Card.use:
            #print x + " can't attack this turn, wasn't reset"
            x.used = True
        else:
            #print x + " was reset"
            x.used = False


#this is the code for doing one turn
def doTurn(g, mplay=False):
    #if we're doing a multiplayer match, change turns / clear the screen

    print ""
    print "--"
    #have the enemy draw a card
    g.e.draw()
    #have the enemy play a card
    g.e.playcard()
    #have the enemy use cards
    g.e.usecards()
    #reset the .used on all enemy cards
    resetturn(g.e)
    #if we're doing a multiplayer match, change turns / clear the screen
    if mplay:
        changeturns(g)
    print ""
    print "--"
    #have you draw a card
    g.draw()
    #have you play a card
    g.playcard()
    #have you use your cards
    g.usecards()
    #reset the .used on all your cards
    resetturn(g)
    if mplay:
        changeturns(g.e)

#used to clear the screen during multiplayer
def changeturns(p):
    i = raw_input("Press Enter to end your turn")
    #call the system clearscreen command
    # IMPORTANT NOTE - IF YOU ARE ON WINDOWS, CHANGE TO:
    # os.system('cls')
    os.system('clear')
    print p.name + "'s turn"
    i = raw_input("Press Enter to Continue")


#for when you want to play against another real person
def multiplayer():
    #create two player gamestates
    p1n = raw_input("Player 1's name? ")
    p2n = raw_input("Player 2's name? ")
    p1 = gamestate.GameState(p1n)
    p2 = gamestate.GameState(p2n)
    #set them as eachother's enemies
    p1.e = p2
    p2.e = p1
    #initialize the decks and hands
    initdecks(p1)
    inithands(p1)
    os.system('clear')
    i = raw_input("Press Enter to begin " + p1n + "'s turn")
    #main game loop
    gameRunning = True
    while gameRunning:
        #do the turns
        doTurn(p2, True)
        #check to see if both players have run out of cards
        if len(p1.deck)<=0 and len(p2.deck)<=0:
            #if so, it's a draw
            print "DRAW"
            sys.exit("DRAW")

#for when you want to play against the computer
def singleplayer():
    #create a gamestate object to hold variables and things
    g = gamestate.GameState()

    #initialzie the decks
    initdecks(g)
    #initialize the hands
    inithands(g)

    #aaand the main game loop
    gameRunning = True
    while gameRunning:
        #do the turns
        doTurn(g, False)
        #check to see if both players have run out of cards
        if len(g.deck)<=0 and len(g.e.deck)<=0:
            #if so, it's a draw
            print "DRAW"
            sys.exit("DRAW")


# when the script is called, this is what runs
if __name__ == '__main__':
    print ""
    print "-----------------------"

    multiplayer()
