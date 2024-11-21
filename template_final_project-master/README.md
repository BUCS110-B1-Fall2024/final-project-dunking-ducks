#Team Name: 
Dunking Ducks

#Project Name:
Duck 'n' Dodge

CS110 B1 Final Project  << Fall Semester, 2024 >>

#Team Members: 
1. Kevin Cai
2. Denis Khrapko

#Project Description:
User must move his player 2-dimensionally in order to dodge asteroids. The asteroids will spawn in at random trajectories, speeds, and with increasing frequency. Randomly spawning power-ups can also be implemented to increase players speed or grant invincibility briefly. The player will earn 1 point for each second survived, and will play for a high score.

#Program Design - Features:
1. Start Menu
2. Moveing Asteroids
3. Moving character must avoid collisions with asteroids
4. Power-ups that change player's state
4. Game Over Screen
5. Score Keeping

### Classes
<< You should have a list of each of your classes with a description >>

# class Player
- The Player class represents the player's character in the game, which can be moved in all four directions and drawn on the game screen

# class Asteroid
- The Asteroid class represents an asteroid in the game, which moves downward at a specified speed and can be drawn on the game screen

# class Powerup
- The PowerUp class represents a collectible item in the game that has a position on the screen and an associated effect. The class provides methods to update its position (moving downward) and to draw it on the game screen.

# class Controller
- The Controller class is responsible for managing the overall game logic, including handling user input, updating game objects, and rendering the game screen

:warning: Everything between << >> needs to be replaced (remove << >> after replacing)

## GUI Design

### Initial Design

![initial gui](assets/gui.jpg)

### Final Design

![final gui](assets/finalgui.jpg)

## ATP

| Step                 |Procedure             |Expected Results                   |
|----------------------|:--------------------:|----------------------------------:|
|  1                   | Run Counter Program  |GUI window appears with count = 0  |
|  2                   | click count button   | display changes to count = 1      |
etc...