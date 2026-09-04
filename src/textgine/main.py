from src.textgine import Ui
import pygame, sverpykit as spk

def frame():
    pass

screen = spk.set_display(800, 500, pygame.RESIZABLE)
spk.set_frame_method(frame)

spk.start()