# CARDGAME
a shitty hearthstone-inspired text-based python card game


## running the game
```bash
python run.py
```
## playing the game
### beginning the game
to begin the game, each player shuffles her deck, and draws two cards. each player starts with 20 health.
### each turn
each turn has three phases - draw, play, and use.
##### draw phase
the player draws one card from her deck
##### play phase
the player plays one card from her hand. this card will not be active until the following turn.
#### use phase
the player "uses" each card in play that is active. card that are active will have a ! after their name.
after selecting a card to use, the player selects a target to attack - or, if there are no opposing cards in play, the player attacks her opponent's health directly.
### ending the game
a player loses when she has 0 health left. the game is a draw if both players have no cards left in their decks

## the interface
**example**
```
you drew a {*a.sacrificer: 4,5}
select a card to play!
you: 19 | enemy: 20

enemy's cards in play:
1 - {a.thunder: 0,1}

player's cards in play:


player's' hand:
1 - {a.stunner: 1,2}
2 - {a.defender: 0,0}
3 - {*a.sacrificer: 4,5}

play card #:
```

## card effects
### no effects
***these cards don't have any effect***
* monster

### activation effects
***these effects happen when a card is first put into play***
* **a.charger** - can attack on the same turn that it is played
* **a.damager** - deal 3 damage to the opponent's health
* **a.defender** - set this card's attack and hp equal to the number of monsters the enemy has in play
* **a.necromancer** - bring back one random monster from the discard pile
* **a.ohealer** - add 2 health to one of your monsters in play
* **a.phealer** - heal the user for 2 health
* **a.sacrificer** - you must discard two cards from your hand to play this card
* **a.spawner** - spawn one 0/1 minion
* **\*a.spawner** - spawn two 0/1 minions
* **a.stunner** - stun all opposing monsters so they cannot attack next turn
* **a.summoner** - draw one card
* **\*a.summoner** - draw two cards
* **a.thunder** - deal one damage to each opposing monster, as well as to the enemy's health
* **\*a.thunder** - deal two damage to each opposing monster, as well as to the enemy's health
* **a.upgrader** - add 1/1 to one of your monsters in play
* **\*a.weakener** - subtract one attack from each opposing monster

### use effects
***these effects happen every time a card is used to attack an opposing monster***
* **\*u.destroyer** - automatically destroy the opposing monster, but lose one health in the process
* **u.grower** - gain one attack point, then attack
* **u.silencer** - reduce the opposing monster's attack to 0

### destroy effects
***these effects happen when a card is destroyed***
* **d.bomb** - destroy all other monsters in play
