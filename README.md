We were inspired by classic text-based adventure games such as Zork, and decided that the alexa had a lot of potential as a new platform for this kind of interactive narrative adventure. We were initially just planning to develop an Alexa port of a preexisting text-based game such as Zork, but later decided it would be more interesting to design our own game from scratch.

The game is set in a mysterious post-apocalyptic future. The player begins in an old abandoned amazon fulfilment centre, and must journey through a number of regions to reach Amazon Headquarters and seek answers. Throughout the journey, the player must find items and fight enemies in the form of malevolent Amazon delivery drones and mutated UCL students. The game culminates with the player fighting a cyborg Jeff Bezos on the roof garden of Amazon HQ.

We used the Alexa Skills Kit and AWS Lambda functions in python 3.6 to build the game as a skill for the echo platform.

configuring a detailed enough intent schema for the game turned out to be really difficult, as did compiling lists of allowed verbs and items. Just getting our echo to connect to imperial wifi also proved to be extremely time-consuming.

We are proud of managing to get a partial working playthrough of the game on our echo

we learned that even simple-sounding applications are difficult to build for alexa

next, we'd like to finish debugging everything so we can get a full playthrough working on our echo, after which we might add some intelligence that tailors elements of the game to the player's identity/location etc

Setup:
How to deploy: zip all contents into zip and upload on lambda
