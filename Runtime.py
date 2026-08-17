import Config, Components
import pygame, sys

def start_frame():
    Config.delta_time = Config.clock.tick(Config.FPS)
    Config.WINDOW.fill(Config.dark_grey)
    Config.events = pygame.event.get()
    for event in Config.events:
        if event.type == pygame.QUIT:
            quit_textgine()
    [component.update() for component in Components.ui]

def end_frame():
    pygame.display.flip()

def quit_textgine():
    pygame.quit()
    sys.exit()