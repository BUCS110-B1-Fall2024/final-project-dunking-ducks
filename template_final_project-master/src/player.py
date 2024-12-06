import pygame
import os
class Player:

    def __init__(self, x, y):
        """
        Initializes the player with position and default speed.
        args:
        - x: int - Starting x-coordinate
        - y: int - Starting y-coordinate
        return: None
        """
        self.x = x
        self.y = y
        self.speed = 7
        player_image_path = os.path.join("assets", "player.jpg")
        self.image = pygame.image.load(player_image_path)
        self.flipped = False
        player_sizex = (150)
        player_sizey = (150)
        player_sizex1 = (100)
        player_sizey2 = (100)
        self.rect = pygame.Rect(self.x, self.y, player_sizex1, player_sizey2)  # Placeholder rect for collisions
        self.image.get_size()
        self.image = pygame.transform.scale(self.image, (player_sizex, player_sizey))
    

    def move_left(self):
        """
        Moves the player left.
        args: None
        return: None
        """
        self.x -= self.speed
        if not self.flipped:
            self.image = pygame.transform.flip(self.image, True, False)
            self.flipped = True
        #self.rect.topleft = (self.x, self.y)


    def move_right(self):
        
        """
        Moves the player right.
        args: None
        return: None
        """
        self.x += self.speed
        if not self.flipped:
            self.image = pygame.transform.flip(self.image, True, False)
            self.flipped = True
        self.rect.topleft = (self.x, self.y)

    def move_up(self):
        """
        Moves the player up.
        args: None
        return: None
        """
        self.y -= self.speed
        if not self.flipped:
            self.image = pygame.transform.flip(self.image, True, False)
            self.flipped = True
        #self.rect.topleft = (self.x, self.y)

    def move_down(self):
        """Moves the player down.
        args: None
        return: None
        """
        self.y += self.speed
        
        if not self.flipped:
            self.image = pygame.transform.flip(self.image, True, False)
            self.flipped = True
        #self.rect.topleft = (self.x, self.y)

    def draw(self, screen):
        """Draws the player on the screen.
        args: None
        - screen : pygame.Surface - the game window draw the power-up on
        return: None
        """
        #pygame.draw.rect(screen, ("yellow"), self.rect)
        screen.blit(self.image,(self.x, self.y))
