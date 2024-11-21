import pygame
from src import Player
from src import create_random_asteroid

class Controller:
    def __init__(self):
        """
        Initializes objects and resources required to run the program.
        """
        pygame.init()
        self.screen_width = 800
        self.screen_height = 600
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.clock = pygame.time.Clock()
        self.player = Player(self.screen_width // 2, self.screen_height - 50, "player.png")
        self.asteroids = [create_random_asteroid(self.screen_width, self.screen_height) for _ in range(5)]

    def mainloop(self):
        """
        Main game loop.
        """
        running = True
        while running:
            # 1. Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.player.move(-1, 0)
                    elif event.key == pygame.K_RIGHT:
                        self.player.move(1, 0)

            # 2. Detect collisions and update models
            for asteroid in self.asteroids:
                asteroid.move()

            # 3. Redraw the next frame
            self.screen.fill((0, 0, 0))  # Black background
            # Example: Draw player and asteroids (requires actual image loading with pygame)
            for asteroid in self.asteroids:
                pygame.draw.circle(self.screen, (255, 0, 0), (int(asteroid.x), int(asteroid.y)), 10)
            pygame.draw.circle(self.screen, (0, 255, 0), (self.player.x, self.player.y), 15)

            # 4. Display the next frame
            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()

if __name__ == "__main__":
    game = Controller()
    game.mainloop()
