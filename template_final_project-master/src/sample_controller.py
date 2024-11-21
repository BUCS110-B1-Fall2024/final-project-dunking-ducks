import random

class Player:
    def __init__(self, x, y, img_file):
        """
        Initializes the player object.
        Args:
            x (int): Starting x-coordinate.
            y (int): Starting y-coordinate.
            img_file (str): Path to the image file for the player.
        """
        self.x = x
        self.y = y
        self.img_file = img_file

    def move(self, dx, dy):
        """
        Updates the player's position based on directional input.
        Args:
            dx (int): Change in x-coordinate.
            dy (int): Change in y-coordinate.
        """
        self.x += dx * 5  
        self.y += dy * 5

class Asteroid:
    def __init__(self, x, y, speed, trajectory, img_file):
        """
        Initializes the asteroid object.
        Args:
            x (int): Starting x-coordinate.
            y (int): Starting y-coordinate.
            speed (int): Speed of the asteroid.
            trajectory (tuple): Direction as (dx, dy).
            img_file (str): Path to the image file for the asteroid.
        """
        self.x = x
        self.y = y
        self.speed = speed
        self.trajectory = trajectory
        self.img_file = img_file

    def move(self):
        """
        Moves the asteroid along its trajectory.
        """
        self.x += self.trajectory[0] * self.speed
        self.y += self.trajectory[1] * self.speed

def create_random_asteroid(screen_width, screen_height, img_file="asteroid.png"):
    """
    Generates an asteroid with random properties.
    Args:
        screen_width (int): Width of the game screen.
        screen_height (int): Height of the game screen.
        img_file (str): Path to the image file.
    Returns:
        Asteroid: A new random asteroid.
    """
    x = random.randint(0, screen_width)
    y = 0 
    speed = random.randint(2, 5)
    trajectory = (random.uniform(-1, 1), random.uniform(0.5, 1))
    return Asteroid(x, y, speed, trajectory, img_file)
