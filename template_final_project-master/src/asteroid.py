import pygame
import random
import os

class Asteroid:
    def __init__(self, screen_width, screen_height, speed):
        """
        Initializes an asteroid with random spawn position and speed.
        """
        self.speed = speed
        player_image_path = os.path.join("assets", "asteroid.jpg")
        self.image = pygame.image.load(player_image_path)
        self.flipped = False
        self.image = pygame.transform.scale(self.image, (100, 100))
        

        # Randomly choose the spawn position along the perimeter
        spawn_side = random.choice(['top', 'bottom', 'left', 'right'])
        
        if spawn_side == 'top':
            self.x = random.randint(0, screen_width)
            self.y = 0
        elif spawn_side == 'bottom':
            self.x = random.randint(0, screen_width)
            self.y = screen_height
        elif spawn_side == 'left':
            self.x = 0
            self.y = random.randint(0, screen_height)
        else: 
            self.x = screen_width
            self.y = random.randint(0, screen_height)

        self.rect = pygame.Rect(self.x, self.y, 70, 70)

        # Randomize movement speed in both x and y directions
        self.speed_x = random.uniform(-1, 1) * self.speed
        self.speed_y = random.uniform(-1, 1) * self.speed
        

    def update_position(self):
        """
        Updates the asteroid's position based on its speed.
        """
        self.x += self.speed_x
        self.y += self.speed_y
        self.rect = pygame.Rect(self.x, self.y, 50, 50)
        

    def draw(self, screen):
        """Draws the asteroid on the screen."""
        #pygame.draw.rect(screen, "red", self.rect)
        screen.blit(self.image,(self.x, self.y))
