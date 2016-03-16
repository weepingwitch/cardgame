import random
import effects, cards



def standardMons(d,g):
    #dynamically generate and append some monsters with no effects
    d.append(cards.Monster("monster",g,3,3))
    d.append(cards.Monster("monster",g,4,2))
    d.append(cards.Monster("monster",g,2,4))
    d.append(cards.Monster("monster",g,3,3))
    d.append(cards.Monster("monster",g,4,2))
    d.append(cards.Monster("monster",g,2,4))
    d.append(cards.Monster("monster",g,1,5))
    d.append(cards.Monster("monster",g,5,1))


def standardEffects(d,g):
    #dynamically generate and append some activation-effect cards
    d.append(cards.Monster("a.phealer",g,1,2,effects.actHeal2))
    d.append(cards.Monster("a.stunner",g,1,2,effects.actStunAll))
    d.append(cards.Monster("a.thunder",g,0,1,effects.actThunder))
    d.append(cards.Monster("a.charger",g,1,1,effects.actCharge))
    d.append(cards.Monster("a.charger",g,1,1,effects.actCharge))
    d.append(cards.Monster("a.charger",g,1,1,effects.actCharge))


#this builds a standard deck
def genDeck(g):

    #start with an empty array
    d = []

    #put in the standard monsters
    standardMons(d,g)

    #put in the standard effects monsters
    standardEffects(d,g)



    d.append(cards.Monster("a.phealer",g,1,2,effects.actHeal2))

    d.append(cards.Monster("*a.weakener",g,1,2,effects.actWeaken))
    d.append(cards.Monster("*a.weakener",g,1,2,effects.actWeaken))
    d.append(cards.Monster("*a.weakener",g,1,2,effects.actWeaken))
    d.append(cards.Monster("*a.weakener",g,1,2,effects.actWeaken))


    d.append(cards.Monster("a.stunner",g,1,2,effects.actStunAll))
    d.append(cards.Monster("a.stunner",g,1,1,effects.actStunAll))

    d.append(cards.Monster("a.damager",g,1,2,effects.actDmg))
    d.append(cards.Monster("a.damager",g,1,2,effects.actDmg))
    d.append(cards.Monster("a.damager",g,1,2,effects.actDmg))


    d.append(cards.Monster("a.thunder",g,0,1,effects.actThunder))
    d.append(cards.Monster("a.thunder",g,0,1,effects.actThunder))
    d.append(cards.Monster("a.thunder",g,0,1,effects.actThunder))
    d.append(cards.Monster("a.thunder",g,0,1,effects.actThunder))
    d.append(cards.Monster("*a.thunder",g,0,1,effects.actxThunder))
    d.append(cards.Monster("*a.thunder",g,0,1,effects.actxThunder))



    d.append(cards.Monster("*a.charger",g,2,1,effects.actCharge))
    d.append(cards.Monster("*a.charger",g,2,1,effects.actCharge))

    d.append(cards.Monster("a.necromancer",g,1,1,effects.actNecromance))
    d.append(cards.Monster("a.necromancer",g,1,1,effects.actNecromance))
    d.append(cards.Monster("a.necromancer",g,1,2,effects.actNecromance))

    d.append(cards.Monster("*a.spawner",g,1,1,effects.actSpawn))
    d.append(cards.Monster("*a.spawner",g,1,1,effects.actSpawn))
    d.append(cards.Monster("a.spawner",g,1,1,effects.actSpawnone))
    d.append(cards.Monster("a.spawner",g,1,1,effects.actSpawnone))
    d.append(cards.Monster("a.spawner",g,1,1,effects.actSpawnone))


    d.append(cards.Monster("*a.sacrificer",g,4,5,effects.actSacrifice))
    d.append(cards.Monster("*a.sacrificer",g,4,5,effects.actSacrifice))


    d.append(cards.Monster("a.summoner",g,2,1,effects.actDraw))
    d.append(cards.Monster("a.summoner",g,1,2,effects.actDraw))
    d.append(cards.Monster("a.summoner",g,1,1,effects.actDraw))
    d.append(cards.Monster("*a.summoner",g,2,1,effects.actDraw2))
    d.append(cards.Monster("*a.summoner",g,1,2,effects.actDraw2))

    d.append(cards.Monster("*a.upgrader",g,2,1,effects.addAtkHealth))
    d.append(cards.Monster("*a.upgrader",g,1,2,effects.addAtkHealth))
    d.append(cards.Monster("*a.upgrader",g,1,1,effects.addAtkHealth))

    d.append(cards.Monster("*a.ohealer",g,1,2,effects.addHealth))
    d.append(cards.Monster("*a.ohealer",g,1,2,effects.addHealth))
    d.append(cards.Monster("*a.ohealer",g,2,1,effects.addHealth))
    d.append(cards.Monster("*a.ohealer",g,1,2,effects.addHealth))
    d.append(cards.Monster("*a.ohealer",g,1,2,effects.addHealth))
    d.append(cards.Monster("*a.ohealer",g,2,1,effects.addHealth))



    #dynamically generate and append some use effect monsters
    d.append(cards.Monster("*u.destroyer",g,0,2,cards.Card.activate,effects.useDestroy))
    d.append(cards.Monster("*u.destroyer",g,0,2,cards.Card.activate,effects.useDestroy))

    d.append(cards.Monster("u.grower",g,1,2,cards.Card.activate,effects.useGrow))
    d.append(cards.Monster("u.grower",g,1,2,cards.Card.activate,effects.useGrow))

    d.append(cards.Monster("u.silencer",g,0,1,cards.Card.activate,effects.useSilence))
    d.append(cards.Monster("u.silencer",g,0,1,cards.Card.activate,effects.useSilence))

    #dynamically generate and append some destroy effect monsters
    d.append(cards.Monster("d.bomb",g,1,2,cards.Card.activate,cards.Card.use,effects.desBomb))
    d.append(cards.Monster("d.bomb",g,1,2,cards.Card.activate,cards.Card.use,effects.desBomb))
    d.append(cards.Monster("d.bomb",g,1,2,cards.Card.activate,cards.Card.use,effects.desBomb))

    #return the generated deck
    return d
