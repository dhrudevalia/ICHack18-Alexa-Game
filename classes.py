class Item: 
    def __init__(self, name, info, switchable, useableActions):
        self.name = name # String
        self.info = info # String
        self.switchable = switchable # Boolean
        self.useableActions = useableActions
    
    def getSwitchable(self):
        return self.switchable
    
    def getName(self):
        return self.name
    ###
    #nge
    ###    
class Weapon(Item):
    def __init__(self, name, info, switchable,useableActions, dmg):
        Item.__init__(self, name, info, switchable, useableActions)
        self.dmg = dmg # Int
    
    def getDmg(self):
        return self.dmg

class Food(Item):
    def __init__(self, name, info, switchable, useableActions, hp):
        Item.__init__(self, name, info, switchable, useableActions)
        self.hp = hp # Int
    
    def getHp(self):
        return self.hp
        
class Room:
    def __init__(self, name, location, description, items, creatures, indoors, locks):
        self.name = name # String
        self.location = location # (x,y,z)
        self.description = description # String
        self.items = items # [Item Obj]
        self.creatures = creatures
        self.indoors = indoors # Boolean
        self.locks = locks #array of booleans

    def getName(self):
        return self.name
        
    def getLocation(self):
        return self.location
        
    def getDescription(self):
        return self.description
        
    def getItems(self):
        return self.items
        
    def takeItem(self, e):
        for item in self.items:
            if (item.getName()==e):
                self.items.remove(item)
                print(item)
                return item
    
    def dropItem(self, item):
        if (self.items == None):
            self.items = [item]
        else:
            self.items.append(item)
        
    def getXCoord(self):
        return self.location[0]
    
    def getYCoord(self):
        return self.location[1]
        
    def getZCoord(self):
        return self.location[2]
        
    def isIndoors(self):
        return self.indoors
        
    def hasItem(self, itemName): # returns boolean
        print(self.items)
        for item in self.items:
            if item.getName() == itemName:
                return True
        return False
        
    def getLocks(self):
        return self.locks
        
    def getCreatures(self):
        return self.creatures

class Player:
    def __init__(self, name, inventory, health, room):
        self.name = name # String
        self.inventory = inventory # [Items Obj]
        self.health = health # Int
        self.room = room # Room Obj
    
    def getName(self):
        return self.name
    
    def addItem(self, item):
        return self.inventory.append(item)
    
    def dropItem(self, e):
        for item in self.inventory:
            if (item.getName()==e):
                self.items = self.inventory.remove(item)
                return item
    
    def getHealth(self):
        return self.health
    
    def getInv(self):
        return self.inventory
        
    def getRoom(self):
        return self.room
        
    def setRoom(self, room):
        self.room = room
        return self.room
        
    def hasItem(self, itemName): # returns boolean
        for item in self.getInv():
            if item.getName() == itemName:
                return True
        return False
        
    def consumeConsumables(self, item):
        self.health = min(100, self.health + item.hp)
        if (item in self.inventory):
            self.inventory.remove(item)
        
    def takeDamage(self, val):
        self.health = max(0, self.health - val)
    
class Creature:
    def __init__(self, name, health, description):
        self.name = name # String
        self.health = health # Int
        self.description = description
        
    def getName(self):
        return self.name
        
    def getDescription(self):
        return self.description
        
    def getHealth(self):
        return self.health
        
        
