import Config
import pygame

base_rect = pygame.Rect(0, 0, 0, 0)

def get_multipliers():
    return {
        "x": Config.WINDOW.get_width()/Config.base_screen_width,
        "y": Config.WINDOW.get_height()/Config.base_screen_height
    }

def opt_rect(rect: pygame.Rect):
    multipliers = get_multipliers()

    base_rect.x = int(rect.x*multipliers["x"])
    base_rect.w = int(rect.w*multipliers["x"])

    base_rect.y = int(rect.y*multipliers["y"])
    base_rect.h = int(rect.h*multipliers["y"])

def opt_dest(dest: tuple[float | int, float | int]):
    multipliers = get_multipliers()

    base_rect.x = int(dest[0]*multipliers["x"])
    base_rect.y = int(dest[1]*multipliers["y"])

def rect(
        surface: pygame.Surface,
        color: pygame.color.Color | tuple[int,int,int],
        rect: pygame.Rect,
        width: int = 0,
        border_radius: int = -1
):
    global base_rect
    opt_rect(rect)
    pygame.draw.rect(
        surface=surface,
        color=color,
        rect=base_rect,
        width=width,
        border_radius=border_radius
    )

def blit(
        surf: pygame.Surface,
        dest: tuple[float | int, float | int]
):
    multipliers = get_multipliers()
    opt_dest(dest)
    Config.WINDOW.blit(
        pygame.transform.scale(
            surf, (surf.get_width()*multipliers["x"], surf.get_height()*multipliers["y"])
        ),
        (
            base_rect.x,
            base_rect.y
        )
    )