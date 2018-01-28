import game
# class move:
        
# returns new room
def goNorth(listOfRooms, currentRoom):
    return [currentRoom.getXCoord(), currentRoom.getYCoord() + 1, 0]
    
def goSouth(listOfRooms, currentRoom):
    return [currentRoom.getXCoord(), currentRoom.getYCoord() - 1, 0]
    
def goEast(listOfRooms, currentRoom):
    return [currentRoom.getXCoord() + 1, currentRoom.getYCoord(), 0]

def goWest(listOfRooms, currentRoom):
    return [currentRoom.getXCoord() - 1, currentRoom.getYCoord(), 0]
    
def isPossible(allRooms, currentRoom, direction): # checks its within bounds
    
    if (direction == 'north'):
        return not (game.getRoomWithCoords(goNorth(allRooms, currentRoom)) == None)
            
    elif (direction == 'south'):
        return not (game.getRoomWithCoords(goSouth(allRooms, currentRoom)) == None)
            
    elif (direction == 'east'):
        return not (game.getRoomWithCoords(goEast(allRooms, currentRoom)) == None)
            
    elif(direction == 'west'):
        return not (game.getRoomWithCoords(goWest(allRooms, currentRoom)) == None)
    return True
    
    
# def InitMove(noun, listOfRooms, currentRoom): # checks its a correct noun 
    
#     if (noun == "north" or noun == "up"):
#         if(isPossible(listOfRooms, currentRoom, 'N')):
#             if(isNotLocked(getRoomWithCoords([currentRoom.getXCoord(), currentRoom.getYCoord() + 1, 0]), currentRoom, ???)):
#                 return goNorth(listOfRooms, currentRoom)
#     elif(noun == "south" or noun == "down"):
#         if(isPossible(listOfRooms, currentRoom, 'S')):
#             return goSouth(listOfRooms, currentRoom)
#     elif(noun == "east" or noun == "right"):
#         if (isPossible(listOfRooms, currentRoom, 'E')):
#             return goEast(listofRooms, currentRoom)
#     elif(noun == "west" or noun == "left"):
#         if(isPossible(listOfRooms, currentRoom, 'W')):
#             return goWest(listOfRooms, currentRoom)     
#     elif(noun == "northeast"):
#         if(isPossible(listOfRooms, currentRoom, 'N')):
#             if(isPossible(listOfRooms, currentRoom, 'E')):
#                 currentRoom = goNorth(listOfRoom, currentRoom)
#                 return goEast(listOfRoom, currentRoom )
#     elif(noun == "northwest"):
#         if(isPossible(listOfRooms, currentRoom, 'N')):
#             if(isPossible(listOfRooms, currentRoom, 'W')):
#                 currentRoom = goNorth(listOfRoom, currentRoom)
#                 return goWest(listOfRoom, currentRoom )            
#     elif(noun == "southeast"):
#         if(isPossible(listOfRooms, currentRoom, 'S')):
#             if(isPossible(listOfRooms, currentRoom, 'E')):
#                 currentRoom = goSouth(listOfRoom, currentRoom)
#                 return goEast(listOfRoom, currentRoom )    
#     elif(noun == "southwest"):
#         if(isPossible(listOfRooms, currentRoom, 'S')):
#             if(isPossible(listOfRooms, currentRoom, 'W')):
#                 currentRoom = goSouth(listOfRoom, currentRoom)
#                 return goWest(listOfRoom, currentRoom )    
#     else:
#         return (False) # need to just continue go to next line
        

def isNotLocked(allRooms, currentRoom, direction):
    if(direction == 'north'):
        if(game.getRoomWithCoords(goNorth(allRooms, currentRoom)).locks[2] != 0):
            return False
    elif(direction == 'south'):
        if(game.getRoomWithCoords(goSouth(allRooms, currentRoom)).locks[0] != 0):
            return False
    elif(direction == 'east'):
        if(game.getRoomWithCoords(goEast(allRooms, currentRoom)).locks[3] != 0):
            return False
    elif(direction == 'west'):
        if(game.getRoomWithCoords(goWest(allRooms, currentRoom)).locks[1] != 0):
            return False
    
    return True
        
        
def initMove(direction, allRooms, currentRoom, player):
    
    
    #case 1 - room does not exist
    if not isPossible(allRooms, currentRoom, direction):
        return False
    
    #print(isPossible(allRooms, currentRoom, direction))
    
    
    #case 2 - room exists and is unlocked from your position
    if (isNotLocked(allRooms, currentRoom, direction)):
        return performMove(allRooms, currentRoom, direction)
    
    
    #case 3 - room exists and is locked from your position
    neededItem = [x for x in game.getRoomWithCoords(performMove(allRooms, currentRoom, direction)).getLocks() if x != 0][0]
    if(player.hasItem(neededItem.name)):
        return performMove(allRooms, currentRoom, direction)
    else:
        return ("It seems like you might need an item to progress through")
    
    
    
def performMove(allRooms, currentRoom, direction):
    if(direction == "north"):
        return goNorth(allRooms, currentRoom)
    elif(direction == "south"):
        return goSouth(allRooms, currentRoom)
    elif(direction == "east"):
        return goEast(allRooms, currentRoom)
    elif(direction == "west"):
        return goWest(allRooms, currentRoom)