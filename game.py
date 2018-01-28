#
#                    MADE BY 
#      SAM LIEM, MAX TAYLOR-DAVIES, AND DHRU DEVALIA
#                DURING ICHACK 2018
#           RIP NGE, "WITH WHAT", and D D 

from weather import Weather
from classes import Item, Weapon, Food, Room, Player, Creature
from world import initRooms
import move
import action
import random

import pickle
import os
import boto

s3 = boto.s3.connect_to_region(
                    "eu-west-2",
                    aws_access_key_id="AKIAJYRKSTJ42QFU524Q",
                    aws_secret_access_key="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"
                )
bucket = s3.get_bucket('ichackgame', validate=False)
key = bucket.new_key('save.dat')

# Insert soundEffect_gunshotPistol or another sfx into toSay string when needed
# can put multiple if wanted
soundEffect_gunshotPistol = '<audio src="https://s3.eu-west-2.amazonaws.com/ichackgame/pistol.mp3"/>'
soundEffect_gunshotRifle = '<audio src="https://s3.eu-west-2.amazonaws.com/ichackgame/rifle.mp3"/>'
soundEffect_jungle = '<audio src="https://s3.eu-west-2.amazonaws.com/ichackgame/jungle.mp3"/>'
soundEffect_eat = '<audio src="https://s3.eu-west-2.amazonaws.com/ichackgame/eat.mp3"/>'
soundEffect_city = '<audio src="https://s3.eu-west-2.amazonaws.com/ichackgame/city.mp3"/>'
soundEffect_punch = '<audio src="https://s3.eu-west-2.amazonaws.com/ichackgame/punch.mp3"/>'
soundEffect_throw = '<audio src="https://s3.eu-west-2.amazonaws.com/ichackgame/throw.mp3"/>'
soundEffect_hmm = '<audio src="https://s3.eu-west-2.amazonaws.com/ichackgame/hmm.mp3"/>'
soundEffect_shatter = '<audio src="https://s3.eu-west-2.amazonaws.com/ichackgame/shatter.mp3"/>'
soundEffect_jeff = '<audio src="https://s3.eu-west-2.amazonaws.com/ichackgame/jeff.mp3"/>' # MY NAME JEFF

# -- Save functions --
def save():
    key.set_contents_from_string(pickle.dumps([player, rooms, weather ]))

def load():
    p, rs, w = pickle.loads(key.get_contents_as_string())
    global player 
    player = p
    global rooms 
    rooms = rs
    global weather
    weather = w

# -- Game functions
def getInventory():
    if player is not None:
        return [item.getName() for item in player.getInv()]
    else:
        return None

def getRoomWithCoords(coords):
    for room in rooms:
        if (room.location == coords):
            return room
    return None

def play(slots, new=False, token="", deviceId=""):
    toSay = ""
    finish = False
    if (new):
        currentRoom = initRooms[0]
        global player
        player = Player("fuckboi",[],100,currentRoom)
        global rooms 
        rooms = initRooms
        global weather
        weather = Weather(token, deviceId)
        global mutant
        mutant = 0
        toSay = currentRoom.description
        if len(currentRoom.creatures) != 0:
            mutant = currentRoom.creatures[0]
            toSay += " " + mutant.description
            
        save()
        
        return toSay
    else:
        load()
        currentRoom = player.getRoom()
        newRoom = ""
        roomItems = currentRoom.getItems()
        
        if all ("value" in slots[key] for key in ("AVerb","BNoun","CUsing","DNoun")):
            values = {}
            toSay = ""
            
            for key in ("AVerb","BNoun","CUsing","DNoun"):
                values[key] = slots[key]['value']

            resStr = ""
            isDead = False
            a = action.doActionFight(values['AVerb'], values['BNoun'], values['DNoun'], player)
            playerAttk = a[1]
            creatureAttk = a[0]
            attkType = a[2]
            
            mutant = currentRoom.creatures[0]
            player.health = player.health - creatureAttk
            resStr = mutant.name + " hit for " + str(creatureAttk)  + " . And has " + str(mutant.health) + " health points remaining."
            if (player.getHealth() > 0):
                mutant.health = mutant.health - playerAttk
                resStr += " . " + player.name + " fought back with a " + attkType + " for " + str(playerAttk) + " damage"
                if (mutant.health < 0):
                    resStr += " and killed it!"
                    currentRoom.creatures = []
            else:
                isDead = True
                resStr += "You died"
            save()
                
            return {"toSay":resStr,"finish":isDead}
            
            # if (len(player.getInv) == 0) or (player.hasItem(DNoun)):
            #     toSay = "You don't have a %(BNoun)s" % values
            # elif (not currentRoom.hasItem(values['DNoun'])): # check if thing in room
            #     toSay = "%(BNoun)s is not in here to %(AVerb)s" % values
            # else:
            #     a = action.doActionFight(values['AVerb'], values['BNoun'], values['DNoun'], player)
            #     res = hits(a[0],a[1],a[2])
            #     save()
            #     return res
                #toSay = "You %(AVerb)s %(BNoun)s with %(DNoun)s" % values

            # You went up into tree
        elif all ("value" in slots[key] for key in ("AVerb","BNoun","CLoc","DNoun")):
            values = {}
            
            for key in ("AVerb","BNoun","CLoc","DNoun"):
                values[key] = slots[key]['value']
            
            if (not currentRoom.hasItem(values['DNoun'])): # check if thing in room
                toSay = "%(BNoun)s is not here!" % values
            else:
                # temp
                flag = False
                
                # Check if possible
                
                #else
                toSay = "You can't %(AVerb)s %(BNoun)s %(CLoc)s %(DNoun)s" % values
                toSay += ""
                # GAME LOGIC
                # res  = currentRoom.quarternaryCommand()
            
        elif all ("value" in slots[key] for key in ("AVerb","BSwitch","CNoun")):
            values = {}
            
            for key in ("AVerb","BSwitch","CNoun"):
                values[key] = slots[key]['value']
                
            if (not currentRoom.hasItem(values['CNoun'])):
                toSay = "%(CNoun)s is not in here to %(AVerb)s" % values
                
                
            # TODO
            # elif (roomItems): # is not switcahble
                # toSay = "" 
                
            else:
                # res = currentRoom.something() Check if valid
                toSay = "You %(AVerb)s %(BSwitch)s %(CNoun)." % values
                toSay += ""
                
            # Go into trapdoor
        elif all ("value" in slots[key] for key in ("AVerb","BLoc","CNoun")):
            values = {}
            
            for key in ("AVerb","BSwitch","CNoun"):
                values[key] = slots[key]['value']
            
            if (not currentRoom.hasItem(values['CNoun'])): # check if thing in room
                toSay = "No %(CNoun)s here" % values
                
            # TODO
            # elif (roomItems): # cannot have movement action
                # toSay = ""
                
            else:
                # res = currentRoom.something() Check if valid
                toSay = "You %(AVerb)s %(BSwitch)s %(CNoun)." % values
                toSay += ""
        
        elif all ("value" in slots[key] for key in ("AVerb","BNoun")):
            values = {}
            for key in ("AVerb","BNoun"):
                values[key] = slots[key]['value']
            
            tryAction = action.doAction(values['AVerb'], values['BNoun'], player)
            
            if (not tryAction):
                toSay = "I don't understand that command"
            elif(len(tryAction) == 3 and type(tryAction[2]) == str):
                resStr = ""
                isDead = False
                
                playerAttk = tryAction[0]
                creatureAttk = tryAction[1]
                attkType = tryAction[2]
                
                print(currentRoom.creatures)
                if (len(currentRoom.creatures) != 0):
                    mutant = currentRoom.creatures[0]
                    player.health = player.health - creatureAttk
                    resStr = mutant.name + " struck first for " + str(creatureAttk)  + " . And has " + str(mutant.health) + " health points remaining."
                    if (player.getHealth() > 0):
                        mutant.health = mutant.health - playerAttk
                        resStr += " . " + player.name + " fought back with a " + attkType + " for " + str(playerAttk) + " damage"
                    else:
                        isDead = True
                        resStr += "You died"
                    save()
                    return {"toSay":resStr,"finish":isDead}
                else:
                    return {"toSay":"Try again","finish":isDead}
            elif (type(tryAction) == str):
                toSay = tryAction
            else:
                newRoom = getRoomWithCoords(tryAction)
                player.setRoom(newRoom)
                toSay += player.getRoom().getDescription()
                m = player.getRoom().creatures
                
                if (len(player.getRoom().creatures) != 0):
                    mutant = m[0]
                    toSay += " " + mutant.description
        else:
            toSay = "I'm sorry, I don't understand!"
        
        save()
        
        return {"toSay":toSay, "finish":finish}