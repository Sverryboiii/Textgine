import pygame, pytools

ui: list = []

def frame():
    pass

screen = pytools.set_display(800, 500, pygame.RESIZABLE)
pytools.set_frame_method(frame)

pytools.start()