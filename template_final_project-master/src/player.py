import pygame

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
        self.speed = 5
        self.image = None  # Placeholder for player image
        self.rect = pygame.Rect(self.x, self.y, 50, 50)  # Placeholder rect for collisions

    def move_left(self):
        """
        Moves the player left.
        args: None
        return: None
        """
        self.x -= self.speed
        self.rect.topleft = (self.x, self.y)

    def move_right(self):
        """
        Moves the player right.
        args: None
        return: None
        """
        self.x += self.speed
        self.rect.topleft = (self.x, self.y)

    def move_up(self):
        """
        Moves the player up.
        args: None
        return: None
        """
        self.y -= self.speed
        self.rect.topleft = (self.x, self.y)

    def move_down(self):
        """Moves the player down.
        args: None
        return: None
        """
        self.y += self.speed
        self.rect.topleft = (self.x, self.y)

    def draw(self, screen):
        """Draws the player on the screen.
        args: None
        - screen : pygame.Surface - the game window draw the power-up on
        return: None
        """
        pygame.draw.rect(screen, ("yellow"), self.rect)