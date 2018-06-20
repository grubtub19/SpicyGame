# SpicyGame
This is one spicy game

Class Structure:

Inside our game "SpicyGame", there exists a Universe that has no form. It only stores the information about all the objects that exist. 
Inside the Universe, there is both an Arena(side view) and an Overworld(top down view). The Overworld gets instantiated once.
However, we instantiate the Arena every time we use it. Once the battle is over, the same Overworld as before appears.

NOT INHERITANCE (just how data flows in general):
SpicyGame
	Universe
		Arena
		or
		Overworld

"Spicy Game calls update() in Universe which calls update() in Arena"




An Entity is any game object that has a position and ASCII representation. A Pokemon is any Entity that can fight. The ArenaHealthBar
is an example of using the Entity class by itself.

Inheritance:
Entity
	Pokemon
		Player
		Monster
	ArenaHealthBar