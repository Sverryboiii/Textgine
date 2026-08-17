import Config, Draw
import pygame, typing

class Button:
    def __init__(
            self,
            *parameters,
            rect: pygame.Rect,
            text: str|int|float,
            color: tuple[int, int, int],
            action,
            border_radius: int|None = None,
            **kw_parameters
    ):
        """
        :param rect: Decides where the button is placed.
        :param color: 3 8-bit values (0-255).
        :param action: A function or class.
        :param text: Will be converted to string so a list will be '['a','b']'
        """

        # Configurations
        self.rect = rect
        self.border_radius = border_radius if border_radius else  int((self.rect.w+self.rect.h) / 10)
        self.color = color
        self.surf = Config.font.render(f"{text}", True, Config.beige)
        self.action = action
        self.parameters = parameters
        self.kw_parameters = kw_parameters

        # Events
        self.pressed = False

    def pressed_update(self) -> typing.Any:
        self.pressed_draw()
        Draw.opt_rect(self.rect)
        if pygame.mouse.get_pressed()[0] and Draw.base_rect.collidepoint(pygame.mouse.get_pos()):
            return None
        self.pressed = False
        return self.action(*self.parameters, **self.kw_parameters)

    def click_check(self):
        if self.pressed:
            return self.pressed_update()
        self.draw()

        mp = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()[0]

        Draw.opt_rect(self.rect)
        if not Draw.base_rect.collidepoint(mp):
            return None
        if not click:
            return None
        self.pressed = True
        return None

    def pressed_draw(self):
        Draw.rect(
            surface=Config.WINDOW,
            color=(
                max(0, self.color[0] - 30),
                max(0, self.color[1] - 30),
                max(0, self.color[2] - 30),
            ),
            rect=self.rect,
            border_radius=self.border_radius
        )
        Draw.rect(
            surface=Config.WINDOW,
            color=(
                max(0, self.color[0] + 30),
                max(0, self.color[1] + 30),
                max(0, self.color[2] + 30),
            ),
            rect=self.rect,
            border_radius=self.border_radius,
            width=2
        )
        Draw.blit(
            surf=self.surf,
            dest=(
                self.rect.x+self.rect.w/2-self.surf.get_width()/2,
                self.rect.y+self.rect.h/2-self.surf.get_height()/2
            )
        )

    def draw(self):
        Draw.rect(
            surface=Config.WINDOW,
            color=self.color,
            rect=self.rect,
            border_radius=self.border_radius
        )
        Draw.rect(
            surface=Config.WINDOW,
            color=(
                max(0, self.color[0] + 30),
                max(0, self.color[1] + 30),
                max(0, self.color[2] + 30),
            ),
            rect=self.rect,
            border_radius=self.border_radius,
            width=2
        )
        Draw.blit(
            surf=self.surf,
            dest=(
                self.rect.x+self.rect.w/2-self.surf.get_width()/2,
                self.rect.y+self.rect.h/2-self.surf.get_height()/2
            )
        )

    def update(self) -> typing.Any:
        self.click_check()