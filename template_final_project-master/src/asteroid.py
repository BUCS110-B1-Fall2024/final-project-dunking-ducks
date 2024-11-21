import pygame

class Asteroid:
    def __init__(self, x, y, speed):
        """
        Initializes an asteroid with position and speed
        args:
        - x: int - Starting x-coordinate
        - y: int - Starting y-coordinate
        - speed: int - Speed of the asteroid
        """
        self.x = x
        self.y = y
        self.speed = speed
        self.image = None  
        self.rect = pygame.Rect(self.x, self.y, 40, 40)  

    def update_position(self):
        self.y += self.speed
        self.rect.topleft = (self.x, self.y)

    def draw(self, screen):
        pygame.draw.rect(screen, ("red"), self.rect)
