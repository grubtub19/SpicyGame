# SpicyGame

> This is one spicy game.

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
