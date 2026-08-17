from Data.Scripts.Ui import Button
import Config, Components
import pygame

pages: dict[str, list] = {
    "homescreen": [
        Button.Button(
            rect=pygame.Rect(50, 50, 175, 50),
            text="Platformer",
            color=Config.blue_grey,
            action=lambda : None,
            border_radius=20
        )
    ]
}

def call(page: str = "homescreen", overwrite: bool = True):
    if overwrite:
        Components.ui = []
    [Components.ui.append(part) for part in pages.get(page, pages["homescreen"])]