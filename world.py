from classes import Room, Item, Weapon, Food, Creature, Player
import random

#-----------ITEMS----------------------------
echo = Item("echo", "an amazon echo, it seems to still be working.", True, ["examine", "b", "take", "drop", "get"])
echo_dot = Item("echo dot", "an amazon echo dot. It seems to still be working.", True, ["examine", "b", "take", "drop", "get"])
button = Item("button", "a button, it can be pressed.", True, ["examine", "b", "take", "drop", "get"])
paper = Item("paper", "a piece of paper, ot seems to have something on it.", False, ["b", "examine", "cut", "take", "drop", "read", "get"])
kindle = Item("kindle", "an amazon kindle paperwhite model 5.", True, ["take", "drop", "b", "examine", "read", "get"])
computer = Item("computer", "a large white apple iMac.", True, ["b", "examine"])
torch = Item("torch", "a flashlight.", True, ["b", "drop", "examine", "take", "get"])
tree = Item("tree", "an enormous tree, which looks like it may be climbable.", False, ["climb"])
gloves = Item("gloves", "a medium sized pair of gloves, they are slightly worn out", False, ["drop", "examine", "take", "get"])
climbing_shoes = Item("climbing shoes", "a large pair of climbing shoes, this could be helpful on slopes", False, ["climb", "drop", "examine", "take", "get"])
body = Item("body", "a perfectly preserved corpse with a slightly surprised expression on its face", False, ["examine", "eat"])
rock = Item("rock", "a large rock, it looks slightly lodged", False, ["examine", "move", "search"])
car = Item("car", "a rusty old car, it hasn't run in years", False, ["examine", "search"])
backpack = Item("backpack", "a dark blue backpack with something in it", False, ["drop", "examine", "open", "take", "get"])
macbook = Item("macbook", "an old macbook from before the linux uprising", True, ["b", "drop", "examine", "take", "get"])
hollowed_tree = Item("hollowed tree", "a hollowed out tree, there could be something inside", False, ["climb", "examine", "search"])
shelves = Item("shelves", "some shelves", False, ["examine", "search"])
rope = Item("rope", "a rope to hang yourself with", False, [])
coat = Item("coat", "a nice warm coat to keep you warm and nice", False, [])
desk = Item("desk", "a modern white desk with a computer on top of it", False, ["examine", "search"])


#----------WEAPONS----------------------------
sword = Weapon("sword", "a beautiful and ancient-looking sword of fearsome proportions.", False, ["take", "get", "drop"], 5)
knife = Weapon("knife", "a short and deadly knife, it has a look of brutality.", False, ["take", "get", "drop"], 3)
machete = Weapon("machete", "a long curved machete, it looks pretty sharp.", False, ["take", "get", "drop"], 4)
pistol = Weapon("pistol", "a lovingly maintained Glock, ready to fire.", False, ["take", "get", "drop"], 7)
rifle = Weapon("rifle", "a semi-automatic rifle with a pretty hardcore military vibe.", False, ["take", "get", "drop"], 10)
noWeapon = Weapon("noWeapon", "you used no weapons", False, [], 2)


#---------FOOD--------------------------------
chocolate = Food("chocolate", "wow this chocolate is so well preserved, it looks sweet and delicious", False, ["examine", "take", "eat", "drop", "get"],2)
noodles = Food("noodles", "wow these noodles are so well preserved, definitley not rotten", False, ["examine", "take", "eat", "drop", "get"],3)
banana = Food("banana", "a surpringly perfectly ripe banana, might have monkey aids though", False, ["examine", "take", "eat", "drop", "get"],3)
apple = Food("apple", "a pink lady apple", False, ["examine", "take", "eat", "drop", "get"],5)
energy_drink = Food("energy drink", "a popular energy drink stole from a basement hackathon", False, ["examine", "take", "eat", "drop", "get"],2)
coffee = Food("coffe", "a cup of coffee, black", False, ["examine", "take", "eat", "drop", "get"],4)
beer = Food("beer", "a glass of Stella not bud lite", False, ["examine", "take", "eat", "drop", "get"], 5)
water = Food("water", "clear blue water, might also have aids", False, ["examine", "take", "eat", "drop", "get"], 1)
pizza = Food("pizza", "a hawaiian pizza, so basically worthless", False, ["examine", "take", "eat", "drop", "get"], 2)
avocado = Food("avocado", "an avocado, could be used on toast unless you're a millenial", False, ["examine", "take", "eat", "drop", "get"], 3)
medicine = Food("medicine", "generic medicine, or hard LSD, your guess", False, ["examine", "take", "drop", "get"], 5)

#--------CREATURES----------------------------
mutant = Creature("mutant", 15, "and a MUTANT stands before you. Before you can react, it attacks, and you take 15 damage. What would you like to do?")
drone = Creature("drone", 10, "and an amazon delivery DRONE buzzes angrily around you. Before you can react, it attacks, and you take 10 damage. What would you like to do?")
cyborg_jeff_bezos = Creature("cyborg jeff bezos", 50, "my name JEFF")

def generate_creatures():
    creatures = []
    i = random.randint(0,3)
    if i == 2:
        creatures.append(mutant)
    elif i == 3:
        creatures.append(drone)
    return creatures

#------------REGION 1: THE JUNGLE------------
warehouse = Room("Warehouse", [0,0,0], """You are in what appears to be a large abandoned amazon fulfilment centre. 
                Rows of shelves stretch along the warehouse. The floor is littered with long-dead package retrieval robots.
                There is no sound, and almost no light, save for a faint glow from a large green message scrawled
                on the north wall. The message reads: if you seek answers, journey north and find headquarters. 
                Under the text, you can see a door, slightly ajar. There do not appear to be any other exits""", [shelves, torch],[], True, [0,0,0,0])
                
jungle_SW = Room("Southwest Jungle",[0,1,0],"You are in a Jungle. Strange noises fill the air. On the ground you can see a machete.",[machete], [], False, [0,0,0,0])
#machete is needed to "cut" through from jungle into forest

jungle_SE = Room("Southeast Jungle",[1,1,0],"You are in another region of jungle. In front of you stands a colossal tree, but it does not look as though it can be climbed. On its lowest branch hangs a rope.",[tree, rope], [], False, [0,0,0,0])
#tree can be used as a vantage point to see the next area

jungle_NE = Room("Northeast Jungle",[1,2,0],"You find yourself in another region of jungle, laying obscured in the bushes you catch a glimpse of a gun",[pistol], generate_creatures(), False, [0,0,0,0])
#pistol is a weapon

jungle_NW = Room("Northwest Jungle",[0,2,0],"You stand in a clearing. The view to the north is obscured by thick vines. There is a body on the ground in front of you.",[body, coat, medicine], generate_creatures(), False, [0,0,0,0])
#coat is needed to survive in the northern half of the forest


#-----------REGION 2: THE FOREST-------------
forest_SW = Room("Southwest Forest",[0,3,0],"You are in a Forest. You can see what looks like an Amazon Kindle on the ground.",[kindle], generate_creatures(), False, [0,0,machete,0])

forest_SE = Room("Southeast Forest",[1,3,0],"You are in another region of Forest. There are some nice-looking gloves on the ground. The region of forest to the north looks extremely cold - warm clothes will be necessary", [gloves], generate_creatures(), False, [0,0,machete,0])
#gloves are needed to protect fingers from frostbite in the mountain region

forest_NE = Room("Northeast Forest",[1,4,0],"The North side of the forest is very cold. There are large patches of snow on the ground, atop one of which sits an echo dot.",[echo_dot], generate_creatures(), False, [0,0,coat,0])

forest_NW = Room("Northwest Forest",[0,4,0],"The North side of the forest is very cold. Before you stands an ancient hollowed-out tree. There might be something inside...",[hollowed_tree, climbing_shoes], generate_creatures(), False, [0,0,coat,0])
#climbing shoes are needed to move from south mountain area to north mountain area


#-----------REGION 3: THE MOUNTAINS----------
mountains_SW = Room("Southwest Mountains",[2,4,0],"You stand at the western base of a tall mountain. Half-buried in the snow next to you there is a body, perfectly preserved. The path to the north looks extremely steep - specialist footwear may be required...",[body, paper], generate_creatures(), False, [0,0,0,gloves])
#paper has code needed to gain entry to the headquarters later on

mountains_SE = Room("Southeast Mountains",[3,4,0],"You stand at the eastern base of a tall mountain. Hidden in the snow by your feet is a small stash of coffee! The path to the north looks extremely steep - specialist footwear may be required...",[coffee], generate_creatures(), False, [0,0,0,0])
#rope is needed to climb down the mountains to the city

mountains_NE = Room("Northeast Mountains",[3,5,0],"You stand proudly at the eastern peak of the mountain. Below you lies a ruined city. It's a long way down, but there's a passage you could go down.",[], generate_creatures(), False, [0,0,climbing_shoes,0])

mountains_NW = Room("Northwest Mountains",[2,5,0],"As you stand and admire the western view from the top of the mountain, you see a large rock with something sticking out from underneath",[rock, rifle], generate_creatures(), False, [0,0,climbing_shoes,0])


#-----------REGION 4: THE CITY--------------
city_SW = Room("Southwest City",[3,6,0],"The once great city of Seattle lies desolate before you. In front of you. all that is left is a decayed body and wreckage",[body, kindle, chocolate], generate_creatures(), False, [0,0,rope,0])

city_SE = Room("Southeast City",[4,6,0],"You are in the Southeast corner of the city. In the abandoned streets you find what's left of a car",[car, echo], generate_creatures(), False, [0,0,0,0])

city_NE = Room("Northeast City",[4,7,0],"You stand in the Northeast corner of the city. Out of the corner of your eye, you notice a backpack leant against the crumbling remains of a building. It is open, and you can see what looks like an old macbook sitting inside.",[backpack, macbook], generate_creatures(), False, [0,0,0,0])

city_NW = Room("Northwest City",[3,7,0],"You pause for a moment in the northwest corner of the city. Immediately north of you stands the great corporate palace that was the Amazon headquarters. It appears as though a high-tech security system is still in place, requiring a 4-digit code for access to be granted.",[], generate_creatures(), False, [0,0,0,0])


#-----------REGION 5: HEADQUARTERS----------
reception = Room("Headquarters Reception",[4,8,0],"You stand in the ground floor reception of the headquarters. It has the look of somewhere that was abandoned extremely rapidly and in great panic, but in the corner there still stands a desk with a computer on it. On the other side of the room you see a large and elegent set of stairs leading upwards.",[desk, computer], [drone], True, [0,0,paper,0])

food_court = Room("Headquarters Food Court", [4,8,1], "Entering the vast food court, you look around and are pleasantly surprised to discover large quantities of beer and pizza. On the side of the hall opposite the one you entered from, you can see another staircase leading up...", [beer, pizza], [drone], True, [0,0,0,0])

roof_garden = Room("Headquarters Roof Garden", [4,8,2], "", ["Emerging into a beautiful and expansive roof garden, you find yourself suddenly facing a large figure, part man and part machine. Slowly, the being turns to face you. MY NAME JEFF, HE BELLOWS."], [cyborg_jeff_bezos], True, [0,0,0,0])





initRooms = [
    warehouse,
    jungle_SW, jungle_SE, jungle_NE, jungle_NW,
    forest_SW, forest_SE, forest_NE, forest_NW,
    mountains_SW, mountains_SE, mountains_NE, mountains_NW,
    city_SW, city_SE, city_NE, city_NW,
    reception, food_court, roof_garden
]

initItems = [
    echo, echo_dot, button, paper, kindle, computer, torch, tree, gloves, climbing_shoes,
    body, rock, car, backpack, macbook, hollowed_tree, shelves, rope, coat, desk]
    
initWeapons = [
    sword, knife, machete, pistol, rifle]

initFood = [
    chocolate, noodles, banana, apple, energy_drink, coffee, beer, water, pizza, avocado, medicine]

initCreatures = [
    mutant, drone, cyborg_jeff_bezos]

initTotalItems = initItems + initWeapons + initFood

