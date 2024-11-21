import pygame

class PowerUp:
    def __init__(self, x, y, effect):
        """
        Initializes a power-up with position and effect.
        args:
        - x: int - Starting x-coordinate
        - y: int - Starting y-coordinate
        - effect: - Effect of the power-up
        """
        self.x = x
        self.y = y
        self.effect = effect  
        self.image = None  
        
    def update_position(self):
        """Moves the power-up downward.
        args: None
        return: None
        """
        self.y += 2  
        self.rect.topleft = (self.x, self.y)

    def draw(self, screen):
        """Moves the power-up downward.
        args:
        - screen : pygame.Surface - the game window draw the power-up on
        return: None
        """
        pygame.draw.rect(screen, ("green"), self.rect)