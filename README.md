# SpicyGame

> This is one spicy game.

# Description

This was a group project at Waseda University for the Advanced Programming class. It is a short rpg game written in python and the "screen" is the terminal window. You walk through the overworld and encounter 3 hot peppers that you fight in the Arena. Each unit has 3 attack options. Some moves apply status effects. There is a status effects GUI to display information about all current ailments. The game is actually pretty difficult, so good use of the status effects is necessary to win (and some luck). Each of the 3 enemies has a specific fighting style (Ex: tank with low damage, but high status effects). The game is rather quick and easy to play.

# Installation

Requires Python 3. Just run Universe.py

# Screenshots

![alt text](https://imgur.com/MHXz7Jr.png)
![alt text](https://imgur.com/ICYuwkK.png)
![alt text](https://imgur.com/Lv5RmKc.png)
![alt text](https://imgur.com/xGZfd8T.png)

## Class Structure

The game starts with a `Universe` that has no form. It only stores the information about all the objects that exist.

Inside the `Universe`, there is both an `Arena` (Pokemon battle style view) and an `Overworld` (top down view). The `Overworld` gets instantiated once. However, we instantiate the `Arena` every time we use it. Once the battle is over, the same `Overworld` as before appears.

## Data Flow
This is not inheritance, but just how data flows in general:

```
Universe
	Screen
	Overworld or Arena
		Entity
			Pokemon
				Player
				Monster
```

`Universe` calls `update()` which calls `update()` in `Overworld` or `Arena`.

### Entity
An `Entity` is any game object that has a position and ASCII representation.

### Pokemon
A `Pokemon` is any `Entity` that can exist in the `Arena`. The `ArenaHealthBar`
is an example of using the `Entity` class by itself.

## Inheritance

```
Entity
	Pokemon
		Player
		Monster
	ArenaHealthBar
```
