import random, cards

#these are the effects that can be passed in when creating a new card


# activation effects - these take place when the card is first put in play


#when a card with this effect is played, it forces you to discard two cards from your hand
def actSacrifice(card):
    card.g.dodiscard()
    card.g.dodiscard()


#when a card with this effect is played, two "minions" are spawned
def actSpawn(card):
    #dynamically create two new monster cards
    nc1 = cards.Monster("minion",card.g,0,1)
    nc2 = cards.Monster("minion",card.g,0,1)
    #let the player know what is happening
    print card.name + " spawned two minions"
    #put the two minions in play
    card.g.inplay.append(nc1)
    card.g.inplay.append(nc2)
    #activate thet wo minions
    nc1.activate()
    nc2.activate()
    #print the current in play list
    card.g.printinplay()

#same as above, bbut only spawns one minion
def actSpawnone(card):
    #create a new card
    nc1 = cards.Monster("minion",card.g,0,1)
    print card.name + " spawned one minion"
    #put it in play and activate it
    card.g.inplay.append(nc1)
    nc1.activate()
    card.g.printinplay()

#when a card with this effect is played, it brings back one monster from the discard pile
def actNecromance(card):
    #check to see if there are any monsters to revive
    if len(card.g.discard)<=0:
        print "there are no discarded monsters to revive"
    else:
        #pop a card from the discard pile
        nc = card.g.discard.pop()
        #rename it to show it is a ghost
        nc.name = "ghost "+ nc.name
        #give it two hp
        nc.hp=2
        #make it ready to use
        nc.used = False
        print card.name + " revives " + nc.name
        print nc + " is now in play"
        #put it in play
        card.g.inplay.append(nc)
        card.g.printinplay()
        #and activate it
        #note - this Will call activation effects, which can have some interesting chained results - a necromancer can bring back another necromancer, who will instantly bring back Another monster!
        nc.activate()

#when a card with this effect is played, the user is healed for 5 health
def actHeal2(card):
    print card.name + " heals the user for 2 health"
    #call the gamestate heal function
    card.g.heal(2)

#when a card with this effect is played, the user draws a card
def actDraw(card):
    print card.name + " causes the user to draw 1 card"
    #call the draw function of the gamestate
    card.g.draw()

#same as above, but draws two cards
def actDraw2(card):
    print card.name + " causes the user to draw 2 cards"
    #wow, such code
    card.g.draw()
    card.g.draw()

#when a card with this effect is played, the opponent loses three health
def actDmg(card):
    print card.name + " attacks the opponenet's health directly"
    #call the damage funciton of the enemy gamestate
    card.g.e.damage(3)

#when a card with this effect is played, it is marked as not yet "used" (aka ready to attack)
def actCharge(card):
    card.used = False

#when a card with this effect is played, it adds 1/1 to one allied card
def addAtkHealth(card):
    print "pick an ally to add 1/1"
    #call the gamestate function to select an ally
    nc = card.g.selectally()
    #add to the variables
    nc.atk += 1
    nc.hp += 1
    print card.name + " upgraded " + nc.name + " to " + nc

#same as above, only this adds 0/2 instead of 1/1
def addHealth(card):
    print "pick an ally to heal 2"
    nc = card.g.selectally()
    nc.hp += 2
    print card.name + " healed " + nc.name + " to " + nc

#when a card with this effect is played, all enemies (including the opponent's health) take one point of damage
def actThunder(card):
    print card.name + " damages all enemies"
    #creating a copy of the enemy's inplay list, just in case cards are damaged and removed by Thunder, we won't lose our place in the list
    ts = list(card.g.e.inplay)
    for c in ts:
        #call the card's damage function
        c.damage(1)
    #call the enemy gamestate's damage function
    card.g.e.damage(1)

#same as above, only this time it deals 2 damage instead of one
def actxThunder(card):
    print card.name + " damages all enemies"
    ts = list(card.g.e.inplay)
    for c in ts:
        c.damage(2)
    card.g.e.damage(2)

#when a card with this effect is played, all of the enemy monsters lose one attack
def actWeaken(card):
    print card.name + " weakens all opponents"
    #loop through the opponent's in-play cards
    for c in card.g.e.inplay:
        #subtract one from attack
        c.atk = c.atk - 1
        #make sure we don't get negative attack
        if c.atk <= 0:
            c.atk = 0
            c.used = True

#when a card with this effect is played, all of the enemy monsters are stunned so they can't attack the next turn
def actStunAll(card):
    print card.name + " stunns all opponents"
    #loop through enemy's cards in play
    for c in card.g.e.inplay:
        #set them all to already being used
        #since the use() period comes before the .used is reset, none of the oponnent's cards will be able to attack next turn
        c.used = True

#when a card with this effect is played, it's attack and HP are set equal to the number of monsters the enemy has in play
def actDefend(card):
    l = len(card.g.e.inplay)
    card.atk += l
    card.hp += l


#use effects - these are called when a card is "used" on a target

#this effect automatically destroys the target, but costs one health
def useDestroy(card,target):
    print card.name + " destroys " + target.name + "!"
    #damage the target card for the amount of it's own hp
    target.damage(target.hp)
    #damage the calling card for 1 hp
    card.damage(1)
    #return True that it Is a destroy, so the normal attack code isn't called
    return True

#this effect silences the target so it can no longer attack
def useSilence(card,target):
    print card.name + " silences " + target.name + "!"
    #sets the target's attack to 0
    target.atk = 0
    target.used = True
    #calls the normal attack code
    return False

#this effect causes the card to "grow" and gain one attack each turn
def useGrow(card,target):

    #increment the attack amount
    card.atk += 1
    print card + " grew and attacked " + target
    #call the normal attack code
    return False


#destroy effects - these are called when a card is destroyed / removed from play

#this effect removes all other cards from play
def desBomb(card):
    print "destroying all other cards in play"
    #loop through your cards in play
    while len(card.g.inplay) > 0:
        #pop them out of the array
        c = card.g.inplay.pop()
        print "destroying "+ c
        #call the discard effect
        c.discard()
        card.g.discard.append(c)
    #loop through the enemy's cards, do the same thing
    while len(card.g.e.inplay) > 0:
        d = card.g.e.inplay.pop()
        print "destroying "+ d
        d.discard()
        card.g.e.discard.append(d)
