#------------FOR TESTING------------
class Room:
    def __init__(self, name, location, description, items, creatures, indoors, locks):
        self.name = name # String
        self.location = location # (x,y,z)
        self.description = description # String
        self.items = items # [Item Obj]
        self.indoors = indoors # Boolean
        self.locks = locks #array of booleans
        
    def getItems(self):
        return self.items
        
    def takeItem(self, item):
        return self.items.remove(item)
    
    def dropItem(self, item):
        return self.items.append(item)
        
    def getXCoord(self):
        return self.location[0]
    
    def getYCoord(self):
        return self.location[1]
        
    def getZCoord(self):
        return self.location[2]
        
    def isIndoors(self):
        return self.indoors
        
    def hasItem(self, itemName): # returns boolean
        for item in items:
            if item.getName == itemName:
                return True
        return False
        
class Player:
    def __init__(self, name, inventory, health, room):
        self.name = name # String
        self.inventory = inventory # [Items Obj]
        self.health = health # Int
        self.room = room # Room Obj
        
    def getRoom(self):
        return self.room
        
    def getName(self):
        return self.name

warehouse = Room("Warehouse", [0,0,0], """You are in what appears to be a large abandoned amazon fulfilment centre. 
                Rows of shelves stretch along the warehouse. The floor is littered with long-dead package retrieval robots.
                There is no sound, and almost no light, save for a faint glow from a large green message scrawled
                on the north wall. The message reads: if you seek answers, journey north and find headquarters. 
                Under the text, you can see a door, slightly ajar. There do not appear to be any other exits""",[],[], True,[])
                
jungle_SW = Room("Southwest Jungle",[1,0,0],"",[], [], False, [])

initRooms = [
    warehouse,
    jungle_SW,
]
# REMOVE ABOVE AND COMMENT IMPORTS WHEN BELOW IS SUITABLE
# from classes import Item, Weapon, Food, Room, Player, Creature
# from world import initRooms
# import move
import pickle
import os
import boto

s3 = boto.s3.connect_to_region(
                    "eu-west-2",
                    aws_access_key_id="AKIAIWDQLBLAQWDY4DCQ",
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
    key.set_contents_from_string(pickle.dumps([player, rooms]))

def load():
    p , rs = pickle.loads(key.get_contents_as_string())
    global player 
    player = p
    global rooms 
    rooms = rs
    
# -- Game functions

def getInventory():
    if player is not None:
        return [item.getName() for item in player.getInv()]
    else:
        return None

def getRoomWithCoords(x,y,z):
    for room in rooms:
        if (room.getXCoord == x and room.getYCoord == y and room.getZCoord == Z):
                return room
    return None

def play(slots, new=False):
    toSay = ""
    finish = False
    if (new):
        global player
        player = Player("Mark",[],100,warehouse)
        global rooms 
        rooms = initRooms
        save()
        toSay = "You're a dumb dumb"
        return toSay
    else:
        load()
        currentRoom = player.getRoom()
        roomItems = currentRoom.getItems()
        
        if all ("value" in slots[key] for key in ("AVerb","BNoun","CUsing","DNoun")):
            values = {}
            toSay = ""
            
            for key in ("AVerb","BNoun","CUsing","DNoun"):
                values[key] = slots[key]['value']
                
            if (len(player.getInv) == 0) or (player.hasItem(DNoun)):
                toSay = "You don't have a %(BNoun)s" % values
            elif (not currentRoom.hasItem(values['DNoun'])): # check if thing in room
                toSay = "%(BNoun)s is not in here to %(AVerb)s" % values
            else:
                doActionFight(AVerb, BNoun, DNoun, player)
                toSay = "You %(AVerb)s %(BNoun)s with %(DNoun)s" % values

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
            
            if (values['CNoun'] not in roomItems): # check if thing in room
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
            
            if (values['CNoun'] not in roomItems): # check if thing in room
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
                
            if (values['BNoun'] not in roomItems): # check if thing in room
                toSay = "No %(CNoun)s here" % values
            else:
                toSay = "You %(AVerb)s %(BNoun)s." % values
                # tries moving
                # m = move.initMove(values['AVerb'],values['BNoun'],rooms,player)
                # if (m != False):
                #     (x,y,z) = m
                #     player.setRoom(getRoomWithCoords(x,y,z))
                # else:
                    
                # toSay += ""
                toSay = doAction(vAVerb, BNoun, player)
                if (not toSay):
                    #repromt SAM HOW DO THISNO VALID COMMAND
        else:
            toSay = "I'm sorry, I don't understand!"
        save()
        return {"toSay":toSay, "finish":finish}