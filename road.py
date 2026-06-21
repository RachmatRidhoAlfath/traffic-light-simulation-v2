import pygame
from settings import *

def draw_road(screen):
    pygame.draw.rect(
        screen,
        GRAY,
        (0, ROAD_Y, WIDTH, ROAD_HEIGHT)
    )

    pygame.draw.line(
        screen,
        WHITE,
        (STOP_LINE, ROAD_Y),
        (STOP_LINE, ROAD_Y + ROAD_HEIGHT),
        5
    )
    