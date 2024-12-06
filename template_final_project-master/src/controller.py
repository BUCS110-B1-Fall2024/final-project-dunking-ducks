import pygame
import random
from src.player import Player
from src.asteroid import Asteroid
from src.powerup import Powerup

class Controller:
    def __init__(self):
        """
        Initializes the game controller, pygame settings, and game objects.
        """
        self.screen_width = 1000
        self.screen_height = 1000
        
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Dodging Duck")
        
        self.clock = pygame.time.Clock()
        
        self.player = Player(375, 275)
        self.asteroids = []
        self.powerup = []
        self.running = True
        self.start_time = pygame.time.get_ticks() 
        self.score = 0

        self.lives = 3  # Player starts with 3 lives
        self.asteroid_spawn_prob = 0.08
        self.powerup_spawn_prob = 0.0005
        self.game_over = False  # Flag to track if the game is over

    def mainloop(self):
        """
        Main loop to handle the game logic and rendering.
        """
        while self.running:
            self.handle_events()
            if not self.game_over:  # Only update the game if it's not over
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
        """Updates the game state."""
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.player.move_left()
        if keys[pygame.K_RIGHT]:
            self.player.move_right()
        if keys[pygame.K_UP]:
            self.player.move_up()
        if keys[pygame.K_DOWN]:
            self.player.move_down()

        # Update the score based on time passed
        self.score = int(pygame.time.get_ticks() - self.start_time)

        self.asteroid_spawn_prob = 0.08 + (self.score // 5000) * 0.02

        # Spawn asteroids randomly based on the current probability
        if random.random() < self.asteroid_spawn_prob:
            self.asteroids.append(Asteroid(self.screen_width, self.screen_height, speed = random.randint(7, 10)))

        # Update asteroid positions
        for asteroid in self.asteroids:
            asteroid.update_position()

        self.powerup_spawn_prob = 0.001 + (self.score // 5000) * 0.005

        # Spawn powerups randomly based on the current probability
        if random.random() < self.powerup_spawn_prob:
            self.powerup.append(Powerup(self.screen_width, self.screen_height, speed = random.randint(7, 10)))

        # Update apowerups positions
        for powerup in self.powerup:
            powerup.update_position()

        # Check for collisions between the player and asteroids
        for asteroid in self.asteroids[:]:
            if self.player.rect.colliderect(asteroid.rect):  # Check for collision
                self.lives -= 1  # Decrease lives on collision
                self.asteroids.remove(asteroid)  # Remove the asteroid that collided
                if self.lives <= 0:
                    self.player_death()  # If no lives left, end the game
                return  # Exit the update method after collision
        
        # Collisions between player and powerups
        for powerup in self.powerup[:]:
             if self.player.rect.colliderect(powerup.rect):  # Check for collision
                 self.lives += 1  # Increases lives on collision
                 self.player.speed += 1
                 self.powerup.remove(powerup)  # Remove the powerup that collided

                # Decrease the player's size every time they touch a powerup
                 player_sizex = max(50, self.player.rect.width - 10)  # Ensure size doesn't go below 50
                 player_sizey = max(50, self.player.rect.height - 10)  # Ensure size doesn't go below 50

                # Update the player's rect to reflect the new size
                 self.player.rect = pygame.Rect(self.player.x, self.player.y, player_sizex, player_sizey)

                # Scale the player's image to the new size
                 self.player.image = pygame.transform.scale(self.player.image, (player_sizex, player_sizey))

                 if self.lives <= 0:
                     self.player_death()  # If no lives left, end the game
                 return  # Exit the update method after collision
            

    def render(self):
        """Renders the game objects and updates the display."""
        self.screen.fill(("black"))  # Fill the screen with black background
    
        if not self.game_over:  # If the game is not over, render the game
            self.player.draw(self.screen)  # Draw the player

            # Draw the asteroids
            for asteroid in self.asteroids:
                asteroid.draw(self.screen)

            for powerup in self.powerup:
                powerup.draw(self.screen)

            # Display the score
            font = pygame.font.SysFont(None, 42)
            score_text = font.render(f"Score: {self.score}", True, ("white"))  
            self.screen.blit(score_text, (10, 10))  # Position the score at the top-left corner

            # Display lives remaining (Lives: X/3)
            lives_text = font.render(f"Lives: {self.lives}/3", True, ("white"))  
            self.screen.blit(lives_text, (self.screen_width - 150, 10))  # Position the lives at the top-right corner
        else:
            # Display Game Over screen
            font = pygame.font.SysFont(None, 70)
            game_over_text = font.render("GAME OVER", True, ("red")) 
            score_text = font.render(f"Final Score: {self.score}", True, ("white")) 

            # Center the text on the screen
            self.screen.blit(game_over_text, (self.screen_width // 2 - game_over_text.get_width() // 2, self.screen_height // 3))
            self.screen.blit(score_text, (self.screen_width // 2 - score_text.get_width() // 2, self.screen_height // 2))

        pygame.display.flip()  # Update the screen with everything drawn

    def player_death(self):
        """Handles player death by setting game_over to True."""
        self.game_over = True  # Set game over flag to True
