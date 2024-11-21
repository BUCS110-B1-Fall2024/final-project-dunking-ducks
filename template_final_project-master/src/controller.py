import pygame
from src.player import Player
from src.asteroid import Asteroid
from src.powerup import PowerUp

class Controller:
    def __init__(self):
        """
        Initializes the game controller, pygame settings, and game objects.
        """
        self.screen_width = 800
        self.screen_height = 600
        
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Asteroid Dodger")
        
        self.clock = pygame.time.Clock()
        
        self.player = Player(400, 500)
        self.asteroids = []
        self.power_ups = []

        self.running = True
        self.score = 0

    def mainloop(self):
        """
        Main loop to handle the game logic and rendering.
        """
        while self.running:
            self.handle_events()
            self.update()
            self.render()
            self.clock.tick(60)

        pygame.quit()

    def handle_events(self):
        """Handles user input and other events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        """Updates the game state"""
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.player.move_left()
        if keys[pygame.K_RIGHT]:
            self.player.move_right()
        if keys[pygame.K_UP]:
            self.player.move_up()
        if keys[pygame.K_DOWN]:
            self.player.move_down()

    def render(self):
        """Renders the game objects and updates the display."""
        self.screen.fill((0, 0, 0)) 
        self.player.draw(self.screen) 
        pygame.display.flip()
