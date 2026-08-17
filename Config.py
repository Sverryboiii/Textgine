import pygame
pygame.init()

# WINDOW
base_screen_width: int = 1000
base_screen_height: int = 600
# Display for the user
WINDOW: pygame.Surface = pygame.display.set_mode((base_screen_width, base_screen_height), pygame.RESIZABLE)

# Events
clock: pygame.time.Clock = pygame.time.Clock()
events: list[pygame.event.Event] = []
FPS: int = 60

# UI
font: pygame.font.Font = pygame.font.SysFont("arial", 32)

# Colors
dark_grey = (25, 25, 25)
beige = (245, 245, 220)
blue_grey = (120, 120, 155)