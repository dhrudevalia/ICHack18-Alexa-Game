import game
from world import initTotalItems, initCreatures, initWeapons
from world import noWeapon
import move
import random


def checkAction(verb, noun, player):
    if(verb in noun.useActions):
        doAction(verb, noun, player)
        
def eat(verb, consumable, player):
    player.consumeConsumables(consumable)
    return "You "+ verb + " the " + consumable.getName() + " for " + str(consumable.hp) + ", current health is " + str(player.getHealth())
def doAction(verb, noun, player):
    currentRoom = player.getRoom()
    if (assignItem(noun)):
        if(verb == "break"):
            player.removeItem(noun)
    
        elif(verb == "climb"):
            if(currentRoom.getLocation() == [1,1,0]):
                player.addItem(rope)
                return "you look around. In the distance you can see a forest and mountains. On one of the tree's many branches you find a rope, which you use to climb back down."
    
        elif(verb == "cut"):
            return("cut with what dumbass")
    
        elif(verb == "drink" or verb == "eat"):
            return eat(verb, obj, player)
    
        elif(verb == "read"):
            return noun.getDescription()
        elif(verb == "search" or verb == "examine"):
            if noun == "car":
                return "inside the car you can see an amazon echo."
            elif noun == "shelves":
                return "while rumaging through the shelves you see a handy torch"
            elif noun == "desk":
                return "there is a computer on the desk."
            elif noun == "hollowed_tree":
                return "inside the hollowed tree you can see a pair of climbing shoes."
            elif noun == "rock":
                return "you push over the rock and find a in tact rifle"
            elif noun == "body":
                if currentRoom.location == [0,2,0]:
                    return "on the body you can see a coat and some medicine."
                elif currentRoom.location == [2,4,0]:
                    return "on the body you can see a piece of paper."
                elif currentRoom.location == [3,6,0]:
                    return "on the body you can see a kindle and some chocolate."
            else:
                return noun.getDescription()
        elif(verb == "take" or verb == "get"):
            if (currentRoom.hasItem(noun)):
                player.addItem(currentRoom.takeItem(noun))
                return "You took the "+noun
            else:
                return "No "+noun+" in here"
        elif(verb == "throw" or verb == "drop"):
            if (player.hasItem(noun)):
                currentRoom.dropItem(player.dropItem(noun))
                return "You dropped your "+noun
            else:
                return "Can't drop a "+noun+" you don't have idiot"
        elif(verb == "move" or verb == "go" or verb == "slide" or verb == "walk"):
            return move.initMove(noun, game.rooms, player.getRoom(), player)
    elif(verb == "look"):
        return player.getRoom().getDescription()
    
    elif (verb == "move" or verb == "go" or verb == "slide" or verb == "walk"):
        return move.initMove(noun, game.rooms, player.getRoom(), player)
        
    elif(verb == "attack" or verb == "strike" or verb == "hit" or verb == "kick"):
        return doActionFight(verb, noun, noWeapon, player )
    
    else:
        
        return False

    
            
def doActionFight(verb, creature, weapon, player):
    for creatures in initCreatures:
        if(creature == creatures.getName()):
            for w in initWeapons:
                if (w.name == weapon):
                    weapon = w
            maxdmg = weapon.getDmg()
            print(maxdmg)
            r = random.randint(0, 3)
            if r == 3: # miss
                return [maxdmg, 0, "miss"]
            elif r == 2: #glancing blow
                return [0, maxdmg/2, "glancing blow"]
            else: # direct hit
                return [0, maxdmg, "direct hit"]
                 
    return "Can't" + verb + creature.getName()
                                                                        
        
def assignItem(noun):
    for item in initTotalItems:
        if(noun == item.getName()):
            global obj
            obj = item
            return True
    return False
    
    