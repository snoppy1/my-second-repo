# Simple Battle Simulator

This is a basic Python battle simulation between a heroic Knight and two enemies: a Goblin and an Ant. The game demonstrates object-oriented programming principles such as classes, methods, and interaction between objects.

## File Structure

- `character.py`: Defines the `Character` class with attributes and methods for combat.
- `main.py`: Runs the battle simulation with one hero and a list of two enemies.

## Character Class

Located in `character.py`, the `Character` class includes:

### Attributes
- `name` (str): The character's name.
- `hp` (int): Hit points (health).
- `attack_power` (int): The base attack power set when the character is created.

### Methods
- `attack(other)`: Deals random damage between 30% and 90% of `attack_power` to the `other` character and prints an attack message.
- `is_alive()`: Returns `True` if HP is greater than 0.
- `__str__()`: Returns a string representation of the character's current HP.

## How the Battle Works

The battle logic in `main.py` follows these steps:

1. Create the Knight and a list of two enemies (Goblin and Ant).
2. Print everyone's starting stats.
3. Loop while the Knight is alive and at least one enemy is alive:
   - The Knight attacks the first enemy that is still alive.
   - Every enemy that is still alive attacks the Knight.
   - Print updated stats.
4. Declare the winner: the Knight if all enemies are defeated, otherwise the enemies.

## Running the Game

To run the simulation, execute `main.py`:

```bash
python main.py
```
