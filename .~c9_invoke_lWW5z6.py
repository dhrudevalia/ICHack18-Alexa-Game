from classes import Room, Item, Weapon, Food, Creature, Player
import random


#-----------ITEMS----------------------------
echo = Item("echo", "an amazon echo, it seems to still be working.", True, [examine, break, take, drop, get])
echo_dot = Item("echo dot", "an amazon echo dot. It seems to still be working.", True, [examine, break, take, drop, get])
button = Item("button", "a button, it can be pressed.", True, [use, examine, break, take, drop, get])
paper = Item("paper", "a piece of paper, ot seems to have something on it.", False, [break, examine, cut, take, drop, read, get])
kindle = Item("kindle", "an amazon kindle paperwhite model 5.", True, [take, drop, break, examine, read, get])
computer = Item("computer", "a large white apple iMac.", True, [break, examine])
torch = Item("torch", "a flashlight.", True, [break, drop, examine, take, get])
tree = Item("tree", "an enormous tree, which looks like it may be climbable.", False, [climb])
gloves = Item("gloves", "a medium sized pair of gloves, they are slightly worn out", False, [drop, examine, take, get])
climbing_shoes = Item("climbing shoes", "a large pair of climbing shoes, this could be helpful on slopes", False, [climb, drop, examine, take, get])
body = Item("body", "a perfectly preserved corpse with a slightly surprised expression on its face", False, [examine, eat])
rock = Item("rock", "a large rock, it looks slightly lodged", False, [examine, move, search])
car = Item("car", "a rusty old car, it hasn't run in years", False, [examine, search])
backpack = Item("backpack", "a dark blue backpack with something in it", False, [drop, examine, open, take, get])
macbook = Item("macbook", "an old macbook from before the linux uprising", True [break, drop, examine, take, get])
hollowed_tree = Item("hollowed tree", "a hollowed out tree, there could be something inside", False, [climb, examine, search])




#----------WEAPONS----------------------------
sword = Weapon("sword", "a beautiful and ancient-looking sword of fearsome proportions.", False, [take, get, drop], 5)
knife = Weapon("knife", "a short and deadly knife, it has a look of brutality.", False, [take, get, drop], 3)
machete = Weapon("machete", "a long curved machete, it looks pretty sharp.", False, [take, get, drop], 4)
pistol = Weapon("pistol", "a lovingly maintained Glock, ready to fire.", False, [take, get, drop], 7)
rifle = Weapon("rifle", "a semi-automatic rifle with a pretty hardcore military vibe.", False, [take, get, drop], 10)




#---------FOOD--------------------------------
chocolate = Food("chocolate", "wow this chocolate is so well preserved, it looks sweet and delicious", False, [examine, take, eat, drop, get])
noodles = Food("noodles", "wow these noodles are so well preserved, definitley not rotten", False, [examine, take, eat, drop, get])
banana = Food("banana", "a surpringly perfectly ripe banana, might have monkey aids though", False, [examine, take, eat, drop, get])
apple = Food("apple", "a pink lady apple", False, [examine, take, eat, drop, get])
energy_drink = Food("energy drink", "a popular energy drink stole from a basement hackathon", False, [examine, take, eat, drop, get])
coffee = Food("coffe", "a cup of coffee, black", False, [examine, take, eat, drop, get])
beer = Food("beer", "a glass of Stella not bud lite", False, [examine, take, eat, drop, get])
water = Food("water", "clear blue water, might also have aids", False, [examine, take, eat, drop, get])
pizza = Food("pizza", "a hawaiian pizza, so basically worthelss", False, [examine, take, eat, drop, get])
avocado = Food("avocado", "an avocado, could be used on toast unless you're a millenial", False [examine, take, eat, drop, get])
medicine = Food("medicine", "generic medicine, or hard LSD, your guess", False, [examine, take, drop, get])



#--------CREATURES----------------------------
mutant = Creature("mutant", False, 15)
drone = Creature("drone", False, 10)
cyborg_jeff_bezos = Creature("cyborg jeff bezos", F)




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
                Under the text, you can see a door, slightly ajar. There do not appear to be any other exits""", [shelves, boxes, torch], True, [])
                
jungle_SW = Room("Southwest Jungle",[0,1,0],"",[machete], [], False, [])
#machete is needed to cut through from jungle into forest

jungle_SE = Room("Southeast Jungle",[1,1,0],"",[tree, rope], [], False, [])
#tree can be used as a vantage point to see the next area

jungle_NE = Room("Northeast Jungle",[1,2,0],"",[pistol], generate_creatures(), False, [])
#pistol is a weapon

jungle_NW = Room("Northwest Jungle",[0,2,0],"",[body, coat, medicine], generate_creatures(), False, [])
#coat is needed to survive in the northern half of the forest


#-----------REGION 2: THE FOREST-------------
forest_SW = Room("Southwest Forest",[0,3,0],"",[kindle], generate_creatures(), False, [])

forest_SE = Room("Southeast Forest",[1,3,0],"",[gloves], generate_creatures(), False, [])
#gloves are needed to protect fingers from frostbite in the mountain region

forest_NE = Room("Northeast Forest",[1,4,0],"",[echo_dot], generate_creatures(), False, [])

forest_NW = Room("Northwest Forest",[0,4,0],"",[hollowed_tree, climbing_shoes], generate_creatures(), False, [])
#climbing shoes are needed to move from south mountain area to north mountain area


#-----------REGION 3: THE MOUNTAINS----------
mountains_SW = Room("Southwest Mountains",[2,4,0],"",[body, paper], generate_creatures(), False, [])
#paper has code needed to gain entry to the headquarters later on

mountains_SE = Room("Southeast Mountains",[3,4,0],"",[coffee], generate_creatures(), False, [])
#rope is needed to climb down the mountains to the city

mountains_NE = Room("Northeast Mountains",[3,5,0],"",[], generate_creatures(), False, [])

mountains_NW = Room("Northwest Mountains",[2,5,0],"",[rock, rifle], generate_creatures(), False, [])


#-----------REGION 4: THE CITY--------------
city_SW = Room("Southwest City",[3,6,0],"",[body, kindle, chocolate], generate_creatures(), False, [])

city_SE = Room("Southeast City",[4,6,0],"",[car, echo], generate_creatures(), False, [])

city_NE = Room("Northeast City",[4,7,0],"",[backpack, macbook], generate_creatures(), False, [])
#keypad is used to access headquarters

city_NW = Room("Northwest City",[3,7,0],"",[water], generate_creatures(), False, [])


#-----------REGION 5: HEADQUARTERS----------
reception = Room("Headquarters Reception",[4,8,0],"",[desk, computer], [drone], True, [])

food_court = Room("Headquarters Food Court", [4,8,1], "", [beer, pizza], [drone], True, [])

roof_garden = Room("Headquarters Roof Garden", [4,8,2], "", [], [cyborg_jeff_bezos], True, [])




    




initRooms = [
    warehouse,
    jungle_SW, jungle_SE, jungle_NE, jungle_NW,
    forest_SW, forest_SE, forest_NE, forest_NW,
    mountains_SW, mountains_SE, mountains_NE, mountains_NW,
    city_SW, city_SE, city_NE, city_NW,
    reception, food_court, roof_garden
]



