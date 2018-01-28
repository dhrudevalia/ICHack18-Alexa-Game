from classes import Room, Item, Weapon, Food, Creature, Player
import random


#-----------ITEMS----------------------------
echo = Item("echo", "an amazon echo, it seems to still be working", True, ][])
echo_dot = Item("echo dot", "an amazon echo")
echo_show = Item()
button = Item()
paper = Item()
kindle = Item()
computer = Item()
torch = Item()
tree = Item()
gloves = Item()
climbing_shoes = Item()
body = Item()
rock = Item()
car = Item()
backpack = Item()
macbook = Item()
hollowed_tree = Item()




#----------WEAPONS----------------------------
sword = Weapon()
knife = Weapon()
machete = Weapon()
pistol = Weapon()
rifle = Weapon()




#---------FOOD--------------------------------
chocolate = Food()
noodles = Food()
banana = Food()
apple = Food()
energy_drink = Food()
coffee = Food()
beer = Food()
water = Food()
pizza = Food()
avocado = Food()
medicine = Food()



#--------CREATURES----------------------------
mutant = Creature()
drone = Creature()
cyborg_jeff_bezos = Creature()




initItems = [echo, echo_dot, echo_show, button, switch, keypad, paper, kindle, computer, torch, medicine]

initWeapons = [sword, knife, machete, pistol, rifle]

initFood = [chocolate, noodles, banana, apple, energy_drink, coffee, beer, water]

initCreatures = [mutant, drone, cyborg_jeff_bezos]



def generate_creatures():
    creatures = []
    i = random.randint(0,3)
    if i == 2:
        creatures.append(mutant)
    elif i == 3:
        creatures.append(drone)
    return creatures
    




#------------REGION 1: THE JUNGLE------------
warehouse = Room("Warehouse", [0,0,0], [], """You are in what appears to be a large abandoned amazon fulfilment centre. 
                Rows of shelves stretch along the warehouse. The floor is littered with long-dead package retrieval robots.
                There is no sound, and almost no light, save for a faint glow from a large green message scrawled
                on the north wall. The message reads: if you seek answers, journey north and find headquarters. 
                Under the text, you can see a door, slightly ajar. There do not appear to be any other exits""", [shelves, boxes, torch], True)
                
jungle_SW = Room("Southwest Jungle",[0,1,0],"",[machete], [], False)
#machete is needed to cut through from jungle into forest

jungle_SE = Room("Southeast Jungle",[1,1,0],"",[tree, rope], [], False)
#tree can be used as a vantage point to see the next area

jungle_NE = Room("Northeast Jungle",[1,2,0],"",[pistol], generate_creatures(), False)
#pistol is a weapon

jungle_NW = Room("Northwest Jungle",[0,2,0],"",[body, coat, medicine], generate_creatures(), False)
#coat is needed to survive in the northern half of the forest


#-----------REGION 2: THE FOREST-------------
forest_SW = Room("Southwest Forest",[0,3,0],"",[kindle], generate_creatures(), False)

forest_SE = Room("Southeast Forest",[1,3,0],"",[gloves], generate_creatures(), False)
#gloves are needed to protect fingers from frostbite in the mountain region

forest_NE = Room("Northeast Forest",[1,4,0],"",[echo_dot], generate_creatures(), False)

forest_NW = Room("Northwest Forest",[0,4,0],"",[hollowed_tree, climbing_shoes], generate_creatures(), False)
#climbing shoes are needed to move from south mountain area to north mountain area


#-----------REGION 3: THE MOUNTAINS----------
mountains_SW = Room("Southwest Mountains",[2,4,0],"",[body, paper], generate_creatures(), False)
#paper has code needed to gain entry to the headquarters later on

mountains_SE = Room("Southeast Mountains",[3,4,0],"",[coffee], generate_creatures(), False)
#rope is needed to climb down the mountains to the city

mountains_NE = Room("Northeast Mountains",[3,5,0],"",[], generate_creatures(), False)

mountains_NW = Room("Northwest Mountains",[2,5,0],"",[rock, rifle], generate_creatures(), False)


#-----------REGION 4: THE CITY--------------
city_SW = Room("Southwest City",[3,6,0],"",[body, kindle, chocolate], generate_creatures(), False)

city_SE = Room("Southeast City",[4,6,0],"",[car, echo], generate_creatures(), False)

city_NE = Room("Northeast City",[4,7,0],"",[backpack, macbook], generate_creatures(), False)
#keypad is used to access headquarters

city_NW = Room("Northwest City",[3,7,0],"",[water], generate_creatures(), False)


#-----------REGION 5: HEADQUARTERS----------
reception = Room("Headquarters Reception",[4,8,0],"",[desk, computer], [drone], True)

food_court = Room("Headquarters Food Court", [4,8,1], "", [beer, pizza], [drone], True)

roof_garden = Room("Headquarters Roof Garden", [4,8,2], "", [], [cyborg_jeff_bezos], True)




    




initRooms = [
    warehouse,
    jungle_SW, jungle_SE, jungle_NE, jungle_NW,
    forest_SW, forest_SE, forest_NE, forest_NW,
    mountains_SW, mountains_SE, mountains_NE, mountains_NW,
    city_SW, city_SE, city_NE, city_NW,
    reception, food_court, roof_garden
]



