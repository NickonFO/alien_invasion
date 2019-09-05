import pygame

from settings import Settings
from ship import Ship
import game_functions as gf


def rungame():
    # Initialize game and create a screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Draw ship
    ship = Ship(screen)

    # Set the background colour.
    #bg_color = (230,230,230)

    # Start the main loop for the game
    while True:
        gf.check_events()
        gf.update_screen(ai_settings, screen, ship)


rungame()