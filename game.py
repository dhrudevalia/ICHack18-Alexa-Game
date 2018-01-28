#
#                    MADE BY 
#      SAM LIEM, MAX TAYLOR-DAVIES, AND DHRU DEVALIA
#                DURING ICHACK 2018
#           RIP NGE, "WITH WHAT", and D D 



#------------FOR TESTING------------
# class Room:
#     def __init__(self, name, location, description, items, creatures, indoors, locks):
#         self.name = name # String
#         self.location = location # (x,y,z)
#         self.description = description # String
#         self.items = items # [Item Obj]
#         self.indoors = indoors # Boolean
#         self.locks = locks #array of booleans
        
#     def getItems(self):
#         return self.items
        
#     def takeItem(self, item):
#         return self.items.remove(item)
    
#     def dropItem(self, item):
#         return self.items.append(item)
        
#     def getXCoord(self):
#         return self.location[0]
    
#     def getYCoord(self):
#         return self.location[1]
        
#     def getZCoord(self):
#         return self.location[2]
        
#     def isIndoors(self):
#         return self.indoors
        
#     def hasItem(self, itemName): # returns boolean
#         for item in items:
#             if item.getName == itemName:
#                 return True
#         return False
        
# class Player:
#     def __init__(self, name, inventory, health, room):
#         self.name = name # String
#         self.inventory = inventory # [Items Obj]
#         self.health = health # Int
#         self.room = room # Room Obj
        
#     def getRoom(self):
#         return self.room
        
#     def getName(self):
#         return self.name

# warehouse = Room("Warehouse", [0,0,0], """You are in what appears to be a large abandoned amazon fulfilment centre. 
#                 Rows of shelves stretch along the warehouse. The floor is littered with long-dead package retrieval robots.
#                 There is no sound, and almost no light, save for a faint glow from a large green message scrawled
#                 on the north wall. The message reads: if you seek answers, journey north and find headquarters. 
#                 Under the text, you can see a door, slightly ajar. There do not appear to be any other exits""",[],[], True,[])
                
# jungle_SW = Room("Southwest Jungle",[1,0,0],"",[], [], False, [])

# initRooms = [
#     warehouse,
#     jungle_SW,
# ]
# REMOVE ABOVE AND COMMENT IMPORTS WHEN BELOW IS SUITABLE

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
    # key.set_contents_from_string(pickle.dumps([player, rooms]))

def load():
    p, rs, w = pickle.loads(key.get_contents_as_string())
    # p , rs = pickle.loads(key.get_contents_as_string())
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
    
def hits(playerAttk, creatureAttk, attkType):
    resStr = ""
    isDead = False
    i = random.randint(0,1)
    
    if (i == 0):
        mutant.health = mutant.health - playerAttk
        res = player.name + " struck first for " + playerAttk + " damage in a " + attkType + " . With " + player.health + " health points remaining."
        if (mutant.getHealth() > 0):
            first.health = first.health - creatureAttk
            res += " . " + mutant.name + " fought back for " + creatureAttk + " damage"
        else:
            mutant = None
            res += " Killing it"
    else:
        player.health = player.health - creatureAttk
        res = mutant.name + " struck first for " + creatureAttk  + " . And has " + mutant.health + " health points remaining."
        if (player.getHealth() > 0):
            mutant.health = mutant.health - playerAttk
            res += " . " + player.name + " fought back with a " + attkType + " for " + playerAttk + " damage"
        else:
            isDead = True
            res += "You died"
    save()
    return {"toSay":resStr,"finish":isDead}

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
            playerAttk = a[0]
            creatureAttk = a[1]
            attkType = a[2]
            mutant = currentRoom.creatures[0]
            player.health = player.health - creatureAttk
            res = mutant.name + " struck first for " + creatureAttk  + " . And has " + mutant.health + " health points remaining."
            if (player.getHealth() > 0):
                mutant.health = mutant.health - playerAttk
                res += " . " + player.name + " fought back with a " + attkType + " for " + playerAttk + " damage"
            else:
                isDead = True
                res += "You died"
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
                
                mutant = currentRoom.creatures
                mutant = mutant[0]
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
