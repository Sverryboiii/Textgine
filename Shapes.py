import pygame

def rounded_rect(rect: pygame.Rect, color: tuple[int,int,int], rounding: int) -> pygame.Surface:
    new_rect = pygame.Surface((rect.w, rect.h)).convert_alpha()
    new_rect.fill((0, 0, 0, 0))

    pygame.draw.rect(
        new_rect,
        color,
        pygame.Rect(rounding, 0, rect.w-2*rounding, rect.h)
    )
    pygame.draw.rect(
        new_rect,
        color,
        pygame.Rect(0, rounding, rect.w, rect.h-2*rounding)
    )

    pygame.draw.circle(
        new_rect, color, (rounding, rounding), rounding
    )
    pygame.draw.circle(
        new_rect, color, (rect.w-rounding, rounding), rounding
    )
    pygame.draw.circle(
        new_rect, color, (rounding, rect.h-rounding), rounding
    )
    pygame.draw.circle(
        new_rect, color, (rect.w-rounding, rect.h-rounding), rounding
    )

    return new_rect